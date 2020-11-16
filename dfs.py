import numpy as np
import time
#Giải được cỡ N ~= 25
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
    size = len(queenPositons)
    for i in range(size):
      for j in range(size):
        #Xét hàng i: nếu vị trí cột đang duyệt ánh xạ trùng với con hậu đã đánh trên bàn cờ thì in Q
        if(j == queenPositons[i]):
          print("Q",end = " ")
        else:
          print(".",end = " ")
      print("\n") 




  def printQueen(self):
    self.__recursiveQueen(self.queenPositons, self.N, 0) 
    self.__printQueen(self.queenPositons, self.N)


def main():
  N = int(input("Enter N: "))
  q = QueenBoard(N)
  start = time.time()
  q.printQueen()
  end = time.time()
  print("Time taken: ", end-start)

if __name__ == "__main__":
    main()



