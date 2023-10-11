def is_prime(n):
    return


def is_diabolic(n):
    return


def test():
    count = 0
    for i in range(1, 100001):
        if is_diabolic(i) and is_prime(i):
            count += 1
            print(i)
    print(f"Count: {count}")
