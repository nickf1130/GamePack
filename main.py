### IMPORTS ###

import time
from time import sleep

import random
from random import randint

### RESPONSE VARIABLES ###

a_A = ["A", "a"]
a_B = ["B", "b"]
a_C = ["C", "c"]
a_D = ["D", "d"]
a_Y = ["Y", "y"]
a_N = ["No", "no", "N", "n"]

### REQUIRED ANSWERS ###

req = ("Answer with A, B, or C.")
req2 = ("Answer with Yes or no.")

### DEFINED GAME FUNCTIONS ###

### Rock, Paper, Scissors. (Normal Mode) ###

def rps_Normal():

  compScore = 0
  playScore = 0
  tieScore = 0

  while True:
    print("Choose: Rock, Paper or Scissors?")
    player = input(">>> ")
    moves = ["Rock", "Paper", "Scissors", "Quit", "quit"]
    computer = moves[randint(0, 2)]

    if player == "Rock" and computer == "Paper":
      print("You Lose!", computer, "covers", player)
      compScore += 1

    elif player == "Rock" and computer == "Scissors":
      print("You Win!", player, "destroys", computer)
      playScore += 1

    elif player == "Scissors" and computer == "Paper":
      print("You Win!", player, "slices", computer)
      playScore += 1

    elif player == "Scissors" and computer == "Rock":
      print("You Lose!", computer, "destroys", player)
      compScore += 1

    elif player == "Paper" and computer == "Rock":
      print("You Win!", player, "covers", computer)
      playScore += 1

    elif player == "Paper" and computer == "Scissors":
      print("You Lose!", computer, "slices", player)
      compScore += 1

    elif player == computer:
      print("It's a tie!")
      tieScore += 1

    elif player == "Quit":
      break

    else:
      print("Invalid Input. Try running this again.")
      rps_Normal()

    print("Computer's Score: ", compScore)
    print("Your score: ", playScore)
    print("Ties: ", tieScore)

  rps_NormalAgain()

### Rock, Paper, Scissors (Normal Mode Restart) ###

def rps_NormalAgain():

  print("Would you like to play again? (Y/N)")

  option = input(">>> ")
  
  if option in a_Y:
    rps_Normal()

  if option in a_N:
    rps()

  else:
    print("Invalid entry. Try again.")
    rps_NormalAgain()

### Rock, Paper, Scissors (2 Player Mode) ###

def rps_2Player():

  compScore = 0
  playScore = 0
  tieScore = 0

  while True:
    moves = ["Rock", "Paper", "Scissors"]

    player1 = input("Player 1 Choose: Rock, Paper, or Scissors? ")
    
    while player1 not in ["Rock", "Paper", "Scissors", "Quit"]:
      print("Error. Invalid input.")
      break

    player2 = input("Player 2 Chose: Rock, Paper, or Scissors? ")

    while player2 not in ["Rock", "Paper", "Scissors", "Quit"]:
      print("Error. Invalid input.")
      break


    if player1 == "Rock" and player2 == "Paper":
      print("Player 2 wins!", player2, "covers", player1)
      compScore += 1

    elif player1 == "Rock" and player2 == "Scissors":
      print("Player 1 wins!", player1, "destroys", player2)
      playScore += 1

    elif player1 == "Scissors" and player2 == "Paper":
      print("Player 1 wins!", player1, "slices", player2)
      playScore += 1

    elif player1 == "Scissors" and player2 == "Rock":
      print("Player 2 wins!", player2, "destroys", player1)
      compScore += 1

    elif player1 == "Paper" and player2 == "Rock":
      print("Player 1 wins!", player1, "covers", player2)
      playScore += 1

    elif player1 == "Paper" and player2 == "Scissors":
      print("Player 2 wins!", player2, "slices", player1)
      compScore += 1

    elif player1 == player2 in moves:
        print("It's a tie!")
        tieScore += 1

    elif player1 == "Quit":
      break

    elif player2 == "Quit":
      break

    else:
      print("Invalid Input. One or more inputs contains an error. Try running this again.")
      rps_2Player()
  

    print("Player 2's Score: ", compScore)
    print("Player 1's: ", playScore)
    print("Ties: ", tieScore)

  rps_2PlayerAgain()

### Rock, Paper, Scissors (2 Player Mode Restart) ###

def rps_2PlayerAgain():

  print("Would you like to play again? (Y/N)")

  option = input(">>> ")
  
  if option in a_Y:
    rps_Normal()

  if option in a_N:
    rps()

  else:
    print("Invalid entry. Try again.")
    rps_2PlayerAgain()

### Rock, Paper, Scissors (Impossible Mode) ###

def rps_Impossible():

  compScore = 0
  playScore = 0
  tieScore = 0

  while True:
    print("Choose: Rock, Paper or Scissors?")
    player = input(">>> ")
    moves = ["Rock", "Paper", "Scissors", "Quit"]

    if player == "Rock": 
      print("You lose! Paper covers", player)
      compScore += 1

    elif player == "Paper":
      print("You lose!", "Scissors slice", player)
      compScore += 1

    elif player == "Scissors":
      print("You lose! Rock destroys", player)
      compScore += 1

    elif player == "Quit":
      break

    else:
      print("Invalid Input. Try running this again.")
      rps_Impossible()

    print("Computer's Score: ", compScore)
    print("Your score: ", playScore)
    print("Ties: ",tieScore)

  rps_ImpossibleAgain()

### Rock, Paper, Scissors (Impossible Mode Restart) ###

def rps_ImpossibleAgain():

  print("Would you like to play again? (Y/N)")

  option = input(">>> ")
  
  if option in a_Y:
    rps_Impossible()

  if option in a_N:
    rps()

  else:
    print("Invalid entry. Try again.")
    rps_ImpossibleAgain()

### Rock, Paper, Scissors (Menu) ###

def rps():
  print("Select Mode: ")
  print("(A) Normal")
  print("(B) 2 Player")
  print("(C) Impossible")
  print("(D) Quit")

  option = input(">>> ")

  if option in a_A:
    rps_Normal()

  elif option in a_B:
    rps_2Player()

  elif option in a_C:
    rps_Impossible()

  elif option in a_D:
    print("Sending you back to the menu!")
    time.sleep(1)
    choices()

  else:
    print("Invalid entry. Try again.")
    rps()

def ttt():
  print("WIP")
  choices()

def speedType():
  print("WIP")
  choices()

### Game Choices (Quit) ###

def quit():
  print("See you next time!")
  exit()

### Game Choices (Menu) ###

def choices():
  print("(A) Rock, Paper, Scissors")
  print("(B) Tic Tac Toe")
  print("(C) Speed Typer")
  print("(D) Quit")

  option = input(">>> ")

  if option in a_A:
    rps()

  elif option in a_B:
    ttt()

  elif option in a_C:
    speedType()

  elif option in a_D:
    quit()

  else:
    print("Incorrect entry. Try again.")
    choices()

### INTRODUCTION ###

print("Welcome to my pack of games!")

time.sleep(1)

print("There are a few different games to play, so try one out!")

print("Here are your options:")
choices()