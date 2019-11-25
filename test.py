import Kmeans
import tdidf
# Este é um exemplo dos dois programas em execução. O programador irá importar as biliotecas
text1 = "It is going to rain today"
text2 = "today I am not going outside"
text3 = "I am going to watch the season premiere"
Words = [text1, text2, text3,text1, text2, text3,text1, text2, text3,text1, text2, text3]
# importando o TFIDF enviando uma lista com os documentos, então o mesmo devolve uma lista com as pontuaões
# respectivas do documento
tdif = tdidf.getPoints(Words)
grupos = 2
TD = Kmeans.Euclidean(tdif, grupos)
print (TD)