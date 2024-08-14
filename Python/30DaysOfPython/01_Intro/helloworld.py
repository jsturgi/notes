# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Strings
first = 'Jake'
last = 'Sturgill'
country = 'United States'
status = 'Enjoys Python'

#check version of python
import sys
print("Python Version: " + sys.version)
print ("My name is " + first + " " + last + ". I am from " + country + '. ' + status)

p1 = (2,3)
p2 = (10,8)
#euclidean distance
sol = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
print(sol)


