"""
                  #PSEUDOCODE
    Function called user_name
    generates username from user's email
"""

def main():
  email = input("Enter your email: ", prompt=name@gmail.com)
  username = user_name(email)
  print("Your username is " + username)

def user_name(n):
  return n.rstrip("@gmail.com")

if __name__ == "__main__:
  main()

                #Extra Challenge
"""
                  #PSEUDOCODE
# A function that takes one argument - a list of integers
# zeros the first and last elements

def main():
  value_input = [2, 5, 7, 8, 9]
  result = zeroed(value_input)
  print(result)

def zeroed(n):
  n[0] = 0
  n[len(n)-1] = 0
  return n

if __name__ == "__main__:
    main()
"""