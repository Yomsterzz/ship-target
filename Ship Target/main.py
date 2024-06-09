import pgzrun
import random
import itertools

WIDTH = 400
HEIGHT = 400

block_positions = [(350, 50), (350, 350), (50, 350),  (50, 50)]
block_pos = itertools.cycle(block_positions)

ship = Actor("player", center=(WIDTH/2, HEIGHT/2))
block = Actor("block", center=(50,50))

def draw():
    screen.clear()
    ship.draw()
    block.draw()


def move_block():
    animate(block, "bounce_end", duration=1, pos=next(block_pos))

move_block()
clock.schedule_interval(move_block, 2)

def next_ship_target():
    x = random.randint(100,300)
    y = random.randint(100,300)
    ship.target = (x,y)
    target_angle = ship.angle_to(ship.target)
    target_angle += 360 * ((ship.angle - target_angle + 180) // 360)
    animate(ship, angle=target_angle, duration=0.3, on_finished=move_ship)

def move_ship():
    a = animate(ship, tween="accel_decel", pos=ship.target, duration=ship.distance_to(ship.target)/200, onfinished=next_ship_target)

def update():
    pass

next_ship_target()


pgzrun.go()