def calibration_value(line):
    for i in line:
        if i.isdigit():
            first = int(i)
            break

    for i in reversed(line):
        if i.isdigit():
            last = int(i)
            break

    return first*10+last

def Sum_calibration(Input):
    sum=0
    for line in Input:
        sum += calibration_value(line)
    return sum

def main():
    Input = []
    while True:
        ele = input()
        if ele == '':
            break
        else:
            Input.append(ele)
    print(Sum_calibration(Input))

if __name__ == "__main__":
    main()