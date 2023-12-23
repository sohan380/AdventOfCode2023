from day_1.day1_Part1 import Sum_calibration

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
    Input = []
    while True:
        ele = input()
        if ele == '':
            break
        else:
            Input.append(ele)

    Input = modify_Input(Input)
    print(Sum_calibration(Input))

# def main():
#     line = "one7one"
#     line = Add_nums(line)
#     print(line)
if __name__ == "__main__":
    main()