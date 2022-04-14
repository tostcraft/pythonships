#!usr/bin/Python3
from turtle import *
import random
t=Pen()
t.speed(0)
tracer(False)


def czy_poprawne(siatka, poz):
    if (poz[0]==0 or poz[0]==9) and (poz[1]<9 and poz[1]>0):
        if poz[0]==0:
            obok=siatka[poz[1]+1][poz[0]]+siatka[poz[1]-1][poz[0]]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]+1][poz[0]+1]+siatka[poz[1]-1][poz[0]+1]
            if obok==0:
                return True
        elif poz[0]==9:
            obok=siatka[poz[1]+1][poz[0]]+siatka[poz[1]-1][poz[0]]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]+1][poz[0]-1]+siatka[poz[1]-1][poz[0]-1]
            if obok==0:
                return True
    elif (poz[1]==0 or poz[1]==9) and (poz[0]<9 and poz[0]>0):
        if poz[1]==0:
            obok=siatka[poz[1]+1][poz[0]]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]+1][poz[0]+1]+siatka[poz[1]+1][poz[0]-1]
            if obok==0:
                return True
        elif poz[1]==9:
            obok=siatka[poz[1]-1][poz[0]]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]-1][poz[0]-1]+siatka[poz[1]-1][poz[0]+1]
            if obok==0:
                return True
    elif (poz[0]==0 or poz[0]==9) and (poz[1]==0 or poz[1]==9):
        if poz[0]==0 and poz[1]==0:
            obok=siatka[poz[1]+1][poz[0]]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]+1][poz[0]+1]
            if obok==0:
                return True
        elif poz[0]==9 and poz[1]==0:
            obok=siatka[poz[1]+1][poz[0]]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]+1][poz[0]-1]
            if obok==0:
                return True
        elif poz[0]==0 and poz[1]==9:
            obok=siatka[poz[1]-1][poz[0]]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]-1][poz[0]+1]
            if obok==0:
                return True
        elif poz[0]==9 and poz[1]==9:
            obok=siatka[poz[1]-1][poz[0]]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]-1][poz[0]-1]
            if obok==0:
                return True
    elif (poz[0]<9 and poz[0]>0) and (poz[1]<9 and poz[1]>0):
        obok=siatka[poz[1]-1][poz[0]]+siatka[poz[1]+1][poz[0]]+siatka[poz[1]][poz[0]-1]+siatka[poz[1]][poz[0]+1]+siatka[poz[1]+1][poz[0]+1]+siatka[poz[1]+1][poz[0]-1]+siatka[poz[1]-1][poz[0]-1]+siatka[poz[1]-1][poz[0]+1]
        if obok==0:
            return True
    return False
        

        
            

    

class gra():
    def __init__(self):
        self.ja=[[0 for x in range(10)] for x in range(10)]
        self.przeciwnik=[[0 for x in range(10)] for x in range(10)]
        self.strzaly=[]

    def ustal(self):
        statki=[[1]]*4+[[1,1]]*3+[[1, 1, 1]]*2+[[1, 1, 1, 1]]*1
        pozycje=[]
        ustawienia=['poz', 'pion']
        for x in statki:
            while True:
                poz=(random.randrange(10), random.randrange(10))
                kier=random.choice(ustawienia)
                pola=[]
                if poz in pozycje:
                    continue
                if kier=='poz':
                    if poz[0]+len(x)>9:
                        continue
                elif kier=='pion':
                    if poz[1]+len(x)>9:
                        continue
                for s in range(len(x)):
                    if kier=='poz':
                        if czy_poprawne(self.przeciwnik, (poz[0]+s, poz[1])):
                            pola.append((poz[0]+s, poz[1]))
                    if kier=='pion':
                        if czy_poprawne(self.przeciwnik, (poz[0], poz[1]+s)):
                            pola.append((poz[0], poz[1]+s))
                if len(pola)==len(x):
                    break
            pozycje.append(pola)
            for y in pola:
                self.przeciwnik[y[1]][y[0]]=1
        return

    def rysuj(self):
        def kwadrat(bok, zam):
            t.fillcolor(zam)
            t.begin_fill()
            for x in range(4):
                t.fd(bok)
                t.rt(90)
            t.end_fill()
        t.up()
        t.bk(450)
        t.lt(90)
        t.fd(200)
        t.rt(90)
        t.down()
        kwadrat(400, 'white')
        for x in self.ja:
            for y in x:
                if y==1:
                    kwadrat(40, 'green')
                else:
                    kwadrat(40, 'white')
                t.fd(40)
            t.up()
            t.rt(90)
            t.fd(40)
            t.rt(90)
            t.fd(400)
            t.rt(180)
            t.down()
        t.up()
        t.fd(450)
        t.lt(90)
        t.fd(400)
        t.rt(90)
        t.down()
        kwadrat(400, 'white')
        for x in self.przeciwnik:
            for y in x:
                if y==2:
                    kwadrat(40, 'red')
                elif y==1 or y==0:
                    kwadrat(40, 'white')
                elif y==3:
                    kwadrat(40, 'blue')
                t.fd(40)
            t.up()
            t.rt(90)
            t.fd(40)
            t.rt(90)
            t.fd(400)
            t.rt(180)
            t.down()
        t.up()
        t.home()
        t.down()
    def ustaw(self, pozycje):
        dostepne=[]
        for x in range(10):
            for y in range(10):
                dostepne.append([x, y])
        for x in pozycje:
            for y in x:
                assert y in dostepne
                dostepne.remove(y)
                self.ja[y[1]][y[0]]=1
    def strzal(self, gdzie):
        assert not gdzie in self.strzaly
        if self.przeciwnik[gdzie[1]][gdzie[0]]==1:
            self.przeciwnik[gdzie[1]][gdzie[0]]=2
        elif self.przeciwnik[gdzie[1]][gdzie[0]]==0:
            self.przeciwnik[gdzie[1]][gdzie[0]]=3
        self.strzaly.append(gdzie)
        self.rysuj()


gra=gra()
gra.ustal()
gra.rysuj()
                
