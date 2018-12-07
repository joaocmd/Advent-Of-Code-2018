fp = open("input.txt", "r")
lines = fp.readlines()
fp.close()

res = 0
for line in lines:
	res += int(line)


print(res)