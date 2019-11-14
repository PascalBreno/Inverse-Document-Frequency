import main
import random
def  adicionarpontosdoTDIF(tdif):
    NumPoints =[]
    MnumberPoints = []
    for Document in tdif:
        for word in Document:
            NumPoints.append(Document.get(word, " "))
        MnumberPoints.append(NumPoints.copy())
        NumPoints.clear()
    return MnumberPoints
def porMedia(NumPointsKmeans, NumPoints, NumPointsBefore):
    grupos ={}
    mediaPont = []
    for MediaPoint in NumPoints:
        Media = sum(MediaPoint)/len(MediaPoint)
        mediaPont.append(Media)
    print(mediaPont ,"Media dos pontos aleatórios")
    for valor,MediaPointList in enumerate(NumPointsKmeans):
        Media = sum(MediaPointList)/len(MediaPointList)
        min =-1
        print(Media)
        for index, x in enumerate(mediaPont):
            if (abs(Media - x) < min and min != 0):
                grupos[valor] = index
                min = abs(Media - x)
            if(min==-1):
                grupos[valor] = index
                min = abs(Media-x)
    #Fez a primeira separação de grupos, agora verifica se pode continuar até a diferença for mínima
    print(NumPointsKmeans)
    print(grupos)
    return grupos
def criaPontosAleatorios(max,min, grupo, tamdoc):
    numerosAleatorio = []
    MnumerosAleatorio = []
    for y in range(grupo):
        for x in range(tamdoc):
            numerosAleatorio.append(random.uniform(min, max))
        MnumerosAleatorio.append(numerosAleatorio.copy())
        numerosAleatorio.clear()
    return MnumerosAleatorio


text1 = "It is going to rain today"
text2 = "today I am not going outside"
text3 = "I am going to watch the season premiere"
Words = []
Words.append(text1)
Words.append(text2)
Words.append(text3)
tdif = main.td(Words)
grupos = 2
def Kmains(tdif, grupos):
    max = 0
    min = 0
    #Aqui estou retirando os valores minimos e máximos para chutar um valor aproximado para fazer o K-Means, além do tamanho do documento
    for Document in tdif:
        tamDoc = len(Document)
        for word in Document:
            if Document.get(word, " ")>max:
                max = Document.get(word, " ")
            if Document.get(word, " ")<min:
                min = Document.get(word, " ")
    num = len(tdif)
    NumPoints = []
    NumPoints = adicionarpontosdoTDIF(tdif)
    NumPointsKmeans = criaPontosAleatorios(max,min,grupos,tamDoc)
    media = porMedia(NumPoints, NumPointsKmeans, NumPoints)
    #Apartir daqui você irá usar o método que o usuário decidiu para calcular o K-Menas
    return media