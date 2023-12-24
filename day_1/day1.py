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

def Add_nums(line):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nos = ["1","2","3","4","5","6","7","8","9"]

    first_Index = line.find(nums[0])
    first_number = 0
    last_Index = line.find(nums[0])
    last_number = 0
    
    for n in range(0, len(nums)):
        start=0
        while(True):
            i = line.find(nums[n],start)
            if i!=-1:
                if i<first_Index or first_Index<0:
                    first_Index = i
                    first_number = n
                if i>last_Index or last_Index<0:
                    last_Index = i
                    last_number = n
                if start<len(line):
                    start = i+1
            else:
                break
            
    if first_Index != -1:
        line = line[:first_Index]+nos[first_number]+line[first_Index:]
    if first_Index!=last_Index and last_Index != -1:
        line = line[:last_Index+1]+nos[last_number]+line[last_Index+1:]
    return line

def modify_Input(Input):
    for i in range(len(Input)):
        Input[i] = Add_nums(Input[i])
    return Input

def main():
    # read input
    Input = open('day_1\day1_Input.txt').read().split('\n')
    print("Part 1: ",Sum_calibration(Input))

    Input = modify_Input(Input)
    print("Part 2: ",Sum_calibration(Input))

if __name__ == "__main__":
    main()