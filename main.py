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
for words in Documents:
    for word in words:
        if word in DicWord:
            DicWord[word] += 1
        else:
            DicWord[word] = 1
    DicWords.append(DicWord.copy())
    DicWord.clear()
for index, Document in enumerate(DicWords):
    #The index is the number of Document
    print("Document: ", index+1)
    for key, value in Document.items():
        print(key, "=>", value)
# Check if the word exist in Dic
