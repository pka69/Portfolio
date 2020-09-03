import time 

def fib(n):
    return n if n <=1 else fib(n-1) + fib(n-2)

def fib2(n):
    if n<=1: return n
    f =[0,1,1]
    for i in range(3,n):
        f.append(f[i-1] +f[i-2])
    return f[n-1] + f[n-2]


def fib3(n):
    if n < 0:
        raise ValueError("błędna ilość elementów")
    last_two = [0, 1]
    for i in range(n+1):
        if i > 1:
            yield sum(last_two)
            last_two = [last_two[1], sum(last_two)]
        else: yield last_two[i]


if __name__ == '__main__':
    print("--------fibonnaci----------------------------------------------")
    start_time = time.time()
    for i in range(15):
        print('dla {} - {}'.format(i, fib(i)))
    elapsed_time = time.time() - start_time
    print('czas wykonania - ', elapsed_time)
    print("--------fibonnaci 2--------------------------------------------")
    start_time = time.time()
    for i in range(15):
        print('dla {} - {}'.format(i, fib2(i)))
    elapsed_time = time.time() - start_time
    print('czas wykonania - ', elapsed_time)
    print("--------fibonnaci 3 generator------------------------------------")
    start_time = time.time()
    for i,f in enumerate(fib3(14)):
        print('dla {} - {}'.format(i, f))
    elapsed_time = time.time() - start_time
    print('czas wykonania - ', elapsed_time)

    