"""
                  #PSEUDOCODE
    Function called hide_password
    takes no parameters
    takes input from the user and returns a hidden password - four inputs long
"""

def hide_password():
  # import maskpass
  # password = maskpass.askpass(mask="*", prompt="Enter password: ")
  import getpass
  password = getpass.getpass(prompt="Enter password not longer than 4 characters: ")
  if len(password) > 4:
    password = password[0:3]
  print(password + "\nYour password is 4 characters long")

if __name__ == "__main__":
  main()

                              #Extra Challenge
"""
                  #PSEUDOCODE
# A function called convert_numbers
# takes one argument - a list of numbers
# returns a formatted list of strings with a thousand separator 

def main():
  num = [1000000, 2356989, 2354672, 9878098]
  print(convert_numbers(num))

def convert_numbers(n):
  for element in range(len(n)):
    result = '{:,d}'.format(element)
  return result

if __name__ == "__main__":
  main()
"""