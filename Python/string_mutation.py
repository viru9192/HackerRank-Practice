def mutate_string(string, position, character):
    s_new = s[:5] + "k" + s[6:]
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)