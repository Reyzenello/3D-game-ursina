from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Setting up the window title and icon
window.title = 'Ursina 3D Platformer Demo'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Sky
sky = Sky()

# Ambient lighting for better aesthetics
AmbientLight(color=color.rgba(100, 100, 100, 0.1))

# Directional light for shadows and depth
DirectionalLight(y=2, z=3, rotation=(45, -45, 45))

# Player class
class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5
        self.jump_height = 2
        self.gravity = 1
        self.mouse_sensitivity = Vec2(40, 40)

# Level creation
def create_platform(position=(0,0,0), scale=(1,1,1), color=color.white):
    return Entity(
        model='cube',
        color=color,
        texture='white_cube',
        collider='box',
        position=position,
        scale=scale
    )

# Creating platforms
ground = create_platform(scale=(10, 1, 10), color=color.green)
platforms = [
    create_platform(position=(3,1,2), scale=(3,0.5,3), color=color.yellow),
    create_platform(position=(-4,2,3), scale=(2,0.5,2), color=color.orange),
    create_platform(position=(0,3,5), scale=(4,0.5,2), color=color.red),
    create_platform(position=(5,4,7), scale=(2,0.5,2), color=color.violet),
    create_platform(position=(0,5,10), scale=(6,0.5,2), color=color.blue),
]

# Goal
goal = Entity(
    model='sphere',
    color=color.gold,
    scale=(1,1,1),
    position=(0,6,12),
    collider='sphere'
)

# Goal rotation animation
def update():
    goal.rotation_y += time.dt * 100
    goal.rotation_x += time.dt * 50
    
    # Win condition
    if distance(player.position, goal.position) < 1.5:
        win_text = Text(text='You Win!', origin=(0, 0), scale=3, color=color.yellow)
        invoke(Func(destroy, win_text), delay=3)
        player.position = (0, 2, 0)  # Reset player position

# Player instance
player = Player(position=(0,2,0))

# UI Elements
def create_ui():
    title = Text(text='Ursina 3D Platformer Demo', origin=(0, 0), scale=2, y=0.45)
    instructions = Text(text='WASD to move, Space to jump, Esc to exit', origin=(0, 0), scale=1.5, y=0.4)
    return [title, instructions]

ui_elements = create_ui()

# Run the game
app.run()
