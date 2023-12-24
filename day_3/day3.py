from collections import defaultdict

# read input
mat = open('day_3\day3_Input.txt').read().split('\n')
mat = [[ch for ch in line] for line in mat]

# no. of rows and columns
n = len(mat)
m = len(mat[0])

sum_parts = 0
# for part 2
sum_gears = 0
gear_nums = defaultdict(list)

for i in range(n):
    num = 0
    is_part = False
    # for finding indices of '*'
    gears = set()
    for j in range(m+1):
        if j<m and mat[i][j].isnumeric():
            num = num*10 + int(mat[i][j])
            # checking if adjacent to any symbol
            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    # making sure of boundaries
                    if 0<= i+r <n and 0<= j+c <m:
                        ch = mat[i+r][j+c]
                        if not ch.isnumeric() and ch != '.':
                            is_part = True
                            if ch == '*':
                                gears.add((i+r, j+c))

        # The number ends, so add it in sum
        elif num>0:
            if is_part:
                sum_parts += num
            for g in gears:
                gear_nums[g].append(num)
            # reset everything for next number
            num = 0
            is_part = False
            gears = set()

print("sum of all part numbers",sum_parts)

for key, val in gear_nums.items():
    if len(val) == 2:
        sum_gears += val[0]*val[1]

print("sum of all gear ratios", sum_gears)