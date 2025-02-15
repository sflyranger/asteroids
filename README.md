# asteroids
Creating a small scale version of the asteroids game
-----------------------
## First Commit:
For my first commit I imported the neccessary pygame package and created a constants.py file that houses some variables I will be using in the asteroids game. 
I also initialized a screen variable that creates an empty black window that can be opened by calling the main.py file and closed by clicking on the top right exit button.
-------------------
## Second commit:
For my second commit I included a few new .py files and some new logic and variables in the main.py file.

### circleshape.py 
For this file I created a CircleShape parent class that creates an invisible circle based on the x,y,radius inputs. I then created two methods that will be used by my future sub-classes of the CircleShape class.

### player.py
This file houses the logic for the Player class that inherits from the CircleShape class.
It initializes a rotation variable on every instance of the class and inherits the x,y and radius from the parent class. From there I created a new method that creates the positional coordinates for a triangle that is the visual representation of the player.
I also wrote over the draw method in the CircleShape class to draw out triangle using the triangle method and pygames .draw.polygon method.

### main.py changes
In my main function I implemented logic to create a player object on the screen by creating both an x and y variable to be used in a future player object. After creating the player object I used the draw method to visually draw the player on the screen.
I also created a global clock variable and delta time variable. Both of these are updated after each iteration of the loop to lower the mount of CPU utilization on my system.
-------------------
## Third Commit:
For my third commit, I added shooting functionality and asteroid spawning logic.

### shot.py
Created a Shot class inheriting from CircleShape to represent the player's shots. Added methods to draw and update the shot's position.

### player.py
Added shooting functionality to the Player class. The player can now shoot by pressing the space bar, creating Shot instances that move in the direction the player is facing.

### main.py changes
Updated the main function to include groups for updatable, drawable, shots, and asteroids. Added collision detection between the player, shots, and asteroids. The game ends if the player collides with an asteroid, and asteroids are destroyed if hit by a shot.

### asteroidfield.py
Created an AsteroidField class to handle spawning new asteroids at random intervals and positions along the screen edges.

### asteroid.py
Created an Asteroid class inheriting from CircleShape to represent asteroids. Added methods to draw and update the asteroid's position.

### constants.py
Added constants for player shooting speed and cooldown, as well as shot radius.

### circleshape.py
Updated the CircleShape class to include a collision detection method to check for collisions between circle objects.
-------------------
## Final Commit:
For my final commit, I added the logic to split asteroids upon collision and updated the README with instructions on how to clone and run the game.

### asteroid.py
Updated the Asteroid class to include a split method that creates smaller asteroids when a larger one is destroyed.

### main.py changes
Updated the collision detection logic to call the split method on asteroids when they are hit by a shot.

### README.md
Added instructions on how to clone and run the game.

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
