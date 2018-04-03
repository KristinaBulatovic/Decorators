import random
import time

#from functools import wraps
def dokumentuj(func):
    #@wraps(func)
    def nova(*args, **kwargs):
        print("Ime funkcije koja se izvrsava:", func.__name__)
        print("Opis funkcije koja se izvrsava:", func.__doc__)
        print("Tip argumenata:",func.__annotations__)
        print("Pozicioni argumenti:", args)
        print("Nepozicioni argumenti:", kwargs)
        start = time.time()
        rezultat=func(*args, **kwargs)
        end = time.time()
        print("Rezultat:", rezultat)
        print("Vreme izvršenja:",end-start)
        return ""
    return nova

@dokumentuj
def add(a:int,b:int):
    "Sabira dva broja sa zadrškom"
    n=random.randrange(1000000,10000000,1)
    while n >0: n-=1
    return a+b

@dokumentuj
def dif(a:float,b:float):
    "Oduzima dva broja sa zadrškom"
    n=random.randrange(1000000,10000000,1)
    while n >0: n-=1
    return a-b


print(add(2,3))

print(dif(4.0, 2.5))

print(add.__name__)
print(add.__doc__)
print(add.__annotations__)

print(dif.__name__)
print(dif.__doc__)
print(dif.__annotations__)

