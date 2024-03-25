def fib(n):
    (i, j) = (0, 1)
    for _ in range(n):
        (i, j) = (j, i + j)
    return i
        
        
def main():
    n = int(input('> '))
    print(fib(n))
    
if __name__ == '__main__':
    main()
