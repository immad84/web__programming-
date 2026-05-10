# The program gets 5 numbers and try to find the min, max and average
def main():
    a = int(input('What\'s a ? '))
    b = int(input('What\'s b ? '))
    x = int(input('What\'s x ? '))
    y = int(input('What\'s y ? '))
    z = int(input('What\'s z ? '))
    print('Min: ', minimum(a, b, x, y, z))
    print('Max: ', maximum(a, b, x, y, z))
    print('Avg: ', f'{avg(a, b, x, y, z):.2f}')

def minimum(a, b, x, y, z):
    min = a
    if b < min:
        min = b
    if x < min:
        min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min

def maximum(a, b, x, y, z):
    max = a
    if b > max:
        max = b
    if x > max:
        max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max

def avg(a, b, x, y, z):
    average = (a + b + x + y + z) / 5
    return average

main()
