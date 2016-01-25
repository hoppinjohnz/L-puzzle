import sys

'''  
#### The Puzzle

Given a nxn chessboard, where n is the power of 2 (e.g. 2, 4, 8, 16, 32, ...). One cell at position (x,y) is occupied. 
Figure out a way to fill the rest of the chessboard with L-shaped fragments (3 cells in shape of an L letter).

#### A General Backtrack Algorithm as a Recursive Function

def solve_puzzle(puzzle)
	Find all possible fill pieces around the filled areas.  If no such pieces exist, all done.
	For each possible piece,
		if solve_puzzle call with the current piece filled returns true
			return true
		else
			unfill the puzzle with the piece and try the next piece
	return false   # not really needed

Puzzle
---------
| 1 | 0 | 
---------
| 0 | 0 | 
---------

Solutions for 2x2:

A possible filling [(0, 1), (1, 0), (1, 1)]

---------
| 1 | 2 | 
---------
| 2 | 2 | 
---------

'''
def dbg(msg):   # Usage: 'python -O my_file.py' => debug on (logic reversed: with no debugging info by default
	if not __debug__ : print msg 

def nicePrint(puzzle, d=True):
	l = len(puzzle)
	for i in range(l):
		r = ''
		for j in range(l):
			r += '{0:3d}'.format(puzzle[i][j])
		if d: dbg(r)
		else: print r
	if d: dbg('--------------')
	else: print '--------------'

def _all_pieces(b):  # return the list of all l-shapes [x,y,z] that are based on the passed in list b of zero cells 
	return [ [x,y,z] for x in b for y in b for z in b if \
            (x[0]+1==y[0] and x[1]==y[1] and y[0]==z[0] and y[1]+1==z[1]) or \
            (x[0]==y[0] and x[1]+1==y[1] and y[0]+1==z[0] and y[1]==z[1]) or \
            (x[0]==y[0] and x[1]==y[1]+1 and y[0]+1==z[0] and y[1]==z[1]) or \
            (x[0]+1==y[0] and x[1]==y[1] and y[0]==z[0] and y[1]==z[1]+1) ]

def _pieces_at(pzl, i, j):
	l = len(pzl)
	b = [(x, y) for x in [i-1, i, i+1] for y in [j-1, j, j+1] if x>-1 and x<l and y>-1 and y<l and pzl[x][y] == 0]
	return _all_pieces(b)
	
def fill_piece(trueOrFalse, pzl, p, v):   # trueOrFalse: true to fill, ow unfill (go back to 0)
	for i in range(len(p)):
		x = p[i] 
		pzl[x[0]][x[1]] = (v if trueOrFalse else 0)

def find_pieces(pzl):
	r = range(len(pzl))
	zeros = [ (x,y) for x in r for y in r if pzl[x][y] == 0 ]
	return _all_pieces(zeros)
	
def all_done(p):
	for i in range(len(p)):
		if ( any( [v == 0 for v in p[i]] ) ):
			return False
	return True

def not_valid(pzl):
    # for each row, check each zero for possible nbr pieces: if no, 'pzl' is invalid
    l = len(pzl)
    for i in range(l):
        for j in range(l):
            if pzl[i][j] == 0:
    			t = _pieces_at(pzl, i, j)
    			if len(t) == 0:           # no valid nbr pieces found
     				dbg('({},{}) stuck'.format(i, j))
    				return True   
	return False 

def solver(pzl):
	global k
	if all_done(pzl): return True      # all done
	if not_valid(pzl): return False    # to backtrack
	fs = find_pieces(puzzle)           # all possible pieces (3 cell tuples)
	for p in fs:
		k += 1
		fill_piece(True, pzl, p, k)
		dbg( 'k = {}'.format(k))
		dbg('forward {}'.format(p))
#		nicePrint(pzl)
		if solver(pzl): return True
		k -= 1
		fill_piece(False, pzl, p, k)
		dbg( 'k = {}'.format(k))
		dbg( 'bckward {}'.format(p))
#		nicePrint(pzl)
	return False


# sample puzzles to be solved
#puzzle=[[1,0],
#		[0,0]]

#puzzle=[[1,0,0,0],
#		[0,0,0,0],
#		[0,0,0,0],
#		[0,0,0,0]]

puzzle=[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1]]

# print the initial puzzle
nicePrint(puzzle, False)

k = 1   # global filling index
solver(puzzle)
# print the solved puzzle
nicePrint(puzzle, False)

