# 3D-game-ursina


This code creates a simple 3D platformer game using the Ursina Engine. 

**1. Importing Libraries:**

- `from ursina import *`: Imports everything from the Ursina engine.
- `from ursina.prefabs.first_person_controller import FirstPersonController`: Imports the first-person controller prefab.

**2. App Initialization:**

- `app = Ursina()`: Creates an instance of the Ursina app.

**3. Window Setup:**

- Sets the window title, disables borderless and fullscreen modes, hides the exit button, and enables the FPS counter.

**4. Scene Setup:**

- `sky = Sky()`: Creates a sky background.
- `AmbientLight(...)`: Adds ambient lighting to the scene.
- `DirectionalLight(...)`: Adds a directional light source to create shadows and depth.

**5. `Player` Class:**

```python
class Player(FirstPersonController):
    # ...
```

- Inherits from `FirstPersonController` to provide basic first-person movement controls.
- Sets the player's speed, jump height, gravity, and mouse sensitivity.

**6. `create_platform` Function:**

```python
def create_platform(position=(0,0,0), scale=(1,1,1), color=color.white):
    # ...
```

- A helper function to create platform entities.
- Takes position, scale, and color as arguments.
- Returns an `Entity` representing the platform, with a cube model, collider, and specified properties.

**7. Level Creation:**

- Creates a ground platform and a list of platforms at different positions, scales, and colors.

**8. Goal:**

- Creates a gold sphere as the goal entity.

**9. `update` Function:**

```python
def update():
    # ...
```

- This function is called every frame.
- Rotates the goal sphere.
- Implements the win condition: If the player is close enough to the goal, displays a "You Win!" message, resets the player's position, and then destroys the win message after 3 seconds.

**10. Player Instance:**

- Creates an instance of the `Player` class, placing the player at the starting position.

**11. UI Elements:**

```python
def create_ui():
    # ...
```

- Creates and returns UI elements (title and instructions as text).

**12. Running the Game:**

- `app.run()`: Starts the Ursina game loop.
