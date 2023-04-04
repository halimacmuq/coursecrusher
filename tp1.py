#################################################
# tp1.py
# Game title: Course Crusher
# Your name: Halima Ahmed
# Your andrew id: halimaa
from cmu_112_graphics import *
import math
import random
import string
#################################################
#Game classes:
class Player: #the character the user will play through
    def __init__(self, app, playerName, playerGender, playerMajor, playerHair, playerOutfit):
        self.playerName = playerName
        self.playerGender = playerGender
        self.playerMajor = playerMajor
        self.playerHair = playerHair
        self.playerOutfit = playerOutfit
    #methods that a player object can perform:    
    def study(app):
        studyCap = 100
        if app.kPointsPerHour == 10:
            app.kPoints = min(app.kPoints + 10, studyCap)
        elif app.kPointsPerHour == 20:
            app.kPoints = min(app.kPoints + 20, studyCap)
        return app.kPoints
    
    def eat(app):
        healthCap = 100
        if app.healthPointsPerMeal == 10:
            app.healthPoints = min(app.healthPoints + 10, healthCap)
        elif app.healthPointsPerMeal == 20:
            app.healthPoints = min(app.healthPoints + 20, healthCap)
        elif app.healthPointsPerMeal == 25:
            app.healthPoints = min(app.healthPoints + 25, healthCap)
        return app.healthPoints
    
    def hit(app): #lets the player hit an NPC (monster or boss)
        pass
class Monster:
    def __init__(self, app, monsterRank, monsterHealth):
        self.monsterHealth = monsterHealth
        self.monsterRank = monsterRank
    
    def attack(app):
        pass #include actions here that reduces player's app.healthPoints
        #the amount of impact on app.healthPoints depends on monsterRank
    
class Boss(Monster):
    pass #similar to Monster class but has a high, fixed rank.

class Task:
    pass

class Assignment(Task):
    pass

class Project(Task):
    pass

class Food:
    def __init__(self, foodName, foodRank):
        self.foodName = foodName
        self.foodRank = foodRank
        
class EnergySource:
    def __init(self, energySourceName, energySourceRank):
        self.energySourceName = energySourceName
        self.energySourceRank = energySourceRank
#################################################
def drawWelcomeScreen(app, canvas, width, height):
    pass #this screen will greet the user
    #with the game title, logo, and a sentence
    #asking the user to press Enter to play

def drawCreateCharacterScreen1(app, canvas, width, height):
    pass #the first character creation screen asks user
    #to enter their name and select their gender (providing text fields)

def drawCreateCharacterScreen2(app, canvas, width, height):
    pass #the second character creation screen asks user
    #to pick their college major (CS/IS/BA/BIO) and
    #also pick their character's look (skin tone + outfit)
    #from 3 options

def drawPlayingEnvironment(app, canvas, width, height):
    pass #this function will draw the background
    #of the game, which includes the interior
    #that includes some of the furniture pieces the
    #player can interact with

def drawSubmitTaskScreen(app, canvas, width, height):
    pass #this screen appears whenever the user
    #mouse-clicks on their laptop to submit a task
    #(a project or an assignment). It will contain the
    #pending assignment, and on the side shows the total
    #assignments for the day.

def drawDailyResultBoard(app, canvas, width, height):
    pass #after the day is up (clock strikes 12AM),
    #the screen enters the daily result state and the
    #total earnings of gold points + courage points
    #are displayed for the user

def drawHungerAlert(app, canvas, width, height):
    pass #this screen appears after the health bar
    #falls under 30. It will alert the user to go eat
    #something from their inventory to refill their health bar.

def drawLowEnergyAlert(app, canvas, width, height):
    pass #similar to hungerAlert, this will notify the
    #user about their energy dropping below 40.

def foodInventory(app, canvas, width, height):
    pass #food screen appears whenever the user mouse-clicks
    #on the fridge

def energyInventory(app, canvas, width, height):
    pass #energy screen appears whenever the user mouse-clicks
    #on the drinks machine.

def drawMonsterAlert(app, canvas, width, height):
    pass #screen appears after energy hits 30 and below to
    #warn that monsters will begin to appear and attack if in proximity.

def drawBossFightScreen(app, canvas, width, height):
    pass #this will be dedicated to level 4, with different background
    #interior/environment loaded.

def drawPlayerScoreboard(app, canvas, width, height):
    pass #after the user completes the game successfully,
    #their final score will be listed alongside those of other
    #players, ranking them all from 1 to 5.

#1. in appStarted function we define the model (data needed for the animation):
def appStarted(app):
    app.lives = []
    app.lives.append(app.loadImage('assets\heart.png'))
    app.lives.append(app.loadImage('assets\heart.png'))
    app.lives.append(app.loadImage('assets\heart.png'))
    app.livesX = app.width//30
    app.livesY = app.height//35
    app.activePlayer = app.loadImage('assets\player_R.png')
    app.playerCx = app.width//2
    #app.playerCy to be done later since as it requires 2 more visual assets
    app.gameState = 'playing' #for now set as playing for testing purposes
    app.newPlayer = Player(app, 'Halima', 'F', 'Computer Science', 'Dark Brown', 'Sport Outfit')
    app.kPoints = 10
    app.kPointsPerHour = 10
    app.healthPoints = 10
    app.healthPointsPerMeal = 10
    app.monsterModeOn = False
    app.bossActive = False
    
#2. Countroller 1: Mouse click event
def mousePressed(app, event):
    pass #this will mostly include mouse clicks
    #on buttons on character creation screen, alert screens, and interacting with environment in
    #the playing state

#2. Countroller 2: Keyboard events for arrows keys, screens, and selecting color:
def keyPressed(app, event):
    if event.key == 'Enter' and app.gameState == 'welcome':
        app.gameState = 'createCharacter1'
    if event.key == 'Right':
        app.activePlayer = app.loadImage('assets\player_R.png')
        if app.playerCx+10 < app.width:
            app.playerCx += 10
        else:
            app.playerCx = app.playerCx
    if event.key == 'Left':
        app.activePlayer = app.loadImage('assets\player_L.png')
        if app.playerCx-10 > 0:
            app.playerCx -= 10
        else:
            app.playerCx = app.playerCx
            
#2. Controller 3: Time function for counting down (integer)
def timerFired(app):
    pass
    #this will include the day-time cycle
    #where each in-game hour is 30 seconds in real life
    #and a full day (6AM - 12AM) would be
    # 9 minutes in real life. After the day finishes,
    # A new day (level) begins.
            
#3. View function (redrawAll):
def redrawAll(app, canvas):
    if app.gameState == 'playing':
        drawPlayingEnvironment(app, canvas, app.width, app.height)
        canvas.create_image(app.livesX, app.livesY, image=ImageTk.PhotoImage(app.lives[0]))
        canvas.create_image(app.livesX+45, app.livesY, image=ImageTk.PhotoImage(app.lives[1]))
        canvas.create_image(app.livesX+90, app.livesY, image=ImageTk.PhotoImage(app.lives[2]))
        canvas.create_rectangle(app.width-40, app.height-90, app.width-10, app.height-10, fill='#c78640')
        canvas.create_rectangle(app.width-40, app.height-110, app.width-10, app.height-10, outline='black', width=3)
        canvas.create_rectangle(app.width-80, app.height-90, app.width-50, app.height-10, fill='#40c758')
        canvas.create_rectangle(app.width-80, app.height-110, app.width-50, app.height-10, outline='black', width=3)
        canvas.create_rectangle(app.width-120, app.height-90, app.width-90, app.height-10, fill='#e8c92c')
        canvas.create_rectangle(app.width-120, app.height-110, app.width-90, app.height-10, outline='black', width=3)
        canvas.create_image(app.playerCx, app.height//2, image=ImageTk.PhotoImage(app.activePlayer))
    if app.gameState == 'welcome':
        drawWelcomeScreen(app, canvas, app.width, app.height)
    if app.gameState == 'createCharacter1':
        drawCreateCharacterScreen1(app, canvas, app.width, app.height)
    if app.gameState == 'createCharacter2':
        drawCreateCharacterScreen2(app, canvas, app.width, app.height)
    if app.gameState == 'submitTask':
        drawSubmitTaskScreen(app, canvas, app.width, app.height)
    if app.gameState == 'dailyResult':
        drawDailyResultBoard(app, canvas, app.width, app.height)
    if app.gameState == 'hungerAlert':
        drawHungerAlert(app, canvas, app.width, app.height)
    if app.gameState == 'lowEnergyAlert':
        drawLowEnergyAlert(app, canvas, app.width, app.height)
    if app.gameState == 'foodInventory':
        foodInventory(app, canvas, app.width, app.height)
    if app.gameState == 'energyInventory':
        energyInventory(app, canvas, app.width, app.height)
    if app.gameState == 'monsterAlert':
        drawMonsterAlert(app, canvas, app.width, app.height)
    if app.gameState == 'bossFightScreen':
        drawBossFightScreen(app, canvas, app.width, app.height)
    if app.gameState == 'playerScoreboard':
        drawPlayerScoreboard(app, canvas, app.width, app.height)
        
runApp(width=800, height=800)