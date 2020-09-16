word = input("Please type a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']

vowelCount = 0
for character in word:
  if character in vowels:
    vowelCount += 1

print(vowelCount)



#For Loop
# a structure that helps achieve iteration
# you can specify a range of numbers using the range() function

#  Range() is na build in function, that takes inputs as: range(start, stop, step):
# When a starting number is not provided -  range defaults to start from 0.
# When a step size is not provided, range defaults to using a step size of 1.
# The ending number must be provided and range excludes this ending number.

#will print 0, 1, 2, 3
for i in range(4):
    print(i)


# will print 1, 3, 5, 7
for i in range(1, 8, 2):
  print(i)


num = input("Please type a number from 1 to 10: ")
num = int(num)
for i in range(num):
    print(i)



vowels = ['a', 'e', 'i', 'o', 'u']
for v in vowels:
  print(v)



vowels = ['a', 'e', 'i', 'o', 'u']
for v in vowels:
  if v == "i":
    break
  print(v) # prints a, e


for x in range(6):
  print(x)
else:
  print("Finally finished!")



# While Loop

vowels = ['a', 'e', 'i', 'o', 'u']
length = len(vowels)
print(length)


vowels = ['a', 'e', 'i', 'o', 'u']
i = 0
while i < len(vowels):
  print(vowels[i])
  i += 1
