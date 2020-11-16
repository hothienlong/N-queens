import time
import random


def initialize_state(size):
    new_board = []
    # generate random board
    for i in range(size):
        new_board.append(random.randint(0, size-1))

    return new_board


def evaluate_state(node, n):

    attacking = 0
    # check if theres a queen in the same column or left/right diagonals
    # and increment the attacking variable
    for i in range(n-1):
        for j in range(i+1, n):
            if node[i] == node[j] or node[i] == (node[j] + (j-i)) or \
                    node[i] == (node[j] + (i-j)):
                attacking += 1

    return attacking

#tạo ra những trạng thái của bàn cờ hợp lệ kề cận
def generate_neighbours(board, n):

    neighbours = []
    count_neighbour = 0
    # đổi 2 hàng bất kì của bàn cờ để tạo 1 bàn cờ mới
    for row in range(n):

        # vị trí con hậu tại hàng đang duyệt
        cur_pos = board[row]

        # place a queen on each possible position in the current row
        # and skip the position where it originally was
        # and append the generated neighbour to the neighbours array
        #thay đổi vị trí con hậu tại hàng row vào các vị trí khác trên hàng
        for pos in range(n): 
            neighbour = board[:]
            if pos != cur_pos:
                neighbour[row] = pos
                neighbours.append(neighbour)
                # print("neighbour: "  + str(len(neighbour)))
            count_neighbour = count_neighbour + 1
            # print("count neighbour ", count_neighbour)

    
    return neighbours


def hill_climbing_search(current, size):
    """returns the best configuration it can find"""

    while True:
        
        E = [] #danh sách các state của neighbours
        neighbours = []

        current_state = evaluate_state(current, size) #n^2
        

        # print("current: "  + str(len(current)))
        neighbours = generate_neighbours(current, size) #n^2
        
        count = 0
        for x in neighbours: #n^4
            E.append(evaluate_state(x, size))
            count = count + 1
            # print("append??",count)
        print("after append")

        min_value = min(E)

        print("current state: ", current_state)
        # nếu current board đã ở trên đỉnh đồi thì không leo nữa
        if current_state <= min_value:
            return current, current_state

        # otherwise pick a random neighbour from the best neighbours and assign the best neighbour to the current node and go back to start of the loop
        else:
            #danh sách index các vị trí kề cận có trạng thái tốt nhất
            best_neighbours = [i for i, x in enumerate(E) if x == min_value]
            #print("Min indices \n", best_neighbours)

            #chọn 1 trong số đó
            neighbour = best_neighbours[random.randrange(len(best_neighbours))]
            #print("random min neighbouyr = ", neighbour)

            current = neighbours[neighbour]


def print_board(node):
    """prints a board"""

    for row in range(len(node)):
        line = ""
        for col in range(len(node)):
            if node[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")


def main():

    # get user input for n
    n = int(input("Enter N: "))
    board = []
    restarts = 0
    start = time.time()

    #số lần restart tối đa nếu chưa tìm được solution
    max_restart = int(input("Enter max restart (lặp càng nhiều đợi càng lâu để chờ kết quả chính xác): "))
    while True:

        # print("initialiaze")
        #khởi tạo board ngẫu nhiên trước khi leo đồi
        board = initialize_state(n)
        solution, state = hill_climbing_search(board, n)

        # if solution is a goal state, print solution and break out of loop
        if state == 0:
            end = time.time()
            print("Solution: ")
            print_board(solution)
            print(solution)
            print("Restarts: ", restarts)
            print("Time taken: ", end-start)
            break

        # nếu kết quả tìm thấy rơi vào cục bộ, lặp lại với 1 board mới
        else:
            restarts += 1
            print("wait: ", restarts)
            if(restarts == max_restart):
              print("Time out! Not found solution! Sorry... Please run again...")
              break


if __name__ == "__main__":
    main()