# importing pygame library and initializing
import pygame
pygame.init()
pygame.mixer.init()

# importing other libraries
import random

# importing the levels.py file so that I can use the level data stored there
import levels

# ------------------------------window setup------------------------------
# setting screen size
win_width = 1300
win_height = 750

# creating and naming the window
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Stuck In between')
# ------------------------------------------------------------------------

# ------------------------------loading images------------------------------
# LEVEL/WORLD IMAGES
# text/other images
arrows_to_move_img = pygame.image.load('images/arrows to move.png')
a_to_attract_fish_img = pygame.image.load('images/a to attract fish.png')
space_for_water_jump_img = pygame.image.load('images/space for water jump.png')
a_to_climb_img = pygame.image.load('images/a to climb.png')
s_to_switch_img = pygame.image.load('images/s to switch.png')

arrow_left_img = pygame.transform.rotate(pygame.image.load('images/arrow right.png'), 180)

# 1 edge dirts
dirt_img = pygame.image.load('images/dirt.png')
dirt_top_img = pygame.image.load('images/dirt top.png')
dirt_bottom_img = pygame.transform.rotate(dirt_top_img, 180)
dirt_right_img = pygame.transform.rotate(dirt_top_img, 270)
dirt_left_img = pygame.transform.rotate(dirt_top_img, 90)
# 1 corner dirts
dirt_bottom_right_corner_img = pygame.image.load('images/dirt bottom right corner.png')
dirt_bottom_left_corner_img = pygame.transform.rotate(dirt_bottom_right_corner_img, 270)
dirt_top_right_corner_img = pygame.transform.rotate(dirt_bottom_right_corner_img, 90)
dirt_top_left_corner_img = pygame.transform.rotate(dirt_bottom_right_corner_img, 180)
# 2 edge dirts
dirt_bottom_right_edge_img = pygame.image.load('images/dirt bottom right edge.png')
dirt_bottom_left_edge_img = pygame.transform.rotate(dirt_bottom_right_edge_img, 270)
dirt_top_right_edge_img = pygame.transform.rotate(dirt_bottom_right_edge_img, 90)
dirt_top_left_edge_img = pygame.transform.rotate(dirt_bottom_right_edge_img, 180)
dirt_bottom_top_img = pygame.image.load('images/dirt bottom top.png')
dirt_right_left_img = pygame.transform.rotate(dirt_bottom_top_img, 90)
# 2 corner dirts
dirt_bottom_corners_img = pygame.image.load('images/dirt bottom corners.png')
dirt_top_corners_img = pygame.transform.rotate(dirt_bottom_corners_img, 180)
dirt_left_corners_img = pygame.transform.rotate(dirt_bottom_corners_img, 270)
dirt_right_corners_img = pygame.transform.rotate(dirt_bottom_corners_img, 90)
# 3 edge dirts
dirt_bottom_right_left_edge_img = pygame.image.load('images/dirt bottom right left edge.png')
dirt_top_right_left_edge_img = pygame.transform.rotate(dirt_bottom_right_left_edge_img, 180)
# mixtures
dirt_top_bottom_right_img = pygame.image.load('images/dirt top edge & bottom right corner.png')
dirt_bottom_top_left_img = pygame.transform.rotate(dirt_top_bottom_right_img, 180)
dirt_bottom_top_right_img = pygame.transform.flip(dirt_bottom_top_left_img, True, False)
dirt_top_bottom_left_img = pygame.transform.flip(dirt_top_bottom_right_img, True, False)
dirt_right_top_left_img = pygame.transform.rotate(dirt_top_bottom_left_img, 270)
dirt_right_bottom_left_img = pygame.transform.flip(dirt_right_top_left_img, False, True)
dirt_left_bottom_right_img = pygame.transform.flip(dirt_right_bottom_left_img, True, False)

dirt_bottom_right_edge_top_left_corner_img = pygame.image.load('images/dirt bottom right edge + opp corner.png')
dirt_top_left_edge_bottom_right_corner_img = pygame.transform.rotate(dirt_bottom_right_edge_top_left_corner_img, 180)
dirt_bottom_left_edge_top_right_corner_img = pygame.transform.flip(dirt_top_left_edge_bottom_right_corner_img, False, True)
dirt_top_right_edge_bottom_left_corner_img = pygame.transform.flip(dirt_top_left_edge_bottom_right_corner_img, True, False)

# other tiles
background_img = pygame.image.load('images/background.png')
water_img = pygame.image.load('images/water.png')
fish_img = pygame.image.load('images/fish.png')
fish_button_right_img = pygame.transform.rotate(pygame.image.load('images/button bottom.png'), 90)
fish_button_left_img = pygame.transform.rotate(fish_button_right_img, 180)
fish_button_yes_right_img = pygame.transform.rotate(pygame.image.load('images/button bottom yes.png'), 90)
fish_button_yes_left_img = pygame.transform.rotate(fish_button_yes_right_img, 180)
gate_img = pygame.image.load('images/exit gate.png')
gate_top_img = pygame.image.load('images/exit gate top.png')
gate_bottom_img = pygame.image.load('images/exit gate bottom.png')
jump_pad_img = pygame.transform.rotate(pygame.image.load('images/jump pad bottom.png'), 180)

# PLAYER IMAGES
# CHARACTER 1
# player model
player1_right1_img = pygame.image.load('images/player1 right1.png')
player1_left1_img = pygame.transform.flip(player1_right1_img, True, False)
# fishing rod
fishing_rod_right_img = pygame.image.load('images/fishing rod right.png')
fishing_rod_left_img = pygame.transform.flip(fishing_rod_right_img, True, False)
# water jump ability button
wj_button_ready_img = pygame.image.load('images/water jump button ready.png')
wj_button_not_ready_img = pygame.image.load('images/water jump button not ready.png')
# water jump animation frames
wj_img_list = []
for i in range(1, 10):
    img = pygame.image.load(f'images/wj frames/water jump {i}.png')
    wj_img_list.append(img)

# CHARACTER 3
# player model
player3_right1_img = pygame.image.load('images/player3 right1.png')
player3_left1_img = pygame.transform.flip(player3_right1_img, True, False)

# MENU IMAGES
# start menu images
start_menu_all_img = pygame.transform.scale(pygame.image.load('images/start menu all.png'), (win_width, win_height))
start_img = pygame.image.load('images/start.png')
quit_img = pygame.image.load('images/quit.png')

# pause menu images
pause_img = pygame.image.load('images/pause.png')
home_img = pygame.image.load('images/home.png')
restart_img = pygame.image.load('images/restart.png')
resume_img = pygame.image.load('images/resume.png')

# confirm menu images
yes_img = pygame.image.load('images/yes.png')
no_img = pygame.image.load('images/no.png')
# --------------------------------------------------------------------------

# ------------------------------loading fonts------------------------------
pixel_font = pygame.font.Font('fonts/Tiny5-Regular.ttf', 999)
googlesans_font = pygame.font.Font('fonts/GoogleSans-Bold.ttf', 999)
# -------------------------------------------------------------------------

# ------------------------------loading sounds------------------------------
water_jump_sound = pygame.mixer.Sound('sounds/water splash.wav')
bounce_sound = pygame.mixer.Sound('sounds/bounce.wav')
vines_sound = pygame.mixer.Sound('sounds/vines.wav')
# --------------------------------------------------------------------------

# ------------------------------defining colours------------------------------
black = (0,0,0)
white = (255,255,255)
dark_brown = (61,24,0)
light_brown = (110,63,1)
# ----------------------------------------------------------------------------

# ------------------------------setting general game variables------------------------------
# game variables
clock = pygame.time.Clock()
fps = 60

# credits variables
credits_running = False

# menu variables
start_menu = True
paused = True
pause_menu = False
option_menu = False
confirm_home_menu = False
r_pressed = False

# level variables
current_lvl = 1
transitioning = False
fish_button_activated = False

# sound variables
sound_multi = 1

# player variables
current_character = 1
fish_attracting = False
vine_climb = False
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

# function for transition start
# - drawing a rectangle that covers the screen and slowly turns black
def transition_start():
    rect_surface = pygame.Surface((1400, 850))
    rect_surface.fill((0,0,0))
    opacity = 0
    fade_speed = 5
    for _ in range(9999):
        rect_surface.set_alpha(opacity)
        win.blit(rect_surface, (0, 0))
        opacity += fade_speed
        pygame.display.update()
        clock.tick(fps)
        if opacity > 255:
            break

# function for transition ending
# - drawing a black rectangle that covers the screen and slowly turns transparent
def transition_end():
    rect_surface = pygame.Surface((1400, 850))
    rect_surface.fill((0,0,0))
    opacity = 255
    fade_speed = 3.5
    for _ in range(9999):
        rect_surface.set_alpha(opacity)
        world.draw()
        player.draw()
        if start_menu == True:
            win.blit(start_menu_all_img, (0, 0))
        win.blit(rect_surface, (0, 0))
        opacity -= fade_speed
        pygame.display.update()
        clock.tick(fps)
        if opacity < 0:
            break

# function for Tangaroa's fish attract ability
def fish_attract_check():
    if key[pygame.K_a]:
        return True
    else:
        return False

# function to run the scrolling credits at the end of the game
def run_credits():
    credits_lines = [
        'T H E   E N D',
        ' ',
        "Luke Low - Code",
        "Luke Low - In game art",
        ' ',
        "Coding with Ross (YT channel) - Pygame tutorials",
        'Freesound (freesound.org) - In-game sound effects',
        ' ',
        'G A M E   T E S T E R S',
        'Oliver Tan',
        'Zech Kim',
        'Isaac Bandara',
        'Raymond Low (dad)',
        'Micah Low (brother)'
    ]
    rect_surface = pygame.Surface((1400, 850))
    rect_surface.fill((0,0,0))
    y = win_height
    line_list = []
    line_widths = []
    for line in credits_lines:
        text_img = googlesans_font.render(line, True, white)
        original_height = text_img.get_height()
        original_width = text_img.get_width()
        scale_factor = tile_size/original_height
        img = pygame.transform.scale(text_img, (original_width*scale_factor, original_height*scale_factor))
        line_list.append((img))
        line_widths.append((original_width*scale_factor))

    while y > 150-(len(credits_lines)*tile_size*1.3):
        win.blit(rect_surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i in range(len(credits_lines)):
            win.blit(line_list[i], (win.width/2-line_widths[i]/2, y+tile_size*i))

        y -= 1.5
        pygame.display.update()
        clock.tick(fps)
# ---------------------------------------------------------------------

# ------------------------------world setup------------------------------
# setting the dimensions of each tile (square)
# tile size of 50x50 in a window size of 1300x750 will make a 26x15 tile grid
tile_size = 50

class World():
    def __init__(self, data):
        global fish_button_activated

        # creating a list that holds data for every tile
        self.tile_list = []

        # going through every number in the level data and adding a tuple to the list created above, containing the tile's image and position
        # different image depending on what number the tile is
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row:
                # 0 draws background tile
                if tile == '0':
                    self.img = pygame.transform.scale(background_img, (tile_size, tile_size))

                # DIRT TILES
                # 1-5 are single edge dirt tiles
                elif tile == '1':
                    self.img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                elif tile == '2':
                    self.img = pygame.transform.scale(dirt_top_img, (tile_size, tile_size))
                elif tile == '3':
                    self.img = pygame.transform.scale(dirt_bottom_img, (tile_size, tile_size))
                elif tile == '4':
                    self.img = pygame.transform.scale(dirt_left_img, (tile_size, tile_size))
                elif tile == '5':
                    self.img = pygame.transform.scale(dirt_right_img, (tile_size, tile_size))
                # dirt variants/orientations
                elif tile == 'q': # corners
                    self.img = pygame.transform.scale(dirt_bottom_right_corner_img, (tile_size, tile_size))
                elif tile == 'p':
                    self.img = pygame.transform.scale(dirt_bottom_left_corner_img, (tile_size, tile_size))
                elif tile == 'z':
                    self.img = pygame.transform.scale(dirt_top_right_corner_img, (tile_size, tile_size))
                elif tile == 'm':
                    self.img = pygame.transform.scale(dirt_top_left_corner_img, (tile_size, tile_size))
                elif tile == 'y': # -----
                    self.img = pygame.transform.scale(dirt_top_corners_img, (tile_size, tile_size))
                elif tile == 'h':
                    self.img = pygame.transform.scale(dirt_left_corners_img, (tile_size, tile_size))
                elif tile == 'k':
                    self.img = pygame.transform.scale(dirt_right_corners_img, (tile_size, tile_size))
                elif tile == 'b':
                    self.img = pygame.transform.scale(dirt_bottom_corners_img, (tile_size, tile_size))
                elif tile == 'w': # edges
                    self.img = pygame.transform.scale(dirt_bottom_right_edge_img, (tile_size, tile_size))
                elif tile == 'o':
                    self.img = pygame.transform.scale(dirt_bottom_left_edge_img, (tile_size, tile_size))
                elif tile == 'x':
                    self.img = pygame.transform.scale(dirt_top_right_edge_img, (tile_size, tile_size))
                elif tile == 'n':
                    self.img = pygame.transform.scale(dirt_top_left_edge_img, (tile_size, tile_size))
                elif tile == '6': # -----
                    self.img = pygame.transform.scale(dirt_bottom_top_img, (tile_size, tile_size))
                elif tile == '7':
                    self.img = pygame.transform.scale(dirt_right_left_img, (tile_size, tile_size))
                elif tile == '>': # -----
                    self.img = pygame.transform.scale(dirt_top_right_left_edge_img, (tile_size, tile_size))
                elif tile == '<':
                    self.img = pygame.transform.scale(dirt_bottom_right_left_edge_img, (tile_size, tile_size))
                elif tile == '-': # mixtures
                    self.img = pygame.transform.scale(dirt_top_bottom_right_img, (tile_size, tile_size))
                elif tile == '_':
                    self.img = pygame.transform.scale(dirt_bottom_top_left_img, (tile_size, tile_size))
                elif tile == '+':
                    self.img = pygame.transform.scale(dirt_bottom_top_right_img, (tile_size, tile_size))
                elif tile == '=':
                    self.img = pygame.transform.scale(dirt_top_bottom_left_img, (tile_size, tile_size))
                elif tile == '*':
                    self.img = pygame.transform.scale(dirt_right_top_left_img, (tile_size, tile_size))
                elif tile == '&':
                    self.img = pygame.transform.scale(dirt_right_bottom_left_img, (tile_size, tile_size))
                elif tile == '^':
                    self.img = pygame.transform.scale(dirt_left_bottom_right_img, (tile_size, tile_size))
                elif tile == '!': # -----
                    self.img = pygame.transform.scale(dirt_bottom_right_edge_top_left_corner_img, (tile_size, tile_size))
                elif tile == '@':
                    self.img = pygame.transform.scale(dirt_top_left_edge_bottom_right_corner_img, (tile_size, tile_size))
                elif tile == '#':
                    self.img = pygame.transform.scale(dirt_bottom_left_edge_top_right_corner_img, (tile_size, tile_size))
                elif tile == '$':
                    self.img = pygame.transform.scale(dirt_top_right_edge_bottom_left_corner_img, (tile_size, tile_size))

                # OTHER TILES
                # j draws jump pad
                elif tile == 'j':
                    self.img = pygame.transform.scale(jump_pad_img, (tile_size, tile_size))
                # 7 draws water
                elif tile == '9':
                    self.img = pygame.transform.scale(water_img, (tile_size, tile_size))
                # a draws fish button 1
                elif tile == 'a': # lvl1
                    if fish_button_activated:
                        self.img = pygame.transform.scale(fish_button_yes_right_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_right_img, (tile_size, tile_size))
                # s draws fish button 2
                elif tile == 's': # lvl2
                    if fish_button_activated == 'True' or fish_button_activated == 1:
                        self.img = pygame.transform.scale(fish_button_yes_left_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_left_img, (tile_size, tile_size))
                # d draws fish button 3
                elif tile == 'd': # lvl2
                    if fish_button_activated == 'True' or fish_button_activated == 2:
                        self.img = pygame.transform.scale(fish_button_yes_right_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_right_img, (tile_size, tile_size))
                # f draws fish button 4
                elif tile == 'f': # lvl3
                    if fish_button_activated == 'True1' or fish_button_activated == 'True2':
                        self.img = pygame.transform.scale(fish_button_yes_left_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_left_img, (tile_size, tile_size))
                # g draws fish button 5
                elif tile == 'g': # lvl3
                    if fish_button_activated == 'True2':
                        self.img = pygame.transform.scale(fish_button_yes_right_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_right_img, (tile_size, tile_size))
                # g draws fish button 6
                elif tile == 'v': # lvl7
                    if fish_button_activated:
                        self.img = pygame.transform.scale(fish_button_yes_right_img, (tile_size, tile_size))
                    else:
                        self.img = pygame.transform.scale(fish_button_right_img, (tile_size, tile_size))
                # . draws a placeholder image for the top tile of the exit gate
                elif tile == '.':
                    self.img = pygame.transform.scale(gate_top_img, (tile_size, tile_size))
                # / draws a placeholder image for the top tile of the exit gate
                elif tile == '/':
                    self.img = pygame.transform.scale(gate_bottom_img, (tile_size, tile_size))

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
        # player variables
        if current_character == 1:
            self.img = pygame.transform.scale(player1_left1_img, (tile_size, tile_size*1.7))
        elif current_character == 3:
            self.img = pygame.transform.scale(player3_left1_img, (tile_size, tile_size*1.7))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.facing_right = False
        self.facing_left = True
        self.vel = 4
        self.y_vel = 0
        self.gravity = True
        self.first_gravity = False
        # fishing rod
        self.fishing_rod_img = pygame.transform.scale(fishing_rod_left_img, (tile_size*0.5, tile_size*0.5))
        # water jump ability variables ("wj" = "water jump")
        self.wj_button_img = pygame.transform.scale(wj_button_ready_img, (tile_size, tile_size))
        self.water_jumping = False
        self.wj_cooldown = 4000
        self.wj_last_ability = 0
        self.wj_next_ability = 0
        self.wj_next_ability_in = 0
        # - water splash animation
        self.wj_img = pygame.transform.scale(wj_img_list[0], (tile_size, tile_size*3.5))
        self.wj_index = 0
        self.wj_frame_cooldown = 1
        self.counter = 0
        self.wj_got_x = False
        self.wj_x = 0
        self.wj_got_y = False
        self.wj_y = 0
        # vine climb ability variables ("vc" = "vine climb")
        self.vc = False
        self.on_ceiling = False
        self.on_wall = False
        self.tile_above = False
        # character switch variables
        self.s_pressed = False

    def update(self, gravity):
        global current_character
        # variable to control whether gravity should be active or not
        if self.first_gravity == False:
            self.gravity = gravity
            self.first_gravity = True

        # creating potential player coordinates to update movement and check for collision before moving the actual character model
        dx = 0
        dy = 0

        # checking if there is a tile above the player
        overhead_rect = pygame.Rect(self.rect.x, self.rect.y-5, self.width, 5)
        for tile in world.tile_list:
            if tile[2] not in ('0', '.', '/'):
                if tile[1].colliderect(overhead_rect):
                    self.tile_above = True
                    break
                else:
                    self.tile_above = False

        if not self.tile_above:
            self.on_ceiling = False
            self.gravity = True

        # player movement using arrow keys (left, right, up for jump)
        if key[pygame.K_LEFT]:
            dx -= self.vel
            self.facing_left = True
            self.facing_right = False
            # changing player model on screen facing different directions
            if current_character == 1:
                self.img = pygame.transform.scale(player1_left1_img, (tile_size, tile_size*1.7))
            elif current_character == 3:
                self.img = pygame.transform.scale(player3_left1_img, (tile_size, tile_size*1.7))
            # changing which direction the fishing rod is facing
            self.fishing_rod_img = pygame.transform.scale(fishing_rod_left_img, (tile_size*0.5, tile_size*0.5))
        
        if key[pygame.K_RIGHT]:
            dx += self.vel
            self.facing_right = True
            self.facing_left = False
            # changing player model on screen facing different directions
            if current_character == 1:
                self.img = pygame.transform.scale(player1_right1_img, (tile_size, tile_size*1.7))
            elif current_character == 3:
                self.img = pygame.transform.scale(player3_right1_img, (tile_size, tile_size*1.7))
            # changing which direction the fishing rod is facing
            self.fishing_rod_img = pygame.transform.scale(fishing_rod_right_img, (tile_size*0.5, tile_size*0.5))
        
        if key[pygame.K_UP] and self.y_vel == 0 and not self.on_ceiling and not self.tile_above:
            self.y_vel = -12.1
        # ------------------------------CHARACTER SWITCH------------------------------
        if current_lvl == 7:
            # if 's' is pressed, it checks which character it's currently on and switches it to the other one
            if key[pygame.K_s] and not self.s_pressed:
                if current_character == 1:
                    current_character = 3
                    if self.facing_right:
                        self.img = pygame.transform.scale(player3_right1_img, (tile_size, tile_size*1.7))
                    elif self.facing_left:
                        self.img = pygame.transform.scale(player3_left1_img, (tile_size, tile_size*1.7))
                elif current_character == 3:
                    current_character = 1
                    self.vc = False
                    if self.facing_right:
                        self.img = pygame.transform.scale(player1_right1_img, (tile_size, tile_size*1.7))
                    elif self.facing_left:
                        self.img = pygame.transform.scale(player1_left1_img, (tile_size, tile_size*1.7))
                self.s_pressed = True
            elif not key[pygame.K_s]:
                self.s_pressed = False
        # ----------------------------------------------------------------------------

        # ------------------------------Water Jump Ability------------------------------
        if current_character == 1:
            self.vc = False
            self.gravity = True
            # calculating time since last jump ability
            time_since_last_wj = pygame.time.get_ticks()-self.wj_last_ability

            # activating jump ability if {space} is pressed
            if key[pygame.K_SPACE] and self.y_vel == 0 and time_since_last_wj > self.wj_cooldown:
                self.water_jumping = True
                self.y_vel = -19.1
                # playing water splash sound effect
                water_jump_sound.set_volume(sound_multi)
                water_jump_sound.play()
                # storing the time the last ability was used
                self.wj_last_ability = pygame.time.get_ticks()
                # storing the next time the ability is ready (in ms)
                self.wj_next_ability = self.wj_last_ability+self.wj_cooldown

        # calculating and storing time until next ability
        self.wj_next_ability_in = self.wj_next_ability-pygame.time.get_ticks()

        # setting the animation frame image
        if self.water_jumping:
            # obtaining original player position when the water jump starts
            # saved so that the water jump animation stays in the same place
            if not self.wj_got_y:
                self.wj_got_y = True
                self.wj_y = self.rect.bottom - tile_size*3.5
            if not self.wj_got_x:
                self.wj_got_x = True
                self.wj_x = self.rect.x
            self.counter += 1
            if self.counter > self.wj_frame_cooldown:
                self.counter = 0
                self.wj_index += 1
                if self.wj_index >= len(wj_img_list):
                    self.water_jumping = False
                    self.wj_index = 0
                self.wj_img = pygame.transform.scale(wj_img_list[self.wj_index], (tile_size, tile_size*3.5))
        # ------------------------------------------------------------------------------

        # ------------------------------Vine Climb Ability------------------------------
        if current_character == 3:
            # checking if the 'a' key is being pressed and only turning off gravity if on ceiling
            if key[pygame.K_a]:
                self.vc = True
                if self.on_ceiling and self.tile_above:
                    self.gravity = False
                    self.on_wall = False
            elif not key[pygame.K_a]:
                self.vc = False
                self.gravity = True
                self.on_wall = False
            # playing vine climbing sound effect
            if self.vc and (self.on_ceiling or self.on_wall):
                vines_sound.set_volume(sound_multi*0.5)
                vines_sound.play()
        # ------------------------------------------------------------------------------

        # gravity
        if self.gravity:
            self.y_vel += 1
        # setting max falling velocity to 15px/frame
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
            if tile[2] not in ('0', '.', '/'):
                # horizontal collision
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    # stopping horozontal movement
                    dx = 0
                    # moving player up when against a wall during vine climb ability
                    if self.vc and not self.on_ceiling:
                        self.on_wall = True
                        self.y_vel = 0.1
                        dy -= self.vel
                # vertical collision
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # stopping water jump when hits ceiling or floor
                    self.water_jumping = False
                    # if jumping, if hitting head
                    if dy < 0 or self.y_vel <= 0:
                        # only changing vertical movement by the distance to the tile it would collide with
                        dy = tile[1].bottom - self.rect.top
                        self.y_vel = 0.1
                        if self.vc:
                            self.on_ceiling = True
                        elif not self.vc:
                            self.on_ceiling = False
                    # if falling, if hitting ground
                    elif self.y_vel > 0:
                        self.wj_got_x = False
                        self.wj_got_y = False
                        # only changing vertical movement by the distance to the tile it would collide with
                        dy = tile[1].top - self.rect.bottom
                        self.y_vel = 0
                        self.on_ceiling = False
                        self.on_wall = False
                        # jump pad launches player up
                        if tile[2] == 'j':
                            self.y_vel = -30.1
                            bounce_sound.set_volume(sound_multi*2)
                            bounce_sound.play()

        # updating player model coordinates
        self.rect.x += dx
        self.rect.y += dy

    def player_xy_bottom(self):
        return (self.rect.x, self.rect.y, self.rect.bottom)

    def draw(self):
        global current_lvl
        # drawing character onto screen
        win.blit(self.img, self.rect)

        if current_lvl in (1, 2, 3, 7):
            # drawing wj (water jump) ability button timer onto screen
            win.blit(self.wj_button_img, (tile_size*0.25, tile_size*1.5))

        if round(self.wj_next_ability_in/1000) <= -1:
            self.wj_button_img = pygame.transform.scale(wj_button_ready_img, (tile_size, tile_size))
        else:
            self.wj_button_img = pygame.transform.scale(wj_button_not_ready_img, (tile_size, tile_size))
            draw_text(f'{round(self.wj_next_ability_in/1000+1)}', pixel_font, white, tile_size*0.63, tile_size*1.65, tile_size/3)

        # drawing fishing rod next to player when attracting fish
        if fish_attracting and current_character == 1:
            if self.facing_right:
                win.blit(self.fishing_rod_img, (self.rect.x+tile_size-7, self.rect.y+self.rect.height/2-7))
            elif self.facing_left:
                win.blit(self.fishing_rod_img, (self.rect.x-tile_size*0.5+7, self.rect.y+self.rect.height/2-7))

        # drawing the water jump animation
        if self.water_jumping:
            win.blit(self.wj_img, (self.wj_x, self.wj_y))
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

# ------------------------------fish setup------------------------------
class Fish():
    def __init__(self, x1, x2, y1, y2, width, num):
        original_width = fish_img.get_width()
        original_height = fish_img.get_height()
        scale_factor = width/original_width
        self.img = pygame.transform.scale(fish_img, (width, original_height*scale_factor))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.vel = 3
        self.fish_num = num
        self.start(x1, x2, y1, y2)

    def start(self, x1, x2, y1, y2):
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(x1, x2)
        self.rect.y = random.randint(y1, y2)

    def update(self):
        # creating potential fish coordinates just like the player
        dx = 0
        dy = 0

        # while the fish attracting ability is active, the fish will move closer to the player
        if fish_attracting:
            if self.rect.x > player_x:
                dx -= self.vel
            elif self.rect.x < player_x:
                dx += self.vel
            
            if self.rect.y > player_bottom:
                dy -= self.vel
            elif self.rect.y < player_bottom:
                dy += self.vel

        # checking for collision with tiles (just like the player)
        for tile in world.tile_list:
            # checking if tile is background or water (fish don't collide with these tiles)
            if tile[2] not in ('0', '9'):
                # if collide on x axis, stop moving in the x direction (horozontally)
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                    dx = 0
                    # checking if fish touched button
                    # fish number 1 for level 1
                    if self.fish_num == 1:
                        if tile[2] == 'a':
                            return True
                    # fish number 2 for level 2
                    elif self.fish_num == 2:
                        if tile[2] == 's':
                            return 'True1'
                        if tile[2] == 'd':
                            return 'True2'
                    # fish number 3 and 4 for level 3
                    elif self.fish_num == 3:
                        if tile[2] == 'f':
                            return True
                    elif self.fish_num == 4:
                        if tile[2] == 'g':
                            return True
                    # fish number 5 for level 7
                    elif self.fish_num == 5:
                        if tile[2] == 'v':
                            return True
                # if collide on y axis, stop moving in the y direction (vertically)
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    dy = 0

        # updating fish model coordinates
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        # drawing the fish onto screen
        win.blit(self.img, self.rect)
# ----------------------------------------------------------------------

# ------------------------------exit gate setup------------------------------
class Gate():
    def __init__(self, x, y, width, height):
        self.img = pygame.transform.scale(gate_img, (width, height))
        self.rect = self.img.get_rect()
        self.draw(x, y)

    def update(self):
        # checking if gate is touching player
        if player.rect.colliderect(self.rect):
            return True

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y
        # drawing the gate onto the screen
        win.blit(self.img, self.rect)
# ---------------------------------------------------------------------------

# starting x and y position of the player
player_x_start = tile_size*22
player_y_start = tile_size*7.1

# changing variables for player position
player_x = player_x_start
player_y = player_y_start

# initializing player
player = Player(player_x, player_y)

# initializing exit gate
gate = Gate(tile_size*24, tile_size*1, tile_size, tile_size*2)

# initializing fish
fish1 = Fish(tile_size*11, tile_size*24, tile_size*11, tile_size*13, tile_size*0.75, 1) # lvl1
fish2 = Fish(tile_size*8, tile_size*10, tile_size*2, tile_size*3, tile_size*0.75, 2) # lvl2
fish3 = Fish(tile_size*14, tile_size*17, tile_size*6, tile_size*7, tile_size*0.75, 3) # lvl3
fish4 = Fish(tile_size*4, tile_size*10, tile_size*8, tile_size*10, tile_size*0.75, 4) # lvl3
fish5 = Fish(tile_size*7, tile_size*8, tile_size*2, tile_size*3, tile_size*0.75, 5) # lvl7

# initializing different buttons
# - start menu buttons
start_button = Button(start_img, win_width/2-tile_size*6.22, tile_size*5.5, tile_size*12.44, tile_size*3.5)
quit_button = Button(quit_img, win_width/2-tile_size*1.92, tile_size*11, tile_size*3.83, tile_size*1.5)
# - in level button
pause_button = Button(pause_img, tile_size*0.25, tile_size*0.25, tile_size, tile_size)
# - pause screen buttons
home_button = Button(home_img, tile_size*5, tile_size*8, tile_size*3, tile_size*3)
restart_button = Button(restart_img, win_width/2-tile_size*1.5, tile_size*8, tile_size*3, tile_size*3)
resume_button = Button(resume_img, win_width-tile_size*8, tile_size*8, tile_size*3, tile_size*3)
# - confirm home menu buttons
yes_button = Button(yes_img, win_width/2-tile_size*4.5, tile_size*8, tile_size*3, tile_size*3)
no_button = Button(no_img, win_width/2+tile_size*1.5, tile_size*8, tile_size*3, tile_size*3)

# the main game loop that always runs
run = True
while run:
    # getting the pygame list of key presses
    key = pygame.key.get_pressed()

    # setting the max frame rate so that the game runs the same on every device
    clock.tick(fps)

    # stops the game when the window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # setting background colour of window
    win.fill(black)

    # showing different levels on screen
    if current_lvl == 1:
        if fish_button_activated:
            world = World(levels.lvl1_activated_data)
        else:
            world = World(levels.lvl1_data)
    elif current_lvl == 2:
        if fish_button_activated == 'True':
            world = World(levels.lvl2_activated_data)
        else:
            world = World(levels.lvl2_data)
    elif current_lvl == 3:
        if fish_button_activated == 'True1':
            world = World(levels.lvl3_activated1_data)
        elif fish_button_activated == 'True2':
            world = World(levels.lvl3_activated2_data)
        else:
            world = World(levels.lvl3_data)
    elif current_lvl == 4:
        world = World(levels.lvl4_data)
    elif current_lvl == 5:
        world = World(levels.lvl5_data)
    elif current_lvl == 6:
        world = World(levels.lvl6_data)
    elif current_lvl == 7:
        if fish_button_activated:
            world = World(levels.lvl7_activated_data)
        else:
            world = World(levels.lvl7_data)
    
    if start_menu:
        world = World(levels.lvl0_data)

    # drawing level/world
    world.draw()

    # if the transition has started
    if transitioning:
        transition_end()
        transitioning = False
        paused = False

    if start_menu:
        # writing the title
        draw_text('STUCK IN BETWEEN', pixel_font, dark_brown, win_width/2-tile_size*10-5, tile_size*1.5+5, tile_size*20)
        draw_text('STUCK IN BETWEEN', pixel_font, light_brown, win_width/2-tile_size*10, tile_size*1.5, tile_size*20)
        # drawing start button
        #  - if the start button is pressed, the start menu closes and game starts
        if start_button.draw():
            start_menu = False
            player.start(player_x_start, player_y_start)
            paused = True
            fish_button_activated = False
            transitioning = True
            transition_start()
        # drawing quit button
        #  - if the quit button is pressed, the game window stops/closes
        if quit_button.draw():
            run = False
    else:
        # (drawing things when paused and unpaused)
        if current_lvl == 1:
            # drawing fish
            fish1.draw()
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*1)
            # drawing key instructions on the screen ("arrows to move" & "'a' to attract fish" & "space for water jump")
            if fish_button_activated:
                win.blit(pygame.transform.scale(space_for_water_jump_img, (tile_size*5, tile_size*1.31)), (tile_size*3.5, tile_size*1.5))
                win.blit(pygame.transform.scale(arrow_left_img, (tile_size*1.75, tile_size*0.5)), (tile_size*1.5, tile_size*1.83))
            else:
                win.blit(pygame.transform.scale(arrows_to_move_img, (tile_size*8, tile_size*2.125)), (tile_size*2.5, tile_size*1.5))
                win.blit(pygame.transform.scale(a_to_attract_fish_img, (tile_size*6, tile_size)), (tile_size*18.75, tile_size*13))
        elif current_lvl == 2:
            # drawing fish
            fish2.draw()
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*12)
        elif current_lvl == 3:
            # drawing fish
            fish3.draw()
            fish4.draw()
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*12)
        elif current_lvl == 4:
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*1)
            # drawing key instructions on the screen ("'a' to climb")
            win.blit(pygame.transform.scale(a_to_climb_img, (tile_size*4, tile_size/3*2)), (tile_size*20.5, tile_size*4.75))
        elif current_lvl == 5:
            # drawing exit gate
            gate.draw(tile_size*2, tile_size*2)
        elif current_lvl == 6:
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*4)
        elif current_lvl == 7:
            # drawing fish
            fish5.draw()
            # drawing exit gate
            gate.draw(tile_size*24, tile_size*12)
            # drawing key instructions on sthe screen ("'s' to switch")
            win.blit(pygame.transform.scale(s_to_switch_img, (tile_size*4, tile_size/3*2)), (tile_size*20.5, tile_size*4.75))
        
        # drawing player
        player.draw()

        if paused:
            if pause_menu:
                # drawing pause menu background
                draw_pause_background()
                # drawing 'PAUSED'
                draw_text('PAUSED', pixel_font, light_brown, win_width/2-tile_size*5, tile_size*3, tile_size*10)
                # drawing (r) above the restart button
                draw_text('(R)', pixel_font, light_brown, win_width/2-tile_size*0.75, tile_size*7, tile_size*1.5)
                # drawing home button
                # - if home button is pressed, it goes back to the main/start menu
                if home_button.draw():
                    pause_menu = False
                    confirm_home_menu = True
                # drawing restart button
                # - if restart button is pressed, the current level restarts
                elif restart_button.draw():
                    pause_menu = False
                    paused = False
                    player.start(player_x_start, player_y_start)
                    fish_button_activated = False
                    if current_lvl == 1:
                        fish1.start(tile_size*11, tile_size*24, tile_size*11, tile_size*13)
                        world = World(levels.lvl1_data)
                    elif current_lvl == 2:
                        fish2.start(tile_size*8, tile_size*10, tile_size*2, tile_size*3)
                        world = World(levels.lvl2_data)
                    elif current_lvl == 3:
                        fish3.start(tile_size*14, tile_size*17, tile_size*6, tile_size*7)
                        fish4.start(tile_size*4, tile_size*10, tile_size*8, tile_size*10)
                        world = World(levels.lvl3_data)
                    elif current_lvl == 7:
                        fish5.start(tile_size*7, tile_size*8, tile_size*2, tile_size*3)
                        world = World(levels.lvl7_data)
                # drawing resume button
                # - if resume button is pressed, the level continues with no change
                elif resume_button.draw():
                    paused = False
                    pause_menu = False
            
            if confirm_home_menu:
                draw_pause_background()
                draw_text('WARNING', pixel_font, light_brown, win_width/2-tile_size*5, tile_size*2.5, tile_size*10)
                draw_text('GOING HOME WILL ALSO RESTART CURRENT LEVEL', pixel_font, light_brown, win_width/2-tile_size*7.5, tile_size*5.25, tile_size*15)
                draw_text('CONFIRM?', pixel_font, light_brown, win_width/2-tile_size*2.5, tile_size*6.25, tile_size*5)
                if yes_button.draw():
                    confirm_home_menu = False
                    start_menu = True
                elif no_button.draw():
                    confirm_home_menu = False
                    pause_menu = True
        else:
            # updating player
            player.update(True)
            player_x = player.player_xy_bottom()[0]
            player_y = player.player_xy_bottom()[1]
            player_bottom = player.player_xy_bottom()[2]

            # setting character so that different abilities will be in use
            if current_lvl in (1, 2, 3):
                current_character = 1
            elif current_lvl in (4, 5, 6):
                current_character = 3

            # CHARACTER 1 LEVELS
            if current_lvl in (1, 2, 3, 7):
                if current_lvl == 1:
                    # updating fish
                    # when fish touches button, it returns true and changes level
                    if fish1.update():
                        fish_button_activated = True
                elif current_lvl == 2:
                    # updating fish
                    # checking if the fish touches either button and to only change level when both have been pressed
                    if fish2.update() == 'True1':
                        if fish_button_activated == False:
                            fish_button_activated = 1
                        elif fish_button_activated == 2:
                            fish_button_activated = 'True'
                    if fish2.update() == 'True2':
                        if fish_button_activated == False:
                            fish_button_activated = 2
                        elif fish_button_activated == 1:
                            fish_button_activated = 'True'
                elif current_lvl == 3:
                    # updating fish
                    # if the fish touches its respective button, the level changes to open up different parts
                    if fish3.update():
                        fish_button_activated = 'True1'
                    if fish4.update():
                        fish_button_activated = 'True2'
                # CHARACTER SWITCH LEVEL
                elif current_lvl == 7:
                    # updating fish
                    # when fish touches button, it returns true and changes the level
                    if fish5.update():
                        fish_button_activated = True

                # checking to see if "a" is being pressed
                if current_character == 1:
                    fish_attracting = fish_attract_check()
                else:
                    fish_attracting = False

            # if the player falls off the bottom of the screen or goes above the screen, the player dies/restarts level
            if player_y > tile_size*17 or player_y < 0:
                fish_button_activated = False
                player.start(player_x_start, player_y_start)
                fish5.start(tile_size*7, tile_size*8, tile_size*1, tile_size*2)
                world = World(levels.lvl7_data)

            # checking to see if player is touching exit gate
            if gate.update():
                if current_lvl == 7:
                    paused = True
                    fish_button_activated = False
                    current_lvl = 1
                    transition_start()
                    credits_running = True
                    run_credits()
                    credits_running = False
                    start_menu = True
                    transition_end()
                else:
                    paused = True
                    current_lvl += 1
                    fish_button_activated = False
                    player.start(player_x_start, player_y_start)
                    transitioning = True
                    transition_start()

            if key[pygame.K_r] and not r_pressed:
                player.start(player_x_start, player_y_start)
                fish_button_activated = False
                if current_lvl == 1:
                    fish1.start(tile_size*11, tile_size*24, tile_size*11, tile_size*13)
                    world = World(levels.lvl1_data)
                elif current_lvl == 2:
                    fish2.start(tile_size*8, tile_size*10, tile_size*2, tile_size*3)
                    world = World(levels.lvl2_data)
                elif current_lvl == 3:
                    fish3.start(tile_size*14, tile_size*17, tile_size*6, tile_size*7)
                    fish4.start(tile_size*4, tile_size*10, tile_size*8, tile_size*10)
                    world = World(levels.lvl3_data)
                elif current_lvl == 7:
                    fish5.start(tile_size*7, tile_size*8, tile_size*2, tile_size*3)
                    world = World(levels.lvl7_data)
                r_pressed = True
            elif not key[pygame.K_r]:
                r_pressed = False

            # if pause button is pressed, open pause menu and pause all game updates
            if pause_button.draw() or key[pygame.K_ESCAPE]:
                paused = True
                pause_menu = True

    # updating the window constantly so that everything appears
    pygame.display.update()

# closes the game window when not running
pygame.quit()
exit()