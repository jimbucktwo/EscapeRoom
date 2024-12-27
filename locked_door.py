import door
import random

class LockedDoor(door.Door):
  """Locked door subclass that uses the interface of the door class."""
  
  def __init__(self):
    """Initializes the attributes."""
    self._key_location = random.randint(1,3)
    self._input = 0
    
  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a locked door, look around for the key."

  def menu_options(self):
    """Returns the menu options."""
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n"

  def get_menu_max(self):
    """Returns the menu max."""
    return 3

  def attempt(self, option):
    """Returns the option the user attempted in a string."""
    self._input = option
    if option == 1:
      return "You looked under the mat."
    elif option == 2:
      return "You looked under the flower pot."
    else:
      return "You looked under the fake rock."

  def is_unlocked(self):
    """Returns correct value depending on if the user unlocked the door."""
    if self._input == self._key_location:
      return True
    else:
      return False

  def clue(self):
    """Returns a string clue."""
    return "Look somewhere else."

  def success(self):
    """Returns a congratulatory message."""
    return "You found the key and opened the door."