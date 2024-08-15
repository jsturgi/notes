age = 26
height = 6.2
complex_number = 1 + 2j

base = input('Enter the base: ')
height = input('Enter the height: ')

area = 0.5 * float(base) * float(height)
print('The area of the triangle is:', area)

a = input('Enter the first side: ')
b = input('Enter the second side: ')
c = input('Enter the third side: ')
perimeter = float(a) + float(b) + float(c)

print('The perimeter of the triangle is:', perimeter)

length = input('Enter the length of the rectangle: ')
width = input('Enter the width of the rectangle: ')
area = float(length) * float(width)
perimeter = 2 * (float(length) + float(width))

radius = input('Enter the radius of the circle: ')
area = 3.14 * float(radius) ** 2
print('The area of the circle is:', area)


#calculate slope of y = 2x - 2  
x1 = 0
y1 = -2
x2 = 1
y2 = 0
slope = (y2 - y1) / (x2 - x1)
print('The slope of the line is:', slope)
# calculate y and x i ntercpet
y_intercept = y1 - slope * x1
x_intercept = -y_intercept / slope
print('The y intercept is:', y_intercept)
print('The x intercept is:', x_intercept)

a1, a2, b1, b2 = 2, 6, 2, 10
distance = ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5
print('The distance between the points is:', distance)
slope2 = (b2 - b1) / (a2 - a1)
print('The slope of the line is:', slope2)

#difference between slopes
print('The difference between the slopes is:', slope - slope2)
i = 2
j = i**2 + 6*i +9
print(j)

pylen = len('Python')
dralen = len('Dragon')
print (pylen > dralen)

print('on' in 'Python' and 'on' in 'Dragon')
jargon = 'I hope this course is not full of jargon'
print('jargon' in jargon)

print('on' not in 'Python' and 'on' not in 'Dragon')

print(type(pylen))
float(pylen)
print(type(pylen))
str(pylen)
print(type(pylen))
# check if number is even
print("Use Modulo to check if number is even: 4 % 2 == 0")
print(4 % 2 == 0)

print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int('9.8')==10)

hours = input('Enter the number of hours: ')
rate = input('Enter the rate per hour: ')
print('Your weekly earning is:', float(hours) * float(rate))

years = input('Enter the number of years you have lived: ')
seconds = 365 * 24 * 60 * 60 * int(years)
print('You have lived for', seconds, 'seconds')

#function that prints 1*1  in top left, 5*5 in bottom right
def print_pattern():
    for i in range(1, 6):
        for j in range(5):
            if j == 0:
                print(i, end=' ')
            else:
                print(i ** j, end=' ')
        print()

print_pattern()