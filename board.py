class board:
    def __init__(self,starting_layout) -> None:
        self.layout = starting_layout
        

    def is_free(self,position_x,position_y):
        
        if(self.layout[position_x][position_y]==None):
            return True
        
        else:
            return False
    

    def has_enemy(self,position_x,position_y,colour):

        if colour == "w":
            enemy_colour = "b"

        else:
            enemy_colour = "w"
        
        return (self.layout[position_x][position_y].colour == enemy_colour)