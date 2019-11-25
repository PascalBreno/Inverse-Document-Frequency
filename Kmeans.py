import tdidf
import random
import math
import numpy as np
def adicionarpontosdoTDIF(tdif):
    NumPoints = []
    MnumberPoints = []
    for Document in tdif:
        for word in Document:
            NumPoints.append(Document.get(word, " "))
        MnumberPoints.append(NumPoints.copy())
        NumPoints.clear()
    return MnumberPoints


def recalcularPontosRandom(grupos, NumPointsKmeans, NumPoints, mediaPont, NumGrup):
    tam = len(mediaPont)
    newGrupo = {}
    newPonts = []
    denovo = False
    for x in range(NumGrup):
        for y, index in enumerate(grupos):
            if grupos[y] == x:
                newPonts.append(index)
        newGrupo[x] = newPonts.copy()
        newPonts.clear()
    newRandomNumber = []

    for Grupo in newGrupo:
        media = 0
        if newGrupo[Grupo]:
            for y in newGrupo[Grupo]:
                media += sum(NumPointsKmeans[y]) / len(NumPointsKmeans[y])
            media = media / len(newGrupo[Grupo])
            # 100=mediala
            # x = mediaAqio*100/mediaLa
            valor = (media * 100.0) / mediaPont[Grupo]
            if valor < 93:
                denovo = True
        else:
            media = mediaPont[Grupo]
        # Pegar os valores médis dos pontos do indice com o grupo X e calcular o novo ponto aleatório

        newRandomNumber.append(media)
    if (denovo):
        porMedia(NumPointsKmeans, newRandomNumber, NumGrup)


def porMedia(NumPointsKmeans, NumPoints, grup):
    grupos = {}
    mediaPont = []
    if type(NumPoints[0]) == list:
        for MediaPoint in NumPoints:
            Media = sum(MediaPoint) / len(MediaPoint)
            mediaPont.append(Media)
    else:
        mediaPont = NumPoints
    for valor, MediaPointList in enumerate(NumPointsKmeans):
        #Identificar para qual grupo vai
        MediaPointList, mediaPont[0] = np.array(v1), np.array(v2)
        diff = v1 - v2
        quad_dist = np.dot(diff, diff)
        result =  math.sqrt(quad_dist)
        Media = sum(MediaPointList) / len(MediaPointList) #MediaPointList é uma lista com todos os pontos

        min = -1
        for index, x in enumerate(mediaPont):
            if abs(Media - x) < min != 0:
                grupos[valor] = index
                min = abs(Media - x)
            if min == -1:
                grupos[valor] = index
                min = abs(Media - x)
    recalcularPontosRandom(grupos, NumPointsKmeans, NumPoints, mediaPont, grup)
    # Fez a primeira separação de grupos, agora verifica se pode continuar até a diferença for mínima
    return grupos


def criaPontosAleatorios(max, min, grupo, tamdoc):
    numerosAleatorio = []
    MnumerosAleatorio = []
    for y in range(grupo):
        for x in range(tamdoc):
            numerosAleatorio.append(random.uniform(min, max))
        MnumerosAleatorio.append(numerosAleatorio.copy())
        numerosAleatorio.clear()
    return MnumerosAleatorio


def Euclidean(tdif, grupos):
    max = 0
    min = 0
    # Aqui estou retirando os valores minimos e máximos para chutar um valor aproximado para fazer o K-Means, além do tamanho do documento
    for Document in tdif:
        tamDoc = len(Document)
        for word in Document:
            if Document.get(word, " ") > max:
                max = Document.get(word, " ")
            if Document.get(word, " ") < min:
                min = Document.get(word, " ")
    num = len(tdif)
    NumPoints = []
    NumPoints = adicionarpontosdoTDIF(tdif)
    NumPointsKmeans = criaPontosAleatorios(max, min, grupos, tamDoc)
    media = porMedia(NumPoints, NumPointsKmeans, grupos)
    # Apartir daqui você irá usar o método que o usuário decidiu para calcular o K-Mens
    return media
