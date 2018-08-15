# Andrew Moss
# Lab 4 : Loops
# CS 002
ex = int(input("Which exercise? "))
if(ex == 1):
    word = input("Enter a word: ")

    if 'e' in word:
        print("Your word,", word, "contains the character 'e'")

    if 'x' in word:
        print("Your word,", word, "contains the character 'x'")

    else:
        print("Neither e nor x was found")

elif(ex == 2):
    it = 0
    word = list(input("Enter a word: "))
    for i in word:
        if word[it] == 'e':
            word[it] = '3'
        if word[it] == 'i':
            word[it] = '1'
        if word[it] == 'x':
            word[it] = '*'
        it+=1
        newWord = "".join(word)
    print("Your word transformed is", newWord)

elif(ex == 3):
    sent = input("Enter a sentence: ")
    if '.' in sent:
        print("The character '.' is located at", sent.index('.'))
    else:
        print("The sentence does not contain the character '.' ")
    if 'stop' in sent:
        print("The word 'stop' starts at index", sent.index('stop'))
    else:
        print("The sentence does not contain the word 'stop' ")
