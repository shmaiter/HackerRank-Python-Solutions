def average(array):
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
