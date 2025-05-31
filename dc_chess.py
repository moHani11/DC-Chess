import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# all the documentation for the code is in the readme file given with the code file
import pygame
pygame.init()

black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (67, 67))
black_queen_small = pygame.transform.scale(black_queen, (41, 41))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (67, 67))
black_king_small = pygame.transform.scale(black_king,(41, 41))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (67, 67))
black_rook_small = pygame.transform.scale(black_rook, (41, 41))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (67, 67))
black_bishop_small = pygame.transform.scale(black_bishop, (41, 41))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (67, 67))
black_knight_small = pygame.transform.scale(black_knight, (41, 41))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (46, 46))
black_pawn_small = pygame.transform.scale(black_pawn, (41, 41))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (67, 67))
white_queen_small = pygame.transform.scale(white_queen, (41, 41))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (67, 67))
white_king_small = pygame.transform.scale(white_king, (41, 41))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (67, 67))
white_rook_small = pygame.transform.scale(white_rook, (41, 41))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (67, 67))
white_bishop_small = pygame.transform.scale(white_bishop, (41, 41))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (67, 67))
white_knight_small = pygame.transform.scale(white_knight, (41, 41))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (46, 46))
white_pawn_small = pygame.transform.scale(white_pawn, (41, 41))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#_______________________________________________________________________________________________
# _______________________________________________________________________________________________

bane = pygame.image.load('assets/villians/bane.png')
bane = pygame.transform.scale(bane, (70, 70))
bane_small = pygame.transform.scale(bane, (45, 45))
joker = pygame.image.load('assets/villians/joker.png')
joker = pygame.transform.scale(joker, (70, 70))
joker_small = pygame.transform.scale(joker, (45, 45))
death_stroke = pygame.image.load('assets/villians/death_stroke.png')
death_stroke = pygame.transform.scale(death_stroke, (70, 70))
death_stroke_small = pygame.transform.scale(death_stroke, (45, 45))
harley_queen = pygame.image.load('assets/villians/harley_queen.png')
harley_queen = pygame.transform.scale(harley_queen, (70, 70))
harley_queen_small = pygame.transform.scale(harley_queen, (45, 45))
black_adam = pygame.image.load('assets/villians/black_adam.png')
black_adam = pygame.transform.scale(black_adam, (70, 70))
black_adam_small = pygame.transform.scale(black_adam, (45, 45))
scarecrow = pygame.image.load('assets/villians/scarecrow.png')
scarecrow = pygame.transform.scale(scarecrow, (50, 50))
scarecrow_small = pygame.transform.scale(scarecrow, (45, 45))

superman = pygame.image.load('assets/heros/superman.png')
superman = pygame.transform.scale(superman, (70, 70))
superman_small = pygame.transform.scale(superman, (45, 45))
batman = pygame.image.load('assets/heros/batman.png')
batman = pygame.transform.scale(batman, (70, 70))
batman_small = pygame.transform.scale(batman, (45, 45))
flash = pygame.image.load('assets/heros/flash.png')
flash = pygame.transform.scale(flash, (70, 70))
flash_small = pygame.transform.scale(flash, (45, 45))
cyborg = pygame.image.load('assets/heros/cyborg.png')
cyborg = pygame.transform.scale(cyborg, (70, 70))
cyborg_small = pygame.transform.scale(cyborg, (45, 45))
wonder_woman = pygame.image.load('assets/heros/wonder.png')
wonder_woman = pygame.transform.scale(wonder_woman, (70, 70))
wonder_woman_small = pygame.transform.scale(wonder_woman, (45, 45))
green_lantern = pygame.image.load('assets/heros/green_lantern.png')
green_lantern = pygame.transform.scale(green_lantern, (50, 50))
green_lantern_small = pygame.transform.scale(green_lantern, (45, 45))

hero_images = [cyborg, wonder_woman, batman, green_lantern, superman, flash]
hero_list = ['cyborg', 'Wonder woman', 'batman', 'greenlantern', 'superman', 'flash']

villian_images = [scarecrow, harley_queen, joker, bane, black_adam, death_stroke]
villian_list = ['scarecrow', 'harley_queen', 'joker', 'bane', 'black_adam', 'death_stroke']



#_______________________________________________________________________________________________
# _______________________________________________________________________________________________


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

screen = pygame.display.set_mode((1200, 550))
pygame.display.set_caption('Welcome')

samll_font = pygame.font.Font('freesansbold.ttf', 20)
font = pygame.font.Font(None, 35)
big_font = pygame.font.Font('freesansbold.ttf', 40)
large_font = pygame.font.Font(None, 60)


guide_text = [
    "WELCOME TO DC CHESS",
    "",
    "Would you want to dive more into the DC world and ","",
     "fight using the actual heros and villians for the fight or ",""
     ,"would you like to use normal chess pieces?",
]

def draw_text(surface, text, pos, font, color="black"):
    lines = text.split('\n')
    y_offset = 10
    for line in lines:
        rendered_text = font.render(line, True, color)
        surface.blit(rendered_text, (pos[0], pos[1] + y_offset))
        y_offset += font.get_height()

# ------------------------------------------------------------------------------    

def villan_guide():
    screen = pygame.display.set_mode((1200, 680))
    pygame.display.set_caption('villian Guide list')
    
    screen.fill((40,30,50))

    guide_running = True
    while guide_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                guide_running = False
        starting_x = 40
        starting_y = 100
        x_offset = 190
        screen.blit(samll_font.render(f"press any key on your keryboard to continue", True, 'red'), (400, 10))
        for i in range(len(black_images)):
            y_offset = 54
            if i%2: y_offset=29
            screen.blit(font.render(f"{villian_list[i]} fights as a : black {piece_list[i]}", True, 'white'), (starting_x-20, starting_y-y_offset))
            screen.blit(pygame.transform.scale(villian_images[i], (200, 230)), (starting_x , starting_y))
            screen.blit(pygame.transform.scale(black_images[i], (150, 150)), (starting_x+ x_offset, starting_y + 20))

            starting_x += 380
            starting_x %= 1180

            if i == 2: starting_y = 400


        pygame.display.flip()

#----------------------------------------------------------------------------------

def hero_guide():
    screen = pygame.display.set_mode((1200, 680))
    pygame.display.set_caption('Hero Guide list')
    
    screen.fill((40,30,50))

    guide_running = True
    while guide_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                guide_running = False
                villan_guide()

        
        starting_x = 40
        starting_y = 100
        x_offset = 190
        screen.blit(samll_font.render(f"press any key on your keryboard to continue", True, 'red'), (400, 10))
        for i in range(len(white_images)):
            y_offset = 54
            if i%2: y_offset=29
            screen.blit(font.render(f"{hero_list[i]} fights as a : white {piece_list[i]}", True, 'white'), (starting_x-20, starting_y-y_offset))
            screen.blit(pygame.transform.scale(hero_images[i], (200, 230)), (starting_x , starting_y))
            screen.blit(pygame.transform.scale(white_images[i], (150, 150)), (starting_x+ x_offset, starting_y + 20))

            starting_x += 380
            starting_x %= 1180

            if i == 2: starting_y = 400
        pygame.display.flip()

# ------------------------------------------------------------------------------

change_images = False
def opening_screen(change_images):
    opening_screen_running = True
    while opening_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = event.pos[0]
                y = event.pos[1]

                if  900 < x <1150 and 30 < y < 160 :
                    opening_screen_running = False

                if  900 < x <1150 and 200 < y < 330 :
                    hero_guide()
                    opening_screen_running = False
                    change_images = True



            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill((170,140,170))

        pygame.draw.rect(screen, (8, 10, 58), [900, 30, 250,  130])
        pygame.draw.rect(screen, (8, 10, 58), [900, 200, 250,  130])

        screen.blit(large_font.render('Normal', True, 'white'), (938, 75))
        screen.blit(large_font.render('DC', True, 'white'), (970, 245))


        for i, line in enumerate(guide_text):
            text_surface = font.render(line, True, "black")
            screen.blit(text_surface, (50, 50 + i * 40))

        pygame.display.flip()
    return change_images

change_images = opening_screen(change_images)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if change_images:
    white_images = [cyborg, wonder_woman, batman, green_lantern, superman, flash]
    small_white_images = [cyborg_small, wonder_woman_small, batman_small, green_lantern_small, superman_small, flash_small]
    black_images = [scarecrow, harley_queen, joker, bane, black_adam, death_stroke]
    small_black_images = [scarecrow_small, harley_queen_small, joker_small, bane_small, black_adam_small, death_stroke_small]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


WIDTH = 900   
HEIGHT = 700
x_edge = 80 * 8
y_edge = 80 * 8


screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')



timer = pygame.time.Clock()
fps = 60

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []



def draw_board():
    pygame.draw.rect(screen, 'gray', [0, y_edge, WIDTH, HEIGHT - y_edge])    
    pygame.draw.rect(screen, (78, 10, 58), [0, y_edge, WIDTH,  HEIGHT - y_edge], 6)
    pygame.draw.rect(screen, (78, 10, 58), [x_edge, 0, WIDTH - x_edge, HEIGHT], 6)
    pygame.draw.rect(screen, (78, 10, 58), [x_edge, y_edge, WIDTH - x_edge, HEIGHT - y_edge])
    screen.blit(big_font.render('FORFEIT', True, 'black'), (710, 660))

    if change_images:
        status_text = ['Heros: Select a Piece to Move!', 'Heros: Select a Destination!',
                    'villians: Select a Piece to Move!', 'villians: Select a Destination!']
    else:
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                        'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, y_edge+20))   
    for i in range(9):
            pygame.draw.line(screen, 'black', (0, 80 * i), (y_edge, 80 * i), 2)
            pygame.draw.line(screen, 'black', (80 * i, 0), (80 * i, x_edge), 2) 
    for i in range(8):
            for j in range(8):
                if i % 2 == 0 and j % 2:
                    pygame.draw.rect(screen, 'black', [i*80, j * 80, 80, 80])
                if i % 2 and j % 2 == 0:
                    pygame.draw.rect(screen, 'black', [i*80, j * 80, 80, 80])

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if index == 0: 
            if change_images: screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 10))
            else:    screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 30))
        else: screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, (30,96,40), [white_locations[i][0] * 80 + 1, white_locations[i][1] * 80 + 1, 80, 80], 3)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])

        if index == 0:
            if change_images: screen.blit(black_images[index], (black_locations[i][0] * 80 + 10, black_locations[i][1] * 80 + 10))
            else: screen.blit(black_images[index], (black_locations[i][0] * 80 + 10, black_locations[i][1] * 80 + 30))
        else: screen.blit(black_images[index], (black_locations[i][0] * 80 + 10, black_locations[i][1] * 80 + 10))
        
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, (178, 30, 98), [black_locations[i][0] * 80 + 1, black_locations[i][1] * 80 + 1, 80, 80], 3)

def draw_dead():

    pygame.draw.line(screen, "black", (x_edge,350), (WIDTH,350), 5)

    dead_black_x_pos = x_edge+10
    dead_black_y_pos = 10

    for i in range(len(captured_pieces_white)):
        index = piece_list.index(captured_pieces_white[i])
   
        screen.blit(small_black_images[index], (dead_black_x_pos + 60*(i) % 240,  dead_black_y_pos + (40*(i) // 160)*55))

    dead_white_x_pos = x_edge+10
    dead_white_y_pos = 370

    for i in range(len(captured_pieces_black)):
        index = piece_list.index(captured_pieces_black[i])
   
        screen.blit(small_white_images[index], (dead_white_x_pos + 60*(i) % 240,  dead_white_y_pos + (40*(i) // 160)*55))
        
def flip_board(white_locations, black_locations):

    flipped_white = []
    for pixel in white_locations:
        flipped_white.append((pixel[0],7-pixel[1]))
    
    flipped_black = []
    for pixel in black_locations:
        flipped_black.append((pixel[0],7-pixel[1]))
    
    return flipped_white, flipped_black




#//////////////////////////////////////////////////////////////////////////////////////

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6 and \
        (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6 and \
        (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations

    for i in range (8):

        if i  == 0:
            x_move = position[0] + 1
            y_move = position[1] + 2
        elif i  == 1:
            x_move = position[0] + 1
            y_move = position[1] - 2
        elif i  == 2:
            x_move = position[0] + 2
            y_move = position[1] + 1
        elif i  == 3:
            x_move = position[0] + 2
            y_move = position[1] - 1
        elif i  == 4:
            x_move = position[0] - 1
            y_move = position[1] + 2
        elif i  == 5:
            x_move = position[0] - 1
            y_move = position[1] - 2
        elif i  == 6:
            x_move = position[0] - 2
            y_move = position[1] + 1
        elif i  == 7:
            x_move = position[0] - 2
            y_move = position[1] - 1

        if 0 <= x_move < 8 and 0 <= y_move < 8  and (x_move, y_move) not in friends_list :  
            moves_list.append((x_move,y_move))
    return moves_list
        
def check_bishop(position, color):
    moves_list = []
    
    if color == "white":
        freinds_list = white_locations
        enemies_list = black_locations
    if color == "black":
        freinds_list = black_locations
        enemies_list = white_locations
    
    for i in range(4):
        chain = 1
        path = True
        if i == 0:
            x_move = 1
            y_move = 1
        elif i == 1:
            x_move = 1
            y_move = -1
        elif i == 2:
            x_move = -1
            y_move = 1
        elif i == 3:
            x_move = -1
            y_move = -1
        
        while(path and 0 <= position[0] + x_move*chain < 8 and 0 <= position[1] + y_move*chain < 8 and \
                (position[0] + x_move*chain, position[1] + y_move*chain ) not in freinds_list):
            moves_list.append((position[0] + x_move*chain, position[1] + y_move*chain ))
            
            if (position[0] + x_move*chain, position[1] + y_move*chain ) in enemies_list: path = False
            chain +=1

        
    return moves_list

def check_queen(position, color):
    moves_list = []
    
    if color == "white":
        freinds_list = white_locations
        enemies_list = black_locations
    if color == "black":
        freinds_list = black_locations
        enemies_list = white_locations
    
    for i in range(8):
        chain = 1
        path = True
        if i == 0:
            x_move = 0
            y_move = 1
        elif i == 1:
            x_move = 0
            y_move = -1
        elif i == 2:
            x_move = 1
            y_move = 0
        elif i == 3:
            x_move = -1
            y_move = 0
        elif i == 4:
            x_move = 1
            y_move = 1
        elif i == 5:
            x_move = 1
            y_move = -1
        elif i == 6:
            x_move = -1
            y_move = 1
        elif i == 7:
            x_move = -1
            y_move = -1
        
        while(path and 0 <= position[0] + x_move*chain < 8 and 0 <= position[1] + y_move*chain < 8 and \
                (position[0] + x_move*chain, position[1] + y_move*chain ) not in freinds_list):
            moves_list.append((position[0] + x_move*chain, position[1] + y_move*chain ))
            
            if (position[0] + x_move*chain, position[1] + y_move*chain ) in enemies_list: path = False
            chain +=1
    return moves_list

def check_king(position, color):
    moves_list = []
    
    if color == "white":
        freinds_list = white_locations
        enemies_options = check_for_king_options(black_pieces, black_locations, 'black')
    if color == "black":
        freinds_list = black_locations
        enemies_options = check_for_king_options(white_pieces, white_locations, 'white')
    
    for i in range(8):
        if i == 0:
            x_move = 0
            y_move = 1
        elif i == 1:
            x_move = 0
            y_move = -1
        elif i == 2:
            x_move = 1
            y_move = 0
        elif i == 3:
            x_move = -1
            y_move = 0
        elif i == 4:
            x_move = 1
            y_move = 1
        elif i == 5:
            x_move = 1
            y_move = -1
        elif i == 6:
            x_move = -1
            y_move = 1
        elif i == 7:
            x_move = -1
            y_move = -1
        
        if  0 <= position[0] + x_move< 8 and 0 <= position[1] + y_move< 8 and \
                (position[0] + x_move, position[1] + y_move ) not in freinds_list:
        
             
            if (position[0] + x_move, position[1] + y_move ) not in [option for sublist in enemies_options for option in sublist]:
                moves_list.append((position[0] + x_move, position[1] + y_move ))
            
    return moves_list        

def king_pawn_check(position, color):
    moves_list = []
    moves_list.append((position[0] + 1, position[1] + 1))
    moves_list.append((position[0] - 1, position[1] + 1))
    return moves_list


def check_for_king_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = king_pawn_check(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

#/////////////////////////////////////////////////////////////////////////////////////////

def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves):
    if turn_step < 2:
        color = (30,96,40)
    else:
        color = (178, 30, 98)
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 80 + 40, moves[i][1] * 80 + 40), 5)

def draw_game_over():
    pygame.draw.rect(screen, (178, 30, 98), [200, 200, 400, 70])
    screen.blit(samll_font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(samll_font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            black_options = check_for_king_options(black_pieces, black_locations, 'black') 
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, (30,96,40), [white_locations[king_index][0] * 80 + 1,
                                                              white_locations[king_index][1] * 80 + 1, 80, 80], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            white_options = check_for_king_options(white_pieces, white_locations, 'white')
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, (178, 30, 98), [black_locations[king_index][0] * 80 + 1,
                                                               black_locations[king_index][1] * 80 + 1, 80, 80], 5)

white_options = []

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

counter = 0
winner = ''
game_over = False

run = True

while run:
    timer.tick(fps)
    screen.fill("dark gray")   
    draw_board()
    draw_pieces() 
    draw_dead()
    draw_check()

    counter += 1
    counter %= 30


    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 80
            y_coord = event.pos[1] // 80
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    white_locations, black_locations = flip_board(white_locations, black_locations)
                    
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')

            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)

                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    white_locations, black_locations = flip_board(white_locations, black_locations)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        
        if change_images: 
            if winner == 'white':
                winner = "Heros"
            if winner == "black":
                winner = "villians"

        draw_game_over()

    pygame.display.flip()
pygame.quit()