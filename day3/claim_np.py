import numpy as np
import re

def start():	
	matrix = np.zeros((1000,1000))
	line_count = 0
	with open("input.txt") as f:
		for line in f:
			i,x,y,sum_x,sum_y = map(int,re.findall(r'-?\d+', line))
			matrix[x:x+sum_x,y:y+sum_y]+=1

	print len(np.where(matrix>=2)[0])
	with open("input.txt") as f:
		for line in f:
			i,x,y,sum_x,sum_y = map(int,re.findall(r'-?\d+', line))
			if len(np.where(matrix[x:x+sum_x,y:y+sum_y]>1)[0]) == 0:
				print i

start()
