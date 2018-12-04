def start():	
	checksum_3 = 0
	checksum_2 = 0
	with open("input_data.txt") as f:
		for line in f:
			true_3=False
			true_2=False
			dict={}
			for letter in line:
				print letter
				if letter in dict.keys():
					dict[letter]+=1
				else:
					dict[letter]=1
			for k in dict.keys():
				if dict[k]==3 and not(true_3):
					checksum_3 += 1
					true_3=True
				elif dict[k]==2 and not(true_2): 
					checksum_2 += 1
					true_2=True
	print checksum_2 * checksum_3
					

start()
