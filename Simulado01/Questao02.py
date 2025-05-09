# Leitura e ordenação de A e B
a, b = map(int, input().split(','))  
if a > b:
    a, b = b, a

k = 0
while a + k <= b - k:
    start = a + k
    end = b - k
    seq = list(range(start, end + 1))
    if k % 2 == 0:
        print(' '.join(str(x) for x in seq))
    else:
        print(' '.join(str(x) for x in reversed(seq)))
    k += 1
