import time

def printBoard(board):
    """Hàm này dùng để in ra bàn cờ"""
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i] == j:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def testBoard(board):
    """Hàm này dùng để kiểm tra xem trên bàn cờ có hai quân hậu bất kì nào đánh nhau hay không"""
    size = len(board)
    if size > 1:
        for i in range(0, size-1, 1):
            for j in range(i+1, size, 1):
                # Kiểm tra trên cùng một cột
                if board[i] == board[j]:
                    return False
                # Kiểm tra trên đường chéo trái đi xuống
                if board[i] == board[j]+(i-j):
                    return False
                # KIểm tra trên đường chéo phải đi xuống
                if board[i] == board[j]-(i-j):
                    return False
    return True


def BrFSQueen(N):
    queue = []
    queue.append([])

    while True:
        """
        - Ban đầu ta sẽ tìm các bàn cờ có kích thước 1x1 thỏa mã đề bài và cho vào queue.
        - Sau đó, trong số các bàn cờ thỏa đề bài, ta tăng dần kích thước bàn cờ lên 2x2, 3x3, 4x4,... và tiếp tục tìm các bàn cờ thỏa đề bài cho vào queue.
        - Lặp cho đến khi tìm được bàn cờ đầu tiên có kích thước NxN thì dừng lại
        """
        currentBoard = queue.pop(0)
        if len(currentBoard) < N: 
            for j in range(N):
                lastQueen = 0
                if(len(currentBoard) == 0):
                    lastQueen = -2
                else:
                    lastQueen = currentBoard[len(currentBoard)-1]
                if j < lastQueen-1 or j > lastQueen+1: #Kiểm tra xem queen mới thêm vào có trùng cột hay đường chéo với queen trước nó hay không
                    afterBoard = currentBoard[:]
                    afterBoard.append(j) #Tạo bàn cờ mới có kích thước lớn hơn bàn cờ hiện tại 1 đơn vị
                    if testBoard(afterBoard):
                        queue.append(afterBoard)
                        if len(afterBoard) == N: #Nếu tìm được bàn cờ có kích thước NxN thì dừng lại
                          return afterBoard


def main():
    N = 0
    N = int(input('Enter N: '))

    start = time.time()
    final = BrFSQueen(N)
    end = time.time()
    printBoard(final)
    print("time: ",end-start)

main()
