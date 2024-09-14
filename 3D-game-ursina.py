from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Texture for blocks
block_texture = load_texture('textures/grass_block.png')

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=block_texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=load_texture('textures/skybox.png'),
            scale=150,
            double_sided=True
        )

class Ground(Entity):
    def __init__(self):
        super().__init__(
            model='plane',
            texture=block_texture,
            scale=100,
            color=color.green,
            position=(0,-0.5,0)
        )

# Create the ground
ground = Ground()

# Create player controller
player = FirstPersonController()

# Create some initial blocks
for z in range(10):
    for x in range(10):
        voxel = Voxel(position=(x,0,z))

# Add a skybox
sky = Sky()

app.run()
