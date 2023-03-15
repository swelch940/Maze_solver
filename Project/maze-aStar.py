import time
from queue import PriorityQueue
start_time = time.time()


maze = [] #Intializing maze.

input_file = input("Enter maze file: ")
input_start = input("Enter the location of the start of the maze: ")
input_end = input ("Enter the location of the end of the maze: ")

input_start =  eval(input_start)


if input_end != "None":
    input_end = eval(input_end)

#Populating maze as 2d array from text file given.
with open(input_file, "r") as file:
    for row in file:
        maze.append(row.strip().split())

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
    g_node = {}
    f_node ={}
    visited = set()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            g_node[(i,j)] = float('infinity')
    g_node[start]= 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            f_node[(i,j)] = float('infinity')
    f_node[start] = heuristic(start, goal)

    queue = PriorityQueue()
    queue.put((heuristic(start,goal), heuristic(start,goal), start))
    path = {}
    while queue:
        currentPoint = queue.get()[2]
        if currentPoint == goal:
            print(str(currentPoint) + " is the exit!")
            print("Number of visted nodes: " +str(len(visited)))
            end_time = time.time()
            total_time = end_time- start_time
            print("Excecution time: " + str(total_time))
            fwdPath = {}
            cell = goal
            while cell != start:
                
                fwdPath[path[cell]] = cell
                cell = path[cell]
            
            #path_through = [i for i in fwdPath]  #
            #path_through.reverse()
            #path_through.append(goal)
            #print(path_through)
   
            print("Total number of steps in path: " + str(len(fwdPath)))
            return
        
        nextPoints = legalMoves(currentPoint, maze)
        for i in nextPoints:
            temp_g_node = g_node[currentPoint] + 1
            temp_f_node = temp_g_node + heuristic(i, goal)

            if temp_f_node < f_node[i]:
                g_node[i] = temp_g_node
                f_node[i] = temp_f_node
                queue.put((temp_f_node, heuristic(i, goal), i))
                path[i] = currentPoint
                visited.add(i)
    
    

aStar(maze, input_start, input_end)