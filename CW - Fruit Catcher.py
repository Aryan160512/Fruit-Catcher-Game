import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = 'Fruit Catcher Game'

xcentre = WIDTH // 2
ycentre = HEIGHT // 2

finalLevel = 8
currentLevel = 1

speed = 10

gameOver = False
gameComplete = False

ITEMS = ['broccoli', 'cabbage', 'carrot', 'potato']
displayedItems = []

def createMessage(title, subheading):
    screen.draw.text(title, fontsize=50, center =(400, 300), color='white')
    screen.draw.text(subheading, fontsize=40, center=(400, 350), color='white')

def getExtraActors(numOfExtraActors):
    allItemsToCreate = ['apple']
    for i in range(numOfExtraActors):
        randomItem = random.choice(ITEMS)
        allItemsToCreate.append(ITEMS[randomItem])
    return allItemsToCreate

def createActors(actorsToBeCreated):
    newActors = []
    for everyItems in actorsToBeCreated:
        createNewActor = Actor(everyItems)
        newActors.append(createNewActor)
    return newActors

def makeActors(extraActors):
    actorsToCreate = getExtraActors(extraActors)
    newActors = createActors(actorsToCreate)

def update():
    global displayedItems, currentLevel

    if len(displayedItems) == 0:
        displayedItems = makeActors(currentLevel)



def draw():
    global displayedItems, currentLevel, gameOver, gameComplete
    screen.clear()
    screen.blit('background', (0, 0))

    if gameOver:
        createMessage('GAME OVER', 'Better Luck Next Time')

    elif gameComplete:
        createMessage('YOU WIN', 'Well Done for completing all the levels')

    else:
        for item in displayedItems:
            item.draw()


pgzrun.go()