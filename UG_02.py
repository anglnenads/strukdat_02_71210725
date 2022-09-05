import timeit

#iteratif
print("Iteratif")
print()
def fib(n):
    i = 0
    nextterm = 1
    present = 1
    previous = 0

    while i < n:
        nextterm = present + previous
        present = previous
        previous = nextterm
        i = i + 1

    return nextterm

x = int(input("Masukkan fibonacci ke : "))
for i in range(1, x+1):
    print(fib(i), end=' ')

print()

for i in range(1,21):
    start = timeit.default_timer()
    n = fib(i)
    end = timeit.default_timer()
    print("n =  {} : waktu {:.10f} seconds". format(i, end-start))

print()

#rekursif
print("Rekursif")
print()
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Suku fibonacci ke :'))
for i in range(1, x+1):
      print(fibo(i), end=' ')

print()

for i in range(1,21):
    start = timeit.default_timer()
    n = fibo(i)
    end = timeit.default_timer()
    print("n =  {} : waktu {:.10f} seconds". format(i, end-start))
