import functools


def my_sort(arr: list, index: list):
    assert len(arr) == len(index), '索引列表错误'

    def cmp(x, y):
        a, b = x[0], y[0]
        return index.index(a) - index.index(b)

    arr.sort(key=functools.cmp_to_key(cmp))
    return arr


def main():
    arr = [(2, 'fef'), (1, 'fs'), (5, 'df'), (4, 'ds0'), (3, 'ss')]
    index = [5, 4, 3, 2, 1]

    my_sort(arr, index)
    print(arr)


if __name__ == '__main__':
    main()
