import re
def paramVerification(param):
	# param that including ONLY [a-z,A-Z,0-9,_] is legal.
	reStr = r'^\w+$'
	m = re.match(reStr, param)
	if m:
		return True
	else:
		return False

print(paramVerification("ashfkAAAsddhf&_234555"))





