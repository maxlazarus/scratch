class StdOutput:
	def __lshift__(self, item):
		print(item)

	def __rshift__(self, item):
		print(item)
		return item

o = StdOutput()


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def test_tables():
	o << ''
	bu = '\u2552', '\u2564', '\u2555'
	bm = '\u2523', '\u254B', '\u2528'
	bl = '\u2517', '\u253B', '\u251B'
	t = '\u255E', '\u256A', '\u2561'
	m = '\u251D', '\u253F', '\u2525'
	l = '\u2515', '\u2537', '\u2519'

	hzb = '\u2550'
	hz = '\u2501'
	hzl = '\u2500'
	vt = '\u2502'
	vtl = '\u2502'

	import numpy as np

	def draw_table(array, width=None):
		if width is not None:
			a = np.array(array).reshape((len(array) // width, width))
		else:
			a = np.array(array)
		a = a.astype('str')

		row_widths = {}

		for j in range(a.shape[1]):
			row_width = max(2 + len(entry) for entry in a[:, j])
			row_widths[j] = row_width

		for i, row in enumerate(a):
			for j, entry in enumerate(row):
				n_spaces = row_widths[j] - len(entry) - 2
				a[i, j] = entry + ' ' * n_spaces

		table_out = ''

		table_out += bu[0]
		for i in range(a.shape[1]):
			table_out += hzb * row_widths[i] + bu[1]
		table_out = table_out[:-1] + bu[2] + '\n'

		for i, row in enumerate(a):
			if i == 0:
				table_out += vt + ' ' + (' ' + vt + ' ').join(row) + ' ' + vt + '\n'
				table_out += t[0]
				for i in range(a.shape[1]):
					table_out += hzb * row_widths[i] + t[1]
				table_out = table_out[:-1] + t[2] + '\n'
			else:
				table_out += vtl + ' ' + (' ' + vtl + ' ').join(row) + ' ' + vtl + '\n'
				
				if i != a.shape[0] - 1:
					table_out += m[0]
					for i in range(a.shape[1]):
						table_out += hz * row_widths[i] + m[1]
					table_out = table_out[:-1] + m[2] + '\n'

		table_out += l[0]
		for i in range(a.shape[1]):
			table_out += hz * row_widths[i] + l[1]
		table_out = table_out[:-1] + l[2] + '\n'

		return table_out

	o << draw_table([
		'here', 'are som biegesgalsfkjsadf', 'some', 
		'cells', 'and_really_long', 'other',
		'ones', 1, 342.234
	
	], 3)

	import itertools
	o << 'Table testing and stuff'
	o << draw_table(list(itertools.combinations(['botty', 'floob', 'marko', 'blobl'], 3)))
	o << draw_table(list(itertools.permutations([0, 1, 2])))

