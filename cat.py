import pyglet
from pyglet.window import Window

xs = 200
ys = 100
window = Window(style=Window.WINDOW_STYLE_OVERLAY)
window.set_caption("Overlay Window")
window.set_size(xs, ys)

# Load the animation
ani = pyglet.resource.animation('catt.gif')
sprite = pyglet.sprite.Sprite(img=ani)

# Adjust the sprite size to match the window
sprite.scale_x = xs / sprite.width
sprite.scale_y = ys / sprite.height

# Define the window movement speed
move_speed = 10

def update(dt):
    global window
    x, y = window.get_location()
    print(window.get_location())
    window.set_location(1200, 200)
    if x > 0:
        window.set_location(x - move_speed, y)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.clock.schedule_interval(update, 0.05) 

pyglet.app.run()
