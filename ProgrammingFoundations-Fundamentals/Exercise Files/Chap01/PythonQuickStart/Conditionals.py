raining = input("Is it raining? (yes/no)")
if raining == "yes":
    print("You need an umbrella!")


print(raining)

#IF Statement

userResponse = input("Choose an integer between 1 and 10 and enter it here:")
#print(type(userResponse))
userResponse = int(userResponse)
#print(type(userResponse))
if userResponse < 5:
    print("The integer you chose is less than 5.")
    # print(userResponse)
    # type(userResponse)


#IF-ELSE Statement

def minimum(x, y):
    if x < y:
        return x
    else:
        return y

# test out minimum on the inputs -7 and -11
result = minimum(-7, -11)
print(result)

# test out minimum on the inputs 2 and 23
result = minimum(2, 21)
print(result)

# test out minimum on the inputs 3 and 3
result = minimum(3, 3)
print(result)

# test out minimum on the inputs 3 and 3.1
result = minimum(3, 3.1)
print(result)

# test out minimum on the inputs 3 and "3" - should return an error!
result = minimum(3, "3")
print(result)


#IF-ELIF Statement
raining = input("Is it raining (yes/no)?")
umbrella = input("Do you have an umbrella (yes/no)?")
if raining == "yes" and "umbrella" == "yes":
    print("You are ready to go for a walk!")
elif raining == "yes" and umbrella == "no":
    print("Get an umbrella first")
else:
    print("Just stay home")



x = input("Enter a number between 1 and 10:")
x = float(x)
if x < 2:
    print("The number is less than 2.")
elif x < 6:
    print("The number is less than 6.")
elif x < 8:
    print("The number is less than 8.")
elif x <= 10:
    print("The number is less or qual 10.")
else:
    print("The number is out of 1-10 range")


x = 1
print(float(x)) #prints 1.0


x = 1.5
print(int(x)) #prints 1

# input is -4 --> absolute value is 4 (4 is -1 * -4)
# input is 0 --> absolute value is 0
# input is 78.3 --> absolute value is 78.3
def abs_val(num):
  if num < 0:
    return -1 * num
  elif num == 0:
    return
  else:
    return num


result = abs_val(-4)
print(result)

result = abs_val(0)
print(result)

result = abs_val(78.3)
print(result)
