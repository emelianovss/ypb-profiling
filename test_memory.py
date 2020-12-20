def get_one_line(i):
    return ' '.join((
        f'hello {i}-{j} world' for j in range(10 ** 5)
    ))


def get_lines(count):
    return [get_one_line(i) for i in range(count)]


def test():
    sum_ = 0
    for i in get_lines(10):
        sum_ += len(i)
    return sum_


if __name__ == '__main__':
    test()
