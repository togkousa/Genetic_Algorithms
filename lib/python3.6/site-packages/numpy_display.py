# Petter Strandmark 2014.
import numpy as np

ip = None
try:
	# Will only work from within IPython.
	ip = get_ipython()
except NameError:
	pass

def float_to_string(num):
	if type(num) == float or type(num) == np.float64 or type(num) == np.float32:
		s = str(num)
		if s.endswith(".0"):
			s = s[:-2]
		s = s.replace("inf", "∞")
		s = s.replace("nan", "<em>NaN</em>")
		return s
	else:
		return str(num)

if ip is not None:
	def array2html(A):
		html = ''
		html += '<div style="border: 1px solid #000000; display: inline-block;">'
		html += '<table style="border: 1px solid #eeeeee;">'
		for row in A:
			html += "<tr>"
			td_style = 'text-align: center; border: 1px solid #eeeeee;'
			if isinstance(row, np.ndarray):
				for elem in row:
					html += '<td style="' + td_style + '">' + float_to_string(elem) + "</td>"
			else:
				html += '<td style="' + td_style + '">' + float_to_string(row) + "</td>"
			html += "</tr>"
		html += '</table>'
		html += '</div><br />'
		html += '<span style="font-size: 10px;">'
		html += str(A.shape[0])
		for i in range(1, len(A.shape)):
			html += '×' + str(A.shape[1])
		html += ' ' + str(A.dtype)
		html += '</span>'
		return html

	html_formatter = ip.display_formatter.formatters['text/html']
	html_formatter.for_type_by_name('numpy', 'ndarray', array2html)
