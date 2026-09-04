'''
STUCK IN BETWEEN
- 2D puzzle platformer built with pygame that has 2 different characters with different abilities used to complete tasks.

main.py
- The main game file that runs all the logic for the game using pygame and pyvidplayer2 to run cut scenes.
'''

# importing pygame library and initializing
import pygame
pygame.init()
pygame.mixer.init()

# importing other libraries
import random
from pyvidplayer2 import Video, READER_FFMPEG

# importing the levels.py file so that I can use the level data stored there
import levels

# ------------------------------window setup------------------------------
# setting screen size
WIN_WIDTH = 1300
WIN_HEIGHT = 750

# creating and naming the window
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Stuck In between')
# ------------------------------------------------------------------------

# ------------------------------loading images------------------------------
# loading in all images used for the game and scaling them to the right size and saving them into a variable to use later

# LEVEL/WORLD IMAGES
# text/instructions/other images
arrows_to_move_img = pygame.transform.scale(pygame.image.load('images/arrows to move.png'), (400, 106.25))
a_to_attract_fish_img = pygame.transform.scale(pygame.image.load('images/a to attract fish.png'), (300, 50))
space_for_water_jump_img = pygame.transform.scale(pygame.image.load('images/space for water jump.png'), (250, 65.5))
a_to_climb_img = pygame.transform.scale(pygame.image.load('images/a to climb.png'), (200, 33.33))
s_to_switch_img = pygame.transform.scale(pygame.image.load('images/s to switch.png'), (200, 33.33))

arrow_left_img = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/arrow right.png'), 180), (87.5, 25))

# all different dirt tiles/variations/rotations
# 1 edge dirts
dirt_img = pygame.transform.scale(pygame.image.load('images/dirt.png'), (50, 50))
dirt_top_img = pygame.transform.scale(pygame.image.load('images/dirt top.png'), (50, 50))
dirt_bottom_img = pygame.transform.scale(pygame.transform.rotate(dirt_top_img, 180), (50, 50))
dirt_right_img = pygame.transform.scale(pygame.transform.rotate(dirt_top_img, 270), (50, 50))
dirt_left_img = pygame.transform.scale(pygame.transform.rotate(dirt_top_img, 90), (50, 50))
# 1 corner dirts
dirt_bottom_right_corner_img = pygame.transform.scale(pygame.image.load('images/dirt bottom right corner.png'), (50, 50))
dirt_bottom_left_corner_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_corner_img, 270), (50, 50))
dirt_top_right_corner_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_corner_img, 90), (50, 50))
dirt_top_left_corner_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_corner_img, 180), (50, 50))
# 2 edge dirts
dirt_bottom_right_edge_img = pygame.transform.scale(pygame.image.load('images/dirt bottom right edge.png'), (50, 50))
dirt_bottom_left_edge_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_edge_img, 270), (50, 50))
dirt_top_right_edge_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_edge_img, 90), (50, 50))
dirt_top_left_edge_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_edge_img, 180), (50, 50))
dirt_bottom_top_img = pygame.transform.scale(pygame.image.load('images/dirt bottom top.png'), (50, 50))
dirt_right_left_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_top_img, 90), (50, 50))
# 2 corner dirts
dirt_bottom_corners_img = pygame.transform.scale(pygame.image.load('images/dirt bottom corners.png'), (50, 50))
dirt_top_corners_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_corners_img, 180), (50, 50))
dirt_left_corners_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_corners_img, 270), (50, 50))
dirt_right_corners_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_corners_img, 90), (50, 50))
# 3 edge dirts
dirt_bottom_right_left_edge_img = pygame.transform.scale(pygame.image.load('images/dirt bottom right left edge.png'), (50, 50))
dirt_top_right_left_edge_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_left_edge_img, 180), (50, 50))
# mixtures
dirt_top_bottom_right_img = pygame.transform.scale(pygame.image.load('images/dirt top edge & bottom right corner.png'), (50, 50))
dirt_bottom_top_left_img = pygame.transform.scale(pygame.transform.rotate(dirt_top_bottom_right_img, 180), (50, 50))
dirt_bottom_top_right_img = pygame.transform.scale(pygame.transform.flip(dirt_bottom_top_left_img, True, False), (50, 50))
dirt_top_bottom_left_img = pygame.transform.scale(pygame.transform.flip(dirt_top_bottom_right_img, True, False), (50, 50))
dirt_right_top_left_img = pygame.transform.scale(pygame.transform.rotate(dirt_top_bottom_left_img, 270), (50, 50))
dirt_right_bottom_left_img = pygame.transform.scale(pygame.transform.flip(dirt_right_top_left_img, False, True), (50, 50))
dirt_left_bottom_right_img = pygame.transform.scale(pygame.transform.flip(dirt_right_bottom_left_img, True, False), (50, 50))

dirt_bottom_right_edge_top_left_corner_img = pygame.transform.scale(pygame.image.load('images/dirt bottom right edge + opp corner.png'), (50, 50))
dirt_top_left_edge_bottom_right_corner_img = pygame.transform.scale(pygame.transform.rotate(dirt_bottom_right_edge_top_left_corner_img, 180), (50, 50))
dirt_bottom_left_edge_top_right_corner_img = pygame.transform.scale(pygame.transform.flip(dirt_top_left_edge_bottom_right_corner_img, False, True), (50, 50))
dirt_top_right_edge_bottom_left_corner_img = pygame.transform.scale(pygame.transform.flip(dirt_top_left_edge_bottom_right_corner_img, True, False), (50, 50))

# other tiles/objects
background_img = pygame.transform.scale(pygame.image.load('images/background.png'), (50, 50))
water_img = pygame.transform.scale(pygame.image.load('images/water.png'), (50, 50))
fish_img = pygame.image.load('images/fish.png')
fish_button_right_img = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/button bottom.png'), 90), (50, 50))
fish_button_left_img = pygame.transform.scale(pygame.transform.rotate(fish_button_right_img, 180), (50, 50))
fish_button_yes_right_img = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/button bottom yes.png'), 90), (50, 50))
fish_button_yes_left_img = pygame.transform.scale(pygame.transform.rotate(fish_button_yes_right_img, 180), (50, 50))
gate_img = pygame.image.load('images/exit gate.png')
gate_top_img = pygame.transform.scale(pygame.image.load('images/exit gate top.png'), (50, 50))
gate_bottom_img = pygame.transform.scale(pygame.image.load('images/exit gate bottom.png'), (50, 50))
jump_pad_img = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/jump pad bottom.png'), 180), (50, 50))

# PLAYER IMAGES
# CHARACTER 1
# player model
# - making empty lists and saving the scaled image data into the lists to iterate through later during animations
player1_right_img_list = []
player1_left_img_list = []
for i in range(1, 5):
    right_img = pygame.transform.scale(pygame.image.load(f'images/player1 frames/player1 right{i}.png'), (50, 85))
    player1_right_img_list.append(right_img)
    left_img = pygame.transform.scale(pygame.transform.flip(right_img, True, False), (50, 85))
    player1_left_img_list.append(left_img)
# fishing rod
fishing_rod_right_img = pygame.image.load('images/fishing rod right.png')
fishing_rod_left_img = pygame.transform.flip(fishing_rod_right_img, True, False)
# water jump ability button
wj_button_ready_img = pygame.transform.scale(pygame.image.load('images/water jump button ready.png'), (50, 50))
wj_button_not_ready_img = pygame.transform.scale(pygame.image.load('images/water jump button not ready.png'), (50, 50))
# water jump animation frames
# - making an empty list and saving the scaled image data into the list to iterate through later during animations
wj_img_list = []
for i in range(1, 10):
    img = pygame.image.load(f'images/wj frames/water jump {i}.png')
    wj_img_list.append(img)

# CHARACTER 3
# player model
# - making empty lists and saving the scaled image data into the lists to iterate through later during animations
player3_right_img_list = []
player3_left_img_list = []
for i in range(1, 5):
    right_img = pygame.transform.scale(pygame.image.load(f'images/player3 frames/player3 right{i}.png'), (50, 85))
    player3_right_img_list.append(right_img)
    left_img = pygame.transform.scale(pygame.transform.flip(right_img, True, False), (50, 85))
    player3_left_img_list.append(left_img)
player3_right1_climb_img = pygame.transform.scale(pygame.image.load('images/player3 frames/player3 right1 climb.png'), (50, 85))
player3_left1_climb_img = pygame.transform.flip(player3_right1_climb_img, True, False)

# MENU IMAGES
# start menu images
start_menu_all_img = pygame.transform.scale(pygame.image.load('images/start menu all.png'), (WIN_WIDTH, WIN_HEIGHT))
start_img = pygame.image.load('images/start.png')
quit_img = pygame.image.load('images/quit.png')
blank_button_img = pygame.image.load('images/blank button.png')
reset_game_img = pygame.image.load('images/reset game.png')

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
pixel_font = pygame.font.Font('fonts/Tiny5-Regular.ttf', 40)
googlesans_font = pygame.font.Font('fonts/GoogleSans-Bold.ttf', 999)
# -------------------------------------------------------------------------

# ------------------------------loading sounds------------------------------
water_jump_sound = pygame.mixer.Sound('sounds/water splash.wav')
bounce_sound = pygame.mixer.Sound('sounds/bounce.wav')
vines_sound = pygame.mixer.Sound('sounds/vines.wav')
# --------------------------------------------------------------------------

# ------------------------------defining colours------------------------------
# saving different key colours into variables to use later instead of having to type the RGB code every time
black = (0,0,0)
white = (255,255,255)
dark_brown = (61,24,0)
light_brown = (110,63,1)
# ----------------------------------------------------------------------------

# ------------------------------setting general game variables------------------------------
# game variables
# time/framerate/FPS variables
clock = pygame.time.Clock()
FPS = 60

# world variables
TILE_SIZE = 50 # (tile size of 50x50 in a window size of 1300x750 will make a 26x15 tile grid on screen)

# speedrun mode variables
speedrun = False
speedrun_time = 0
speedrun_start_time = 0
speedrun_stored_time = 0
speedrun_display_time = 0
speedrun_timer_img = 0
pause_start_time = 0

# credits variables
credits_running = False

# cut scene variables
scene_running = False
vid = None

# menu variables
start_menu = True
paused = True
pause_menu = False
option_menu = False
confirm_home_menu = False
r_pressed = False
esc_held = False
resetted_game = False

# level variables
current_lvl = 1
lvl_changed = False
transitioning = False
fish_button_activated = False

# sound variables
sound_multi = 1

# player variables
player_x_start = TILE_SIZE*22
player_y_start = TILE_SIZE*7.1
player_x = player_x_start
player_y = player_y_start
current_character = 1
fish_attracting = False
vine_climb = False
# ------------------------------------------------------------------------------------------

# ------------------------------functions------------------------------
# function that converts text to an image and draws it on the screen
# /function to write text on screen
# - turns the text inputted into an image which then gets scaled and drawn onto screen
def draw_text(text, font, colour, x, y, width):
    '''
    Writes text onto the screen based on inputs

    Parameters:
    - text (str): the text that you want to write onto the screen
    - font (pygame.font.Font()): the font of the text written
    - colour (RGB tuple): the colour of the text
    - x, y (int): the x and y coordinates of where the text will be written
    - width (int): set width of the total line of text. The height ratio is worked out
    '''
    text_img = font.render(text, True, colour)
    original_width = text_img.get_width()
    original_height = text_img.get_height()
    scale_factor = width/original_width
    img = pygame.transform.scale(text_img, (width, original_height*scale_factor))
    win.blit(img, (x, y))

# function that draws the pause menu background
def draw_pause_background():
    pygame.draw.rect(win, dark_brown, (TILE_SIZE*3, TILE_SIZE*2, TILE_SIZE*20, TILE_SIZE*11), 0, 15)
    pygame.draw.rect(win, light_brown, (TILE_SIZE*3, TILE_SIZE*2, TILE_SIZE*20, TILE_SIZE*11), 15, 15)

# function for transition start
# - drawing a rectangle that covers the screen and slowly turns from transparent to black
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
        clock.tick(FPS)
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
        clock.tick(FPS)
        if opacity < 0:
            break

# function for Tangaroa's fish attract ability
# checking if "a" is being pressed
def fish_attract_check():
    if key[pygame.K_a]:
        return True
    else:
        return False

# function to reset current level
# resets player position, world layout, fish position, and fish button states
def restart_lvl():
    global player
    global fish1
    global fish2
    global fish3
    global fish4
    global fish5
    global lvl_changed
    global fish_button_activated
    global world
    global speedrun_start_time
    lvl_changed = True
    player.start(player_x_start, player_y_start)
    fish_button_activated = False
    if current_lvl == 1:
        fish1.start(TILE_SIZE*14, TILE_SIZE*24, TILE_SIZE*11, TILE_SIZE*13)
        world = World(levels.lvl1_data)
        speedrun_start_time = pygame.time.get_ticks()
    elif current_lvl == 2:
        fish2.start(TILE_SIZE*8, TILE_SIZE*10, TILE_SIZE*2, TILE_SIZE*3)
        world = World(levels.lvl2_data)
    elif current_lvl == 3:
        fish3.start(TILE_SIZE*14, TILE_SIZE*17, TILE_SIZE*6, TILE_SIZE*7)
        fish4.start(TILE_SIZE*4, TILE_SIZE*10, TILE_SIZE*8, TILE_SIZE*10)
        world = World(levels.lvl3_data)
    elif current_lvl == 7:
        fish5.start(TILE_SIZE*7, TILE_SIZE*8, TILE_SIZE*2, TILE_SIZE*3)
        world = World(levels.lvl7_data)

# function to run the scrolling credits at the end of the game
def run_credits():
    global esc_held
    credits_lines = [
        'T H E   E N D',
        ' ',
        ' ',
        ' ',
        "Luke Low - Code",
        "Luke Low - In game art",
        ' ',
        'Lila Asi - Cut scenes',
        ' ',
        "Coding with Ross (YT channel) - Pygame tutorials",
        'Freesound (freesound.org) - In-game sound effects',
        'Google Fonts - Text fonts',
        ' ',
        'G A M E   T E S T E R S',
        'Oliver Tan',
        'Lila Asi',
        'Zech Kim',
        'Isaac Bandara',
        'Minghao He',
        'Caleb Bull',
        'Caleb Whitcombe',
        'Judah Thornton',
        'James Dustow',
        'Raymond Low',
        'Micah Low',
        'Joshua Low',
        'Quan Low',
        'Tobias Low'
    ]
    # adding lines to the credits saying the player's speedrun time if speedrun mode was on
    if speedrun:
        credits_lines.insert(2, ' ')
        credits_lines.insert(2, f'{(speedrun_time/1000):.3f}s',)
        credits_lines.insert(2, 'Y O U R   T  I M E')
        credits_lines.insert(2, ' ')

    # making background black
    rect_surface = pygame.Surface((1400, 850))
    rect_surface.fill((0,0,0))

    y = WIN_HEIGHT

    # making an empty list and saving the scaled text images into the list to iterate through later to draw them onto screen
    # (similar logic to loading animation frames earlier)
    line_list = []
    line_widths = []
    for line in credits_lines:
        text_img = googlesans_font.render(line, True, white)
        original_height = text_img.get_height()
        original_width = text_img.get_width()
        scale_factor = TILE_SIZE/original_height
        img = pygame.transform.scale(text_img, (original_width*scale_factor, original_height*scale_factor))
        line_list.append((img))
        line_widths.append((original_width*scale_factor))

    esc_to_exit_img = pygame.transform.scale(googlesans_font.render('ESC to skip', True, white), (TILE_SIZE*2, TILE_SIZE*0.5))

    # the position of the credits words starts below the screen and slowly moves up 1.5 pixels each frame,
    # until all the words have gone off the top of the screen and the credits end
    while y > 150-(len(credits_lines)*TILE_SIZE*1.2):
        win.blit(rect_surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # letting the user skip the credits if the escape key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            y = 150-(len(credits_lines)*TILE_SIZE*1.3)
            esc_held = True

        # iterating through the list which holds all the text image data and drawing it onto the screen, each line below each other
        for i in range(len(credits_lines)):
            win.blit(line_list[i], (win.width/2-line_widths[i]/2, y+TILE_SIZE*i))

        win.blit(esc_to_exit_img, (TILE_SIZE*0.25, TILE_SIZE*14.25))

        y -= 1.5
        pygame.display.update()
        clock.tick(FPS)

# function for playing a video
def play_vid(path):
    '''
    Plays a video using the FFmpeg reader

    Parameters:
    - path(file pathway): the file path to the video that will be played
    '''
    global esc_held
    vid = Video(path, reader=READER_FFMPEG)
    vid.restart()
    vid.resize((1000, WIN_HEIGHT))
    playing = True
    esc_to_exit_img = pygame.transform.scale(googlesans_font.render('ESC to skip', True, white), (TILE_SIZE*2, TILE_SIZE*0.5))

    # while the video is playing, it iterates through each frame of the video and draws it onto the screen
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            playing = False
            esc_held = True

        vid.draw(win, (150, 0))
        win.blit(esc_to_exit_img, (TILE_SIZE*0.25, TILE_SIZE*14.25))

        pygame.display.update()

        if vid.get_pos() >= vid.duration:
            playing = False
    vid.close()
# ---------------------------------------------------------------------

# ------------------------------world setup------------------------------
class World():
    def __init__(self, data):
        global fish_button_activated

        # creating an empty list that will hold data for every tile
        self.tile_list = []

        # going through every number in the level data from levels.py and adding a tuple to the list created above, containing the tile's image and position
        # different image depending on what number the tile is
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row:
                # 0 draws background tile
                if tile == '0':
                    self.img = background_img

                # DIRT TILES
                # 1-5 are single edge dirt tiles
                elif tile == '1':
                    self.img = dirt_img
                elif tile == '2':
                    self.img = dirt_top_img
                elif tile == '3':
                    self.img = dirt_bottom_img
                elif tile == '4':
                    self.img = dirt_left_img
                elif tile == '5':
                    self.img = dirt_right_img
                # dirt variants/orientations
                elif tile == 'q': # corners
                    self.img = dirt_bottom_right_corner_img
                elif tile == 'p':
                    self.img = dirt_bottom_left_corner_img
                elif tile == 'z':
                    self.img = dirt_top_right_corner_img
                elif tile == 'm':
                    self.img = dirt_top_left_corner_img
                elif tile == 'y': # -----
                    self.img = dirt_top_corners_img
                elif tile == 'h':
                    self.img = dirt_left_corners_img
                elif tile == 'k':
                    self.img = dirt_right_corners_img
                elif tile == 'b':
                    self.img = dirt_bottom_corners_img
                elif tile == 'w': # edges
                    self.img = dirt_bottom_right_edge_img
                elif tile == 'o':
                    self.img = dirt_bottom_left_edge_img
                elif tile == 'x':
                    self.img = dirt_top_right_edge_img
                elif tile == 'n':
                    self.img = dirt_top_left_edge_img
                elif tile == '6': # -----
                    self.img = dirt_bottom_top_img
                elif tile == '7':
                    self.img = dirt_right_left_img
                elif tile == '>': # -----
                    self.img = dirt_top_right_left_edge_img
                elif tile == '<':
                    self.img = dirt_bottom_right_left_edge_img
                elif tile == '-': # mixtures
                    self.img = dirt_top_bottom_right_img
                elif tile == '_':
                    self.img = dirt_bottom_top_left_img
                elif tile == '+':
                    self.img = dirt_bottom_top_right_img
                elif tile == '=':
                    self.img = dirt_top_bottom_left_img
                elif tile == '*':
                    self.img = dirt_right_top_left_img
                elif tile == '&':
                    self.img = dirt_right_bottom_left_img
                elif tile == '^':
                    self.img = dirt_left_bottom_right_img
                elif tile == '!': # -----
                    self.img = dirt_bottom_right_edge_top_left_corner_img
                elif tile == '@':
                    self.img = dirt_top_left_edge_bottom_right_corner_img
                elif tile == '#':
                    self.img = dirt_bottom_left_edge_top_right_corner_img
                elif tile == '$':
                    self.img = dirt_top_right_edge_bottom_left_corner_img

                # OTHER TILES
                # j draws jump pad
                elif tile == 'j':
                    self.img = jump_pad_img
                # 7 draws water
                elif tile == '9':
                    self.img = water_img
                # a draws fish button 1
                elif tile == 'a': # lvl1
                    if fish_button_activated:
                        self.img = fish_button_yes_right_img
                    else:
                        self.img = fish_button_right_img
                # s draws fish button 2
                elif tile == 's': # lvl2
                    if fish_button_activated == 'True' or fish_button_activated == 1:
                        self.img = fish_button_yes_left_img
                    else:
                        self.img = fish_button_left_img
                # d draws fish button 3
                elif tile == 'd': # lvl2
                    if fish_button_activated == 'True' or fish_button_activated == 2:
                        self.img = fish_button_yes_right_img
                    else:
                        self.img = fish_button_right_img
                # f draws fish button 4
                elif tile == 'f': # lvl3
                    if fish_button_activated == 'True1' or fish_button_activated == 'True2':
                        self.img = fish_button_yes_left_img
                    else:
                        self.img = fish_button_left_img
                # g draws fish button 5
                elif tile == 'g': # lvl3
                    if fish_button_activated == 'True2':
                        self.img = fish_button_yes_right_img
                    else:
                        self.img = fish_button_right_img
                # g draws fish button 6
                elif tile == 'v': # lvl7
                    if fish_button_activated:
                        self.img = fish_button_yes_right_img
                    else:
                        self.img = fish_button_right_img
                # . draws a placeholder image for the top tile of the exit gate
                elif tile == '.':
                    self.img = gate_top_img
                # / draws a placeholder image for the top tile of the exit gate
                elif tile == '/':
                    self.img = gate_bottom_img

                self.rect = self.img.get_rect()
                self.rect.x = column_count * TILE_SIZE
                self.rect.y = row_count * TILE_SIZE
                tile_info = (self.img, self.rect, tile)
                self.tile_list.append(tile_info)

                column_count += 1
            row_count += 1

    def draw(self):
        # going through the list and drawing each tile onto the screen according to it's image and position assigned
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])
# -----------------------------------------------------------------------

# ------------------------------player setup------------------------------
class Player():
    def __init__(self, x, y):
        self.start(x, y)

    def start(self, x, y):
        # setting inital/start player variables
        if current_character == 1:
            self.img = player1_left_img_list[0]
        elif current_character == 3:
            self.img = player3_left_img_list[0]
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
        # - player walking animation
        self.walk_index = 0
        self.walk_counter = 0
        self.walk_frame_cooldown = 5
        self.on_ground = True
        # fishing rod
        self.fishing_rod_img = pygame.transform.scale(fishing_rod_left_img, (TILE_SIZE*0.5, TILE_SIZE*0.5))
        # water jump ability variables ("wj" = "water jump")
        self.wj_button_img = pygame.transform.scale(wj_button_ready_img, (TILE_SIZE, TILE_SIZE))
        self.water_jumping = False
        self.wj_cooldown = 4000
        self.wj_last_ability = 0
        self.wj_next_ability = 0
        self.wj_next_ability_in = 0
        # - water splash animation
        self.wj_img = pygame.transform.scale(wj_img_list[0], (TILE_SIZE, TILE_SIZE*3.5))
        self.wj_index = 0
        self.wj_frame_cooldown = 1
        self.wj_counter = 0
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
        # going through every tile's position data from the tile data list from the world generation,
        # and seeing if the y position is less than 5 pixels above the player's head
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

        # ------------------------------movement------------------------------
        # player movement using arrow keys (left, right, up for jump)
        if key[pygame.K_LEFT]:
            dx -= self.vel
            self.facing_left = True
            self.facing_right = False
            # only runs walking animation while on the ground
            if self.on_ground:
                self.walk_counter += 1
            self.fishing_rod_img = pygame.transform.scale(fishing_rod_left_img, (TILE_SIZE*0.5, TILE_SIZE*0.5))
        if key[pygame.K_RIGHT]:
            dx += self.vel
            self.facing_right = True
            self.facing_left = False
            # only runs walking animation while on the ground
            if self.on_ground:
                self.walk_counter += 1
            self.fishing_rod_img = pygame.transform.scale(fishing_rod_right_img, (TILE_SIZE*0.5, TILE_SIZE*0.5))
        if key[pygame.K_UP] and self.y_vel == 0 and not self.on_ceiling and not self.tile_above:
            self.on_ground = False
            self.y_vel = -12.1
        # if the user is not pressing left or right keys, or just isn't touching the ground, then it resets the character model to an idle frame
        if (not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]) or not self.on_ground:
            self.walk_counter = 0
            self.walk_index = 0
            if self.facing_right:
                if current_character == 1:
                    self.img = player1_right_img_list[self.walk_index]
                elif current_character == 3:
                    self.img = player3_right_img_list[self.walk_index]
            elif self.facing_left:
                if current_character == 1:
                    self.img = player1_left_img_list[self.walk_index]
                elif current_character == 3:
                    self.img = player3_left_img_list[self.walk_index]

        # walking animation
        # iterating through the player walking animation frame list and changing the character model image (with a cooldown between frames)
        if self.walk_counter > self.walk_frame_cooldown:
            self.walk_counter = 0
            self.walk_index += 1
            if self.walk_index >= len(player1_left_img_list):
                self.walk_index = 0
            if self.facing_right:
                if current_character == 1:
                    self.img = player1_right_img_list[self.walk_index]
                elif current_character == 3:
                    self.img = player3_right_img_list[self.walk_index]
            elif self.facing_left:
                if current_character == 1:
                    self.img = player1_left_img_list[self.walk_index]
                elif current_character == 3:
                    self.img = player3_left_img_list[self.walk_index]
        # --------------------------------------------------------------------
        
        # ------------------------------character switch------------------------------
        if current_lvl == 7:
            # if 's' is pressed, it checks which character it's currently on and switches it to the other one
            if key[pygame.K_s] and not self.s_pressed:
                if current_character == 1:
                    current_character = 3
                    if self.facing_right:
                        self.img = player3_right_img_list[0]
                    elif self.facing_left:
                        self.img = player3_left_img_list[0]
                elif current_character == 3:
                    current_character = 1
                    self.vc = False
                    if self.facing_right:
                        self.img = player1_right_img_list[0]
                    elif self.facing_left:
                        self.img = player1_left_img_list[0]
                self.s_pressed = True
            elif not key[pygame.K_s]:
                self.s_pressed = False
        # ----------------------------------------------------------------------------

        # ------------------------------Water Jump Ability------------------------------
        if current_character == 1:
            # setting climbing variables back to default so that when you switch to character 1, it stops climbing automatically
            self.vc = False
            self.gravity = True
            # calculating time since last jump ability
            time_since_last_wj = pygame.time.get_ticks()-self.wj_last_ability

            # activating jump ability if {space} is pressed
            if key[pygame.K_SPACE] and self.y_vel == 0 and time_since_last_wj > self.wj_cooldown:
                self.water_jumping = True
                self.on_ground = False
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

        # water jump animation
        if self.water_jumping:
            # obtaining original player position when the water jump starts
            # saved so that the water jump animation stays in the same place
            if not self.wj_got_y:
                self.wj_got_y = True
                self.wj_y = self.rect.bottom - TILE_SIZE*3.5
            if not self.wj_got_x:
                self.wj_got_x = True
                self.wj_x = self.rect.x
            # works the same way as the walking animation
            # iterating through the water jump animation frames list and changing the animation frame by 1 (with a cooldown between frames)
            self.wj_counter += 1
            if self.wj_counter > self.wj_frame_cooldown:
                self.wj_counter = 0
                self.wj_index += 1
                if self.wj_index >= len(wj_img_list):
                    self.water_jumping = False
                    self.wj_index = 0
                self.wj_img = pygame.transform.scale(wj_img_list[self.wj_index], (TILE_SIZE, TILE_SIZE*3.5))
        # ------------------------------------------------------------------------------

        # ------------------------------Vine Climb Ability------------------------------
        if current_character == 3:
            # checking if the 'a' key is being pressed and only turning off gravity if on ceiling
            if key[pygame.K_a]:
                self.vc = True
                if self.on_ceiling and self.tile_above:
                    self.on_ground = False
                    self.gravity = False
                    self.on_wall = False
                    if self.facing_right:
                        self.img = player3_right1_climb_img
                    elif self.facing_left:
                        self.img = player3_left1_climb_img
            elif not key[pygame.K_a]:
                self.vc = False
                self.gravity = True
                self.on_wall = False
            # playing vine climbing sound effect if climbing (wall or ceiling)
            if self.vc and (self.on_ceiling or self.on_wall):
                vines_sound.set_volume(sound_multi*0.5)
                vines_sound.play()
        # ------------------------------------------------------------------------------

        # gravity
        # making the player move/fall down by 1px per frame
        if self.gravity:
            self.y_vel += 1
        # setting max falling velocity to 15px/frame
        if self.y_vel > 15:
            self.y_vel = 15
        dy += self.y_vel

        # checking for collision
        # going through every tile in the list created in world.__init__
        # only checking for collision in tiles that aren't 0 (aren't background) or the placeholder exit gate tiles
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
                        self.on_ground = False
                        self.y_vel = 0.1
                        dy -= self.vel
                # vertical collision
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                    # stopping water jump when the player hits ceiling or floor
                    self.water_jumping = False
                    # if jumping/if hitting head
                    if dy < 0 or self.y_vel <= 0:
                        # only changing vertical movement by the distance to the tile it would collide with
                        dy = tile[1].bottom - self.rect.top
                        self.y_vel = 0.1
                        if self.vc:
                            self.on_ceiling = True
                        elif not self.vc:
                            self.on_ceiling = False
                    # if falling/if hitting ground
                    elif self.y_vel > 0:
                        self.on_ground = True
                        self.wj_got_x = False
                        self.wj_got_y = False
                        # only changing vertical movement by the distance to the tile it would collide with
                        dy = tile[1].top - self.rect.bottom
                        self.y_vel = 0
                        self.on_ceiling = False
                        self.on_wall = False
                        # if the tile it collides with is a "j" (jump pad), then it launches the player up and plays a bounce sound effect
                        if tile[2] == 'j':
                            self.y_vel = -30.1
                            bounce_sound.set_volume(sound_multi*2)
                            bounce_sound.play()

        # updating player model coordinates
        self.rect.x += dx
        self.rect.y += dy

    # function to find the player x, y, and bottom coords
    # (made this before I knew how to access global variables in functions)
    def player_xy_bottom(self):
        return (self.rect.x, self.rect.y, self.rect.bottom)

    def draw(self):
        global current_lvl
        # drawing character image onto screen
        win.blit(self.img, self.rect)

        if current_lvl in (1, 2, 3, 7):
            # drawing wj (water jump) ability cooldown button onto screen
            win.blit(self.wj_button_img, (TILE_SIZE*0.25, TILE_SIZE*1.5))
        # changing the wj ability cooldown button to a more greyed out icon and adds a cooldown timer when not ready
        if round(self.wj_next_ability_in/1000) <= -1:
            self.wj_button_img = wj_button_ready_img
        else:
            self.wj_button_img = wj_button_not_ready_img
            draw_text(f'{round(self.wj_next_ability_in/1000+1)}', pixel_font, white, TILE_SIZE*0.63, TILE_SIZE*1.65, TILE_SIZE/3)

        # drawing fishing rod in player's hand when attracting fish
        if fish_attracting and current_character == 1:
            if self.facing_right:
                win.blit(self.fishing_rod_img, (self.rect.x+TILE_SIZE-7, self.rect.y+self.rect.height/2-7))
            elif self.facing_left:
                win.blit(self.fishing_rod_img, (self.rect.x-TILE_SIZE*0.5+7, self.rect.y+self.rect.height/2-7))

        # drawing the water jump animation frames onto the screen
        if self.water_jumping:
            win.blit(self.wj_img, (self.wj_x, self.wj_y))
# ------------------------------------------------------------------------

# ------------------------------button setup------------------------------
class Button():
    def __init__(self, image, x, y, width, height):
        # setting initial image and coordinates of the button
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
            # checking if left mouse button is also clicked then saves that it has been clicked
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
        # setting initial image and coordinates of the fish
        original_width = fish_img.get_width()
        original_height = fish_img.get_height()
        scale_factor = width/original_width
        self.img = pygame.transform.scale(fish_img, (width, original_height*scale_factor))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.vel = 3
        self.fish_num = num
        self.start(x1, x2, y1, y2)

    # starting position of the fish
    # randomly picked in a range
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
                    # checking if fish touched their respective button and returning the value
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
        # setting initial image and coordinates of the gate
        self.img = pygame.transform.scale(gate_img, (width, height))
        self.rect = self.img.get_rect()
        self.draw(x, y)

    def update(self):
        # checking if gate is touching player and returning the value
        if player.rect.colliderect(self.rect):
            return True

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y
        # drawing the gate onto the screen
        win.blit(self.img, self.rect)
# ---------------------------------------------------------------------------

# initializing player
player = Player(player_x, player_y)

# initializing exit gate
gate = Gate(TILE_SIZE*24, TILE_SIZE*1, TILE_SIZE, TILE_SIZE*2)

# initializing fish
fish1 = Fish(TILE_SIZE*13, TILE_SIZE*24, TILE_SIZE*11, TILE_SIZE*13, TILE_SIZE*0.75, 1) # lvl1
fish2 = Fish(TILE_SIZE*8, TILE_SIZE*9, TILE_SIZE*2, TILE_SIZE*3, TILE_SIZE*0.75, 2) # lvl2
fish3 = Fish(TILE_SIZE*14, TILE_SIZE*17, TILE_SIZE*6, TILE_SIZE*7, TILE_SIZE*0.75, 3) # lvl3
fish4 = Fish(TILE_SIZE*4, TILE_SIZE*10, TILE_SIZE*8, TILE_SIZE*10, TILE_SIZE*0.75, 4) # lvl3
fish5 = Fish(TILE_SIZE*7, TILE_SIZE*8, TILE_SIZE*2, TILE_SIZE*3, TILE_SIZE*0.75, 5) # lvl7

# initializing different buttons
# - start menu buttons
start_button = Button(start_img, WIN_WIDTH/2-TILE_SIZE*6.22, TILE_SIZE*5.5, TILE_SIZE*12.44, TILE_SIZE*3.5)
quit_button = Button(quit_img, WIN_WIDTH/2-TILE_SIZE*1.92, TILE_SIZE*11, TILE_SIZE*3.83, TILE_SIZE*1.5)
speedrun_no_button = Button(blank_button_img, TILE_SIZE*21, TILE_SIZE*7, TILE_SIZE*2, TILE_SIZE*2)
speedrun_yes_button = Button(yes_img, TILE_SIZE*21, TILE_SIZE*7, TILE_SIZE*2, TILE_SIZE*2)
reset_game_button = Button(reset_game_img, TILE_SIZE*1.25, TILE_SIZE*12.75, TILE_SIZE*2, TILE_SIZE)
# - in level button
pause_button = Button(pause_img, TILE_SIZE*0.25, TILE_SIZE*0.25, TILE_SIZE, TILE_SIZE)
# - pause screen buttons
home_button = Button(home_img, TILE_SIZE*5, TILE_SIZE*8, TILE_SIZE*3, TILE_SIZE*3)
restart_button = Button(restart_img, WIN_WIDTH/2-TILE_SIZE*1.5, TILE_SIZE*8, TILE_SIZE*3, TILE_SIZE*3)
resume_button = Button(resume_img, WIN_WIDTH-TILE_SIZE*8, TILE_SIZE*8, TILE_SIZE*3, TILE_SIZE*3)
# - confirm home menu buttons
yes_button = Button(yes_img, WIN_WIDTH/2-TILE_SIZE*4.5, TILE_SIZE*8, TILE_SIZE*3, TILE_SIZE*3)
no_button = Button(no_img, WIN_WIDTH/2+TILE_SIZE*1.5, TILE_SIZE*8, TILE_SIZE*3, TILE_SIZE*3)

# the main game loop that always runs
run = True
while run:
    # getting the pygame list of key presses which checks whether a key is being pressed
    key = pygame.key.get_pressed()

    # setting the max frame rate so that the game runs the same on every device
    clock.tick(FPS)

    # stops the game when the window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # setting background colour of window
    win.fill(black)

    # showing different level layouts on screen
    if lvl_changed:
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
        lvl_changed = False
    
    if start_menu:
        world = World(levels.lvl0_data)

    # drawing level/world
    world.draw()

    # if the transition has started
    if transitioning:
        transition_end()
        transitioning = False
        paused = False

    # start menu code
    if start_menu:
        paused = True
        # writing the title on screen with a shadow
        draw_text('STUCK IN BETWEEN', pixel_font, dark_brown, WIN_WIDTH/2-TILE_SIZE*10-5, TILE_SIZE*1.5+5, TILE_SIZE*20)
        draw_text('STUCK IN BETWEEN', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*10, TILE_SIZE*1.5, TILE_SIZE*20)
        # drawing start button
        #  - if the start button is pressed, the start menu closes and starts/resumes the game
        #  - if it's currently on level 1, it plays the beginning cut scene first then starts the game
        if start_button.draw():
            restart_lvl()
            start_menu = False
            pause_menu = False
            player.start(player_x_start, player_y_start)
            paused = True
            fish_button_activated = False
            transitioning = True
            lvl_changed = True
            transition_start()
            if current_lvl == 1:
                play_vid('cut scenes/start scene.mp4')
                transition_start()
            if speedrun:
                if current_lvl == 1:
                    speedrun_start_time = pygame.time.get_ticks()
                elif current_lvl in range(2, 8):
                    speedrun_start_time += pygame.time.get_ticks() - pause_start_time
        # writing the words "SPEEDRUN MODE" above the button to turn on/off speedrun mode
        draw_text('SPEEDRUN', pixel_font, light_brown, TILE_SIZE*20, TILE_SIZE*5, TILE_SIZE*4)
        draw_text('MODE', pixel_font, light_brown, TILE_SIZE*20.75, TILE_SIZE*5.83, TILE_SIZE*2.5)
        # drawing the speedrun mode button
        # - each time it gets clicked, it adds/removes the check mark indicating whether speedrun mode is turned on/off
        if speedrun:
            if speedrun_yes_button.draw():
                speedrun = False
        elif not speedrun:
            if speedrun_no_button.draw():
                speedrun = True
        # drawing quit button
        #  - if the quit button is pressed, the game window stops/closes
        if quit_button.draw():
            run = False
        # drawing reset game button
        # - if the reset game button is pressed, it disappears and the entire game resets itself, starting back at level one
        if not resetted_game:
            if reset_game_button.draw():
                resetted_game = True
                current_lvl = 1
                fish_button_activated = False
                restart_lvl()
    else:
        # (drawing things whether paused and unpaused)
        if current_lvl == 1:
            # drawing fish
            fish1.draw()
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*1)
            # drawing key instructions on the screen ("arrows to move" & "'a' to attract fish" & "space for water jump")
            if fish_button_activated:
                win.blit(space_for_water_jump_img, (TILE_SIZE*3.5, TILE_SIZE*1.5))
                win.blit(arrow_left_img, (TILE_SIZE*1.5, TILE_SIZE*1.83))
            else:
                win.blit(arrows_to_move_img, (TILE_SIZE*2.5, TILE_SIZE*1.5))
                win.blit(a_to_attract_fish_img, (TILE_SIZE*18.75, TILE_SIZE*13))
        elif current_lvl == 2:
            # drawing fish
            fish2.draw()
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*12)
        elif current_lvl == 3:
            # drawing fish
            fish3.draw()
            fish4.draw()
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*12)
        elif current_lvl == 4:
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*1)
            # drawing key instructions on the screen ("'a' to climb")
            win.blit(a_to_climb_img, (TILE_SIZE*20.5, TILE_SIZE*4.75))
        elif current_lvl == 5:
            # drawing exit gate
            gate.draw(TILE_SIZE*2, TILE_SIZE*2)
        elif current_lvl == 6:
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*4)
        elif current_lvl == 7:
            # drawing fish
            fish5.draw()
            # drawing exit gate
            gate.draw(TILE_SIZE*24, TILE_SIZE*12)
            # drawing key instructions on sthe screen ("'s' to switch")
            win.blit(s_to_switch_img, (TILE_SIZE*20.5, TILE_SIZE*4.75))
        
        # drawing player
        player.draw()

        # drawing speedrun timer on screen based on the stored display time which updates when unpaused
        if speedrun:
            speedrun_display_time = f'{(speedrun_time/1000):.1f}s'
            # (only renders a new timer text image if it's actually changed (every 0.1secs) to reduce lag)
            if speedrun_display_time != speedrun_stored_time:
                speedrun_stored_time = speedrun_display_time
                speedrun_timer_img = pixel_font.render(speedrun_display_time, True, white)
                speedrun_timer_img = pygame.transform.scale(speedrun_timer_img, (len(speedrun_display_time)*TILE_SIZE*0.5, TILE_SIZE))
            win.blit(speedrun_timer_img, (TILE_SIZE*0.25, TILE_SIZE*14))

        if paused:
            if pause_menu:
                # drawing pause menu background
                draw_pause_background()
                # drawing 'PAUSED'
                draw_text('PAUSED', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*5, TILE_SIZE*3, TILE_SIZE*10)
                # drawing "(r)" above the restart button to indicate that you can also press "r" during the level to restart it
                draw_text('(R)', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*0.75, TILE_SIZE*7, TILE_SIZE*1.5)
                # drawing home button
                # - if home button is pressed, it opens a confirm menu which asks whether the user actually wants to go back (restarts current level)
                if home_button.draw():
                    pause_menu = False
                    confirm_home_menu = True
                    resetted_game = False
                # drawing restart button
                # - if restart button is pressed, the current level restarts
                elif restart_button.draw():
                    pause_menu = False
                    paused = False
                    restart_lvl()
                # drawing resume button
                # - if resume button is pressed, the level continues with no change
                elif resume_button.draw():
                    paused = False
                    pause_menu = False
                    if speedrun:
                        speedrun_start_time += pygame.time.get_ticks() - pause_start_time
            
            if confirm_home_menu:
                # drawing the same background as the pause menu
                draw_pause_background()
                # writing a warning message to the user
                draw_text('WARNING', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*5, TILE_SIZE*2.5, TILE_SIZE*10)
                draw_text('GOING HOME WILL ALSO RESTART CURRENT LEVEL', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*7.5, TILE_SIZE*5.25, TILE_SIZE*15)
                draw_text('CONFIRM?', pixel_font, light_brown, WIN_WIDTH/2-TILE_SIZE*2.5, TILE_SIZE*6.25, TILE_SIZE*5)
                # drawing the confirm button
                # - if pressed, it continues and goes back to the start menu and restarts current level
                if yes_button.draw():
                    confirm_home_menu = False
                    start_menu = True
                    restart_lvl()
                # drawing the decline button
                # - if pressed, it goes back to the normal pause menu
                elif no_button.draw():
                    confirm_home_menu = False
                    pause_menu = True
        else:
            # updating player
            player.update(True)
            player_x = player.player_xy_bottom()[0]
            player_y = player.player_xy_bottom()[1]
            player_bottom = player.player_xy_bottom()[2]

            # updating speedrun timer
            if speedrun:
                speedrun_time = pygame.time.get_ticks()-speedrun_start_time

            # setting character so that different abilities will be in use depending on what level it's currently on
            if current_lvl in (1, 2, 3):
                current_character = 1
            elif current_lvl in (4, 5, 6):
                current_character = 3

            # if currently in a level with a fish
            if current_lvl in (1, 2, 3, 7):
                if current_lvl == 1:
                    # updating fish
                    # when fish touches button, it returns true and changes level layout, creating a new platform to reach the exit gate
                    if fish1.update():
                        fish_button_activated = True
                        lvl_changed = True
                elif current_lvl == 2:
                    # updating fish
                    # checking if the fish touches either button and to only change level layout when both have been pressed, opening a gap to the exit gate
                    if fish2.update() == 'True1':
                        if fish_button_activated == False:
                            fish_button_activated = 1
                            lvl_changed = True
                        elif fish_button_activated == 2:
                            fish_button_activated = 'True'
                            lvl_changed = True
                    if fish2.update() == 'True2':
                        if fish_button_activated == False:
                            fish_button_activated = 2
                            lvl_changed = True
                        elif fish_button_activated == 1:
                            fish_button_activated = 'True'
                            lvl_changed = True
                elif current_lvl == 3:
                    # updating fish
                    # if the fish touches its respective button, the level changes to open up different parts
                    #  - first fish opens the level to access the other fish
                    #  - 2nd fish opens a gap to the exit gate
                    if fish3.update():
                        fish_button_activated = 'True1'
                        lvl_changed = True
                    if fish4.update():
                        fish_button_activated = 'True2'
                        lvl_changed = True
                # CHARACTER SWITCH LEVEL
                elif current_lvl == 7:
                    # updating fish
                    # when fish touches button, it returns true and changes the level layout, opening a gap to make a path to the exit gate
                    if fish5.update():
                        fish_button_activated = True
                        lvl_changed = True

                # checking to see if "a" is being pressed
                if current_character == 1:
                    fish_attracting = fish_attract_check()
                else:
                    fish_attracting = False

            # if the player falls off the bottom of the screen or goes above the screen, the player dies/restarts level
            if player_y > TILE_SIZE*17 or player_y < 0:
                lvl_changed = True
                fish_button_activated = False
                player.start(player_x_start, player_y_start)
                fish5.start(TILE_SIZE*7, TILE_SIZE*8, TILE_SIZE*1, TILE_SIZE*2)
                world = World(levels.lvl7_data)

            # checking to see if player is touching exit gate
            #  - if on level 7 (last level) then it plays the ending cut scene and then the credits
            #  - if on any other level, it plays transition and starts the player on the next level
            if gate.update():
                lvl_changed = True
                if current_lvl == 7:
                    paused = True
                    fish_button_activated = False
                    current_lvl = 1
                    transition_start()
                    play_vid('cut scenes/end scene.mp4')
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

            # checking to see if "r" is being pressed,
            # and if so, then it restarts the level
            if key[pygame.K_r] and not r_pressed:
                restart_lvl()
                r_pressed = True
            elif not key[pygame.K_r]:
                r_pressed = False

            # if pause button is pressed, open pause menu and pause all game updates
            if pause_button.draw() or (key[pygame.K_ESCAPE] and not esc_held):
                paused = True
                pause_menu = True
                pause_start_time = pygame.time.get_ticks()

            # checking to see whether the escape key is being held behind the scenes when the game wasn't updating
            if key[pygame.K_ESCAPE]:
                esc_held = True
            else:
                esc_held = False
    
    # updating the window constantly so that everything appears
    pygame.display.update()

# closes the game window when not running
pygame.quit()
exit()