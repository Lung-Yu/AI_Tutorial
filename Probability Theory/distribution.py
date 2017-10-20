import numpy as np
import matplotlib.pyplot as plt
import random

from Coins import ThrowCoins

def factorial(x):
    if x > 1:
        return factorial(x-1) * x
    else:
        return 1

# poisson distribution
def poisson(lambda_num,k):
    k_factorial = factorial(k)
    molecular = pow(lambda_num,k)
    
    return (float(molecular) / k_factorial) * np.exp(-lambda_num)

#C(n,m) = n!/(m!*(n-m)!) 
def combinations(n,m):
    a = factorial(n)
    b = (factorial(m) * factorial(n-m))
    return  a / b 


def bernoulli(k,n,p):
    a = combinations(k,n)
    b = pow(p,2)
    c = pow(1 - p,k - n)    
    return  a * b * c


def make_poisson(lambda_num ,k_num=20):
    xs = list()
    ys = list()
    for i in range(0,k_num):
        xs.append(i)
        y = poisson(lambda_num,k = i)
        ys.append(y)
        # print ("k=%d,p(%d)=%f")%(i,i,y)
    return (xs,ys)


def plot_chart(x_axis="x-axis",y_axis="y-axis",the_title="The Title"):
    plt.legend()
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(the_title) 
    plt.show()


    
class Player:
    def __init__(self):
        self.time = 100
        self.unitTime = 100
        self.threshold = 0.5

    def __init__(self,threshold):
        self.time = 100
        self.unitTime = 100
        self.threshold = threshold

    def play(self):
        self.game = ThrowCoins(self.threshold)
        for i in range(0,self.time) :
            self.game.play(self.unitTime)

def playgame(threshold,times=10000):
    play = Player(threshold)
    play.time = times
    play.unitTime = 100
    play.play()

    return play.game

def plot_poisson():  
    (x1,y1) = make_poisson(1)
    (x2,y2) = make_poisson(4)
    (x3,y3) = make_poisson(10)
    plt.plot(x1 ,y1 ,'ro' ,label='lambda = 1')
    plt.plot(x1 ,y1 ,'r')

    plt.plot(x2 ,y2 ,'go' ,label='lambda = 4')
    plt.plot(x2 ,y2 ,'g')

    plt.plot(x3 ,y3 ,'bo' ,label='lambda = 10')
    plt.plot(x3 ,y3 ,'b')

    plot_chart("k","P(k)","Poisson Distribution")

def plot_gaussian(mu=0.5):
    game1 = playgame(mu)    
    plt.plot(game1.statistics,'b') 
    plot_chart(the_title="Coinss Gaussian")

def main():
    # print poisson(lambda_num = 2 ,k = 5)
    # print bernoulli(k = 4 ,n = 2 ,p = float(1)/3)    
    # random.uniform(1, 10) 
    
    #plot_poisson()
    plot_gaussian()

if __name__ == '__main__':
    main()
    

    
