"""Group 8 Jimmy Tran, Tien Dieu 10/24/22

Escape room simulator, the goal of the game is to open three randomly assigned doors from the five different door types that all use the interface of door. The player is provided with clues until they manage to open every door.
"""

import check_input
import random
import basic_door
import code_door
import combo_door
import deadbolt_door
import locked_door

def open_door(door):
  """Open door function, loops until the door is unlocked. Displays the door description and the menu as well as take in user input. """
  print(f"\n{door.examine_door()}")
  valid = True
  while valid:
    user_selection = int(check_input.get_int_range(door.menu_options(), 1, door.get_menu_max()))
    print(door.attempt(user_selection))
    if door.is_unlocked():
      print(door.success())
      valid = False
    else:
      print(door.clue())

def main():
  """Main function, executes the game by looping three times for each door, and creating three different doors based on a random selection."""
  
  print("Welcome to the Escape Room.\nYou must unlocked 3 doors to escape...\n")
  for i in range(3):
    door_types = [basic_door.BasicDoor(), code_door.CodeDoor(), combo_door.ComboDoor(), deadbolt_door.DeadboltDoor(), locked_door.LockedDoor()]
    door_selection = random.randint(1,5)
    open_door(door_types[door_selection - 1])

  print("\nCongratulations! You escaped... this time.")

main()