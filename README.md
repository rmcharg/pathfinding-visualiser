# Pathfinding Visualiser

## Description
Graph search algorithm visualiser built in Python using the Pygame and Tkinter libraries. Users can select an algorithm and watch it find the shortest distance between two points (selected by user) on the grid. The grid can be customised by the user drawing barriers on the grid, or they can choose for a random distribution of barriers to be generated on the grid.

## Demo

### Breadth First Search
Breadth first search (BFS) is an algorithm for searching a tree or graph data structure for a target node. The algorithm starts at a particular  node (or the root node for a tree) and visits all of the adjacent nodes before exploring nodes at the next level out. In an unweighted graph this algorithm guarantees to find the shortest path.

### Depth First Search
Depth first search (DFS) is an algorithm for searching a tree or graph data structure. The algorithm starts at a particular node (root node for a tree) and explores as far as possible along each branch before backtracking. This algorithm will find a path if it exists it does not guarantee the shortest path.



## Usage

### Requirements
* Python 3.10 with Tkinter installed
* Pygame

### Installation
To install visualiser follow the steps below:
1. **clone repo:** git clone https://github.com/rmcharg/pathfinding-visualiser.git

2. **Navigate to cloned directory:** cd pathfinding-visualiser
3. **Install** python package requirements using provided requirements.txt file
4. **Run:** python run.py or python3 run.py