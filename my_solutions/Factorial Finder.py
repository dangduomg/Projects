def fact_recur(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('argument must be a non-negative integer')
    if n == 0:
        return 1
    return n * fact_recur(n - 1)

def fact_iter(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('argument must be a non-negative integer')
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def main():
    while True:
        n = int(input('number: '))

        iter_or_recur = input('(i)terative or (r)ecursive (default: i): ')
        if iter_or_recur in {'', 'i'}:
            fact = fact_iter
        elif iter_or_recur == 'r':
            fact = fact_recur
        else:
            continue

        try:
            res = fact(n)
        except ValueError as e:
            print(e.args[0])
            continue

        print(res)
        break

if __name__ == '__main__':
    main()