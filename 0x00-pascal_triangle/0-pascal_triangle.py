def pascal_triangle(n):
    p_triangle = []

    if n > 0:
        #creates triangle rows
        for i in range(1, n + 1):
            row = []
            #frist element of a row
            m = 1

            #calculates each element in the current row
            for j in range(1, i + 1):
                row.append(m)

                #updates c to the next binomial coefficient
                m = m * (i - j) // j

            p_triangle.append(row)
    return p_triangle