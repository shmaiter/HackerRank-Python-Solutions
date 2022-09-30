import textwrap


def wrap(string, max_width):

    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = "ABC DEFGH IJKLIMNOQRS TUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)
