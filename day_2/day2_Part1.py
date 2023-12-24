import re

def possible(game):
    # Checking if count is greater than limit
    for i in range(1, len(game)):
        if game[i] == 'blue' and int(game[i-1])>14:
            return False
        if game[i] == 'green' and int(game[i-1])>13:
            return False
        if game[i] == 'red' and int(game[i-1])>12:
            return False
    return True
            
def sum_IDs(Games):
    sum = 0
    for i in range(len(Games)):
        if possible(Games[i]):
            sum += i+1
    return sum

def main():
    # Read input and modifying it to store only count and color
    Games = open('day_2\day2_Input.txt').read().split('\n')
    Games = [re.sub('[^A-Za-z0-9 ]+', '', line[8:]).split() for line in Games]

    print(sum_IDs(Games))

if __name__ == "__main__":
    main()