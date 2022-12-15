"""
                  #PSEUDOCODE
    Function called only_float
    takes two arguments - a and b
    returns 2 if both arguments are floats
    returns 1 if only one argument is a float
    returns 0 if none of the arguments are floats
"""

def main():
  a = input("Enter the first number: ")
  b = input("Enter the second number: ")
  result = only_float(a, b)
  print(result)

def only_float(n, m):
  if isinstance(n, float) and isinstance(m, float):
    return 2
  elif isinstance(n, float) or isinstance(m, float):
    return 1
  else:
    return 0

if __name__ = "__main__":
  main()

                #Extra Challenge
"""
                  #PSEUDOCODE
# A function that takes one argument - a list of strings
# returns the index of the longest word

def main():
  furnitures = ['Mattress', 'Pillows', 'Sheets', 'Cooker', 'Chairs', 'Otto-stools', 'Curtains', 'Pots', 'Television', 'Play-station']
  result = word_index(furnitures)
  print("The longest word has the index: " + result)

def word_index(n):
  for element_one in range(element_one=0, len(n)):
    for element_two in range(element_one=element_one+1, len(n)):
      if len(element_one) > len(element_two):
        result = len.index(element_one)
      elif len(element_one) < length(element_two):
        result = len.index(element_two)
      elif len(element_one) == len(element_two):
        result = len.index(element_one)
       # result = max(n, len(element_one))
  return result

 # return max(enumerate(n), key=lambda x: len(x[1]))[0]

if __name__ = "__main__":
  main()
"""