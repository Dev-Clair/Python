"""
                  #PSEUDOCODE
    Function called my_discount
    Asks for USERINPUTS - price and discount
    Calculates and returns price after discount
"""

def main():
  print(my_discount())

def my_discount():
  price = float(input("Please Enter Price for Item: "))
  discount = float(input("Please Enter Discount for Item: ")/100)

  return (price - price*discount)

if __name__ = "__main__":
  main()

                #Extra Challenge
"""
                  #PSEUDOCODE
# A function that takes one argument - a list of strings
# returns a formatted list of tuple

def main():
  students = ['Male', 'Female', 'Female', 'Male', 'Male', 'Male','Female', 'Mle', 'Female', 'Male', 'Female', 'Male', 'Female']
  result = tuple_of_sex(students)
  print(result)

def tuple_of_sex(n):
  j = 0
  k = 0
  for student in range(i=0, len(n)):
    if student == 'Male':
      list1 = ('Male', j+=1)
      #list1 = ('Male', n.count(i))
    elif student == 'Female':
      list1 = ('Female', k+=1)
      #list2 = ('Female', n.count(i))
  return [list1, list2]

 if __name__ == "__main__":
  main()
"""