# Imports
import pygame
import random

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
TITLE = "Creat Performance Task"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# colors
WHITE = (255, 255, 255)
GREY = (188, 62, 62)
# Fonts
FONT_SM = pygame.font.Font("assets/LibreBaskerville-Bold.ttf", 15)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/Gianna.ttf", 96)

# Images
startscreen = pygame.image.load('images/splashscreen.png').convert()
ship_img = pygame.image.load('newimages/player.png')
blood = pygame.image.load('images/burger2.png')
laser = pygame.image.load('newimages/laser.png')
enemy = pygame.image.load('newimages/enemy2.png')
bonus = pygame.image.load('newimages/enemy3.png')
enemy2 = pygame.image.load('newimages/enemy1.png')
bomb_img = pygame.image.load('newimages/enemy-laser.png')
bomb2_img = pygame.image.load('newimages/enemy-laser2.png')
bombx_img = pygame.image.load('images/enemy-laser.png')
background = pygame.image.load('images/forest.png')
end = pygame.image.load('images/forest2.png')
win = pygame.image.load('images/winscreen.png')

# stages
START = 0
PLAYING = 1
END = 2

# Sound Effects
pew = pygame.mixer.Sound("sounds/laser.ogg")
pew2 = pygame.mixer.Sound("sounds/laser.ogg")
EXPLOSION = pygame.mixer.Sound("sounds/ouch.ogg")
OOF = pygame.mixer.Sound("sounds/hit.ogg")
die = pygame.mixer.Sound("sounds/stink.ogg")


def setup():
    global ship, lasers, mobs, player, bombs, fleet, mobsx, bombsx, fleetx, stage, time_remaining, ticks
    
    ship = Ship(460, 830, ship_img, blood)
    lasers = []
    mob1 = Mob(20, 30, enemy2)
    mob2 = Mob(60, 30, enemy)
    mob3 = Mob(100, 30, enemy2)
    mob4 = Mob(140, 30, enemy)
    mob5 = Mob(180, 30, enemy2)
    mob6 = Mob(210, 30, enemy)
    mob7 = Mob(250, 30, enemy2)
    mob8 = Mob(290, 30, enemy)
    mob9 = Mob(330, 30, enemy2)
    mob10 = Mob(370, 30, enemy)
    mob11 = Mob(410, 30, enemy2)
    mob12 = Mob(450, 30, enemy)
    mob13 = Mob(490, 30, enemy2)
    mob14 = Mob(530, 30, enemy)
    mob15 = Mob(570, 30, enemy2)
    mob16 = Mob(610, 30, enemy)
    mob17 = Mob(20, 60, enemy2)
    mob18 = Mob(60, 60, enemy)
    mob19 = Mob(100, 60, enemy2)
    mob20 = Mob(140, 60, enemy)
    mob21 = Mob(180, 60, enemy2)
    mob22 = Mob(210, 60, enemy)
    mob23 = Mob(250, 60, enemy2)
    mob24 = Mob(290, 60, enemy)
    mob25 = Mob(330, 60, enemy2)
    mob26 = Mob(370, 60, enemy)
    mob27 = Mob(410, 60, enemy2)
    mob28 = Mob(450, 60, enemy)
    mob29 = Mob(490, 60, enemy2)
    mob30 = Mob(530, 60, enemy)
    mob31 = Mob(570, 60, enemy2)
    mob32 = Mob(610, 60, enemy)
    mob33 = Mob(20, 90, enemy2)
    mob34 = Mob(60, 90, enemy)
    mob35 = Mob(100, 90, enemy2)
    mob36 = Mob(140, 90, enemy)
    mob37 = Mob(180, 90, enemy2)
    mob38 = Mob(210, 90, enemy)
    mob39 = Mob(250, 90, enemy2)
    mob40 = Mob(290, 90, enemy)
    mob41 = Mob(330, 90, enemy2)
    mob42 = Mob(370, 90, enemy)
    mob43 = Mob(410, 90, enemy2)
    mob44 = Mob(450, 90, enemy)
    mob45 = Mob(490, 90, enemy2)
    mob46 = Mob(530, 90, enemy)
    mob47 = Mob(570, 90, enemy2)
    mob48 = Mob(610, 90, enemy)
    mob49 = Mob(20, 120, enemy2)
    mob50 = Mob(60, 120, enemy)
    mob51 = Mob(100, 120, enemy2)
    mob52 = Mob(140, 120, enemy)
    mob53 = Mob(180, 120, enemy2)
    mob54 = Mob(210, 120, enemy)
    mob55 = Mob(250, 120, enemy2)
    mob56 = Mob(290, 120, enemy)
    mob57 = Mob(330, 120, enemy2)
    mob58 = Mob(370, 120, enemy)
    mob59 = Mob(410, 120, enemy2)
    mob60 = Mob(450, 120, enemy)
    mob61 = Mob(490, 120, enemy2)
    mob62 = Mob(530, 120, enemy)
    mob63 = Mob(570, 120, enemy2)
    mob64 = Mob(610, 120, enemy)

    mobx1 = MobX(10, 150, bonus)
    mobx2 = MobX(70, 150, bonus)
    mobx3 = MobX(138, 150, bonus)
    mobx4 = MobX(198, 150, bonus)
    mobx5 = MobX(266, 150, bonus)
    mobx6 = MobX(326, 150, bonus)
    mobx7 = MobX(394, 150, bonus)


    # Make sprite groups
    player = pygame.sprite.Group()
    player.add(ship)
    player.score = 0
    player.shield = 5

    lasers = pygame.sprite.Group()

    mobs = pygame.sprite.Group()
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11,
             mob12, mob13, mob14, mob15, mob16, mob17, mob18, mob19, mob20, mob21,
             mob22, mob23, mob24, mob25, mob26, mob27, mob28, mob29, mob30, mob31,
             mob32, mob33, mob34, mob35, mob36, mob37, mob38, mob39, mob40, mob41,
             mob42, mob43, mob44, mob45, mob46, mob47, mob48, mob49, mob50, mob51,
             mob52, mob53, mob54, mob55, mob56, mob57, mob58, mob59, mob60, mob61,
             mob62, mob63, mob64)


    mobsx = pygame.sprite.Group()
    mobsx.add(mobx1, mobx2, mobx3, mobx4, mobx5, mobx6, mobx7)


    bombs = pygame.sprite.Group()
    bombsx = pygame.sprite.Group()

    fleet = Fleet(mobs)
    fleetx = FleetX(mobsx)

    # set stage
    stage = START
    time_remaining = 40
    ticks = 0

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image, blood):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.w = 32
        self.h = 32
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 10
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            
    def move_right(self):
        self.rect.x += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH - 0
            
    def shoot(self):
        las = Laser(laser)
        
        las.rect.centerx = self.rect.centerx
        las.rect.centery = self.rect.top
        
        lasers.add(las)
        pew.play()

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True)

        for hit in hit_list:
            OOF.play()
            self.image = blood
            self.shield -= 1
            player.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
            stage == END

  
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 8
        
    def update(self):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()

        
class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 4

    def drop_bomb(self):
        pew2.play()
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, players):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        
        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 1
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()


    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 4

    def drop_bomb(self):
        pew2.play()
        bomb = Bomb(bomb2_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, players):
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        
        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 1
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()



                

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 10
        

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 20
        self.speed = 3
        self.moving_right = True
    

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobs:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
            for m in mobs:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse:
            self.moving_right = not self.moving_right
            for m in mobs:
                #m.rect.y += 20
                pass


    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()




class MobX(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shield = 3

    def drop_bomb(self):
        pew2.play()
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
    
    def update(self, lasers, players):
        hit_list = pygame.sprite.spritecollide(self, lasers, True)
        
        if len(hit_list) > 0:
            EXPLOSION.play()
            player.score += 10
            self.kill()

        for hit in hit_list:
            OOF.play()
            self.shield -= 1

        if self.shield == 0:
            die.play()
            self.kill()
                
    
    
class FleetX:

    def __init__(self, mobsx):
        self.mobsx = mobsx
        self.bombx_rate = 20
        self.speed = 10
        self.moving_right = True
    

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobsx:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
            for m in mobsx:
                m.rect.x -= self.speed
                if m.rect.left <= 0:
                    reverse = True

        if reverse:
            self.moving_right = not self.moving_right
            for m in mobsx:
                m.rect.y += 20


    def choose_bomber(self):
        rand = random.randrange(0, self.bombx_rate)
        all_mobsx = mobsx.sprites()
        
        if len(all_mobsx) > 0 and rand == 0:
            return random.choice(all_mobsx)
        else:
            return None
    
    def update(self):
        self.move()

        bomberx = self.choose_bomber()
        if bomberx != None:
            bomberx.drop_bomb()



# Game helper functions
def show_title_screen():
    screen.blit(startscreen, (0, 0))
    title_text = FONT_XL.render("The Sun Vanished", 1, WHITE)
    extra_text = FONT_MD.render("Press SPACE to play", 1, WHITE)
    extra_text2 = FONT_SM.render("The sun has completely vanished! Everything is dark", 1, GREY)
    extra_text3 = FONT_SM.render("and cold, all electrical power has been shut down,", 1, GREY)
    extra_text4 = FONT_SM.render("and everyone seems to be losing it. There are entities", 1, GREY)
    extra_text5 = FONT_SM.render("in the sky that look like giant ships not from this world.", 1, GREY)
    extra_text6 = FONT_SM.render("The creatures coming out from these ships flash some sort ", 1, GREY)
    extra_text7 = FONT_SM.render("of red light from their mouth and eyes that seems to be ", 1, GREY)
    extra_text8 = FONT_SM.render("taking control of humans. There are other entities that flash", 1, GREY) 
    extra_text9 = FONT_SM.render("some sort of blue light that eats you from the inside when you", 1, GREY)
    extra_text10 = FONT_SM.render("look at it. As strong as they may seem these creatures still", 1, GREY)
    extra_text11 = FONT_SM.render("have their weaknesses…. Daylight. That’s why their ships create", 1, GREY)
    extra_text12 = FONT_SM.render("some sort of powerful smoke to completely cover the sun.", 1, GREY)
    extra_text13 = FONT_SM.render("You are amongst one of the last survivors left on Earth and it’s", 1, GREY)
    extra_text14 = FONT_SM.render("up to the remaining survivors to take the planet back and free the sun.", 1, GREY)
    extra_text15 = FONT_SM.render("Use the arrow keys to move left or right, tap the space key to shoot", 1, GREY) 
    extra_text16 = FONT_SM.render("sun rays at the entities. ", 1, GREY)
    screen.blit(title_text, [250, 220])
    screen.blit(extra_text, [400, 700])
    screen.blit(extra_text2, [290, 320])
    screen.blit(extra_text3, [300, 340])
    screen.blit(extra_text4, [290, 360])
    screen.blit(extra_text5, [290, 380])
    screen.blit(extra_text6, [280, 400])
    screen.blit(extra_text7, [290, 420])
    screen.blit(extra_text8, [280, 440])
    screen.blit(extra_text9, [275, 460])
    screen.blit(extra_text10, [280, 480])
    screen.blit(extra_text11, [270, 500])
    screen.blit(extra_text12, [275, 520])
    screen.blit(extra_text13, [280, 540])
    screen.blit(extra_text14, [255, 560])
    screen.blit(extra_text15, [270, 580])
    screen.blit(extra_text16, [400, 600])
    

def show_stats(player):
    score_text = FONT_MD.render("Score: " + str(player.score), 1, WHITE)
    screen.blit(score_text, [0, 0])

    shield_text = FONT_MD.render("Shield: " + str(player.shield), 1, WHITE)
    screen.blit(shield_text, [0, 20])

def show_end():
    if len(mobs) == 0:
          screen.blit(win, [0,0])
    if len(player) == 0: 
          screen.blit(end, [0,0])

# Global Variables
def start_music(stage):
     if stage == START:
          pygame.mixer.music.load("sounds/creepyintro.ogg")
          pygame.mixer.music.play(-1) 

     if stage == PLAYING:
          pygame.mixer.music.load("sounds/creepybackgroundmusic.ogg")
          pygame.mixer.music.play(-1)
          
     if stage == END:
          pygame.mixer.music.load("sounds/creepyintro.ogg")
          pygame.mixer.music.play(-1)

    
# Game loop
setup()
start_music(stage)
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    start_music(PLAYING)
                    
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    start_music(END)
                    setup()
                    

    if stage == PLAYING:            
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()

        

            
                        
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        player.update(bombs)
        lasers.update()
        bombs.update()
        mobs.update(lasers, player)
        fleet.update()
        mobsx.update(lasers, player)
        fleetx.update()


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(background, [0,0])
    lasers.draw(screen)
    bombs.draw(screen)
    bombsx.draw(screen)
    player.draw(screen)
    mobs.draw(screen)
    mobsx.draw(screen)
    show_stats(player)

    if stage == START:
        show_title_screen()


    elif stage == PLAYING:
        timer_text = FONT_MD.render(str(time_remaining), True, WHITE)
        screen.blit(timer_text, [490, 0])

        if time_remaining == 0:
            stage = END
            start_music(END)

        elif len(player) == 0:
            stage = END

        elif len(mobs) == 0:
            stage = END

    if stage == END:
        show_end()
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
