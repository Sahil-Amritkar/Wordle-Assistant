import re

def eliminate(letter_positions, word, colours):
    for i in range(len(word)):
        if(colours[i]=='b'):
            del letter_positions[word[i]]
        elif(colours[i]=='y'):
            letter_positions[word[i]].remove(i+1)
        elif(colours[i]=='g'):
            #letter_positions[word[i]]=[i+1]
            for l in letter_positions:
                if l!=word[i]:
                    try:
                        letter_positions[l].remove(i+1)
                    except ValueError:
                        temp=1
                
def match_criteria(letter_positions, words):
    words_copy=words.copy()
    for word in words_copy:        
        for l in range(len(word)):
            if not word[l] in letter_positions:
                words.remove(word)
                break
            if l+1 not in letter_positions[word[l]]:
                words.remove(word)
                break
        
    printing(words)        

def printing(words):
    print("\nPossible Words:")
    print(*words, sep='\t')
    print("")




def input_word():
    print("Enter Word typed:")
    word=input()
    print("Enter Colours of the letters b-black, y-yellow, g-green:")
    colours=input()
    return word, colours


#main
print("Hello")
f = open("WordSearch\words5.txt", "r")
words=list(f.read().split('\n'))
#print(words[:10])
f.close()

letter_positions={}
for i in range(97,123):
    letter_positions[chr(i)]=[1,2,3,4,5]

#print(letter_positions)

for i in range(5):
    print(letter_positions)
    word, colours = input_word()
    eliminate(letter_positions, word, colours)
    match_criteria(letter_positions, words)
    #printing(words)

# textfile = open("WordSearch\words5.txt", "w")

# for i in words:
#     print(i)
#     if(len(i)==5):
#         textfile.write(i + "\n")

# textfile.close()