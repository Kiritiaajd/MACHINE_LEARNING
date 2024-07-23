# Casting a number to a string 
decade = 1980
decade=str(decade)
print(decade," ",type(decade))
statement = 'I like pop music since '
print(statement + decade)
#Multiple Lines 
multiLine = '''
Hello , How are you : 
Iwas just checking in .
                     All good ?'''
print(multiLine)

#Escaping Special character 
sentence = 'I\'m back at work!\t Hey \n where is this located'
print(sentence)
print(len(decade))
print("Multiline : " , len(multiLine))
name = "KIRITI AAJAD"
print(name)
#Usig Len() function 
print("Length of name is " , len(name))
#Using isUpper() adn isLower() functions 
print(name.isupper())
name = "kiriti aajad"
print(name.islower())
name = "Kiriti Aajad"
print(name.isupper())
print(name.islower())
print(name.startswith('K'))
print(name.capitalize())
print(name.find('i'))
print(name.count('i'))

