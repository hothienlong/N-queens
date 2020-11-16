import time
import random

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

def main():
    # Nhập số quân hậu
    n = int(input("Enter N: "))
    solve_heuristic(n)
    
    


    

if __name__ == "__main__":
    main()