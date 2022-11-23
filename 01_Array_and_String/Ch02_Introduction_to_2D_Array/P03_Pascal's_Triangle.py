def generate(numRows):
    # 전체를 담을 배열 생성
    rows = []
    for i in range(numRows):
        # 행의 시작
        row = [1]
        for j in range(1, i):
            prev_row = rows[i-1]
            row.append(prev_row[j-1]+prev_row[j])
        if i > 0:
            row.append(1)
        rows.append(row)
    return rows

def generate2(numRows):
    rows = []

    for i in range(numRows):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1

        for j in range(1, i):
            row[j] = rows[i-1][j-1] + rows[i-1][j]

        rows.append(row)
    return rows