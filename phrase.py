phrase = input('Enter a Phrase: ')
letter = input('Letter to count: ')

word = 0

for x in range(len(phrase)):
        if(phrase[x] == letter):
                word = word + 1
                
print("Count: ", word)

