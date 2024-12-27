import abc

class Door:
  """Door class that is an interface for other door subclasses."""
  
  @abc.abstractmethod
  def examine_door(self):
    """Abstract method for examine_door."""
    pass

  @abc.abstractmethod
  def menu_options(self):
    """Abstract method for menu_options."""
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    """Abstract method for get_menu_max."""
    pass

  @abc.abstractmethod
  def attempt(self, option):
    """Abstract method for attempt."""
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    """Abstract method for is_unlocked."""
    pass

  @abc.abstractmethod
  def clue(self):
    """Abstract method for clue."""
    pass

  @abc.abstractmethod
  def success(self):
    """Abstract method for success."""
    pass
    