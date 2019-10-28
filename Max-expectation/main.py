import math

def calcWeight(p, Tetha):
    x = 0
    y = 0
    for i in Tetha:
        x = (math.pow((Tetha[0]/10), p[0]) * math.pow ( (1- (Tetha[0]/10) ), (p[0]-(p[0]+p[1]))))
        y = (math.pow((Tetha[1]/10), p[0]) * math.pow ( (1- (Tetha[1]/10) ), (p[0]-(p[0]+p[1]))))
        print (x, y)
    for j in Tetha:
        Wa = x/x+y
        Wb = y/x+y

def expectation():
    p = [5,5]
    Tetha = [0.6, 0.4]
    calcWeight(p, Tetha)

expectation()




#datasets grandes bittorrent
#dimensionalidad
#Tamaño