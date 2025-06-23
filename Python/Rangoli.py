import string
def print_rangoli(size):
    chars = string.ascii_lowercase
    lst =[]
    width = 4*size - 3

    for i in range(size):
        s = '-'.join(chars[i:size])
        lst.append((s[::-1] + s[1:]).center(width, '-'))
    print('\n'.join(lst[:0:-1] + lst))

if __name__ == '__main__':
    n =int(input())
    print(print_rangoli(n))
