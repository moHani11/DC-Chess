# documentation For The Chess code

# We first start by importing **pyGame library** 
pyGame library: is responsible for all the GUI in the game 

## loading images

### using pygame.image.load and  pygame.transform.scale functions
we start loading the images for all the pieces we will use on our chess board 
then, we start scaling those images so they can fit well inside our screen

- for every side we make two lists for small scaled images used on our board and samller scaled images for the pieces the will be captured and put aside
> white_images, small_white_images, black_images, small_black_images


- the heros and villians lists work the same as the normal pieces in case the user chooses the DC mode of the chess so we can replace the images for the normal pieces by the characters images.

---
# Initial Window
code: 
> screen = pygame.display.set_mode((1200, 550))
>pygame.display.set_caption('Welcome')

>samll_font = pygame.font.Font('freesansbold.ttf', 20)
>font = pygame.font.Font(None, 35)
>big_font = pygame.font.Font('freesansbold.ttf', 40)
>large_font = pygame.font.Font(None, 60)

- we set the initial window size to be (1200, 550) and by using set_caption('Welcome') we set the window's caption to welcome 
- then we start initializing different sizes of fonts to use through put the code
---

### guide_text: is the text i am going to display on the initial welcome window and the draw_text function is using the pygame function to display thet text


## opening_screen(change_images) : is the function responsible for displaying the initial window function 
code:
>screen.fill((170,140,170))

>       pygame.draw.rect(screen, (8, 10, 58), [900, 30, 250,  130])
>       pygame.draw.rect(screen, (8, 10, 58), [900, 200, 250,  130])

>       screen.blit(large_font.render('Normal', True, 'white'), (938, 75))
>       screen.blit(large_font.render('DC', True, 'white'), (970, 245))

- we start putting some color in the bacground and draw two rectangles with "normal" and "DC" written in them so the player can choose which mode he wants to play

# Choosing Game Mode
- we use event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

which tells if the user left-clicked on the window 

- x = event.pos[0], y = event.pos[1]
then we get if position of that click

- if the player clicked on the DC box we change the boolean value of change_images to true, and we open two extra windows by calling these functions:["hero_guide()", "villians_guide()"]

which will show the user The DC chracters as chess pieces 


code: 
> if change_images:
    white_images = [cyborg, wonder_woman, batman, green_lantern, superman, flash]
    small_white_images = [cyborg_small, wonder_woman_small, batman_small, green_lantern_small, superman_small, flash_small]
    black_images = [scarecrow, harley_queen, joker, bane, black_adam, death_stroke]
    small_black_images = [scarecrow_small, harley_queen_small, joker_small, bane_small, black_adam_small, death_stroke_small]

- by changing the boolean value of change_images to true we cange the chess pieces lists to contain the images of the DC characters so we can activate the Dc mode

---
# Main Code

code:
> WIDTH = 900   
HEIGHT = 700
x_edge = 80 * 8
y_edge = 80 * 8


> screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!') # setting the wondow name to 'Two-Player Pygame Chess!'

- we initialize the global variables WIDTH and HEIGHT which refers to the width and the height of the main game window 
- I also declared two variables x_edge, y_edge which refer to the chess board edges 


# Declairing Lists
code:
> black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

> captured_pieces_white = []
captured_pieces_black = []
valid_moves = []

 

- for each side we initialize two list one containg the name of the all the pieces that are still un_captured and another list which contains the positions of those pieces

- we also initialize two empty lists for both side contains the captured pieces 

- valid_moves will be filled with the moves the piece you selected can take

### declaring the variable turn_step to know which side's turn is it

# Drawing The Board

-  the **draw_board** function uses pygame functions to draw the board's essential features as the board boxes, the part where capture piesces go, the forfeat box and the bottom box which displays the text showing which players turn is it.

- the **draw_pieces**  function

code:
> def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if index == 0: 
            if change_images: screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 10))
            else:    screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 30))
        else: screen.blit(white_images[index], (white_locations[i][0] * 80 + 10, white_locations[i][1] * 80 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, (30,96,40), [white_locations[i][0] * 80 + 1, white_locations[i][1] * 80 + 1, 80, 80], 3)

- it takes the uncaptured piesces from the  the position of the (white_pieces, black_pieces)list and take their corresponding location on the grid from the (white_locations , black_locations) list so it can display the image of each peice in its correct position, the function also display acolored box around the peice that is selected

- the **draw_dead** function draws the captured peices on the right side of the board  by using two counters so it can display them one next to another and go to a new line when it is the end of the precieving line.

- the flip_board() function 
code: 
> def flip_board(white_locations, black_locations):

    flipped_white = []
    for pixel in white_locations:
        flipped_white.append((pixel[0],7-pixel[1]))
    
    flipped_black = []
    for pixel in black_locations:
        flipped_black.append((pixel[0],7-pixel[1]))
    
    return flipped_white, flipped_black
 - it works by making the y position of the piece equal to 7 - the previous y-poition so it can reverse its vertical on the grid

# Pieces Functionality

### there is a function for each peice on the board so it can determine the possible moves for this peice we will go through some of them:

code:
> def check_queen(position, color):
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

- since the queen has 8 possible directions we go through each conition of those we define a **path boolean** which will be True in case of not finding any peice in in that direction and while we are still on the grid and while the Path is true we add the **chain variable** so we can check a further box in that direction.

### * notice that the rook and bishop use a simillar algorithm except that they go in only four directions (horizontal, vertical ) for the rook (diaginal) for the bishop *

code: 
> def check_pawn(position, color):
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

-  for the pawn we check
1. if no pieces infront of it so it can move one forward move

2. if its in its inital place and no pieces infront of it with two boxes so it can move two forward moves 

3. if there is an enemy piece infront of it diagonally so it can capture them 

code:
> def check_king(position, color):
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

- just like the queen the king moves in 8 directions but it doesnt need the **path and chain variables** as it cant move more than one block in any direction

- we also call the check_for_king_options() function to get the options for the oponent pieces so we can make sure that the king isnt going into a place where it can be captured immediatly

### NOTE: check_for_king_options() works the same as check_options() but for the pawn it uses a different function for check its optiions **king_pawn_check()** which will check for just his diagonal options tnot the forward one as a pawn can not capture any piec infront of it.

---
- the **check_options()** function is used to make a list which consists of all the list of valid moves for each piece in the list and it takes the color of the pieces we want to check for its options.

- **the check_valid_moves**()
takes the valid options for the selcted piece of the all available moves list cearted by **check_options()** and put it in the valid_options list so when clicked on a piece you can see the valid options for that piece it calls the draw_valid function to draw those optinos .

- the **draw_check** function draws a flashing colored box around the king when it is being checked 

---
---
code: 
> black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

> winner = ''
game_over = False


- we fill each side's avilable options by calling the check_options mentioned before

- and the winner string is initialized empty and if some color wins it gets put in this string variable declairing it won

- game_over is a boolean that datermines weather the game is over or not 

# Main Run Loop

code:
> while run:
    timer.tick(fps)
    screen.fill("dark gray")   
    timer.tick(fps)
    screen.fill("dark gray")   
    draw_board()
    draw_pieces() 
    draw_dead()
    draw_check()

- we set a dark grey background

- we start by calling  all the draw function explained earlier to display our window with all its features drawn on it 

code:
>   if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

- in the begining of the code the selection variable was a dummy variable set to 100 

but if an item on the grid is selcted it have the index of that item then it draws all this piece possible moves using the draw_valid() function

code: 
>  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 80
            y_coord = event.pos[1] // 80
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'

- if the user lift clickedthe screen and the **game_over boolean** is still False we get the coordinates of that click and then check if its white's turn using **if turn_step <= 1**

> if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
- refers to the forfeet box drawn in the window which announce the other color as the winner

>                 if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
- if the player hadn't clicked on any piece earlier when it clicks on one it checks if the piece location is stored in the selection variable and increases the turn step declairing that a piece is now selected

> if click_coords in valid_moves and selection != 100:
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


- then if a piece was already selected we start checking if the next slection is in the piece's valid options and if it is we change the piece's location to the new location and if an enemy's piece was already there delete that peice loction from its corresponding locations list and put it in the corresonding captured list.

---
 We check if the captured item is the king we put the color's name in the **empty winner ='' variable** and end game.
---

- then we update the options for both black and white pieces

> if turn_step > 1:
- does the same for the black side

---
# Game over 

code:
>  if winner != '':
        game_over = True
        
        if change_images: 
            if winner == 'white':
                winner = "Heros"
            if winner == "black":
                winner = "villians"

- if the winner empty string is not empty nomore then its game over and we declare  the winner.


code:
>  if event.type == pygame.KEYDOWN and game_over:
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
- in case game_over and the user clicked on **Enter key** then we start re initalizing all the items and restart the game.

