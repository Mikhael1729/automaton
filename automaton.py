"""
A simple automaton machine that determines whether a given binary number is divisible 
by 5 or not.
"""
class Automaton:
  def __init__(self):
    self.states = [0, 1, 2, 3, 4]
    self.current = self.states[0]

  """
  Delta transition function.

  It determines the new state of the automaton given a certain letter for the accepted
  alphabet.
  """
  def react(self, binary_digit):
    adjacency = [
      [0, 2, 4, 0, 2],
      [1, 3, 0, 2, 3]
    ]

    self.current = adjacency[binary_digit][self.current]

  """
  Extended delta function.

  It gets the result of the automaton after processing a whole word.
  """
  def process(self, word):
    for letter in word:
      self.react(int(letter))

    return self.current

