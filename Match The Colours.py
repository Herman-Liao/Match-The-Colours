import pygame, sys, random, math
from pygame.locals import*
from math import*
width = 1920
height = 1080
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Match the Colours!")

#Define functions
def Deflect(projectile_direction, deflector_direction):
    direction_difference = projectile_direction - deflector_direction
    new_projectile_direction = deflector_direction - direction_difference
    return new_projectile_direction

def Draw_text(surface, font, x, y, text, colour = (192, 192, 192)):
    text_object = font.render(text, 1, colour)
    text_rect = text_object.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_object, text_rect)

def Choose_settings():
    FPS = 60
#Define variables
    #Fonts
    regular_font = pygame.font.SysFont(None, 50)
    
    #Lists
    buttons = [Button(width / 2, 9 * height / 10, 100, 50, False, "Start"),
               Button(50, 25, 100, 50, False, "Quit"),
               Button(width / 4, 50, 225, 50, False, "Instructions"),
               Button(width / 2, 50, 300, 50, False, "Default Settings"),
               Button(3 * width / 4, 50, 175, 50, False, "FPS: " + str(FPS))]
    sliders = [Slider(1 * width / 6, 790 * height / 1080, 50, 30, (1 * width / 6, 125), (1 * width / 6, height - 125), False, 0),
               Slider(2 * width / 6, 642 * height / 1080, 50, 30, (2 * width / 6, 125), (2 * width / 6, height - 125), False, 0),
               Slider(3 * width / 6, 605 * height / 1080, 50, 30, (3 * width / 6, 125), (3 * width / 6, height - 125), False, 0),
               Slider(4 * width / 6, 125 * height / 1080, 50, 30, (4 * width / 6, 125), (4 * width / 6, height - 125), False, 0),
               Slider(5 * width / 6, 955 * height / 1080, 50, 30, (5 * width / 6, 125), (5 * width / 6, height - 125), False, 0)]

    #Booleans
    running = True

    #Settings menu
    while running:
        window.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for slider in sliders:
                        if slider.x - slider.length / 2 <= mouse_pos[0] <= slider.x + slider.length / 2 and slider.y - slider.width / 2 <= mouse_pos[1] <= slider.y + slider.width / 2:
                            slider.moving = True
                    for button in buttons:
                        if button.x - button.length / 2 <= mouse_pos[0] <= button.x + button.length / 2 and button.y - button.width / 2 <= mouse_pos[1] <= button.y + button.width / 2:
                            button.pressed = True
                            button_text = button.text
                if event.button == 2:
                    print(mouse_pos)
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    for slider in sliders:
                        slider.moving = False
                    for button in buttons:
                        if button.x - button.length / 2 <= mouse_pos[0] <= button.x + button.length / 2 and button.y - button.width / 2 <= mouse_pos[1] <= button.y + button.width / 2 and button.text == button_text:
                            if button.text == "Start":
                                running = False
                            if button.text == "Quit":
                                pygame.quit()
                                sys.exit()
                            if button.text == "Default Settings":
                                sliders[0].y = 790 * height / 1080
                                sliders[1].y = 642 * height / 1080
                                sliders[2].y = 605 * height / 1080
                                sliders[3].y = 125 * height / 1080
                                sliders[4].y = 955 * height / 1080
                            if button.text == "FPS: " + str(FPS):
                                FPS += 30
                                if FPS == 150:
                                    FPS = 30
                                button.text = "FPS: " + str(FPS)
                        button.pressed = False
        for slider in sliders:
            if slider.moving == True:
                if slider.linestart[0] == slider.lineend[0]:
                    if mouse_pos[1] < slider.linestart[1]:
                        slider.y = slider.linestart[1]
                    elif mouse_pos[1] > slider.lineend[1]:
                        slider.y = slider.lineend[1]
                    else:
                        slider.y = mouse_pos[1]
                if slider.linestart[1] == slider.lineend[1]:
                    if mouse_pos[0] < slider.linestart[0]:
                        slider.x = slider.linestart[0]
                    elif mouse_pos[0] > slider.lineend[0]:
                        slider.x = slider.lineend[0]
                    else:
                        slider.x = mouse_pos[0]
            if slider == sliders[0]:
                slider.value = int((slider.lineend[1] - slider.y) / (slider.lineend[1] - slider.linestart[1]) * 49) + 1
            if slider == sliders[1]:
                slider.value = int((slider.lineend[1] - slider.y) / (slider.lineend[1] - slider.linestart[1]) * 240) + 10
            if slider == sliders[2]:
                slider.value = int((slider.lineend[1] - slider.y) / (slider.lineend[1] - slider.linestart[1]) * 25)
            if slider == sliders[3]:
                slider.value = int((slider.lineend[1] - slider.y) / (slider.lineend[1] - slider.linestart[1]) * 27) + 1
            if slider == sliders[4]:
                slider.value = int((slider.lineend[1] - slider.y) / (slider.lineend[1] - slider.linestart[1]) * 300)
            slider.display()
            Draw_text(window, regular_font, width / 6, 100, "# of pairs", (0, 0, 0))
            Draw_text(window, regular_font, width / 3, 100, "Square size", (0, 0, 0))
            Draw_text(window, regular_font, width / 2, 100, "Square speed", (0, 0, 0))
            Draw_text(window, regular_font, 2 * width / 3, 100, "max # of colours", (0, 0, 0))
            Draw_text(window, regular_font, 5 * width / 6, 100, "Timer (0 for none)", (0, 0, 0))
        for button in buttons:
            button.display()
        pygame.display.flip()
        clock.tick(FPS)
    Game(sliders[0].value, sliders[1].value, sliders[2].value, sliders[3].value, FPS, sliders[4].value)

def Game(number_of_pairs, square_size, square_speed, number_of_colours, FPS, timer = 0):
#Define variables
    #Fonts
    regular_font = pygame.font.SysFont(None, 50)
    large_font = pygame.font.SysFont(None, 200)
    
    #Integers
    layer = 0
    top_layer = 0

    #Lists
        #There are 125 possible square colours
    colours = []
##    colours = [(0, 0, 0), (64, 64, 64), (128, 128, 128), (192, 192, 192),
##               (255, 0, 0), (0, 255, 0), (0, 0, 255),
##               (0, 255, 255), (255, 0, 255), (255, 255, 0),
##               (64, 0, 0), (0, 64, 0), (0, 0, 64),
##               (0, 64, 64), (64, 0, 64), (64, 64, 0),
##               (128, 0, 0), (0, 128, 0), (0, 0, 128),
##               (0, 128, 128), (128, 0, 128), (128, 128, 0),
##               (192, 0, 0), (0, 192, 0), (0, 0, 192),
##               (0, 192, 192), (192, 0, 192), (192, 192, 0)]
    rgb_values = [0, 64, 128, 192, 255]
    for r in rgb_values:
        for g in rgb_values:
            for b in rgb_values:
                colours.append((r, g, b))
    squares = []
    removal_list = []
    possible_colours = []

    #Other
    selected = None

#Choose all the possible square colours
    for i in range(number_of_colours):
        chosen_colour = random.choice(colours)
        while chosen_colour in possible_colours:
            chosen_colour = random.choice(colours)
        possible_colours.append(chosen_colour)

#Make squares with random colours
    for i in range(number_of_pairs):
        square_colour = random.choice(possible_colours)
        for j in range(2):
            squares.append(Square(random.randint(round(square_size / 2, 0), width - round(square_size / 2, 0)),
                                  random.randint(round(square_size / 2, 0), height - round(square_size / 2, 0)),
                                  random.uniform(0, pi / 2),
                                  random.uniform(-square_speed, square_speed),
                                  square_colour, square_size, layer, FPS))
            layer += 1

    timer *= FPS
    if timer == 0:
        timer_display = False
    else:
        timer_display = True

#Game loop
    while True:
        window.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()
#Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for square in squares:
                        if square.x - square.side / 2 <= mouse_pos[0] <= square.x + square.side / 2 and square.y - square.side / 2 <= mouse_pos[1] <= square.y + square.side / 2:
                            removal_list.append(square)
                    top_layer = -1
                    for square in removal_list:
                        if square.layer > top_layer:
                            top_layer = square.layer
                    for square in squares:
                        if square.layer == top_layer:
                            if selected == None or selected.colour != square.colour or selected == square:
                                selected = square
                            else:
                                if selected.colour == square.colour:
                                    squares.remove(square)
                                    squares.remove(selected)
                                    selected = None
                    removal_list = []
#Class functions
        for square in squares:
            square.move()
            square.display()
#Other
        if squares == []:
            Draw_text(window, large_font, width / 2, height / 2, "You win!", (255, 0, 0))
            Draw_text(window, large_font, width / 2, height / 2 + 250, str(format(timer / FPS, ".2f")) + " s", (255, 0, 0))
            break
        if selected != None:
            pygame.draw.circle(window, (255, 255, 255), (int(selected.x), int(selected.y)), int(selected.side / 4))
            pygame.draw.line(window, (0, 0, 0), (int(selected.x - selected.side / 4), int(selected.y)), (int(selected.x + selected.side / 4), int(selected.y)), 5)
            pygame.draw.line(window, (0, 0, 0), (int(selected.x), int(selected.y - selected.side / 4)), (int(selected.x), int(selected.y + selected.side / 4)), 5)
        if timer_display == True:
            if timer != 0:
                timer -= 1
            else:
                Draw_text(window, large_font, width / 2, height / 2, "Time's up!", (255, 0, 0))
                Draw_text(window, large_font, width / 2, height / 2 + 250, "0 s", (255, 0, 0))
                break
        else:
            timer += 1
        Draw_text(window, regular_font, width / 2, height / 25, str(format(timer / FPS, ".2f")), (0, 0, 0))
#Draw everything, set FPS
        pygame.display.flip()
        clock.tick(FPS)

    timer = 3 * FPS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if timer != 0:
            timer -= 1
        else:
            break
        pygame.display.flip()
        clock.tick(FPS)
    Choose_settings()

#Define classes
class Square:
    def __init__(self, x, y, direction, speed, colour, side, layer, FPS):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.side = side
        self.colour = colour
        self.layer = layer
        self.FPS = FPS
    def move(self):
        if self.x - self.side / 2 <= 0 or self.x + self.side / 2 >= width:
            self.direction = Deflect(self.direction, pi / 2)
        if self.y - self.side / 2 <= 0 or self.y + self.side / 2 >= height:
            self.direction = Deflect(self.direction, 0)
        self.x += self.speed * cos(self.direction) * 60 / self.FPS
        self.y += self.speed * sin(self.direction) * 60 / self.FPS
    def display(self):
        pygame.draw.rect(window, self.colour, (self.x - self.side / 2, self.y - self.side / 2, self.side, self.side))
        pygame.draw.rect(window, (0, 0, 0), (self.x - self.side / 2, self.y - self.side / 2, self.side, self.side), 1)

class Slider:
    def __init__(self, x, y, length, width, linestart, lineend, moving, value):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.linestart = linestart
        self.lineend = lineend
        self.value = value
        self.font = pygame.font.SysFont(None, 50)
        self.moving = moving
    def display(self):
        pygame.draw.line(window, (128, 128, 128), self.linestart, self.lineend, 7)
        pygame.draw.rect(window, (64, 64, 64), (self.x - self.length / 2, self.y - self.width / 2, self.length, self.width))
        Draw_text(window, self.font, self.x, self.y + 2, str(self.value))

class Button:
    def __init__(self, x, y, length, width, pressed = False, text = ""):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.pressed = pressed
        self.text = text
        self.font = pygame.font.SysFont(None, 50)
    def display(self):
        if self.pressed == False:
            pygame.draw.rect(window, (255, 0, 0), (self.x - self.length / 2, self.y - self.width / 2, self.length, self.width))
            Draw_text(window, self.font, self.x, self.y + 2, self.text, (0, 255, 0))
        if self.pressed == True:
            pygame.draw.rect(window, (0, 255, 0), (self.x - self.length / 2, self.y - self.width / 2, self.length, self.width))
            Draw_text(window, self.font, self.x, self.y + 2, self.text, (255, 0, 0))

Choose_settings()
