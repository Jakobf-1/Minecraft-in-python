from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 1. Define the block class
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube', # Uses a built-in Ursina texture
            color=color.lime,
            collider='box',      # REQUIRED: Otherwise you fall through the floor
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

def update():
    # If the player falls below the floor (-10)
    if player.y < -10:
        player.position = (0, 20, 0)  # Teleport to safety

        # FIX: Reset velocity so you don't keep falling at 100mph
        if hasattr(player, 'velocity'):
            player.velocity = (0, 0, 0)

for z in range(10):
    for x in range(10):
        Voxel(position=(x, 0, z))

# 3. Add the player and push them UP so they don't get stuck in the floor
# Create player with higher sensitivity (default is 40)
player = FirstPersonController(mouse_sensitivity=Vec2(100, 100))
player.y = 2 # Keep them above the floor

app.run()
