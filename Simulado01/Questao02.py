def left_rotate(lst):
    if len(lst) > 1:
        return lst[1:] + [lst[0]]
    return lst

def print_line(lst):
    print(" ".join(str(x) for x in lst))

entrada = input().strip()
num1, num2 = map(int, entrada.split(","))

menor = min(num1, num2)
maior = max(num1, num2)

base = list(range(menor, maior + 1))

level = 0

while True:
    current_slice = base[:len(base) - level]

    if len(current_slice) == 1:
        print_line(current_slice)
        break

    mod = level % 4
    if mod == 0:
        print_line(current_slice)
    elif mod == 1:
        print_line(current_slice[::-1])
    elif mod == 2:
        print_line(left_rotate(current_slice))
    elif mod == 3:
        print_line(current_slice[::-1])

    level += 1