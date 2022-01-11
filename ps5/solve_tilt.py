def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    '''
    M = []
    xt, yt = t
    P = {B: None}
    levels = [[B]]
    directions = ['up', 'down', 'left', 'right']

    # While previous level is not empty, conduct BFS on the level
    while levels[-1]:
        
        curr_level = []
        prev_level = levels[-1]

        # For each B in previous level, look into the 4 successors and add them to curr level
        for B in prev_level:
            for direction in directions:
                B_ = move(B, direction)

                # If B_ has not been traversed yet 
                if(B_ not in P):

                    # B is B_'s predecessor, and add B_ to curr level
                    P[B_] = [B, direction]
                    curr_level.append(B_)

                    # If B_ is solution, traverse back to source B and insert moves on the way
                    if B_[yt][xt] == 'o':

                        while P[B_]:
                            M.insert(0, P[B_][1])
                            B_ = P[B_][0]
                        
                        return M

        # Add curr level to level sets
        levels.append(curr_level)
    
    return M

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + ('-'*n) + '+']
    for row in B:
        rows.append('|' + ''.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S
