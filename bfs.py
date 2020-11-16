import time
global N
# initialize the board


def printboard(b):
    num = len(b)
    for i in range(num):
        for j in range(num):
            if b[i] == j:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()

# Final test function


def finaltest(board):
    num = len(board)
    if num > 1:
        for i in range(num-1, 0, -1):
            for j in range(i-1, -1, -1):
                # checking Down
                if board[i] == board[j]:
                    return False
                # checking left diagonal up
                if board[i] == board[j]+(i-j):
                    return False
                # checking right diagonal up
                if board[i] == board[j]-(i-j):
                    return False
    return True


def bfs(board):
    # initial state
    global N
    queue = []
    queue.append(board)

    while True:
        current = queue.pop(0)
        if len(current) != N:
            for j in range(N):
                lastpos = 0
                if(len(current) == 0):
                    lastpos = N + 10
                else:
                    lastpos = current[len(current)-1]
                if j < lastpos-1 or j > lastpos+1:
                    newBoard = current[:]
                    newBoard.append(j)
                    # newBoard[level] += j + 1
                    if finaltest(newBoard):
                        queue.append(newBoard)
        else:
            queue.insert(0, current)
            break
    return queue


def main():
    global N
    board = []

    N = int(input('Enter N: '))
    # initialize the board
    # for i in range(N):
    #     row = [-1] * N
    #     board.append(row)

    final = bfs(board)
    for f in final:
      print(f)
      printboard(f)
      s = '-' * N
      print(s)


main()
