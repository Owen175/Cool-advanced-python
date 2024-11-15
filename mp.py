from multiprocessing import Process, Queue, Pool
from math import ceil

def isPrime(n):
    for i in range(2, ceil(n**0.5) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    data = list(range(1, 10000))
    with Pool(8) as p:
        answers = p.imap(isPrime, data)
        [print(data[i]) for i, a in enumerate(answers) if a]

