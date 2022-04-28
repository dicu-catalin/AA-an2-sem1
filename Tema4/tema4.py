import sys
def main():
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	m = int(sys.stdin.readline())
	fnc = ""
	for line in sys.stdin:
		line = line.split()
		v = int(line[0])
		u = int(line[1])
		fnc += "("
		for i in range(1, k+1):
			if i == k:
				fnc += str((v-1)*k + i) + "V" + str((u-1)*k + i)
			else:
				fnc += str((v-1)*k + i) + "V" + str((u-1)*k + i) + "V"
		fnc += ")^"
	for i in range(1, k+1):
		if i != 1:
			fnc += "^"
		fnc += "("
		for j in range (0, n):
			if j != n-1:
				fnc += str(j*k + i) + "V"
			else:
				fnc += str(j*k + i)
		fnc += ")"
		for j in range(0, n):
			for l in range(j, n):
				if j == l:
					continue
				fnc += "^(~" + str(j*k + i) + "V~" + str(l*k + i) + ")"
	for i in range(0, n):
		for j in range(1, k):
			fnc += "^(~" + str(i*k + j) + "V~" + str(i*k + j + 1) + ")"
	print(fnc)


if __name__ == "__main__":
	main()