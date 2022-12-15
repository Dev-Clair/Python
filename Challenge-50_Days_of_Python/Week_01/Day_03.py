"""
                  #PSEUDOCODE
    Function called register_check
    checks the number of students in a school
    takes a dictionary as argument
    if student is in school, say 'yes'
    else 'no'
    function should should return number of students in school
"""

def main():
  register = {"Michael":"yes", "John":"no", "Peter":"yes","Mary":"yes"}
  students = register_check(register)
  print(students)

def register_check(n):
  while True:
    name = input("Enter a name to check if student is in school: \n"
    "\tEnter 'q' to quit")
    try:
      name in n
       print("yes")
    except:
      name == 'q'
      break
    else:
      print("no")
      continue
  return count((n.values() == "yes"))

main()

                #Extra Challenge
"""
                  #PSEUDOCODE
# Given a list  of names made up of lower and upper letters
# write a code that returns a tuple of all the names in lowercase
# names returned should be sorted alphabetically in descending order

def main():
  name_list = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
  result = name_lower(name_list)
  print(result.sort())

def name_lower(n):
  for name in range(len(n)):
    if name == n.capitalize()
      n.remove(name)
  return tuple(n)

main()
"""