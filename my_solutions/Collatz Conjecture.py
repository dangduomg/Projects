# this will end when the number goes to 1


def collatz(n: int) -> list[int]:
	res = []
	while n > 1:
		res.append(n)
		if n % 2 == 0:
			n //= 2
		else:
			n = n * 3 + 1
	res.append(n)
	return res


def main():
	n = int(input('enter number: '))
	print(*collatz(n))

if __name__ == '__main__':
	main()