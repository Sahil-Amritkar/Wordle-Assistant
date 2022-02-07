import linecache

def eliminate(letter_positions, word, colours):
    for i in range(len(word)):
        if(colours[i]=='b'):
            try:
                del letter_positions[word[i]]
            except:
                temp=1
        elif(colours[i]=='y'):
            try:
                letter_positions[word[i]].remove(i+1)
            except ValueError:
                temp=1

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

def print_possible_words(words):
    print("\nPossible Words:")
    for i in range(0, len(words), 10):
        print(*words[i:i+10], sep="\t")
    print("")

def print_letter_positions(letter_positions):
    print("\nPossible Letters and their Positions:")
    for key, value in letter_positions.items():
        print(key, ' : ', value)    
    print("")

def input_word(wordle_no):
    print("Enter Word typed:")
    word=input()
    wordle_of_today=linecache.getline('wordle_answers.txt', wordle_no)
    colours=""
    for i in range(len(word)):
        if word[i]==wordle_of_today[i]:
            colours+='g'
        elif word[i] in wordle_of_today:
            colours+='y'
        else:
            colours+='b'
    print(colours)
    return word, colours


#main
print("Hello, Welcome to Worldle Assistant!")
print("Enter the Wordle number")
while(True):
    wordle_no=int(input())
    if(wordle_no>0 and wordle_no<2315):
        break
    else:
        print("Enter Valid Wordle Number")

print("Choose your difficulty:")
print("Enter 1 for EASY: Only words that can be the wordle will be shown")
print("Enter 2 for CHALLENGE: All 5 letter words will be shown")
while(True):
    difficulty=input()
    if(difficulty=='1' or difficulty=='2'):
        break
    else:
        print("Please enter 1 or 2")

if(difficulty=='1'):
    f = open("words_easy.txt", "r")
    words=list(f.read().split('\n'))
    f.close()
elif(difficulty=='2'):
    f = open("words_challenge.txt", "r")
    words=list(f.read().split('\n'))
    f.close()

letter_positions={}
for i in range(97,123):
    letter_positions[chr(i)]=[1,2,3,4,5]

first_words=['crate', 'roate', 'realo', 'alter', 'irate', 'adieu', 'soare', 'stare', 'arise']
print_letter_positions(letter_positions)
print("Possible Words:")
print(*first_words, sep='\t')
print("")

for i in range(6):
    word, colours = input_word(wordle_no)
    if(colours=="ggggg"):
        print("\nSUCESS!")
        print("It took ", i+1, "tries!")
        break
    eliminate(letter_positions, word, colours)
    match_criteria(letter_positions, words)
    print_letter_positions(letter_positions)
    print_possible_words(words)
    if(i==5):
        print("Oh no! Out of Tries")
print("Thanks for using wordle Assistant!")
