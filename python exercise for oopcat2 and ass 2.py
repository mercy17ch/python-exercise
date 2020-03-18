
#program to calculate compound interest
def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result


P = float(input("Enter the principal amount: "))
R = float(input("Enter the interest rate: "))
T = float(input("Enter the time in years: "))

amount = compound_interest(P, R, T)
interest = amount - P
print("Compound amount is %.2f" % amount)
print("Compound interest is %.2f" % interest)

# Python function to convert temperatures to and from celsius, fahrenheit.
#  [ Formula : c/5 = f-32/9 [where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
#temperature input in either c or f
temp = input("Input the  temperature, please add either 'F' after the integer for fahrenheit or 'C' for celcious; ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()

print((temp[:-1]),u'\N{DEGREE SIGN}',temp[-1],"is",result,"in", o_convention)

#a program that will take a word
#  and output the pig latin version of the word by following the following rules:
#If a word starts with a consonant or group of consonants, move all letters
#before the first vowel to the end of the word then add "ay". eg,will='illway,''dog= ogday,chatter -> atterchay
# If the word starts with a vowel,
# simply add "way" to the end of the word eg electrician – electricianway.

print("PIG LATIN GAME")

ay = 'ay'
way = 'way'
consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')
user_word = input('Enter a word : ')
# getting first letter and making sure its a string and setting it to uppercase
first_letter = user_word[0]
first_letter = str(first_letter)
first_letter=first_letter.upper()
if first_letter in consonant:
   print(first_letter,'is a consonant')
   length_of_word = len(user_word)
   remove_first_letter = user_word[1:length_of_word]
   pig_latin=remove_first_letter+first_letter+ay
   print('The word in Pig Latin is:',pig_latin)
elif first_letter in vowel:
   print(first_letter,'is a vowel')
   pig_latin=user_word+way
   print('The word in Pig Latin is:',pig_latin)
else:
   print("invalid word")

# Python function to find the Max of three numbers
def maximum(x,y,z):
    result=max(x,y,z)
    return result
#user input
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))
#print result
print("x=",x,"y=",y,"z=",z)
print("the max  is;", maximum(x,y,z))

#program to print even numbers
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print( is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
