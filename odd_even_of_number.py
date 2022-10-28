# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num_list = input("Enter a list of number: "))
num_dict = input("Enter a dict of count and list number: "))
# find odd even in array
# check if only int instance
for num in num_list:
   if isinstance(int, num):
      if (num % 2) == 0:
         print("WE ARE HERE in IF")
         print("{0} is Even".format(num))
      else:
         # for debug
         # this is for 4th one
         print("Only debug purpose")
         print("WE ARE HERE")
         print("{0} is Odd".format(num))
