print("Hello Shahjade")
message = "Let's do it"
print(message)
# Name = ['alam', 'shahjade']
Name = 'shahjade alam'
x = Name.upper()
print(x)
x = Name.lower()
print(x)
x = Name.title()
print(x)
first = 'shahjade'
last = 'alam'
print(first + '-' + last)
print("SHAHJADE\n\tALAM")
xyz = "   shahajde     "
print(xyz.strip())
print(2+3)
print(2*3)
print(2/3)
print(2-3)
Bicycle = ['A', 'B', 'C', 'D']
print(Bicycle[:3])
print(Bicycle[-1])
Bicycle.append('F')
print(Bicycle)
bike = []
bike.append('Honda')
bike.append('YAMAHA')
bike.append('SUZUKI')
print(bike)
bike.insert(1, 'Harley')
print(bike)
bike.remove('Harley')
print(bike)
Guest = ['A', 'B', 'C', 'D', 'E', 'F']
print(Guest)
Guest.insert(0, 'X')
Guest.remove('A')
print(Guest)
for i in range(1, 5):
    Guest.append('Y'+str(i))
print(Guest)
Guest.sort()
print(Guest)
Guest.sort(reverse=True)
print(Guest)

for j in Guest:
    print("Awsome : " + str(j))
for value in range(0, 10):
    print(value)
X = []
for value in range(0, 10):
    X = value
print(X)
num = list(range(2, 10))
print(num)
print(min(num))
print(max(num))
print(sum(num))
for value in range(0, 21):
    print(value)
x = []
for value in range(0, 1):
    print(value)
print(x)
z = list(range(1, 10, 2**3))
print(z)
m = z[:]
print(m)
p = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for x in p:
    print(x)
 #####################
print(bike)
if 'Honda' in bike:
    print('HONDA is present')
else:
    print('Not present')
#####################
age = 25
if age == 21:
    print(21)
elif age <= 18:
    print(18)
elif age == 25:
    print(25)
#####################
req_topping = ['mushroom', 'extra cheese']

if 'mushroom' in req_topping:
    print('Adding::'+'mushroom')
if 'pepper' in req_topping:
    print('Adding::'+'pepper')
if('extra cheese' in req_topping):
    print('Adding::'+'Extra cheese')
print('--------------------------------')
for topping in req_topping:
    print('Adding::' + topping)
