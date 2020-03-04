def rect_in_square(lengh, width, squares):
    square = 1
    if lengh <= 1 and lengh <= 1:
        return square
    while lengh >= square and width >= square:
        if square >= lengh:
            rect_in_square(width - lengh, lengh, squares)
            squares.append(square)
            return squares
        if square >= width:
            rect_in_square(width, lengh - width, squares)
            squares.append(square)
            return squares
        square += 1
    squares.reverse()
    return squares

squares = []
print(rect_in_square(30, 16, squares))