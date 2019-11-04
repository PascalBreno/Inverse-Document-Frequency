# TF-IDF é uma medida estatística que indica a importância de uma palavra  TF - IDF = TF*IDF
# TF = Numero de vezes que uma palavra ocorre no documento / Número total de palavras no documento
import math

text1 = "It is going to rain today"
text2 = "today I am not going outside"
text3 = "I am going to watch the season premiere"


def includeWordsOfDocuments():
    # TODO here need to add read in all Documents e add e return the number Documents
    Words = []
    Words.append(text1.split(" "))
    Words.append(text2.split(" "))
    Words.append(text3.split(" "))
    return Words


def printAllDocument():
    for index, Document in enumerate(DicWords):
        # The index is the number of Document
        print("Document: ", index + 1)
        for key, value in Document.items():
            print(key, "=>", value)

    # Here print all words in all Documents
    print("All Document: ")
    for key, value in DicWordAllDocument.items():
        print(key, "=>", value)
def setTFinAllWords():
    for Document in DicWords:
        tam = 0
        for word in Document:
            if Document.get(word,"")>0:
                tam +=1
        for word in Document:
            aux = Document.get(word,"")
            Document[word] = float(aux/tam)
def setTF():
    for Document in DicWords:
        for word in Document:
            Document[word] = Document.get(word,"")*NumberWordDocument.get(word, "")
    printAllDocument()
Documents = includeWordsOfDocuments()
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
            DicWordAllDocument[word] += 1
        else:
            DicWordAllDocument[word] = 1
    DicWords.append(DicWord.copy())
    DicWord.clear()
# Add all words in all Documents. If the Document dont have the Word, so add 0 to your value
NumberWordDocument = {}
for index, Document in enumerate(DicWords):
    for word in DicWordAllDocument:
        if word in Document and Document.get(word, "") > 0:
            if word in NumberWordDocument:
                if not (NumberWordDocument[str(word)] > index):
                    NumberWordDocument[str(word)] += 1
            else:
                NumberWordDocument[str(word)] = 1
        else:
            Document[word] = 0

setTFinAllWords()
printAllDocument()

NumberOfDocuments = len(DicWords)
for word in NumberWordDocument:
    x = NumberOfDocuments/NumberWordDocument.get(word," ")
    NumberWordDocument[word] = math.log(x)
setTF()
