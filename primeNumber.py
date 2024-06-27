def primeNo(x):
     m = x/2
     if x==0 or x == 1:
         print({x} + "is not a prime No")

     else:
         for i in range(2, int(m)):
             if x % i == 0 :
                 print(x," is not a prime No")
                 break


     print(x," is prime No")

if __name__ == "__main__":
  primeNo(4)
