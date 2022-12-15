              #Division and Square-root
def main():
  n = int(input("Enter a number: "))
  result = divide_or_square(n)
  print("The result is" + result)


def divide_or_square(n):
  """
    * takes an argument - an integer
    * performs specified operation and
    * returns output to the caller
  """
  if n%5 == 0:
    import math
    return math.sqrt(n)
  elif n%5 != 0:
    return n%5

    main()

                #Extra Challenge
"""
# takes a dictionary as an argument
# returns the longest value

def main():
  Automobile = {"truck":"hilux", "sedan":"mercedez", "suv":"hyundai", "trailer":"iveco"} 
  result = longest_value()
  print("The longest value is" + result)

def longest_value(n):
  # max_len = " "
  # for i in range(len(n)):
  #   if len(i) > len(max_len):
  #     max_len = i
  #     result = i
  #   return result

  result = max(n.value, key=len)
  return result

main()
"""