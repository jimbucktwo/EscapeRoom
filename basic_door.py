import door
import random

class BasicDoor(door.Door):
  """Basic door subclass that uses the interface of the door class."""
  
  def __init__(self):
    """Initializes the attributes."""
    self._state = random.randint(1,2)
    self._input = 0
    
  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a basic door, you can either pull it or push it to open."

  def menu_options(self):
    """Returns the menu options."""
    return "1. Push\n2. Pull\n"

  def get_menu_max(self):
    """Returns the menu max."""
    return 2

  def attempt(self, option):
    """Returns the option the user attempted in a string."""
    self._input = option
    if option == 1:
      return "You push the door."
    else:
      return "You pull the door."

  def is_unlocked(self):
    """Returns correct value depending on if the user unlocked the door."""
    if self._input == self._state:
      return True
    else:
      return False

  def clue(self):
    """Returns a string clue."""
    return "Try the other way."

  def success(self):
    """Returns a congratulatory message."""
    return "Congratulations, you opened the door."