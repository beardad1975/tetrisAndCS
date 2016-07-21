
class Block:
    turn_delta = ( 
            ((0,0),(0, 0),(0,0),(0,0)),
            ((0,0),(0, 0),(0,0),(0,0)),
            ((0,0),(0, 0),(0,0),(0,0)),
           ((0,0),(0, 0),(0,0),(0,0)), 
           )
    color_num = 1
    block_type = '.'   

    def __init__(self, row, col, turn_type=0):
        self.ref_pos = [row, col]
        self.turn_type = turn_type

    def tellDelta(self, target='default'):
        if target == 'default':
            return self.turn_delta[self.turn_type]
        elif target == 'clockwise':
            return self.turn_delta[(self.turn_type + 1) % 4]
        elif target == 'counter':
            return self.turn_delta[(self.turn_type - 1) % 4]

    def tellAllPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta():
            all_pos.append([row + row_delta, col + col_delta])  
        return all_pos

    def tellRightPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta():
            all_pos.append([row + row_delta, col + col_delta + 1])  
        return all_pos

    def moveRight(self):
        row, col = self.ref_pos
        self.ref_pos = [row, col+1]

    def tellLeftPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta():
            all_pos.append([row + row_delta, col + col_delta - 1])  
        return all_pos

    def moveLeft(self):
        row, col = self.ref_pos
        self.ref_pos = [row, col-1]

    def tellDownPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta():
            all_pos.append([row + row_delta + 1, col + col_delta ])  
        return all_pos
    
    def moveDown(self):
        row, col = self.ref_pos
        self.ref_pos = [row + 1, col]

    def tellClockwisePos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta(target='clockwise'):
            all_pos.append([row + row_delta, col + col_delta ])  
        return all_pos

    def tellClockwisePushRightPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta(target='clockwise'):
            all_pos.append([row + row_delta, col + col_delta + 1 ])  
        return all_pos

    def turnClockwise(self):
        self.turn_type = ( self.turn_type + 1) % 4

    def tellCounterPos(self):
        row , col = self.ref_pos
        all_pos = []
        for row_delta, col_delta in self.tellDelta(target='counter'):
            all_pos.append([row + row_delta, col + col_delta ])  
        return all_pos

    def turnCounter(self):
        self.turn_type = ( self.turn_type - 1) % 4
        
    def draw_shape(self):
        tmp_board = []
        for i in range(7):
            tmp_board.append([0]*7) 
        
        for row, col in self.turn_delta[self.turn_type]:
            tmp_board[row+3][col+3] = 1

        print(' '*7, end='')
        for i in range(-3,4) :
            print( '{:2d}'.format(i) , end='')
        print()

        for j, row in  enumerate(tmp_board, -3):
            print(' '*4, format(j,'2') , end='')
            for col in row :
                if col >= 1:
                    print('■', end='')
                    
                else:
                    print('  ', end='')
                    
            print()

        print(' '*7, end='')
        print()    

class T_Shape(Block):
    
    turn_delta = ( 
            ((0,-1),(0, 0),(0,1),(1,0)),
            ((0,1),(1, 0),(1,1),(2,1)),
            ((0,0),(1, -1),(1,0),(1,1)),
           ((0,0),(1, 0),(1,1),(2,0)), 
           )
    color_num = 1
    block_type = 'T'


       
class O_Shape(Block):
    turn_delta = ( 
           ((0,0),(0, 1),(1,0),(1,1)), 
           ((0,0),(0, 1),(1,0),(1,1)), 
           ((0,0),(0, 1),(1,0),(1,1)), 
           ((0,0),(0, 1),(1,0),(1,1)), 
           )
    color_num = 2
    block_type = 'O'

        

class I_Shape(Block):
    turn_delta = ( 
           ((0,0),(1, 0),(2,0),(3,0)), 
           ((1,-1),(1, 0),(1,1),(1,2)), 
           ((0,0),(1, 0),(2,0),(3,0)), 
           ((1,-1),(1, 0),(1,1),(1,2)), 
           )
    color_num = 3
    block_type = 'I'


        
class L_Shape(Block):
    turn_delta = ( 
           ((0,0),(1,0),(2,0),(2,1)), 
           ((1,0),(1,1),(1,2),(2,0)), 
           ((1,0),(1,1),(2,1),(3,1)), 
           ((1,2),(2,0),(2,1),(2,2)), 
           )
    color_num = 4
    block_type = 'L'



class J_Shape(Block):
    turn_delta = ( 
           ((0,1),(1,1),(2,0),(2,1)), 
           ((1,0),(2,0),(2,1),(2,2)), 
           ((0,0),(0,1),(1,0),(2,0)), 
           ((0,0),(0,1),(0,2),(1,2)), 
           )
    color_num = 5
    block_type = 'J'



class S_Shape(Block):
    turn_delta = ( 
           ((0,0),(1,0),(1,1),(2,1)), 
           ((1,0),(1,1),(2,-1),(2,0)), 
           ((0,0),(1,0),(1,1),(2,1)), 
           ((1,0),(1,1),(2,-1),(2,0)), 
           )
    color_num = 6
    block_type = 'S'



class Z_Shape(Block):
    turn_delta = ( 
           ((0,1),(1,0),(1,1),(2,0)), 
           ((1,0),(1,1),(2,1),(2,2)), 
           ((0,1),(1,0),(1,1),(2,0)), 
           ((1,0),(1,1),(2,1),(2,2)), 
           )
    color_num = 7
    block_type = 'Z'


