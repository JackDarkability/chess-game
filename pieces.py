class piece:

    def __init__(self,colour,position_x,position_y,image) -> None:
        self.colour = colour
        self.position_x = position_x
        self.position_y = position_y
        self.image = image

    def get_possible_moves(board):
        '''
        Returns list of possible positions that the piece can move to
        (To mirror the highlighting of when you click on a piece in chess.com)
        '''
        pass


    def is_empty(self,board,position_x,position_y):
        
        if(board[position_x,position_y]==None):
            return True
        
        else:
            return False


class pawn(piece):

    def __init__(self,colour,position_x,position_y,image):

        super().__init__(colour,position_x,position_y,image)

        # Get how position_y changes with movement based on colour (moving up or down board)
        if(self.colour == "w"):
            self.direction = 1

        else:
            self.direction = -1
        
        self.notation_letter = ""


    def at_end_of_board(self):

        '''
        Check if piece at the end of the board (for promoting etc)
        '''

        if(self.position_y == 7 or self.position_y==0):
            return True
        
        else:
            return False
        

    def get_possible_moves(self,board):
        '''
        Returns list of possible positions that the piece can move to
        (To mirror the highlighting of when you click on a piece in chess.com)
        '''

        moves = []

        # Move forward
        if (self.at_end_of_board(board)==False) and (board.is_free(self.position_x,self.position_y+self.direction)):
            moves.append((self.position_x,self.position_y+self.direction))
        
        # Take diagonally right
        if (board.has_enemy(self.position_x+1,self.position_y+self.direction,self.colour)):
            moves.append((self.position_x+1,self.position_y+self.direction))

        # Take diagonally left
        if (board.has_enemy(self.position_x-1,self.position_y+self.direction,self.colour)):
            moves.append((self.position_x-1,self.position_y+self.direction))

        
        # TODO add en passant

        return moves



class rook(piece):

    def __init__(self,colour,position_x,position_y,image):

        super().__init__(colour,position_x,position_y,image)
        self.notation_letter = "r"

    
    def get_possible_moves(self,board):
        '''
        Returns list of possible positions that the piece can move to
        (To mirror the highlighting of when you click on a piece in chess.com)
        '''
        
        moves = []

        # Moving right
        for i in range(self.position_x+1,8):
            if board.is_free(i,self.position_y):
                moves.append((i,self.position_y))
            
            elif board.has_enemy(i,self.position_y,self.colour):
                moves.append((i,self.position_y))
                break # Can't go further if there is enemy

            else:
                break # Has friendly

        #Moving Up
        for i in range(self.position_y+1,8):
            
            if board.is_free(self.position_x,i):
                moves.append((self.position_x,i))
            
            elif board.has_enemy(self.position_x,i,self.colour):
                moves.append((self.position_x,i))
                break # Can't go further if there is enemy

            else:
                break # Has friendly
        
        #Moving Left
        for i in range(self.position_x-1,-1,-1):

            if board.is_free(i,self.position_y):
                moves.append((i,self.position_y))
            
            elif board.has_enemy(i,self.position_y,self.colour):
                moves.append((i,self.position_y))
                break # Can't go further if there is enemy

            else:
                break # Has friendly

        # Moving Down
        for i in range(self.position_y+1,-1,-1):
            
            if board.is_free(self.position_x,i):
                moves.append((self.position_x,i))
            
            elif board.has_enemy(self.position_x,i,self.colour):
                moves.append((self.position_x,i))
                break # Can't go further if there is enemy

            else:
                break # Has friendly


        return moves


class bishop(piece):

    def __init__(self,colour,position_x,position_y,image):

        super().__init__(colour,position_x,position_y,image)
        self.notation_letter = "b"

    
    def get_possible_moves(self,board):
        '''
        Returns list of possible positions that the piece can move to
        (To mirror the highlighting of when you click on a piece in chess.com)
        '''
        
        moves = []

        # Moving up right
        amount_up = 1
        for i in range(self.position_x+1,8):

            if board.is_free(i,self.position_y+amount_up):
                moves.append((i,self.position_y+amount_up))
            
            elif board.has_enemy(i,self.position_y+amount_up,self.colour):
                moves.append((i,self.position_y+amount_up))
                break # Can't go further if there is enemy
            
            else:
                break # Has friendly

            amount_up+=1


        # Moving up left
        amount_up = 1
        for i in range(self.position_x-1,-1,-1):
            if board.is_free(i,self.position_y+amount_up):
                moves.append((i,self.position_y+amount_up))
            
            elif board.has_enemy(i,self.position_y+amount_up,self.colour):
                moves.append((i,self.position_y+amount_up))
                break # Can't go further if there is enemy

            else:
                break # Has friendly

            amount_up+=1

        
        #Moving down right
        amount_down = 1
        for i in range(self.position_x+1,8):
            if board.is_free(i,self.position_y-amount_down):
                moves.append((i,self.position_y-amount_down))
            
            elif board.has_enemy(i,self.position_y-amount_down,self.colour):
                moves.append((i,self.position_y-amount_down))
                break # Can't go further if there is enemy

            else:
                break # Has friendly
            amount_down +=1


        # Moving down left
        amount_down = 1
        for i in range(self.position_x-1,-1,-1):

            if board.is_free(i,self.position_y-amount_down):
                moves.append((i,self.position_y-amount_down))
            
            elif board.has_enemy(i,self.position_y-amount_down,self.colour):
                moves.append((i,self.position_y-amount_down))
                break # Can't go further if there is enemy

            else:
                break # Has friendly

            amount_down +=1


        
        return moves


class queen(piece):

    def __init__(self,colour,position_x,position_y,image):
        super().__init__(colour,position_x,position_y,image)
        self.notation_letter = "q"

    def get_possible_moves(self,board):

        # Queen moves is just the combination of rook and bishop moves
        temp_rook = rook(self.colour,self.position_x,self.position_y,self.image)
        temp_bishop = bishop(self.colour,self.position_x,self.position_y,self.image)

        moves = temp_rook.get_possible_moves(board) + temp_bishop.get_possible_moves(board)

        return moves


class knight(piece):

    def __init__(self,colour,position_x,position_y,image):
        super().__init__(colour,position_x,position_y,image)
        self.notation_letter = "n"

    def get_possible_moves(self,board):

        moves = []

        moves.append((self.position_x-2,self.position_y+1))
        moves.append((self.position_x+2,self.position_y+1))
        moves.append((self.position_x+2,self.position_y-1))
        moves.append((self.position_x-2,self.position_y-1))

        moves.append((self.position_x+1,self.position_y+2))
        moves.append((self.position_x-1,self.position_y+2))
        moves.append((self.position_x+1,self.position_y-2))
        moves.append((self.position_x-1,self.position_y-2))

        valid_moves = []

        for i in moves:
            if(i[0]<0 or i[0]>7 or i[1]<0 or i[1]>7):
                continue

            elif(board.is_free(i[0],i[1]) == False):
                continue

            else:
                valid_moves.append(i)
    
        return valid_moves



class king(piece):

    def __init__(self,colour,position_x,position_y,image):
        super().__init__(colour,position_x,position_y,image)
        self.notation_letter = "k"

    def get_possible_moves(self,board):

        moves = []

        # All right side moves
        moves.append((self.position_x+1,self.position_y+1))
        moves.append((self.position_x+1,self.position_y))
        moves.append((self.position_x+1,self.position_y-1))

        # All left side moves
        moves.append((self.position_x-1,self.position_y+1))
        moves.append((self.position_x-1,self.position_y))
        moves.append((self.position_x-1,self.position_y-1))

        # Up and down
        moves.append((self.position_x,self.position_y+1))
        moves.append((self.position_x,self.position_y-1))

        valid_moves=[]
        for i in moves:
            if(i[0]<0 or i[0]>7 or i[1]<0 or i[1]>7):
                continue

            elif(board.is_free(i[0],i[1]) == False):
                continue

            else:
                valid_moves.append(i)
    
        return valid_moves


