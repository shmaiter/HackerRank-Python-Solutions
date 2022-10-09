
''' ROWS '''
# [print(f'Position for {i}: is row {i // 3}') for i in range(9)]

''' MODULOS FORMULA

a - (n * floor(a/n))

100 % 7 = 2
a = 100, n = 7
100 - (7 * floor(100/7)) = 2

'''

''' COLUMNS
If the numerator {i} is lower than the denominator {3}, 
the result will always be equal to the numerator.
'''
# [print(f'Position for {i}: is column {i % 3}') for i in range(12)]


pixels = [[1, 1, 0],
          [0, 0, 1],
          [1, 1, 0]]


def max_greyness(cell):
    cell = cell - 1 if cell != 0 else cell
    print(f'cell: {cell}')
    length = len(pixels[0])
    row_area = list()
    col_area = list()
    cell_row_index = cell // length
    cell_col_index = cell % length

    ''' Comprehension List Short Version '''
    # row_area = [value for index, value in enumerate(
    #     pixels) if index == cell_row_index]
    # col_area = [
    #     value for row in pixels for index, value in enumerate(row) if index == cell_col_index]

    for index, value in enumerate(pixels):
        if index == cell_row_index:
            row_area.extend(value)

    for row in pixels:
        for index, value in enumerate(row):
            print(
                f'index: {index} value: {value} cell_col_ind: {cell_col_index}')
            if index == cell_col_index:
                col_area.append(value)

    print(f'Row area: {row_area}')
    print(f'Column area: {col_area}')


if __name__ == '__main__':
    cell = 1
    max_greyness(cell)
