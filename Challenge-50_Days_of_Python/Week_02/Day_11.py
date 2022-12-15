"""
                  #PSEUDOCODE
    Function called equal_strings
    takes two arguments - strings
    compares if the have the same characters and equal length
    returns True is the above condition is satified else it should return False
"""

def main():
  str_1 = input("Enter a string or character sequence: ")
  str_2 = input("Enter another string or character sequence: ")

  result = equal_strings(str_1, str_2)
  print(result)

def equal_strings(n, m):
  # Try using List Comprehension
  for i in range(i=0, len(n)):
    for j in range(i=i+1, len(n)):
      if n == m and len(n) == len(m):
        return "True"
      else:
        return "False"

if name = "__main__":
  main()

                             #Extra Challenge
"""
                  #PSEUDOCODE
# A function called swap_values
# takes a list of numbers
# swaps the first element with the last 

def main():
  list_num = [2, 4, 67, 7]
  result = swap_values(list_num)
  print(result)

def swap_values(n):
  temp = n
  for value in range(len(temp)):
    temp[0] = n[len(n-1)]
    temp[len(n-1)] = n[0]
  n = temp
  return n

if name = "__main__":
  main()
"""