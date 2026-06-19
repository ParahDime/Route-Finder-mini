# Route finder mini

A python based, algorithm focused program in determining distance, allowing user interaction in adding data.

## Features

Several different data models, stored in .txt files allows for the user to experiment with different amounts of data and connections. Each file contains different connections, ensuring each file is not simply an addition onto other files.

Several algorithms are used within the program, including: knapsack sort; recursive binary sort; heap sort and . Knapsack is used due to the small data amount, being almost instantaneous. Binary search tree is also used in order to handle the speed of accessing data, even if larger data maps are used, such as if the data is scaled. Dijkstra's algorithm is also used, a common algorithm for find the shortest path possible between 2 points in the data

Data is able to be manipulated by the user. In addition to being able to sort through the data, the user can reload the state to ensure data integrity after any changes make. In addition, the data can be sorted via the algorithm for a specific target. Data is persistent, ensuring that once the program closes, the data is carried over to the next session, including new data points added.

## Prerequisites
Python 3.0 (available via the python website)
A computer that can run python 3.0

## What i learned

I began to implement a more 'algorithm focused' approach to the software, including taking advantage of O notation.
In addition, looking at where breadth and depth first searches are best utilised in data management and data handling.