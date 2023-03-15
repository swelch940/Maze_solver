import time
from queue import PriorityQueue

maze = [] #Intializing maze.

input_file = input("Enter maze file: ")
input_start = input("Enter the location of the start of the maze: ")
input_end = input ("Enter the location of the end of the maze: ")

input_start =  eval(input_start)

#Check to see if a user inputs the actual coordinates.
if input_end != "None":
    input_end = eval(input_end)

#Populating maze as 2d array from text file given.
with open(input_file, "r") as file:
    for row in file:
        maze.append(row.strip().split())

#Calculates the exit if a user enters None
if input_end == "None":
    for i in maze[len(maze)-1]:
        if i == "-":
            input_end = (len(maze)-1, maze[len(maze)-1].index(i))


#Function that returns a list of all the possible legal moves at a certain point in the maze.
def legalMoves(points, maze):
    nextPoints = []
    if points[1] + 1 < len(maze[points[0]]) and maze[points[0] + 1][points[1]] != "#":
        nextPoints.append((points[0] + 1, points[1]))
    if points[1] + 1 < len(maze[points[0]]) and maze[points[0]][points[1] + 1] != "#":
        nextPoints.append((points[0], points[1] + 1))
    if points[0] - 1 >= 0 and maze[points[0] - 1][points[1]] != "#":
        nextPoints.append((points[0] - 1, points[1]))
    if points[1] - 1 >= 0 and maze[points[0]][points[1] - 1] != "#":
        nextPoints.append((points[0], points[1] - 1))
    
    return nextPoints


#Heuristic function to calculate the manhattan distance for a point. 
#Using the manhattan distance as the heuristic in this algorithm.
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1- x2) + abs(y1 -y2) #Returns manhattan distance for a given point on the graph. 


#A* search to find the most opitmal path through the maze.
def aStar(maze, start, goal):
    start_time = time.time() #Start time of the algorithms
    gN = {} #dictionary of the G(n) values for the points
    fN ={}  #dictionary of the F(n) values for the points
    visited = set() #Set of visited points.

    """
    Loops through all the points in the maze and sets all their G(n)
    and F(n) values to infinity.
    """
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            gN[(i,j)] = float('infinity')

    gN[start]= 0 #Sets the starting point's G(n) to 0.
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            fN[(i,j)] = float('infinity')
    
    fN[start] = heuristic(start, goal) # Calculates F(n) for the starting point.

    queue = PriorityQueue() #Intialize priority queue.
    queue.put((heuristic(start,goal), heuristic(start,goal), start)) #Adds start to queue.
    path = {} #Dictonary to backtrack for the path.
    
    
    while queue:
        currentPoint = queue.get()[2]
        if currentPoint == goal:
            print(str(currentPoint) + " is the exit!")
            print("Number of visted nodes: " +str(len(visited)))
            end_time = time.time()
            total_time = end_time- start_time
            print("Execution time: " + str(total_time))
            fwdPath = {}
            cell = goal
            while cell != start:
                
                fwdPath[path[cell]] = cell
                cell = path[cell]
             
            path_through = list(fwdPath)
            path_through.append(goal)
            
            #path_through.reverse()
            #print(path_through)
   
            print("Total number of steps in path: " + str(len(path_through)))
            return
        
        nextPoints = legalMoves(currentPoint, maze) #Lst of possible moves from the current point.
        
        #Loops through the list of the nextpoints
        #Calculates the G(n) and (Fn) of all the next points
        # Selects the next points to search based on if the F(n) has decreased. 
        for i in nextPoints:
            tempGN = gN[currentPoint] + 1
            tempFN = tempGN + heuristic(i, goal)

            if tempFN < fN[i]:
                gN[i] = tempGN
                fN[i] = tempFN
                queue.put((tempFN, heuristic(i, goal), i))
                path[i] = currentPoint
                visited.add(i)
    
    
aStar(maze, input_start, input_end)