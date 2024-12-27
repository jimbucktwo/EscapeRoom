import door
import random

class DeadboltDoor(door.Door):
  """Deadbolt door subclass that uses the interface of the door class."""

  def __init__(self):
    """Initializes the attributes. 1 is locked and 2 is unlocked."""
    self._bolt1 = random.randint(1,2)
    self._bolt2 = random.randint(1,2)
    
  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked."

  def menu_options(self):
    """Returns the menu options."""
    return "1. Toggle bolt 1\n2. Toggle bolt 2\n"

  def get_menu_max(self):
    """Returns the menu max."""
    return 2

  def attempt(self, option):
    """Returns the option the user attempted in a string."""
    if option == 1:
      if self._bolt1 == 1:
        self._bolt1 = 2
      else:
        self._bolt1 = 1
      return "You toggle the first bolt."
    elif option == 2:
      if self._bolt2 == 1:
        self._bolt2 = 2
      else:
        self._bolt2 = 1
      return "You toggle the second bolt."

  def is_unlocked(self):
    """Returns correct value depending on if the user unlocked the door."""
    if self._bolt1 == 2 and self._bolt2 == 2:
      return True
    else:
      return False

  def clue(self):
    """Returns a string clue."""
    if self._bolt1 == self._bolt2:
      return "You jiggle the door... it seems like it's completely locked"
    else:
      return "You jiggle the door... it seems like one of the bolts is unlocked."
    
  def success(self):
    """Returns a congratulatory message."""
    return "You unlocked both the deadbolts and opened the door."