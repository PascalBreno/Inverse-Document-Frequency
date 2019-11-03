# TF-IDF é uma medida estatística que indica a importância de uma palavra  TF - IDF = TF*IDF
# TF = Numero de vezes que uma palavra ocorre no documento / Número total de palavras no documento

text1 = "It is going to rain today to rain"
text2 = "Today I am not going outside"
text3 = "I am going to watch the season premiere"


def includeWordsOfDocuments():
    # TODO here need to add read in all Documents e add e return the number Documents
    Words = []
    Words.append(text1.split(" "))
    Words.append(text2.split(" "))
    Words.append(text3.split(" "))
    return Words

Documents  = includeWordsOfDocuments()
DicWords = []
DicWord = {}
DicWordAllDocument = {}
# Check if exist word in Document actual and All Documents
for words in Documents:
    for word in words:
        if word in DicWord:
            DicWord[word] += 1
        else:
            DicWord[word] = 1
        if word in DicWordAllDocument:
            DicWordAllDocument[word]+=1
        else:
            DicWordAllDocument[word]=1
    DicWords.append(DicWord.copy())
    DicWord.clear()
for index, Document in enumerate(DicWords):
    #The index is the number of Document
    print("Document: ", index+1)
    for key, value in Document.items():
        print(key, "=>", value)

#Here print all words in all Documents
print("All Document: ")
for key, value in DicWordAllDocument.items():
    print(key, "=>", value)

#TODO get a number of word in N Documents and calculate LN(Number of all Documents / Number of Documents with the word W). This is your IDF