## COMP1730/6730 Project assignment

# Your ANU ID: u7568823
# Your NAME: Fan Yue
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]

## You should implement the functions with pass as body.
## You can define new function(s) if it helps you decompose the problem
## into smaller subproblems.

import random
import matplotlib.pyplot as plt
import numpy as np
import random
from math import cos, sin, pi
import array as arr
# Task 1

def create_array():
    """ returns created array """
    zeroArray= [1,0,0,0,0,0,0,0,0,1];
    
    return zeroArray;

# Task 2

def simulate_1d_diffusion(array):
    """ argument: current array
        returns updated array """
    lenArray=len(array)
    # new array to store the result after running
    newArray=[None for _ in range(lenArray)]
    for index in range(lenArray) :
        # the first one
        if(index==0):
            newArray[index]=getArrayMean( array[0:2])
            # the last one 
        elif(index==lenArray-1):
            newArray[index]=getArrayMean(array[lenArray-2:])
        else:
            newArray[index]=getArrayMean(array[index-1:index+2])
        
    return newArray
# get the average of an array
def getArrayMean(array):
    average=0;
    lenArray=len(array)
    for oneNumber in array:
        average+=oneNumber
    average/=lenArray
    average=round(average,3)
    return average;
 

#region testRegion


# oneA=create_array()
# newOneA=simulate_1d_diffusion(oneA);
# newNewOneA=simulate_1d_diffusion(newOneA);
# print(oneA)
# print(newOneA)
# print(newNewOneA)


# newOneAP=plt.plot(newOneA)
# newNewOneAP=plt.plot(newNewOneA)
# # plt.legend(handles=[oneAP,newOneAP,newNewOneAP],labels=['oneA','newOneA','newNewOneA'],loc='best')
# l0=plt.plot(oneA,label='oneA')
# l1=plt.plot(newOneA,label='newOneA')
# l2=plt.plot(newNewOneA,label='newNewOneA')
# plt.legend(loc=0)
# plt.show()
#endregion

# Task 3

def plot_temperatures(initial, new, new2):
    """parameters: initial=original array, new=after 1 iteration, new2=after 2 iterations"""
    
    l0=plt.plot(initial,label='initial')
    l1=plt.plot(new,label='new')
    l2=plt.plot(new2,label='new2')
    plt.legend(loc=0)
   
    plt.show()

# 1D diffusion exercise code:
def exercise_1D_diffusion():    
    initial_array = create_array()
    new_array1 = simulate_1d_diffusion(initial_array)
    new_array2 = simulate_1d_diffusion(new_array1)
    plot_temperatures(initial_array, new_array1, new_array2)

# exercise_1D_diffusion()
# Task 4

def create_grid(size=5):
    """ argument: grid division
    returns size x size 2D grid as list of list """
    result=[]
    for i in range(size):
        # the top and botttom row
        if i==0 or i==size-1:
            oneArray=[1]*size
            result.append(oneArray)
            # middle row
        else:
            oneArray=[0]*size
            oneArray[0]=1
            oneArray[size-1]=1
            result.append(oneArray)
    return result



# Task 5

def simulate_2d_diffusion(grid):
    """ argument: current 2D grid 
    returns updated grid after one iteration of simulation """

    lenArray=len(grid)
    # new array to store the result after running
    newArray=[[0]*lenArray for _ in range(lenArray)]

    for row in range(lenArray):
        for col in range(lenArray):
            dataArray=[grid[row][col] ] 
            rowPre= row-1
            rowPost=row+1
            colPre=col-1
            colPost= col+1

            # top
            if  rowPre>=0:
                dataArray.append(grid[rowPre][col]) 
            # right
            if  colPost<=lenArray-1:
                dataArray.append( grid[row][colPost])
            # bot
            if  rowPost<=lenArray-1:
                dataArray.append( grid[rowPost][col])
            # left
            if  colPre>=0:
                dataArray.append( grid[row][colPre])
            
            newArray[row][col]= getArrayMean(dataArray)


        
    return newArray
     
# region testGrid

# tempSize=6
# tempArray=create_grid(tempSize)  
# print(len(tempArray))
# lenArray=len(tempArray)
# newArray=[[0]*lenArray for _ in range(lenArray)]
# for i in range(tempSize):
#     print (newArray[i])

# print(len(tempArray))
# for i in range(tempSize):
#     print (tempArray[i])

#endregion


# 2D diffusion exercise code:
def multiple_iterations(grid, num_iterations):
    for _ in range(num_iterations):
        for row in grid:
            print(' '.join(f'{temp:.2f}' for temp in row))
        print()
        grid = simulate_2d_diffusion(grid)

def exercise_2D_diffusion():    
    multiple_iterations(create_grid(),5)

exercise_2D_diffusion()
# Task 6

def simulate_large_scale(num_iterations,size=10):
    """ arguments: num_iterations=number of iterations to perform,
                   size=dimension of 2D grid 
        No return value.
        Use NumPy for efficient large-scale simulation and visualization, correctly handling edges."""
    pass

# 2D diffusion (numpy implementation) exercise code:
def exercise_2D_diffusion_numpy():    
    simulate_large_scale(5)

# Task 7:
    
def create_graph():
    """Generates a graph with nodes having initial random temperatures stored in a separate list."""
    num_nodes = 10
    # Initialize node temperatures
    temperatures = [random.randint(20, 30) for _ in range(num_nodes)]
    # Adjacency list to store edges
    edges = [[] for _ in range(num_nodes)]
    # Manually adding edges
    connections = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (0, 9),
                   (1, 3), (2, 4), (5, 7), (6, 8), (0, 5)]
    for start, end in connections:
        edges[start].append(end)
        edges[end].append(start)
    return edges, temperatures

def visualize_graph(edges, temperatures):
    """Visualizes the graph with node labels showing temperatures."""
    plt.figure(figsize=(10, 10))  # Increase figure size for better visibility
    num_nodes = len(temperatures)
    # Position nodes in a circle
    positions = {i: (cos(2 * pi * i / num_nodes), sin(2 * pi * i / num_nodes)) for i in range(num_nodes)}
    # Draw edges
    for i, neighbors in enumerate(edges):
        for neighbor in neighbors:
            plt.plot([positions[i][0], positions[neighbor][0]], 
                     [positions[i][1], positions[neighbor][1]], 'gray')
    # Draw nodes larger and with clear labels
    for i, pos in positions.items():
        plt.scatter(*pos, color='lightblue', s=1000)  # Increased node size
        plt.text(pos[0], pos[1], f'{temperatures[i]:.1f}°C', color='black', ha='center', va='center', fontweight='bold', fontsize=10)
    plt.axis('off')
    plt.show()

def simulate_diffusion(edges, temperatures):
    """ arguments: edges=edge list defining graph, 
    temperatures=current temps of graph nodes
    returns updated temperatures list"""
    pass

# Graph diffusion exercise code:

def exercise_graph_diffusion():
    edges, temperatures = create_graph()
    print("Initial temperatures:", temperatures)
    visualize_graph(edges, temperatures)
    for _ in range(3):  # simulate multiple iterations
        temperatures = simulate_diffusion(edges, temperatures)
        visualize_graph(edges, temperatures)

    