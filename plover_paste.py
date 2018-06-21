"""
A module for a Plover plugin which outputs the clipboard contents
"""
from PyQt5.Qt import QApplication


def output_clipboard(ctx, cmdline):
	"""
	Return an action whose text is set to the clipboard's current contents
	"""
	clip = QApplication.clipboard().text()
	action = ctx.new_action()

	# Make sure we don't cause weirdness if the clipboard is empty or an image
	if clip != "":
		action.text = clip

	return action
