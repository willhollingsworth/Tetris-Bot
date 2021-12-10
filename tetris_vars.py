tetris_screen_start = (503,360)
tetris_screen_size = (261,522)

tetris_screen = (tetris_screen_start[0],tetris_screen_start[1],
                tetris_screen_start[0] + tetris_screen_size[0],
                tetris_screen_start[1] + tetris_screen_size[1],
                )
tetris_grid = (10,20)


# realative coordinates for each peice 
# x -->   Y ^
block_l = [[0,1],[1,-1],[1,0]]
block_t = [[1,0],[-1,1],[-1,-1]]
block_i = [[0,1],[0,1],[0,1]]
block_t = [[0,1],[1,-1],[-2,0]]
block_o = [[0,1],[1,-1],[0,1]]
block_s = [[1,0],[0,1],[1,0]]
block_z = [[-1,0],[0,1],[-1,0]]