def main():
	fp = open("input.txt", "r")
	res = 0
	
	lines = fp.readlines()
	fp.close()
	
	inputs = [int(line) for line in lines]
	results = set()
	
	i = 0
	while True:
		res += inputs[i%len(inputs)]
		if res in results:
			print(res)
			return
		results.add(res)
		i += 1	