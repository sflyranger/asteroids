# Asteroids  

Creating a small-scale version of the Asteroids game  

---

## First Commit  

For my first commit, I imported the necessary `pygame` package and created a `constants.py` file that houses some variables I will be using in the Asteroids game. I also initialized a screen variable that creates an empty black window that can be opened by calling the `main.py` file and closed by clicking on the top-right exit button.  

---

## Second Commit  

For my second commit, I included a few new `.py` files and some new logic and variables in the `main.py` file.  

### `circleshape.py`  
- Created a `CircleShape` parent class that generates an invisible circle based on the `x`, `y`, and `radius` inputs.  
- Added two methods that will be used by future subclasses of `CircleShape`.  

### `player.py`  
- Created a `Player` class that inherits from `CircleShape`.  
- Initialized a rotation variable for each instance, inheriting `x`, `y`, and `radius` from the parent class.  
- Added a method to generate the positional coordinates of a triangle, visually representing the player.  
- Overrode the `draw` method from `CircleShape` to draw the triangle using the triangle method and Pygame’s `draw.polygon` method.  

### `main.py` Changes  
- Implemented logic to create a `Player` object on the screen, using `x` and `y` variables.  
- Used the `draw` method to visually display the player on the screen.  
- Created a global `clock` variable and `delta time` variable to reduce CPU utilization.  

---

## Third Commit  

For my third commit, I added shooting functionality and asteroid spawning logic.  

### `shot.py`  
- Created a `Shot` class inheriting from `CircleShape` to represent the player's shots.  
- Added methods to draw and update the shot’s position.  

### `player.py`  
- Added shooting functionality to the `Player` class.  
- The player can now shoot by pressing the space bar, creating `Shot` instances that move in the direction the player is facing.  

### `main.py` Changes  
- Updated the main function to include groups for updatable, drawable, shots, and asteroids.  
- Added collision detection between the player, shots, and asteroids.  
- The game ends if the player collides with an asteroid.  
- Asteroids are destroyed when hit by a shot.  

### `asteroidfield.py`  
- Created an `AsteroidField` class to handle spawning new asteroids at random intervals and positions along the screen edges.  

### `asteroid.py`  
- Created an `Asteroid` class inheriting from `CircleShape` to represent asteroids.  
- Added methods to draw and update the asteroid’s position.  

### `constants.py`  
- Added constants for player shooting speed and cooldown.  
- Defined shot radius.  

### `circleshape.py`  
- Updated the `CircleShape` class to include a collision detection method to check for collisions between circle objects.  

---

## Final Commit  

For my final commit, I added the logic to split asteroids upon collision and updated the README with instructions on how to clone and run the game.  

### `asteroid.py`  
- Updated the `Asteroid` class to include a `split` method that creates smaller asteroids when a larger one is destroyed.  

### `main.py` Changes  
- Updated the collision detection logic to call the `split` method on asteroids when they are hit by a shot.  

### `README.md`  
- Added instructions on how to clone and run the game.  

---

## How to Clone and Run the Game:
1. Clone the repository:
    ```sh
    git clone https://github.com/sflyranger17/asteroids.git
    cd asteroids
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the game:
    ```sh
    python main.py
    ```

## Game Controls:
- Use the WASD keys to move the player.
- Press the SPACE bar to shoot.
