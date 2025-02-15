# asteroids
Creating a small scale version of the asteroids game

# First Commit
For my first commit I imported the neccessary pygame package and created a constants.py file that houses some variables I will be using in the asteroids game. 
I also initialized a screen variable that creates an empty black window that can be opened by calling the main.py file and closed by clicking on the top right exit button.
-------------------
# Second commit
For my second commit I included a few new .py files and some new logic and variables in the main.py file.

## circleshape.py 
For this file I created a CircleShape parent class that creates an invisible circle based on the x,y,radius inputs. I then created two methods that will be used by my future sub-classes of the CircleShape class.

## player.py
This file houses the logic for the Player class that inherits from the CircleShape class.
It initializes a rotation variable on every instance of the class and inherits the x,y and radius from the parent class. From there I created a new method that creates the positional coordinates for a triangle that is the visual representation of the player.
I also wrote over the draw method in the CircleShape class to draw out triangle using the triangle method and pygames .draw.polygon method.

# main.py changes
In my main function I implemented logic to create a player object on the screen by creating both an x and y variable to be used in a future player object. After creating the player object I used the draw method to visually draw the player on the screen.
I also created a global clock variable and delta time variable. Both of these are updated after each iteration of the loop to lower the mount of CPU utilization on my system.
