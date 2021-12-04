f = open("input.txt", "r")
lines = f.read().split('\n')
lines.remove('')
f.close()

nums = list(map(int, lines[0].split(',')))

#remove empty lines
lines = list(filter(lambda a: a != '', lines))
boards = []

i=0
board = {'all': [], 'lines': []}
for l in lines[1:]:
    line = list(map(int, l.split()))
    if len(line) == 0:
        next

    board['lines'].append(line)
    board['all'].extend(line)
    i+=1
    if (i%5 == 0):
        boards.append(board.copy())
        board = {'all': [], 'lines': []}

for board in boards:
    for i in range(5):
        line = []
        for j in range(5):
            line.append(board['all'][j*5+i])
        board['lines'].append(line) 

def has_won(board):
    for l in board['lines']:
        if len(l) == 0:
            return True
    return False
        
def boards_left():
    count = 0
    for board in boards:
        if not has_won(board):
            count += 1
    return count

def tick_number(num, mylist):
    if mylist.count(num) != 0:
        mylist.remove(num)

first=True
for n in nums:
    for board in boards:
        tick_number(n, board['all'])
        for l in board['lines']:
            tick_number(n, l)
        if has_won(board):
            if first:
                print("Soution part1 is {}".format(sum(board['all'])*n))
                first = False
            else:
                if boards_left() == 0:
                    print("Soution part2 is {}".format(sum(board['all'])*n))
                    exit(0)
