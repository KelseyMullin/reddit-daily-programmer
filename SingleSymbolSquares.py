#Challenge from https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/

from random import randint

square = [['X', 'X'], ['X', 'O']]


def make_square(dimension):
    while len(square[0]) < dimension:
        for i in range(len(square)):
            square[i].append('X')
        square.append(['X'])
        for i in range(len(square[0])-1):
            square[len(square)-1].append('X')


def check_square():
    changed = False
    for row in range(len(square)):
        for col in range(len(square[0])):
            gap = 1
            while row + gap < len(square) and col + gap < len(square[0]):
                if (square[row][col] == square[row][col + gap] and
                        square[row][col] == square[row + gap][col] and
                        square[row][col] == square[row + gap][col + gap]):
                    if square[row + gap][col + gap] == 'X':
                        newChar = 'O'
                    else:
                        newChar = 'X'
                    rand = randint(1,4)
                    if rand == 1:
                        square[row][col] = newChar
                    elif rand == 2:
                        square[row][col + gap] = newChar
                    elif rand == 3:
                        square[row + gap][col] = newChar
                    else:
                        square[row + gap][col + gap] = newChar
                    changed = True
                gap = gap + 1
    if not changed:
        return True
    else:
        return False


def print_square():
    for i in range(len(square)):
        print(square[i])


make_square(7)
while not check_square():
    check_square()
print("Solved:")
print_square()