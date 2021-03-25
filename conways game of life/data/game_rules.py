
def conways_game(dic,sizex,sizey,tile_size):
    """
    needs a dictionary with all the positios in str forma "x_y" = (state of the cell), the size of the screen width, height, size of the tiles in pixels
    example: conways_game(dictionary,600,600,16)
    outputs a dictionary with all the updated positions of the cells in the game
    """
    game = dic.copy()
    y = 0
    for y in range(sizey//tile_size):
        x = 0
        for x in range(sizex//tile_size):            
            elementos = str(x * tile_size) + "_" + str(y * tile_size)
            aux = 0
            # comprobacion de vecinos
            if x > 0:
                if dic[str((x-1) * tile_size) + "_" + str(y * tile_size)] == 1:
                    aux += 1

            if x < (sizex//tile_size) - 1:
                if dic[str((x+1) * tile_size) + "_" + str(y * tile_size)] == 1 :
                    aux += 1

            if y > 0:
                if dic[str(x * tile_size) + "_" + str((y-1) * tile_size)] == 1 :
                    aux += 1

            if y < sizey//tile_size-1:
                if dic[str(x * tile_size) + "_" + str((y+1) * tile_size)] == 1 :
                    aux += 1

            if x > 0 and  y > 0:
                if dic[str((x-1) * tile_size) + "_" + str((y-1) * tile_size)] == 1 :
                    aux += 1

            if x < sizex//tile_size-1 and  y > 0:
                if dic[str((x+1) * tile_size) + "_" + str((y-1) * tile_size)] == 1 :
                    aux += 1

            if x > 0 and y < sizey//tile_size-1:
                if dic[str((x-1) * tile_size) + "_" + str((y+1) * tile_size)] == 1 :
                    aux += 1

            if x < sizex//tile_size-1 and y < sizey//tile_size-1:
                if dic[str((x+1) * tile_size) + "_" + str((y+1) * tile_size)] == 1 :
                    aux += 1
            #reglas del juego para saber si muere o no
            if  dic[elementos] == 1 and (aux == 2 or aux == 3):
                game[elementos] = 1
            elif  dic[elementos] == 0 and aux == 3:
                game[elementos] = 1
            elif dic[elementos] == 1:game[elementos] = 0
      
    return game
