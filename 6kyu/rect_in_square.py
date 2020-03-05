def rect_in_square(lengh, width, squares):
    square = 1
    if lengh <= 0 and lengh <= 0:
        return squares
    while lengh >= square and width >= square:
        if square >= lengh:
            squares.append(square)
            return rect_in_square(width - lengh, lengh, squares)
        if square >= width:
            squares.append(square)
            return rect_in_square(width, lengh - width, squares)
        square += 1


squares = []
print(rect_in_square(1000, 6, squares))
