"""
                  #PSEUDOCODE
    Function called biggest_odd
    takes a string of numbers as argument
    returns the biggest odd number in the list
"""

def main():
  value = input("Enter a string of integer numbers: ")
  print(biggest_odd(value))

def biggest_odd(n):
  list_num = list[map(str, n)]
  for num in range(num=0, len(list_num)):
    for check in range(num = num+1, len(list_num)):
      if num % 2 != 0:
        try:
          num > check
          max_odd = num
        except (num < check, num == check):
          max_odd = check
      else:
        continue
  return max_odd

if __name__ == "__main__":
  main()


                              #Extra Challenge
"""
                  #PSEUDOCODE
#Function called zeros_last
#takess an argument - a list of input from the user
#if the list contains zeros, it moves them to the end of the list
# whilee maintaining th eorder of the other elements 
#else, if there are no zeros, it returns a sorted list in ascendig order

def main():
  list_num = list(map(str, input("Enter the values of the list separated by white spaces: \n""Press Enter to terminate input process\n").split()))
  print(zeros_last(list_num))

def zeros_last(n):
  result = []
  for num in range(num=0, len(n)):
    if num == 0:
      n.insert(len(n)-1, num)
      n.remove(num)
    else:
      continue
  result = n
  return result

if __name__ == "__main__":
  main()
"""