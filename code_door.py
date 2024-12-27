import door
import random

class CodeDoor(door.Door):
  """Code door subclass that uses the interface of the door class."""

  def __init__(self):
    """Initializes the attributes."""
    self._correct_code = []
    for i in range(3):
      char = random.randint(1,2)
      if char == 1:
        self._correct_code.append("X")
      else:
        self._correct_code.append("O")
    self._input = ["X","X","X"]
    
  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a door with a coded keypad with three characters,  each key toggles a value with an ‘X’ or an ‘O’."

  def menu_options(self):
    """Returns the menu options."""
    return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3\n"

  def get_menu_max(self):
    """Returns the menu max."""
    return 3

  def attempt(self, option):
    """Returns the option the user attempted in a string."""
    if self._input[option - 1] == "X":
      self._input[option - 1] = "O"
      
    else:
      self._input[option - 1] = "X"
      
    return "You pressed Key " + str(option)
    
  def is_unlocked(self):
    """Returns correct value depending on if the user unlocked the door."""
    for i in range(3):
      if self._input[i] != self._correct_code[i]:
        return False
    return True
    
  def clue(self):
    """Returns a string clue for which characters are correct."""
    correct_clue = []
    for i in range(3):
      if self._input[i] == self._correct_code[i]:
        correct_clue.append(f"Key {i+1}")
    return "Correct keypad characters: " + ", ".join(correct_clue)

  def success(self):
    """Returns a congratulatory message."""
    return "You matched all keypad characters and opened the door."