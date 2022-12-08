# N-Queen using Hill Climbing
import random


def generateBoard(n):

    m = []
    for i in range(n):
        q = (random.randint(0, n-1))
        m.append(q)
        m=[1,7,4,8,0,9,1,5,2,6]
    return m


def solve(board):

    cur = board
    cost = heuristic(board)

    while(cost != 0):
        cur = bestNeighbour(board, cost)
        if(cur == None):
            generateBoard(board)
            cur = board
        cost = heuristic(cur)
    print_(cur)


def heuristic(board):

    d = 0
    n = len(board)

    for k in range(n):
        i, j = k, board[k]
        for l in range(k+1, n):
            p, q = l, board[l]
            if(q == j or (i+j) == (p+q) or (j-i) == (q-p)):
                d += 1
    return d


def print_(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if(m[i] == j):
                print("Q", end=" ")
            else:
                print("_", end=" ")
        print()


def bestNeighbour(board, cost):
    mini = cost
    ans = None
    n = len(board)

    for i in range(n):
        temp = board[i]
        for j in range(n):
            board[i] = j
            cost = heuristic(board)
            if(cost < mini):
                ans = board.copy()
        board[i] = temp
    return ans


if __name__ == "__main__":
    print("Enter n: ")
    n = int(input())
    b = generateBoard(n)

    print("\nBefore: ")
    print_(b)
    print("\n\nAfter: ")
    solve(b)
