import door
import random

class ComboDoor(door.Door):
  """Combo door subclass that uses the interface of the door class."""

  def __init__(self):
    """Initializes the attributes."""
    self._correct_value = random.randint(1,10)
    self._input = 0
    
  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    """Returns the menu options."""
    return "Enter # 1-10: "

  def get_menu_max(self):
    """Returns the menu max."""
    return 10

  def attempt(self, option):
    """Returns the option the user attempted in a string."""
    self._input = option
    return "You turn the dial to..." + str(option)

  def is_unlocked(self):
    """Returns correct value depending on if the user unlocked the door."""
    if self._input == self._correct_value:
      return True
    else:
      return False

  def clue(self):
    """Returns a string clue."""
    if self._input > self._correct_value:
      return "Try a lower value."
    else:
      return "Try a higher value."

  def success(self):
    """Returns a congratulatory message."""
    return "You found the correct value and opened the door."