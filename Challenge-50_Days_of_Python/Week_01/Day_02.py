"""
                  #PSEUDOCODE
    in the main function declare a variable
    assign a list of strings to the variable
    call a function that takes a list as argument
    function converts string to integers and sums the list
    returns value back to caller
"""

def main():
  list_string = ['4','8','12','16','20','24','28']
  print(convert_add(list_string))

def convert_add(n):
  n = list[map(int, n)]
  result = 0

  for i in range(len(n)):
    result = result + i
  return result

  """
  n = list[map(int, n)]
  for i in range(len(n)):
    result = sum(i)
  return result
  """

if __name__ = "__main__":
  main()

                #Extra Challenge
"""
                  #PSEUDOCODE
# in the main function declare a variable
# call a function that takes a string as argument
# function should check if there are duplicates
# returns duplicate if any
# else function should return "No Duplicates"

def main():
  list_string = ["Rotimi", "Emeka", "Leye", "Tupac", "Samuel", "Sunday", "Joshua", "Emmanuel", "Andrew", "Destiny", "Agogo", "Samuel"]
  result = check_duplicates(list_string)
  print("The duplicate string is" + result)

def check_duplicate(n):
  for i in range(i=0, len(n)):
    for j in range(i=i+1, len(n)):
      if i == j:
        return i
      else:
        return "No Duplicates"
        
  if __name__ = "__main__":
    main()
"""