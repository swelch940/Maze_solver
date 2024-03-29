# Maze Solver

### Github: https://github.com/swelch940/Maze_solver 


## Table of Contents

### 1. [About](#about)
### 2. [Requirments](#requirements)
### 3. [How to run](#Howtorun)
### 4. [Output](#output)
### 5. [Editing to get path](#EditingPath)



## About  <a name="about"></a>

In this project we look to be able to solve a given maze by returning a path through the maze. We have implemented two different search algorithms which both will search through each potiental position of the maze until the path through the maze is found. The first algorithm implemented is a Depth-first search which will contiously consider each potiential position in the maze until a path through the maze is found. However, this algorithm does not gurantee it will find the most optimal path through the maze. It will just return the first path through the maze it finds. The second algorithm implemented is A* search. This is similar, however a huestric function is implemented making the algorithm more efficient and gurantees to return the most optimal path through the maze.

## Requirements  <a name="requirements"></a>

The only requirement to run either of the algorithms is that you have Python installed, preferrable Python3.10 or later. 

If you have your own mazes you would like to test with either of these algorithms, you will need to make sure they are in a .txt file formatted the same way as the example mazes provided. You will also need to know the coordinates for the start of the maze and the exit of the maze. 

## How to run <a name="Howtorun"></a>

In order to run the code, make sure you have navigated to the directory of both the .py files and the Mazes folder in your terminal. 

Once in the correct directory you can run the following command in your terminal :

```console
python3 maze-solver.py
```
If done correctly, you should see the following response prompt in your terminal :

```console
Enter maze file:
```
If you have left the Mazes folder in the same directory as given in the repository you can use the following path to enter a maze:

```console
Mazes/maze-Small.txt
```

If done correctly, you should be prompted to enter the starting coordinates of the maze:

```console
Enter the location of the start of the maze: 
```
It is important that you given this coordinates as a tuple. (x,y) where x is the row position and y is the column. Also note that because we're using arrays the rows and columns start at 0. 

The start coordinates for all the mazes provided is (0,1).

Example for the starting coordinates for maze-Small.txt is given below 

```console
(0,1)
```
You will then be prompted for the exit coordinates of the maze:

```console
Enter the location of the exit of the maze:
```
For the exit coordinates, you can either provide the xits coordinates liek you did for start or you can write "None" and the program will calculate the exit for you. Note, if you wirte "None" the program will take longer to run as it will need to calculate the exit coordinates. 

Example for the exit coordinates for maze-Small.txt is given below.

```console
(9,18)
```

or 

```console
None
```


If all done correctly, the algorithm will run and you should see an output similar to the one below:

```console
(9, 18) is the exit!
Excecution time: 27.20883560180664
Total nodes visited: 80
Total number of steps in path: 27
```

To run the aStar search instead of the depth-first search is the same process except just run the maze-aStart file instead:

```console
python3 maze-aStar.py
```

The remaining process is excatly the same.


## Output <a name="output"></a>

The output of both algorithms will provide you with 4 different things. The first is confirmation that your exit coordinates are the exit. The second is the execution time of the algorithm. Thirdly, the total number of nodes that were visited to find the path, and lastly, the total number of steps in the path to the exit. 


## Editing the files to get the path. <a name="EditingPath"></a>

You can edit the code to print out each of the coordinates in the path by uncommenting the print statements in the code. The code to produce the coordinates for each point along the path to the exit is already in the code, however, since this was a university project it is currently commented out due to my professor not wanting it. Just make sure lines 58 and 59 are uncommented in the maze-solver.py file and in maze-aStar make sure lines 96 and 97 are uncommented and the program will then also output the coordinates for every point in the path.
