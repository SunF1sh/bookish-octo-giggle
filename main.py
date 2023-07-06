"""import asyncio
async def l():
    print("yfxfkb cnbhrf")
    await asyncio.sleep(70)
    print("закончили стирку")

async def s():
    print("поставили суп")
    await asyncio.sleep(60)
    print("убрали суп")

async def t():
    print("чай")
    await asyncio.sleep(15)
    print("конец чая")

async def main():
    await l()
    await s()
    await t()

async def amain():
    await asyncio.gather(l(), s(), t())

asyncio.run(amain())

import asyncio
import random
async def k1():
    print("kot1")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot1")
async def k2():
    print("kot2")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot2")
async def k3():
    print("kot3")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot3")
async def k4():
    print("kot4")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot4")
async def k5():
    print("kot5")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot5")
async def k6():
    print("kot6")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot6")
async def k7():
    print("kot7")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot7")
async def k8():
    print("kot8")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot8")
async def k9():
    print("kot9")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot9")
async def k10():
    print("kot10")
    await asyncio.sleep(random.randint(1,10000))
    print("конец kot10")
async def main():
    await k1()
    await k2()
    await k3()
    await k4()
    await k5()
    await k6()
    await k7()
    await k8()
    await k9()
    await k10()
async def amain():
    await asyncio.gather(k1(), k2(),k3(),k4(),k5(),k6(),k7(),k8(),k9(),k10())

asyncio.run(amain())

import requests
urla=[]
url='https://api.thecatapi.com/v1/images/search?limit=10'
response = requests.get(url).json()
for line in response:
    urla = line['url']
for i in range(10):
    file = open(f'')


class Human:
    genom_count = 46
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def calc(self)-> float:
        return round((sum(self.grades)/len(self.grades) - 2)/3)
Vlad=Human("Vlad", 16, [3,4,5,2,7,5])

class ing:
    def __init__(self, calories: float, mass: float)->None:
        self._calories = calories
        self._mass = mass
    def prepare(self)-> float:
        return self._calories
    def gc(self)-> float:
        return self._calories
    def gm(self)-> float:
        return self._mass
class Bread(ing):
    def prepare(self) -> float:
        self._calories+=10
        self._mass*=0,8
        return super().prepare()
class tomato(ing):
    def prepare(self) -> float:
class soap(ing):
    def prepare(self) -> float:
        self._calories+=10
        self._mass*=0,8
        return super().prepare()"""


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'hedfhf{self.__class__.__name__}({self.x},{self.y})'


p = Point(input(), input())
print(p)