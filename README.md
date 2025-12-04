# Eulerian Path & Cycle Checker

This Python script allows you to check whether a given undirected graph (provided as an adjacency list) contains:

* an Eulerian Cycle

* an Eulerian Path

It uses depth-first search (DFS) to verify graph connectivity and checks vertex degrees to determine Eulerian properties.

# Features

* Accepts adjacency list input directly in Python dictionary format
* Safely parses user input using ast.literal_eval
* Checks if the graph is connected
* Determines if the graph has an Eulerian Cycle
* Determines if the graph has an Eulerian Path

# Definitions

* Eulerian Cycle: A cycle that uses every edge exactly once and returns to the starting node.
  * Condition:

    * Graph must be connected

    * All vertices have even degree

* Eulerian Path: A path that uses every edge exactly once but does not need to end where it started.
  * Condition:

    * Graph must be connected

    * Exactly 2 vertices have odd degree

# How It Works

The script:

* Parses the input adjacency list into a Python dictionary

* Checks connectivity using DFS

* Counts vertex degrees

Determines if the graph meets the conditions for:

* Eulerian Cycle

* Eulerian Path
