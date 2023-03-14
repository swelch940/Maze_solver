import time

start_time = time.time() #Gets the start time of the algorithm

maze = [] #Intialising maze.

input_file = input("Enter maze file: ")
input_start = input("Enter the location of the start of the maze: ")
input_end = input ("Enter the location of the end of the maze: ")
print(input_end)

input_start =  eval(input_start)

if input_end != "None":
    input_end = eval(input_end)


#Popluating maze as a 2d array from the text file given.
with open(input_file, "r") as file:
    for row in file:
        maze.append(row.strip().split())

if input_end == "None":
    for i in maze[len(maze)-1]:
        if i == "-":
            input_end = (len(maze)-1, maze[len(maze)-1].index(i))


print(input_end)
#Depth-first search algorithm to calculate a path through a given matrix.
def dfs(maze, start, goal, stack, seen):
    seen = set() #Set of possible positions in the maze we have seen. 
    stack = [start] #A stack to keep track of the positions in the maze wee need to evaluate.
    parentMap = {} #Hash map to keep track of the path we take through the maze.
    

    #While loop that make sure we keep going until there are no more possible moves in the stack.
    while stack:
        print("\n")
        currentPoint = stack.pop() #Gets a position to evaluate.
        #print(currentPoint)
        #print("Looking at " + str(currentPoint))
        #print("Is " + str(currentPoint) + " the exit?")

        #If the current point we are at ion the maze is the exit, we are finished.
        if currentPoint == goal:
            print(str(currentPoint) + " is the exit!")
            end_time = time.time()
            total_time = end_time- start_time
            print("Excecution time: " + str(total_time))
            print("Total nodes visited: " + str(len(seen)))
            path = []
            while currentPoint != start:
                path.append(currentPoint)
                currentPoint = parentMap.get(currentPoint)
                
            #print("Path: " + str(path)) #Prints the path returned for the maze.
            print("Total number of steps in path: " + str(len(path)))
            return
        print("No!")
        

        #Gets the list of all the possible legal moves for the current point in the maze.
        nextPoints = legalMoves(currentPoint, maze)
        #print("Possible moves: " + str(nextPoints))
        
        #Goes through the list of all the possible moves and adds them to the list of seen and the stack.
        #Also adds them as the key to their parent node. Meaning the previous move to get to that 
        for i in nextPoints:
            if i in seen:
                #print(" Already seen " + str(i))
                continue
            seen.add(i)
            parentMap[i] = currentPoint
            #print("Visted nodes: " + str(seen))
            stack.append(i)
            #print("List of nodes to visit: " + str(stack))


#Function that returns a list of all the possible legal moves at a certain point in the maze.
def legalMoves(points, maze):
    nextPoints = []
    if points[0] - 1 >= 0 and maze[points[0] - 1][points[1]] != "#":
        nextPoints.append((points[0] - 1, points[1]))
    if points[1] + 1 < len(maze[points[0]]) and maze[points[0] + 1][points[1]] != "#":
        nextPoints.append((points[0] + 1, points[1]))
    if points[1] + 1 < len(maze[points[0]]) and maze[points[0]][points[1] + 1] != "#":
        nextPoints.append((points[0], points[1] + 1))
    if points[1] - 1 >= 0 and maze[points[0]][points[1] - 1] != "#":
        nextPoints.append((points[0], points[1] - 1))
    
    
    return nextPoints




stack = []
seen = set()
dfs(maze, input_start, input_end, stack, seen)


