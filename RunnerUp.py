def printStream():
	stream = []
	print('Input total number of streams: ')
	N = int(input())
	for i in range(N):
		new_string = input()
		stream.append(new_string.split())
	print(stream)

	for i in range(N):
		if stream[i][0] == "odd":
			for value in range(1, int(stream[i][1]) + 1):
				if value%2 != 0:
					print(value)
		elif stream[i][0] == "even":
			end = int(stream[i][1]) + 1
			for value in range(0, int(stream[i][1]) + 1):
				if value%2 == 0:
					print(value)

if __name__ == '__main__':
	printStream()

#[['John', 30, 'M'], ['Hedwick', 26, 'F'], ['Luke', 23, 'M']]
