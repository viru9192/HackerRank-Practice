def average(array):
    unique = set(array)
    total = sum(unique)
    average = total / len(unique)
    return f"{average:.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)