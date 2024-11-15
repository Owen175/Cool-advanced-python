# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

x = fibon(1000)
print(next(x))

# OR

for x in fibon(1000):
  print(x)
