state = 0
aux = True
dict={} 

def is_previous(state_variable):
	if state in dict.keys():
		print 'First repetition', state
		return False
	dict[state]=1
	return True
	  

while aux:
	with open("input_data.txt") as f:
		for line in f:
			state += float(line)
			if aux:
				aux = is_previous(state)


print "Final state:", state

