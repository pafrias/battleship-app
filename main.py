from random import randint
from time import sleep

print "Welcome to Battleship! One player version"
sleep(1)
print "Place your ship and try and take out the enemy before you are destroyed!!!"
sleep(1)

player_board = []
player2_board = [] # or enemy
player_ships = [] #test[[3, 3],[2, 4]]
player2_ships = [] # enemy
ship_num = 2

def one_player(grid_size): # wipe board and place enemy ship
  grid = grid_size - 1
  for i in range(grid_size):
    player_board.append(["O"] * grid_size)
    player2_board.append(["O"] * grid_size)
  placement(grid)
  print player2_ships
  display(player2_board, player_board, grid_size)
  print "FIRE AT WILL"
  turn = 0
  while len(player_ships) > 0 and len(player2_ships) > 0:
    turn += 1
    fire(grid_size, grid,turn)
#test line    print player2_ships
  cont()
    
def placement(x):
  while len(player2_ships) < ship_num:
    col = randint(0, x)
    row = randint(0, x)
    if [row, col] not in player2_ships:
      player2_ships.append([row, col])
      player2_board[row][col] = "E" # can be removed
  print "Place your ships!"
  sleep(1)
  display(player2_board, player_board, 5)
  while len(player_ships) < ship_num:
    row = raw_input("Which row? (must be a letter from A - " + chr(65 + x) + ") ")
    row = (ord(row.upper()) - 65)
    col = raw_input("Which column? (must be a number from 1 - " + str(x + 1) + ") ")
    col = int(col) - 1
    if [row, col] not in player_ships:
      player_ships.append([row, col])
      player_board[row][col] = "B" #only for 1 player version
#def comp_placement:  
def fire(x,y,z):
  print "Turn #" + str(z)
  display(player2_board,player_board,x)
  row = raw_input("Target row (must be a letter from A - " + chr(65 + y) + ") ")
  row = (ord(row.upper()) - 65)
  col = raw_input("Which column (must be a number from 1 - " + str(x) + ") ")
  col = int(col) - 1
  sleep(2)
  if [row, col] in player2_ships:
    print "DIRECT HIT!!!"  
    player2_ships.pop(player2_ships.index([row,col]))
    player2_board[row][col] = "X"
  else:
    print "NEGATIVE IMPACT!"
    player2_board[row][col] = "0"
  sleep(2)
  print "RETURNING FIRE!"
  sleep(1)
  col = randint(0, y)
  row = randint(0, y)
  if [row, col] in player_ships:
    print "YOU'VE BEEN HIT!!!"
    player_ships.pop(player_ships.index([row,col]))
    player_board[row][col] = "X" # can be removed
  else:
    print "ENEMY MISS"
    player_board[row][col] = "0"
  sleep(1) #only for 1 player version  
#def return fire():
  
def cont():
  if len(player_ships) == len(player2_ships):
    print "The war has claimed both sides"
  elif len(player_ships) == 0:
    print "You have been destroyed"
  elif len(player2_ships) == 0:
    print "You have destroyed the enemy"
  sleep(2)
  cont = str(raw_input("Play Again? "))
  sleep(1)
  if cont == "yes" or cont == "y":
    one_player(5)
  elif cont == "no" or cont == "n":
    print "Until we meet again!"
  else:
    print "Clearly, the war has taken a heavy toll on you..."
  
def display(x,y,z):
  print
  print "   Enemy Waters"
  print "    1 2 3 4 5" # worry about other grid numbers later
  print "    ----------"
  for i in range(z):
    print chr(65 + i) + " |",
    print " ".join(x[i]),
    print
  print
  print "   Friendly Waters"
  print "    1 2 3 4 5"
  print "    ----------"  
  for i in range(z):
    print chr(65 + i) + " |",
    print " ".join(y[i]),
    print
    
one_player(5)
