#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle, n):
    """
    Print the triangle
    """
    # for i in range(n):
    #     for j in range(n-i-1):
    #         print(format(" ", "<2"), end="")
    #     for j in range(i+1):
    #         print(format(triangle[i][j], "<3"), end=" ")
    #     print()

    i = 0
    for row in triangle:
        print((" " * (n - i - 1)), end="")
        print("[{}]".format(",".join([str(x) for x in row])))
        i += 1



if __name__ == "__main__":
    print_triangle(pascal_triangle(6), 6)
