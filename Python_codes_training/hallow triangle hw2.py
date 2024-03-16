rows=4
for i in range(1, rows + 1):
    for j in range(1, 2 * rows):
        if j <= rows - i:
            print(" ", end=" ")
        elif j >= rows + i:
            break
        else:
            if i == rows or j == rows - i + 1 or j == rows + i - 1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
    print()