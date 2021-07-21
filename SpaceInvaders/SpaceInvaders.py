import pgzrun
player = Actor("topdownfighter.png")
player.x = 400
player.y = 600 - player.height*0.5
aliens = []
def add_alien():
    alien = Actor("alienshiptex")
    alien.x = 400
    alien.y = 150
    aliens.append(alien)
clock.schedule_interval(add_alien, 5)    
lasers = []
def fire_laser():
    laser = Rect((player.x,player.y), (2,5))
    lasers.append(laser)
def update(): 
    if keyboard.left and player.x > player.width*0.5:
        player.x -= 10
    if keyboard.right and player.x < 800 -player.width* 0.5:
        player.x = player.x +10
    if keyboard.space:  
        fire_laser()
    for laser in lasers:
        laser.y -= 10
def draw():
    screen.clear()
    player.draw()
    for laser in lasers:
         screen.draw.filled_rect(laser, (0,255,255))
    for alien in aliens:
         alien.draw()
pgzrun.go()





















































































































































































