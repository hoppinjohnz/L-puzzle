
## Python Backtracking Solver for L-puzzles

### The L-Puzzle

Given an nxn chessboard, where n is the power of 2 (e.g. 2, 4, 8, 16, 32, ...). One cell at position (x,y) is occupied. 
Figure out a way to fill the rest of the chessboard with L-shaped fragments (3 cells in shape of an L letter).

### A General Backtrack Algorithm as a Recursive Function
```
  def solve_puzzle(puzzle)
  	Find all possible fill pieces around the filled areas.  If no such pieces exist, all done.
  	For each possible piece,
  		if solve_puzzle call with the current piece filled returns true
  			return true
  		else
  			unfill the puzzle with the piece and try the next piece
  	return false   # not really needed
```
### Example Puzzles and Solution Data Structure

Puzzle
```
  ---------
  | 1 | 0 | 
  ---------
  | 0 | 0 | 
  ---------
```

Basic data structure
```
A cell is
(i, j)
```

Solutions for 2x2:
```
A possible filling represented by a 3-tuple of cells as [(0, 1), (1, 0), (1, 1)]:
---------
| 1 | 2 | 
---------
| 2 | 2 | 
---------
```

### Sample Run
```
python l.puzzle.solver.py 

  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  1
--------------
  2  2  3  3  4  4  5  5
  6  2  7  3  8  4  9  5
  6  6  7  7  8  8  9  9
 10 10 11 11 12 12 13 13
 14 10 15 11 16 12 17 13
 14 14 15 15 16 16 17 17
 18 19 19 20 21 21 22 22
 18 18 19 20 20 21 22  1
--------------
```
