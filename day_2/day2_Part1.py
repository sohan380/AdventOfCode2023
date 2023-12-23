import re

def possible(game):
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
    Games = []
    while True:
        ele = input()[8:]
        if ele == '':
            break
        else:
            ele = re.sub('[^A-Za-z0-9 ]+', '', ele).split()
            Games.append(ele)
            
    print(sum_IDs(Games))

if __name__ == "__main__":
    main()