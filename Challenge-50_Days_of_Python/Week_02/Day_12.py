"""
                  #PSEUDOCODE
    Function called count_dots
    takes input from the user and returns number of dots in USERINPUT
"""

# def main():
#   print(count_dots())

def count_dots():
  while True:
    word = input("Give me a word with each letter separated by dots and I'll count the dots in each word\n"
    "\tEnter 'q' to quit")
    if word == 'q':
      break
    print(word.count('.'))

if __name__ = "__main__":
  main()
  
                             #Extra Challenge
"""
                  #PSEUDOCODE
#