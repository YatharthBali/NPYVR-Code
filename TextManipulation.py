# String in python
greeting = "Hello, world!"
name = "Rutu"

# Length of a string
# using len() function to get the length of a string
print(len(greeting))  
# Indexing 
print(greeting[0])
print(greeting[2])
print(name[-1])
# slicing
# the systex is string[start:enf:end:step]
print(greeting[0:5])
print(name[1:3])
print(greeting[::-1])
print(greeting[::-2])
# Concatenation
full_name = name + '  ' + 'Khakal'
print(full_name)

# Repetition
chant = name*3
print(chant) 
# using string methods 
print(greeting.upper())      
print(name.upper())
print(greeting.lower())
print(name.lower())
# count all string
string=input("Enter the string:")
lowerC=0
upperC=0
digitC=0
specialC=0
for charcter in string:
    if charcter.islower():
        lowerC=lowerC+1
    elif charcter.isupper():
        upper=upperC+1
    elif charcter.isdigit(): 
        digit=digitC+1
    else:
        specialC=specialC+1
        print("Lower Count:",lowerC)
        print("Upper Count:",upperC)
        print("Digit Count:",digitC)
print("Special Symbol Count:",specialC)
# Reverse each word of a string
s=input("Enter a strings:")
for word in s.split():
    print(word[::-1],end=" ")

