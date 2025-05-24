# Joseph Bath, Vincenzo Milano, Ethan Corno
# Mr. Tauro
# ICS4U1
# June 13th 2021
# Final CPT - MusicGuessr Game

# Library and class imports
import pygame, random, sys
from pyvidplayer import Video
from pygame import mixer
from button import Button

# Initializations
pygame.init()
pygame.mixer.init()

# Answer Key Dictionary
answerKey = [
    "Grenade", 
    "Baby",
    "Beautiful Girls",
    "Broken",
    "Danza Kaduro",
    "Ego",
    "Just Cant Get Enough",
    "Love Me Again",
    "Papaoutai",
    "Pursuit of Happiness",
    "Riptide",
    "Rude",
    "Summer",
    "Sweater Weather",
    "Young Girls"
]

# Constant Variables:
bg = pygame.image.load("Assets\\bg.png")
bgMusic = pygame.mixer.Sound("Assets\\bgMusic.wav")
beep_sound = pygame.mixer.Sound("Assets\\Beep.wav")
gong_sound = pygame.mixer.Sound("Assets\\Gong.wav")
width = 1450
height = 750
isMute = False
currentTime = 0
rounds = 7
clock = pygame.time.Clock()
clients = 2
user_text = ''
vidNum = 0
correct = 0
incorrect = 0

# Other setup prompts
screen = pygame.display.set_mode([width,height])
mixer.music.load('Assets\\bgMusic.wav')

# Font Functions
def get_font(size): # Returns font in the desired size
    return pygame.font.Font("Assets\\gameFont.ttf", size)
def get_title_font(size): # Returns font in the desired size
    return pygame.font.Font("Assets\\fontShaded.ttf", size)

# Checks if the program is muted or not
def func_isMute():
    global isMute
    if isMute:
        mixer.music.stop()
    return isMute

# Game function that plays countdown, plays video and user results     
def game():
    pygame.display.set_caption("Music Guessr")

    while True:
        # Pastes backgroud over existing UI
        screen.blit(bg, (0,0))

        # Gets user mouse position
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        # Checks if quit button has been clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
                
        # Updates Display
        pygame.display.update()

# Options Function
def options():
    global clients, rounds
    pygame.display.set_caption("Options")
    mixer.music.play()
    while True:
        global isMute, clients
        func_isMute()
        # Pastes backgroud over existing UI
        screen.blit(bg, (0,0))

        # Gets user mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Options Title
        OPTIONS_TITLE_TEXT = get_title_font(100).render("OPTIONS", True, "#EA4492")
        OPTIONS_TITLE_RECT = OPTIONS_TITLE_TEXT.get_rect(center=(width/2, 75))
        screen.blit(OPTIONS_TITLE_TEXT, OPTIONS_TITLE_RECT)

        # Initialize buttons
        RETURN_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/4) * 3.5, 700), 
                            text_input="RETURN", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")
        MUTE_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/2), 200), 
                            text_input="MUTE", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")
        PLAYERS_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(1050, 375), 
                            text_input= str(clients), font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")
        ROUNDS_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(1050 - 125, 535), 
                            text_input= str(rounds), font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        # Players Title
        PLAYERS_TITLE_TEXT = get_title_font(75).render("NUM OF PLAYERS:", True, "#EA4492")
        PLAYERS_TITLE_RECT = OPTIONS_TITLE_TEXT.get_rect(center=(400, 385))
        screen.blit(PLAYERS_TITLE_TEXT, PLAYERS_TITLE_RECT)

        # Rounds title
        ROUNDS_TEXT = get_title_font(75).render("ROUNDS:", True, "#EA4492")
        ROUNDS_RECT = ROUNDS_TEXT.get_rect(center=(675 - 125 , 535))
        screen.blit(ROUNDS_TEXT, ROUNDS_RECT)

        if func_isMute():
            MUTE_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/2), 215), 
                            text_input="UNMUTE", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        # Load buttons and updates if they are hovered over
        for button in [RETURN_BUTTON, MUTE_BUTTON, PLAYERS_BUTTON, ROUNDS_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        # Checks for user clicks on buttons or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    return
                if MUTE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    isMute = not isMute
                    if not isMute:
                        mixer.music.play()
                if PLAYERS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    clients += 1
                    if clients > 4:
                        clients = 1
                if ROUNDS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    rounds += 1
                    if rounds > 15:
                        rounds = 1
                    
        
        # Updates display
        pygame.display.update()

# Rules function - called as the first sequence of play() function
def rules():
    gong_sound.play()
    while True:
        # Pastes backgroud over existing GUI
        screen.blit(bg, (0,0))

        # Gets user mouse position
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        # Rules title code
        RULES_TITLE_TEXT = get_title_font(100).render("RULES", True, "#EA4492")
        RULES_TITLE_RECT = RULES_TITLE_TEXT.get_rect(center=(width/2, 75))
        screen.blit(RULES_TITLE_TEXT, RULES_TITLE_RECT) 

        # Rules code
        RULES_TEXT = get_font(50).render("1. Guess the name of the song stright from your device", True, "#EA4492")
        RULES_RECT = RULES_TEXT.get_rect(center=(width/2, 200))
        RULES1_TEXT = get_font(30).render("2. Capitalization does not matter, as long as you spell the name correctly, you will be awarded!", True, "#EA4492")
        RULES1_RECT = RULES1_TEXT.get_rect(center=(width/2, 275))
        RULES2_TEXT = get_font(40).render('3. Do not include punctuation in your answer (E.x \', ! , .)', True, '#EA4492')
        RULES2_RECT = RULES2_TEXT.get_rect(center=(width/2, 350))
        RULES3_TEXT = get_font(40).render('4. Players are awarded based on speed and accuracy', True, '#EA4492')
        RULES3_RECT = RULES3_TEXT.get_rect(center=(width/2, 425))
        RULES4_TEXT = get_font(70).render('GOOD LUCK AND HAVE FUN!', True, '#EA4492')
        RULES4_RECT = RULES4_TEXT.get_rect(center=(width/2, 575))
        screen.blit(RULES_TEXT, RULES_RECT)
        screen.blit(RULES1_TEXT, RULES1_RECT)
        screen.blit(RULES2_TEXT, RULES2_RECT)
        screen.blit(RULES3_TEXT, RULES3_RECT)
        screen.blit(RULES4_TEXT, RULES4_RECT)

        # Initialize buttons
        CONTINUE_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/4) * 3.5, 700), 
                            text_input="CONTINUE", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        # Load buttons and updates if they are hovered over
        for button in [CONTINUE_BUTTON]:
            button.changeColor(RULES_MOUSE_POS)
            button.update(screen)

        # Checks for user clicks on buttons or quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if CONTINUE_BUTTON.checkForInput(RULES_MOUSE_POS):
                    return
        
        # Updates Display
        pygame.display.update()

# Countdown function
def countdown():
    global width, height

    screen.blit(bg, (0,0))
    counter, text = 6, '6'
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    COUNTDOWN_TITLE_TEXT = get_title_font(100).render("Click To Begin!", True, "#EA4492")
    COUNTDOWN_TITLE_RECT = COUNTDOWN_TITLE_TEXT.get_rect(center=(width/2, height/2))
    screen.blit(COUNTDOWN_TITLE_TEXT, COUNTDOWN_TITLE_RECT)

    pygame.display.update()
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                screen.blit(bg, (0,0))
                counter -= 1
                text = str(counter) if counter > 0 else 'Good Luck!'
                COUNTDOWN_TEXT = get_title_font(100).render(text, True, "#EA4492")
                COUNTDOWN_RECT = COUNTDOWN_TEXT.get_rect(center=(width/2, height/2))
                screen.blit(COUNTDOWN_TEXT, COUNTDOWN_RECT)
                beep_sound.play()
                pygame.display.update()
            if e.type == pygame.QUIT: 
                run = False
                pygame.quit()
                sys.exit()
        if counter < 1:
            return
    clock.tick(60)

# Results function
def results():
    global response, answer, bg, user_text, correct, incorrect

    answer = answerKey[vidNum - 1]
    if user_text.lower() == answer.lower():
        response = True
        correct += 1
    else:
        response = False
        incorrect += 1
    
    while True:
        screen.blit(bg, (0,0))

        # Gets user mouse position
        RESULTS_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if CONTINUE_BUTTON.checkForInput(RESULTS_MOUSE_POS):
                    return

        # Initialize buttons
        CONTINUE_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/4) * 3.5, 700), 
                            text_input="CONTINUE", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        # Load buttons and updates if they are hovered over
        for button in [CONTINUE_BUTTON]:
            button.changeColor(RESULTS_MOUSE_POS)
            button.update(screen)

        # Generstes and displays results title text
        RESULT_TEXT = get_title_font(100).render(f'{response}!', True, "#EA4492")
        RESULT_RECT = RESULT_TEXT.get_rect(center=(width/2, 75))
        screen.blit(RESULT_TEXT, RESULT_RECT)

        if response:
            RESULT2_TEXT = get_font(50).render("Good job! Click the button to advance.", True, "#EA4492")
            RESULT2_RECT = RESULT2_TEXT.get_rect(center=(width/2, height/2))
            screen.blit(RESULT2_TEXT, RESULT2_RECT)
        else:
            RESULT3_TEXT = get_font(50).render("Better luck next time! Click the button to advance.", True, "#EA4492")
            RESULT3_RECT = RESULT3_TEXT.get_rect(center=(width/2, height/2))
            screen.blit(RESULT3_TEXT, RESULT3_RECT)

            # Displays the correct song name
            RESULT4_TEXT = get_font(50).render(f"Song name: {answerKey[vidNum - 1]}", True, "#EA4492")
            RESULT4_RECT = RESULT4_TEXT.get_rect(center=(width/2, height/2 + 200))
            screen.blit(RESULT4_TEXT, RESULT4_RECT)
        
        pygame.display.update()
        user_text = ''

# Leaderboard Function
def leaderboard():
    global correct, incorrect, bg

    while True:
        screen.blit(bg, (0,0))

        # Gets user mouse position
        LEAD_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if CONTINUE_BUTTON.checkForInput(LEAD_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if CONTINUE1_BUTTON.checkForInput(LEAD_MOUSE_POS):
                    return

        # Initialize buttons
        CONTINUE_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((width/4) * 3.5, 700), 
                            text_input="QUIT", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        # Initialize buttons
        CONTINUE1_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=((170, 700)), 
                            text_input="PLAY AGAIN", font=get_font(50), base_color="#FFFFFF", hovering_color="#041B2D")

        # Load buttons and updates if they are hovered over
        for button in [CONTINUE_BUTTON, CONTINUE1_BUTTON]:
            button.changeColor(LEAD_MOUSE_POS)
            button.update(screen)

        # Generates leaderboard title and displays it
        LEAD_TEXT = get_title_font(100).render("Thanks for playing!", True, "#EA4492")
        LEAD_RECT = LEAD_TEXT.get_rect(center=(width/2, 75))
        screen.blit(LEAD_TEXT, LEAD_RECT)

        # Generates correct answers label and displays it
        LEAD1_TEXT = get_font(100).render(f"Correct Guesses: {correct}", True, "#EA4492")
        LEAD1_RECT = LEAD1_TEXT.get_rect(center=(width/2, 300))
        screen.blit(LEAD1_TEXT, LEAD1_RECT)

        # Generates incorrect answers label and displays it
        LEAD2_TEXT = get_font(100).render(f"Incorrect Guesses: {incorrect}", True, "#EA4492")
        LEAD2_RECT = LEAD2_TEXT.get_rect(center=(width/2, 500))
        screen.blit(LEAD2_TEXT, LEAD2_RECT)

        pygame.display.update()

# Video display fuction
def displayVideo():
    global height, width, user_text, vidNum
    screen.blit(bg, (0,0))

    # Generates a random number to pull video from, ensures that numbers arent repeating
    vidNum = random.randint(1, 15) 
    video = Video(f"Assets\\Videos\\video{vidNum}.mp4") # Pulls a random video from "Videos" folder
    video.set_size((900, 550))
    list=[]
    if vidNum in list:
        vidNum = random.randint(1, 15)
    else:
        list.append(vidNum)

    base_font = pygame.font.Font(None, 32)

    # create rectangle
    input_rect = pygame.Rect(200, 675, 140, 32)
  
    # color_active stores color("#EA4492") which
    # gets active when input box is clicked by user
    color_active = "#EA4492"
  
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = "#808080"
    color = color_passive
  
    active = False

    while True:
        video.draw(screen, (width/2 - 450, height/2 - 275), force_draw=False)

        PROMPT_TEXT = get_title_font(50).render("Quick! Guess the Name of This Song!", True, "#EA4492")
        PROMPT_RECT = PROMPT_TEXT.get_rect(center=(width/2, 50))
        screen.blit(PROMPT_TEXT, PROMPT_RECT)

        if video.active == False:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    video.active = False
                    return
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
  
        if active:
            color = color_active
        else:
            color = color_passive
        
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)
  
        text_surface = base_font.render(user_text, True, (255, 255, 255))
      
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x, input_rect.y+5))
      
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, 1050)
      
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
                
        pygame.display.update()

# Play function
def play():
    pygame.display.set_caption("Play!")
    rules()
    for i in range(rounds):
        countdown()
        displayVideo()
        results()
    leaderboard()
    main_menu()

# Main Menu Function
def main_menu():
    global bgMusic
    pygame.display.set_caption("Main Menu")
    mixer.music.play()
    while True:
        func_isMute()
        screen.blit(bg, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_title_font(100).render("MUSIC GUESSR", True, "#EA4492")
        MENU_RECT = MENU_TEXT.get_rect(center=(width/2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play Rect.png"), pos=(width/2, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Assets/Options Rect.png"), pos=(width/2, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit Rect.png"), pos=(width/2, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#FFFFFF", hovering_color="#041B2D")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.stop()
                    play()
                    return
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.stop()
                    options()
                    return
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    return

        pygame.display.update()

# Calls the main menu function
main_menu()



