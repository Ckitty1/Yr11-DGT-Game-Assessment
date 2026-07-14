# importing pygame library and initializing
import pygame
pygame.init()

# ------------------------------importing level layouts from "levels.py"------------------------------
from levels import lvl1_data
# ----------------------------------------------------------------------------------------------------

# ------------------------------window setup------------------------------
# setting screen size
win_width = 1300
win_height = 750

# creating and naming the window
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Stuck Inbetween')
# ------------------------------------------------------------------------

# ------------------------------loading images------------------------------
# level images
dirt_img = pygame.image.load('images/dirt.jpg')
background_img = pygame.image.load('images/background.png')
water_img = pygame.image.load('images/water.png')
# player images
player_img = dirt_img
# start menu images
start_img = pygame.image.load('images/start.jpg')
quit_img = pygame.image.load('images/quit.jpg')
# pause images
pause_img = pygame.image.load('images/pause.png')
home_img = pygame.image.load('images/home.png')
restart_img = pygame.image.load('images/restart.png')
resume_img = pygame.image.load('images/resume.png')
# confirm images
yes_img = pygame.image.load('images/yes.png')
no_img = pygame.image.load('images/no.jpg')
# --------------------------------------------------------------------------

# ------------------------------loading fonts------------------------------
pixel_font = pygame.font.Font('fonts/Tiny5-Regular.ttf', 999)
# -------------------------------------------------------------------------

# ------------------------------defining colours------------------------------
black = (0,0,0)
white = (255,255,255)
dark_brown = (41,11,6)
light_brown = (99,63,29)
# ----------------------------------------------------------------------------

# ------------------------------setting general game variables------------------------------
start_menu = True
paused = True
pause_menu = False
current_lvl = 1
option_menu = False
confirm_home_menu = False

# player variables
current_son = 'tangaroa'
current_ability = 'sea control'
# ------------------------------------------------------------------------------------------

# ------------------------------functions------------------------------
# function that converts text to an image and draws it on the screen
# /function to write text
def draw_text(text, font, colour, x, y, width):
    text_img = font.render(text, True, colour)
    original_width = text_img.get_width()
    original_height = text_img.get_height()
    scale_factor = width/original_width
    img = pygame.transform.scale(text_img, (width, original_height*scale_factor))
    win.blit(img, (x, y))

# function that draws the pause menu background
def draw_pause_background():
    pygame.draw.rect(win, dark_brown, (tile_size*3, tile_size*2, tile_size*20, tile_size*11), 0, 15)
    pygame.draw.rect(win, light_brown, (tile_size*3, tile_size*2, tile_size*20, tile_size*11), 15, 15)
# ---------------------------------------------------------------------

# ------------------------------world setup------------------------------
# setting the dimensions of each tile (square)
# tile size of 50x50 in a window size of 1300x750 will make a 26x15 tile grid
tile_size = 50

class World():
    def __init__(self,data):
        # creating a list that holds data for every tile
        self.tile_list = []

        # going through every number in the level data and adding a tuple to the list created above, containing the tile's image and position
        # if it's a 1, its image is a dirt
        # if it's a 0, its image is a black square (background)
        # if it's a 2, its image is a water
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row:
                if tile == 1:
                    self.img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                elif tile == 0:
                    self.img = pygame.transform.scale(background_img, (tile_size, tile_size))
                elif tile == 2:
                    self.img = pygame.transform.scale(water_img, (tile_size, tile_size))
                self.rect = self.img.get_rect()
                self.rect.x = column_count * tile_size
                self.rect.y = row_count * tile_size
                tile_info = (self.img, self.rect, tile)
                self.tile_list.append(tile_info)
                column_count += 1
            row_count += 1

    # making a function that goes through the list and draws each tile according to it's image and position assigned
    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])
# -----------------------------------------------------------------------

# ------------------------------player setup------------------------------
class Player():
    def __init__(self, x, y):
        self.start(x, y)

    def start(self, x, y):
        self.img = pygame.transform.scale(player_img, (tile_size, tile_size*1.75))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.vel = 5
        self.y_vel = 0
        self.last_ability = 0

    def update(self):
        # creating potential player coordinates to update movement and check for collision before moving the actual character model
        dx = 0
        dy = 0

        # player movement
        if key[pygame.K_LEFT]:
            dx -= self.vel
        if key[pygame.K_RIGHT]:
            dx += self.vel
        if key[pygame.K_UP] and self.y_vel == 0:
            self.y_vel = -15.1

        # calculating time since last ability
        time_since_last_ability = pygame.time.get_ticks()-self.last_ability

        # activate jump ability
        if key[pygame.K_SPACE] and self.y_vel == 0 and time_since_last_ability > 5000:
            self.y_vel = -20.1
            # storing the time the last ability was used
            self.last_ability = pygame.time.get_ticks()

        # gravity
        self.y_vel += 1
        # max falling velocity
        if self.y_vel > 15:
            self.y_vel = 15
        dy += self.y_vel

        # checking for collision
        # going through every tile in the list created in world.__init__
        # only checking for collision in tiles that aren't 0 (aren't background)
        # if the potential x player position collides/overlaps with the tile, it resets the potential player x to 0, stopping horozontal movement
        # if the potential y player position collides/overlaps with the tile, it first checks whether the player is falling or jumping (hitting ground or hits head)
        # - if the player is jumping, it only changes the player's potential y position by the distance between the bottom of the tile and the top of the player
        # - if the player is falling, it only changes the player's potential y position by the distance between the top of the tile and the bottom of the player
        for tile in world.tile_list:
            # checking if tile is background or real
            if tile[2] != 0:
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # if jumping, if hitting head
                    if self.y_vel < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.y_vel = 0.1
                    # if falling, if hitting ground
                    elif self.y_vel >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.y_vel = 0

        # updating player model coordinates
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        # drawing character onto screen
        win.blit(self.img, self.rect)
# ------------------------------------------------------------------------

# ------------------------------button setup------------------------------
class Button():
    def __init__(self, image, x, y, width, height):
        self.img = pygame.transform.scale(image, (width, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # storing mouse position in 'pos'
        pos = pygame.mouse.get_pos()

        # checking if button is touching mouse
        if self.rect.collidepoint(pos):
            # checking if left mouse button is also clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # drawing button onto screen
        win.blit(self.img, self.rect)

        # returning whether the button has been pressed or not
        return action
# ------------------------------------------------------------------------

# starting x and y position of the player
x = tile_size*3
y = tile_size*13

# loading player
player = Player(x, y)

# loading levels
lvl1 = World(lvl1_data)

# loading different buttons
# - start menu buttons
start_button = Button(start_img, win_width/2-tile_size*2.5, win_height/2.5, tile_size*5, tile_size*2)
quit_button = Button(quit_img, win_width/2-tile_size*2.5, win_height/2.5+tile_size*5, tile_size*5, tile_size*2)
# - in level button
pause_button = Button(pause_img, tile_size*0.25/2, tile_size*0.25/2, tile_size*0.75, tile_size*0.75)
# - pause screen buttons
home_button = Button(home_img, tile_size*5, tile_size*8, tile_size*3, tile_size*3)
restart_button = Button(restart_img, win_width/2-tile_size*1.5, tile_size*8, tile_size*3, tile_size*3)
resume_button = Button(resume_img, win_width-tile_size*8, tile_size*8, tile_size*3, tile_size*3)
# - confirm home menu buttons
yes_button = Button(yes_img, tile_size*6, tile_size*9, tile_size*5, tile_size*2)
no_button = Button(no_img, win_width-tile_size*11, tile_size*9, tile_size*5, tile_size*2)

# the main game loop that always runs
run = True
while run:
    # getting the pygame list of key presses
    key = pygame.key.get_pressed()

    # setting the frame rate
    pygame.time.delay(17)

    # stops the game when the window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # setting background colour of window
    win.fill(black)

    # showing different levels on screen
    if current_lvl == 1:
        world = lvl1
    elif current_lvl == 2:
        pass

    if start_menu:
        # writing the title
        draw_text('STUCK INBETWEEN', pixel_font, white, win_width/2-tile_size*10, win_height*1/10, tile_size*20)

        # drawing start button
        #  - if the start button is pressed, the start menu closes and game starts
        if start_button.draw():
            start_menu = False
            paused = False
            player.start(x, y)
        # drawing quit button
        #  - if the quit button is pressed, the game window stops/closes
        if quit_button.draw():
            run = False
    else:
        # drawing level
        world.draw()

        # drawing player
        player.draw()
        if paused:
            if pause_menu:
                # drawing pause menu background
                draw_pause_background()
                # drawing 'PAUSE'
                draw_text('PAUSED', pixel_font, white, win_width/2-tile_size*5, tile_size*3, tile_size*10)
                # drawing home button
                # - if home button is pressed, a 
                if home_button.draw():
                    pause_menu = False
                    confirm_home_menu = True
                # drawing restart button
                # - if restart button is pressed, the current level restarts
                elif restart_button.draw():
                    pause_menu = False
                    paused = False
                    player.start(x, y)
                # drawing resume button
                # - if resume button is pressed, the level continues with no change
                elif resume_button.draw():
                    paused = False
                    pause_menu = False
            
            if confirm_home_menu:
                draw_pause_background()
                draw_text('WARNING', pixel_font, white, win_width/2-tile_size*5, tile_size*2.5, tile_size*10)
                draw_text('GOING HOME WILL ALSO RESTART CURRENT LEVEL', pixel_font, white, win_width/2-tile_size*7.5, tile_size*5.25, tile_size*15)
                draw_text('CONFIRM?', pixel_font, white, win_width/2-tile_size*2.5, tile_size*6.25, tile_size*5)
                if yes_button.draw():
                    confirm_home_menu = False
                    start_menu = True
                elif no_button.draw():
                    confirm_home_menu = False
                    pause_menu = True
        else:
            # updating player
            player.update()

            # if pause button is pressed, open pause menu and pause all game updates
            if pause_button.draw() or key[pygame.K_ESCAPE]:
                paused = True
                pause_menu = True

    # updating the window constantly so that everything appears
    pygame.display.update()

# closes the game window when not running
pygame.quit
exit()