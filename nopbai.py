import numpy as np
import time
import random
"""
Không gian trạng thái: Tất cả trạng thái của bàn cờ NxN có N quân hậu nằm trên N dòng
Ví dụ: board = [0,1,3,2] => Hàng 0 có quân hậu ở cột 0, hàng 1 có quân hậu ở cột 1, hàng 2 có quân hậu ở cột 3, hàng 3 có quân hậu ở cột 2
"""
#--------------------------------------DFS--------------------------------------#
#Giải được cỡ N ~= 20 tầm 2 phút

#Lưu N quân hậu vào mảng queensPositon[N], index biểu diễn vị trí hàng, queensPositon[index] biểu diễn vị trí cột
#queensRowCurrent là vị trí hàng của quân hậu cuối cùng được đặt ngay trên bàn cờ hiện tại (queensRowCurrent+1 là số con hậu đã đặt hiện tại)
# j 0 1 2 3 
#i  __________
#0 |X       |
#1 |    X   | ->queensRowCurrent--> đệ quy -->
#2 |        | <-- đặt con hậu thứ queensRowCurrent+1 vào hàng tiếp theo <--
#3 |        |
#  __________

class QueenBoard:

  def __init__(self, N):
    self.N = N
    self.queenPositons = np.zeros(N)

  #kiểm tra con hậu có position(x,y) có đánh nhau mấy con đã đặt trước không
  def __isSafe(self, x, y):
    for row in range(y):
      if(x == self.queenPositons[row] or abs(x-self.queenPositons[row]) == abs(y-row)):
        return False
        
    return True

  def __recursiveQueen(self, queenPositons, N, queensRowCurrent):#N=4 = length(queenPositons)
    #trường hợp đã đặt đủ N quân lên bàn cờ => in ra màn hình và kết thúc giải thuật
    
    if(queensRowCurrent > N-1):#queensRowCurrent==4
      return True
    else:
      #Tại hàng queensRowCurrent, tìm cột thứ col thích hợp để đặt con hậu thứ queensRowCurrent xuống
      for col in range(N):

        #kiểm tra con hậu thứ queensRowCurrent đặt vào vị trí col có đánh nhau với những con hậu đã đặt không
        if(self.__isSafe(col, queensRowCurrent)):

          #nếu hợp lệ thì đặt con hậu hàng thứ queensRowCurrent xuống
          queenPositons[queensRowCurrent] = col

          #đệ quy đặt con hậu tiếp theo
          if(self.__recursiveQueen(queenPositons, N, queensRowCurrent+1)):           
            return True

      #Ko tìm thấy con hậu hợp lệ -> Backtracking (kết thúc vòng đệ quy top)


  def __printQueen(self, queenPositons, N):
    for i in range(N):
      for j in range(N):
        #Xét hàng i: nếu vị trí cột đang duyệt ánh xạ trùng với con hậu đã đánh trên bàn cờ thì in Q
        if(j == queenPositons[i]):
          print("Q",end = " ")
        else:
          print(".",end = " ")
      print("\n") 


  def printQueen(self):
    self.__recursiveQueen(self.queenPositons, self.N, 0) 
    self.__printQueen(self.queenPositons, self.N)

#--------------------------------------BFS--------------------------------------#
#Giải được cỡ N ~= 10 tầm 8 giây
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


#-----------------------steepest-ascent-hill-climbing--------------------------#
#Giải được cỡ N ~= 60 tầm 5 phút
def initialize_state(size):
    new_board = []
    # Tạo bảng ngẫu nhiên
    for i in range(size):
        new_board.append(random.randint(0, size - 1))

    return new_board

# hàm lượng giá: số vi phạm trong bàn cờ
def evaluate_state(board, n):
    attacking = 0
    # lưu current state của cột, đường chéo trái, phải
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for i in range(n):
        # quân hậu đang xét có vị trí cột đã tồn tại trong dict
        if board[i] in dict1:
            attacking += 1
        else:
            dict1.update({board[i]: True})
        # quân hậu đang xét có vị trí đường chéo trái đã tồn tại trong dict
        if board[i] - i in dict2:
            attacking += 1
        else:
            dict2.update({board[i] - i: True})
        # quân hậu đang xét có vị trí đường chéo phải đã tồn tại trong dict
        if board[i] + i in dict3:
            attacking += 1
        else:
            dict3.update({board[i] + i: True})

    return attacking

# tạo ra những trạng thái của bàn cờ hợp lệ kề cận
def generate_neighbours(board, n):
    neighbours = []
    count_neighbour = 0
    # đổi vị trí con hậu 1 hàng bất kì của bàn cờ để tạo 1 trạng thái mới
    for row in range(n):
        # vị trí con hậu tại hàng đang duyệt
        cur_pos = board[row]
        # Đặt một quân hậu ngẫu nhiên trên hàng hiện tại
        # thay đổi vị trí con hậu tại hàng row vào các vị trí khác trên hàng
        for pos in range(n):
            neighbour = board[:]
            if pos != cur_pos:
                neighbour[row] = pos
                neighbours.append(neighbour)
            count_neighbour = count_neighbour + 1
    return neighbours


def hill_climbing_search(board, size):
    """trả về bàn cờ có trạng thái tốt nhất với trạng thái khởi tạo đưa vào"""

    while True:
        E = []  # danh sách các state của neighbours
        neighbours = []

        current_state = evaluate_state(board, size)  # n^2

        neighbours = generate_neighbours(board, size)  # n^2

        count = 0
        for x in neighbours:  # n^4
            E.append(evaluate_state(x, size))
            count = count + 14
        min_value = min(E)

        # nếu current board đã ở trên đỉnh đồi thì không leo nữa
        if current_state <= min_value:
            return board, current_state

        # Nếu không thì chọn một neighbour trong những neighbour tốt nhất
        else:

          # danh sách index các vị trí kề cận có trạng thái tốt nhất
            best_neighbours = [i for i, x in enumerate(E) if x == min_value]

            # chọn 1 trong số đó
            neighbour = best_neighbours[random.randrange(len(best_neighbours))]

            board = neighbours[neighbour]

def solve_heuristic(n):
    board = []  
    start = time.time()
    restarts = 0
    # số lần restart tối đa nếu chưa tìm được solution
    # lặp càng nhiều đợi càng lâu để chờ kết quả chính xác
    max_restart = int(input("Enter max restart: "))
    while True:

        # khởi tạo board ngẫu nhiên trước khi leo đồi
        board = initialize_state(n)
        solution, state = hill_climbing_search(board, n)
        # Nếu tìm thấy kết quả thì in ra màn hình và kết thúc
        if state == 0:
            end = time.time()
            print("Solution: ")
            printBoard(solution)
            print(solution)
            print("Restarts: ", restarts)
            print("Time taken: ", end - start)
            break
        # nếu kết quả tìm thấy rơi vào cục bộ, lặp lại với 1 board mới
        else:
            restarts += 1
            print("wait: ", restarts)
            if (restarts == max_restart):
                print("Time out! Not found solution! Sorry... Please run again...")
                break


""" Vui lòng comment lại phần giải thuật không dùng để test """
def main():
#----------------DFS----------------#
# N~=20 trong 2 phút
  N = int(input("Enter N: "))
  q = QueenBoard(N)
  start = time.time()
  q.printQueen()
  end = time.time()
  print("Time taken: ", end-start)

#----------------BFS----------------#
# N~=10 trong 8 giây
    # N = int(input('Enter N: '))

    # start = time.time()
    # final = BrFSQueen(N)
    # end = time.time()
    # printBoard(final)
    # print("Time taken: ",end-start)

#---------steepest-ascent-hill-climbing----------#
# N~=60 trong 5 phút
    # n = int(input("Enter N (N ~= 1000): "))
    # solve_heuristic(n)


if __name__ == "__main__":
    main()



