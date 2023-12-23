import re

def power_set(game):
    r = g = b = 0
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
    Games = []
    while True:
        ele = input()[8:]
        if ele == '':
            break
        else:
            ele = re.sub('[^A-Za-z0-9 ]+', '', ele).split()
            Games.append(ele)
            
    print(sum_power(Games))

if __name__ == "__main__":
    main()