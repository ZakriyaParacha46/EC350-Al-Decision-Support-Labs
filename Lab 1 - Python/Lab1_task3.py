##task 3
vowels =['i','o','u','a','e']
text = input("Enter a text:")
textlst =text.split(' ')
Pig_Latin = []

for word in textlst:
    if(word[0].lower() not in vowels):
        Pig_Latin.append(word[1:]+word[0]+'ay')
    else: 
        Pig_Latin.append(word+'hay')

print(' '.join(Pig_Latin))