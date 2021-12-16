# CSE 432 
# Artificial intelligence lab
# Raihan Munim <181400138>

# 8 Puzzle using BFS

# Where 0 denotes the blank tile or space.
goal_state = [5, 7, 4, 3, 0, 1, 6, 2, 8]
# goal_state = [1, 4, 6, 2, 0, 7, 3, 5, 8]
starting_state = [3, 5, 4, 7, 1, 0, 6, 2, 8]

### Code begins.
import sys

def display_board( state ):
	print("*************")
	print("| %i | %i | %i |" % (state[0], state[3], state[6]))
	print("*************")
	print("| %i | %i | %i |" % (state[1], state[4], state[7]))
	print("*************")
	print("| %i | %i | %i |" % (state[2], state[5], state[8]))
	print("*************")
	
def move_up( state ):
	# Moves the blank tile up on the board. Returns a new state as a list.
	new_state = state[:]
	index = new_state.index( 0 )  #this will return index of blank
	
	if index not in [0, 3, 6]:
		# Swap the values.
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None 
		return None

def move_down( state ):
	# Moves the blank tile down on the board. Returns a new state as a list.

	new_state = state[:]
	index = new_state.index( 0 )
	
	if index not in [2, 5, 8]:
		# Swap the values.
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None.
		return None

def move_left( state ):
	# Moves the blank tile left on the board. Returns a new state as a list.
	new_state = state[:]
	index = new_state.index( 0 )
	
	if index not in [0, 1, 2]:
		# Swap the values.
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move it, return None
		return None

def move_right( state ):
	# Moves the blank tile right on the board. Returns a new state as a list.
	# Performs an object copy. Python passes by reference.
	new_state = state[:]
	index = new_state.index( 0 )
	
	if index not in [6, 7, 8]:
		# Swap the values.
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		# Can't move, return None
		return None

def create_node( state, parent, operator, depth,cost):
	return Node( state, parent, operator, depth,cost)

def expand_node( node,open_nodes,close_nodes):
	# Returns a list of expanded nodes.
	expanded_nodes = []
	
	expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1,0) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1,0) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1,0) )
	expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1,0) )
	
	# Filter the list and remove the nodes that are impossible (move function returned None)
	expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
	open_state = []
	for o in open_nodes:
		open_state.append(o.state)

	close_state = []
	for c in close_nodes:
		close_state.append(c.state)	
	
	#Remove repeated nodes
	#Remove the nodes that are in open list
	expanded_nodes = [node for node in expanded_nodes if node.state not in open_state]
	#Remove the nodes that are in close list
	expanded_nodes = [node for node in expanded_nodes if node.state not in close_state]
	return expanded_nodes

def solution_path(node):
	moves = []
	states = []
	temp = node
	while True:
		moves.insert(0, temp.operator)
		states.insert(0,temp.state)
		if temp.depth <= 1: break
		temp = temp.parent
	states.insert(0,starting_state)
	return moves,states				

def bfs( start, goal ):
	# Performs a breadth first search from the start state to the goal
	# A list can act as a queue for the nodes.
	open_nodes = []
	close_nodes = []
	# Create the queue with the root node in it.
	open_nodes.append( create_node( start, None, None, 0 , 0) )
	while True:
		# We've run out of states, no solution.
		if len( open_nodes ) == 0: return None,None
		# take the node from the front of the queue
		node = open_nodes.pop(0)
		close_nodes.append(node)

		# Append the move we made to moves
		# if this node is the goal, return the moves it took to get here.
		if node.state == goal:
			return solution_path(node)

		# Expand the node and add all the expansions to end of the queue
		open_nodes.extend( expand_node( node, open_nodes,close_nodes) )

# Node data structure
class Node:
	def __init__( self, state, parent, operator, depth,cost):
		# Contains the state of the node
		self.state = state
		# Contains the node that generated this node
		self.parent = parent
		# Contains the operation that generated this node from the parent
		self.operator = operator
		# Contains the depth of this node (parent.depth +1)
		self.depth = depth
		# Contains the cost of this node
		self.cost = cost
		
# Main method
def main():
	# Calling bfs function with the starting and goal node
	result,states = bfs( starting_state, goal_state )
	if result == None:
		print("No solution found")
	elif result == [None]:
		print("Start node was the goal!")
	else:
		print (result)
		print (len(result), "moves")
		
		#To display board content
		for state in states:
			display_board(state)

# execute the main() function.
if __name__ == "__main__":
	main()

"""Data Structures
# The state of the board is stored in a list. The list stores values for the
# board in the following positions:
#
# *************
# | 3 | 7 | 6 |
# *************
# | 5 | 1 | 2 |
# *************
# | 4 | 0 | 8 |
# *************
#
# The goal is defined as:
#
# *************
# | 5 | 3 | 6 |
# *************
# | 7 | 0 | 2 |
# *************
# | 4 | 1 | 8 |
# *************
#
# Where 0 denotes the blank tile or space.
"""