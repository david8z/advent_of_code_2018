import itertools
def start():	
	actual_dif=100
	with open("input_data.txt") as f:
		for line1, line2 in itertools.combinations(f,2):
			eq = []
			dif = []
			if not(line2 in line1):
				for l1, l2 in zip(line1, line2):
					#print(l1, l2, dif)
					if l1 == l2:
						eq+=l1
					else:
						dif+=l2
			if len(dif) < actual_dif:
				actual_dif = len(dif)
				result= "".join(eq)
	print result
				
start()
