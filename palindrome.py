def palindromeNumber(z):
  sum = 0
  dum = z
  while dum > 0:
      rem = dum % 10
      sum = sum + rem*10
      dum = dum/10

  if sum == z:
      print(z, "is the palindrome number")
  else:
      print(z, "is not a palindrome number")


if __name__ == "__main__":
    palindromeNumber(121)