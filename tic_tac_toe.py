def ticTacToeWinner(moves, n):
    board=[]
    for i in range(3):
        board.append([""]*3)
    for i,(r,c) in enumerate(moves):
        if i %2==0:
            board[r][c]="X"
        else:
            board[r][c]="0"
    
    def check(symbol):
        for i in range(3):
            if board[i][0]==board[i][1]==board[i][2]==symbol:
                return True
        for i in range(3):
            if board[0][i]==board[1][i]==board[2][i]==symbol:
                return True
        if board[0][0]==board[1][1]==board[2][2]==symbol:
            return True
        if board[0][2]==board[1][1]==board[2][0]==symbol:
            return True
    if check("X"):
        return "player1"
    if check("0"):
        return "player2"
    if len(moves)<9:
        return "uncertain"
    return "draw"

n=int(input("Enter number of moves"))
moves=[]
for i  in range(n):
    r,c=map(int,input().split())
    moves.append((r,c))
    
print("Result is ",ticTacToeWinner(moves,n))