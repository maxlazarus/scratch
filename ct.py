from scratch import o
import os
import pytest
import time
from threading import Thread

def python_file_list():
	file_list = []
	for root, _, files in os.walk('.'):
		for file in files:
			if os.path.splitext(file)[-1] == '.py':
				file_list += [os.path.join(root, file)]
	return file_list

def main(argv):
	o << 'running automatic testing'
	try:
		file_hashes = {}

		while True:
			for filename in python_file_list():
				with open(filename) as f:
					new_hash = hash(f.read())
				try:
					if file_hashes[filename] == new_hash:
						continue
					else:	
						o << f'{filename} rehashed'
						if 'ct.py' in filename:
							if not os.system('python ct.py'):
								quit()
						else:
							os.system(f'python ct.py -f {filename} -s -q')	
							file_hashes[filename] = new_hash
				except KeyError:
					file_hashes[filename] = new_hash

					
	except KeyboardInterrupt:
		o << 'Breaking'


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--filename')
	parser.add_argument('--force-fail', action='store_true')
	args, unknown = parser.parse_known_args()
	
	if args.force_fail:
		raise Exception('forced Exception raised')
	if args.filename:
		pytest.main([args.filename] + unknown)
	else:
		main(unknown)
	