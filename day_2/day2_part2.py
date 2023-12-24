import re

def power_set(game):
    r = g = b = 0
    # Finding highest count required for each color
    for i in range(1, len(game)):
        if game[i] == 'red' and int(game[i-1])>r:
            r = int(game[i-1])    
        if game[i] == 'green' and int(game[i-1])>g:
            g = int(game[i-1])   
        if game[i] == 'blue' and int(game[i-1])>b:
            b = int(game[i-1])   
    return r*g*b

def sum_power(Games):
    sum = 0
    for game in Games:
        sum += power_set(game)
    return sum

def main():
    # read input
    Games = open('day_2\day2_Input.txt').read().split('\n')
    Games = [re.sub('[^A-Za-z0-9 ]+', '', line[8:]).split() for line in Games]
            
    print(sum_power(Games))

if __name__ == "__main__":
    main()