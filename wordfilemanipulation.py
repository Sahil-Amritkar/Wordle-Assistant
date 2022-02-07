import linecache
f = open("wordle_answers.txt", "r")

# f2 = open("temp.txt", "r")
# words=list(f2.read().split('","'))
# print(words[:10])
# for i in words:
#     f.write(i + "\n")    
#f2.close()

particular_line = linecache.getline('wordle_answers.txt', 145)
print(particular_line)
f.close()       
