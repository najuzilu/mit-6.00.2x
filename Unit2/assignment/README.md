## Problem Set #2 ## 

###Simulation Overview###
iRobot is a company (started by MIT alumni and faculty) that sells the Roomba vacuuming robot (watch one of the product videos to see these robots in action). Roomba robots move around the floor, cleaning the area they pass over.

In this problem set, you will code a simulation to compare how much time a group of Roomba-like robots will take to clean the floor of a room using two different strategies.

The following simplified model of a single robot moving in a square 5x5 room should give you some intuition about the system we are simulating.

The robot starts out at some random position in the room, and with a random direction of motion. The illustrations below show the robot's position (indicated by a black dot) as well as its direction (indicated by the direction of the red arrowhead).

###Simulation Details###
* Here are additional details about the simulation model. Read these carefully.

####Multiple robots####
* In general, there are N > 0 robots in the room, where N is given. For simplicity, assume that robots are points and can pass through each other or occupy the same point without interfering.

####The room####
* The room is rectangular with some integer width w and height h, which are given. Initially the entire floor is dirty. A robot cannot pass through the walls of the room. A robot may not move to a point outside the room.

####Tiles####
* You will need to keep track of which parts of the floor have been cleaned by the robot(s). We will divide the area of the room into 1x1 tiles (there will be w * h such tiles). When a robot's location is anywhere in a tile, we will consider the entire tile to be cleaned (as in the pictures above). By convention, we will refer to the tiles using ordered pairs of integers: (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).

####Robot motion rules####
* Each robot has a position inside the room. We'll represent the position using coordinates (x, y) which are floats satisfying 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances of the Position class to store these coordinates.
* A robot has a direction of motion. We'll represent the direction using an integer d satisfying 0 ≤ d < 360, which gives an angle in degrees.
* All robots move at the same speed s, a float, which is given and is constant throughout the simulation. Every time-step, a robot moves in its direction of motion by s units.
* If a robot detects that it will hit the wall within the time-step, that time step is instead spent picking a new direction at random. The robot will attempt to move in that direction on the next time step, until it reaches another wall.

####Termination####
The simulation ends when a specified fraction of the tiles in the room have been cleaned.

###Download and save###
* ps2.py, a skeleton of the solution.
ps2_visualize.py, code to help you visualize the robot's movement (an optional - but cool! - part of this problem set).
* ps2_verify_movement35.pyc, precompiled module for Python 3.5 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.5.
* ps2_verify_movement36.pyc, precompiled module for Python 3.6 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.6.
* ps2_verify_movement37.pyc, precompiled module for Python 3.7 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.7.

###Problem 1: RectangularRoom Class###
You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.

In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:

* RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
* Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a robot in a room.

Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.

####Problem 1####
In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and decide how the following operations are to be performed:

* Initializing the object
* Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
* Determining if a given tile has been cleaned
* Determining how many tiles there are in the room
* Determining how many cleaned tiles there are in the room
* Getting a random position in the room
* Determining if a given position is in the room
* Complete the RectangularRoom class by implementing its methods in ps2.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.

**Hint**: During debugging, you might want to use random.seed(0) so that your results are reproducible.

###Problem 2: Robot Class###
In ps2.py we provided you with the Robot class, which stores the position and direction of a robot. For this class, decide what fields you will use and decide how the following operations are to be performed:
* Initializing the object
* Accessing the robot's position
* Accessing the robot's direction
* Setting the robot's position
* Setting the robot's direction

Complete the Robot class by implementing its methods in ps2.py.

**Note**: When a Robot is initialized, it should clean the first tile it is initialized on. Generally the model these Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only a couple of lines of code.

**Note**: The Robot class is an abstract class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at this link and if you want more examples on abstract classes, follow this link.

In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method updatePositionAndClean().

###Problem 3: StandardRobot Class###
Each robot must also have some code that tells it how to move about a room, which will go in a method called updatePositionAndClean.

Ordinarily we would consider putting all the robot's methods in a single class. However, later in this problem set we'll consider robots with alternate movement strategies, to be implemented as different classes with the same interface. These classes will have a different implementation of updatePositionAndClean but are for the most part the same as the original robots. Therefore, we'd like to use inheritance to reduce the amount of duplicated code.

We have already refactored the robot code for you into two classes: the Robot class you completed in Problem 2 (which contains general robot code), and a StandardRobot class that inherits from it (which contains its own movement strategy).

Complete the updatePositionAndClean method of StandardRobot to simulate the motion of the robot after a single time-step (as described on the Simulation Overview page).

###Problem 4: Running the Simulation###
In this problem you will write code that runs a complete robot simulation.

Recall that in each trial, the objective is to determine how many time-steps are on average needed before a specified fraction of the room has been cleaned. Implement the following function:
```python
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    """
```

The first six parameters should be self-explanatory. For the time being, you should pass in StandardRobot for the robot_type parameter, like so:  
`avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)`  
Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) whenever you wish to instantiate a robot. (This will allow us to easily adapt the simulation to run with different robot implementations, which you'll encounter in Problem 6.)

###Problem 5: RandomWalkRobot Class###
iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after every time step, rather than just when they run into walls. You have been asked to design a simulation to determine what effect, if any, this change has on room cleaning times.

Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement strategy. RandomWalkRobot should have the same interface as StandardRobot.

Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to make sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing RandomWalkRobot instead of StandardRobot.

Enter your code for classes Robot and RandomWalkRobot below.

###Problem 6: Data Plotting###
Now, you'll use your simulation to answer some questions about the robots' performance.

In order to do this problem, you will be using a Python tool called PyLab. 

Below is an example of a plot. This plot does not use the same axes that your plots will use; it merely serves as an example of the types of images that the PyLab package produces.

Note to those who did the optional visualization: For problem 6, we make calls to runSimulation() to get simulation data and plot it. However, you don't want the visualization getting in the way. If you chose to do the visualization exercise, before you get started on problem 6 (and before you submit your code in submission boxes), make sure to comment the visualization code out of runSimulation(). There should be 3 lines to comment out. If you do not comment these lines, your code will take a REALLY long time to run!!

For the questions below, call the given function with the proper arguments to generate a plot using PyLab.

####Problem 6-1####
Examine showPlot1 in ps2.py, which takes in the parameters title, x_label, and y_label. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot1 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

1. Which of the following would be the best title for the graph?  
**Answer**:  Time it takes 1-10 robots to clean 80% of a room
2. Which of the following would be the best x-axis label for the graph?  
**Answer**: Number of robots
3. Which of the following would be the best y-axis label for the graph?  
**Answer**: Time-steps

####Problem 6-2####
Examine showPlot2 in ps2.py, which takes in the parameters title, x_label, and y_label. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot2 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

1. Which of the following would be the best title for the graph?  
**Answer**: Time it takes two robots to clean 80% of variously **shaped** rooms

Examine showPlot2 in ps2.py, which takes in the same parameters as showPlot1. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot2 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.

2. Which of the following would be the best x-axis label for the graph?  
**Answer**: aspect ratio
3. Which of the following would be the best y-axis label for the graph?  
**Answer**: time-steps