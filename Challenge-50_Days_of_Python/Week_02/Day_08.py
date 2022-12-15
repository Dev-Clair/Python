"""
                  #PSEUDOCODE
    Function called odd_even
    has one parameter and takes a list of numbers as argument
    returns difference between largest even number and smallest odd number
"""

def main():
  list_num = [13, 4, 5, 12, 7, 25, 16, 19]
  print(odd_even(list_num))

def odd_even(n):
  n_even = []
  n_odd = []
  for num in range(len(n)):
    if num % 2 == 0:
      n_even = n_even.append(num)
    else:
      n_odd = n_odd.append(num)
  result = max(n_even) - min(n_odd)
  return result

if __name__ = "__main__":
  main()

                              #Extra Challenge
"""
                  #PSEUDOCODE
# A function called prime_numbers
# that takes USERINPUT - an integer
# returns a list of prime numbers within it's range 

def main():
  num = int(input("Enter an integer: "))
  result = prime_numbers(num)
  print(result)

def prime_numbers(n):
  m = []
  for num in range(n):
    if num // 1 == num and num // num == 1:
      m.append(num)
  return m

if __name__ = "__main__":
  main()
"""