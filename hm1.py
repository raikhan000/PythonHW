# Python program to fill a matrix with
# values from 1 to n*n in spiral fashion.

# Fills a[m][n] with values
# from 1 to m*n in spiral fashion.
def spiralFill(m, n, a):
    # Initialize value to be filled in matrix.
    val = 0

    # k - starting row index
    # m - ending row index
    # l - starting column index
    # n - ending column index
    k, l = 0, 0
    while (k < m and l < n):

        # Print the first row from the remaining rows.
        for i in range(l, n):
            a[k][i] = val
            val += 1
            if val > 9:
                val = 0
        k += 1

        # Print the last column from the remaining columns.
        for i in range(k, m):
            a[i][n - 1] = val
            val += 1
            if val > 9:
                val = 0
        n -= 1

        # Print the last row from the remaining rows.
        if (k < m):
            for i in range(n - 1, l - 1, -1):
                a[m - 1][i] = val
                val += 1

                if val > 9:
                    val = 0
            m -= 1

        # Print the first column from the remaining columns.
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                a[i][l] = val
                val += 1

                if val > 9:
                    val = 0
            l += 1


# Driver program
if __name__ == '__main__':
    m, n = 5, 4
    a = [[0 for j in range(m)] for i in range(n)]
    spiralFill(m, n, a)
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print('')

# This code is contributed by Parin Shah
