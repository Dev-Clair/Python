"""
                  #PSEUDOCODE
    Function called string_range
    takes a single number as argument
    returns a string of its range
"""

def main():
  number = input("Enter an Integer Value: ")
  print(string_range(number))

def string_range(n):
  for element in range(n):
   # result = print(i, end =" " + sep = ",")
    return str(element, sep = ",", end= " ")
  
if __name__ = "__main__":
  main()

                              #Extra Challenge
"""
                  #PSEUDOCODE
# A function that takes one argument - a list of names
# returns a dictionary of the names that start with S as keys 

def main():
  names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
  final_value = list_to_dict(names)
  print(final_value)

def list_to_dict(n):
  j=0
  m = {}
  for name in range(name = 0, len(n)):
    for check in range(name = name + 1, len(n)):
      if name[0] == "S" and name == check:
        m[name] = j+=1
      else:
        # n.remove(name)
        continue
  return m

if __name__ = "__main__":
  main()
"""