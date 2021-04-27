from automaton import Automaton

word = "1111" # Number 15 in binary system.

automaton = Automaton()
result = automaton.process(word) 

if result == 0:
  print(f"The number {word} is divisible by 5")
else:
  print(f"The number {word} is not divisible by 5")
