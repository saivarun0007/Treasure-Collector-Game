import pgzrun
import pygame  
from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
time_left = 30  
fox = Actor("fox")  
fox.pos = 100, 100
coin = Actor("coin") 
coin.pos = 200, 200
def draw():
    """Draw the game screen."""
    global game_over
    screen.fill((124, 252, 10))
    if not game_over:
        fox.draw()
        coin.draw()
        screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))     
        screen.draw.text(f"Time Left: {int(time_left):02d}s", color="black", topright=(WIDTH - 10, 10))
    else:
        screen.fill("pink")
        screen.draw.text(f"Final Score: {score}", color="black", topleft=(10, 10), fontsize=60)
def place_coin():
    """Place the coin at a random position."""
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)
def time_up():
    """End the game when the timer reaches zero."""
    global game_over
    game_over = True
def update():
    """Update game state based on input and collisions."""
    global score, time_left
    if not game_over:
        if keyboard.left:
            fox.x -= 4
        if keyboard.right:
            fox.x += 4
        if keyboard.up:
            fox.y -= 4
        if keyboard.down:
            fox.y += 4
        fox.x = max(0, min(WIDTH, fox.x))
        fox.y = max(0, min(HEIGHT, fox.y))
        if fox.colliderect(coin):
            score += 10
            place_coin()
        time_left -= 1 / 60 
        if time_left <= 0: 
            time_up()
place_coin()
pgzrun.go()

# There are lots of ways to modify this game. We could try changing the "FOX" to different character like "HEDGEHOG, LION, TIGER, ..." and 
# we could make the game last longer.
# =====================================
# ===> clock.schedule(time_up.15.0)
# ===> hedegehog = Actor("hedgehog")
# ===>  if keyboard.left:
#            fox.x -= 4
#        if keyboard.right:
#            fox.x += 4
#        if keyboard.up:
#            fox.y -= 4
#        if keyboard.down:
#            fox.y += 4
# =====================================