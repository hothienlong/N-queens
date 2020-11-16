import time
import random


def initialize_state(board, size):
    # generate random board
    for i in range(size):
        board.append(random.randint(0, size-1))
    #print_board(board)
    #print(board)

    return board


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


def generate_neighbours(node, n):

    neighbours = []

    # for each row, move node to each other possible position
    for row in range(n):

        # get current position
        curr_pos = node[row]

        # place a queen on each possible position in the current row
        # and skip the position where it originally was
        # and append the generated neighbour to the neighbours array
        for pos in range(n):
            neighbour = node[:]
            if pos != curr_pos:
                neighbour[row] = pos
                neighbours.append(neighbour)

    #print("Total neighbours: ", len(neighbours))
    return neighbours


def hill_climbing_search(current, size):
    """returns the best configuration it can find"""

    while True:

        E = [] #danh sách các state của neighbours
        neighbours = []

        current_state = evaluate_state(current, size)
        #print("current state = ", current_state)

        #print("Current board:")
        # print_board(current)

        neighbours = generate_neighbours(current, size)

        for x in neighbours:
            E.append(evaluate_state(x, size))

        min_value = min(E)

        # if the current node has a better state than the best neighbour, return the current node
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

    while True:

        # generate a random initial board and pass it to the hill climbing function
        board = initialize_state(board, n)
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

        # if not a goal, restart with a new random board
        else:
            restarts += 1


if __name__ == "__main__":
    main()