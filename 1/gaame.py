from pygame import *

init()

window = display.set_mode((700,500))
display.set_caption("Догонялки котов")
background = transform.scale(image.load("../2/pict1.png"), (700, 500))

x1 = 100
x2 = 300

y1 = 300
y2 = 300

spritel1 = transform.scale(image.load("1.png"), (50, 50))
spritel2 = transform.scale(image.load("ball.png"), (50, 50))
speed = 10


run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(background, (0,0))
    window.blit(spritel1, (x1, y1))
    window.blit(spritel2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    key_pressed = key.get_pressed()

    if key_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
    if key_pressed[K_RIGHT] and x1 < 600:
        x1 += speed
    if key_pressed[K_UP] and y1 > 0:
        y1 -= speed
    if key_pressed[K_DOWN] and y1 < 400:
        y1 += speed

    if key_pressed[K_a] and x2 > 0:
        x2 -= speed
    if key_pressed[K_d] and x2 < 600:
        x2 += speed
    if key_pressed[K_w] and y2 > 0:
        y2 -= speed
    if key_pressed[K_s] and y2 < 400:
        y2 += speed
    display.update()
    clock.tick(FPS)

