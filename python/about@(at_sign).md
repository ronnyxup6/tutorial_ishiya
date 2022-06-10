在開始之前我們必須先對工廠模式有一點點概念  
* 工廠模式，就是使用工廠方法的程式設計模式。  
* 設計模式 :「設計模式」是個被驗證過可行，並且讓我們可以重複使用程式碼的解決方案。  


1. 工廠方法  
顧名思義，當一個prject的code量大時，為了要更方便的使用一個物件，就不能將使物件的創建與使用寫死，可以重複使用同一個物件，我們就會用到此種設計模式。其用法就是在一個class之中，寫一個interface，下面的@method中有範例。  
2. 抽象工廠設計模式
抽象工廠方法的設計模式，我的理解是，另外寫一個interface。也就是將原本的calss寫成只是abstract的，然後寫一個獨立的interface利用這個interface創建及使用物件。  

https://zh.wikipedia.org/zh-tw/%E5%B7%A5%E5%8E%82%E6%96%B9%E6%B3%95   
https://medium.com/seaniap/python-%E8%A8%AD%E8%A8%88%E6%A8%A1%E5%BC%8F-%E5%B7%A5%E5%BB%A0%E6%96%B9%E6%B3%95-factory-pattern-8a3751b985b  

---
# @正題開始
* @staticmethod  
阿就是那個static  
```
@staticmethod
def func(args, ...)
```
* @classmethod  
```
@classmethod
def func(cls, args...)
```
(以下全是抄來的)  
(希望文件能夠簡潔、一讀就懂，避免還要去查找過多資料，又要避免太過冗長。之後會再做調整，做到簡短又好懂。by RonnyLin)
* cls是甚麼?  
其實就如同類別內的其他函數一樣，利用self來指向自己，但在classmethod中的第一個參數，指向的自己是該類別的記憶體位置。  
區別在於一般函數的第一個參數指的是該物件的記憶體位置，classmethod的第一個參數指的是該類別的記憶體位置。  
---
## classmethod與staticmethod的差別？
因為classmethod利用的cls來把自己綁定在類別上，所以classmethod可以透過cls來呼叫類別內的成員；但staticmethod只能操作傳入的參數。
```
#Example
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()
```
```
#Output
The age is: 25
```
***
## 什麼時候用classmethod比較好？
1. 工廠模式 factory pattern  
```
#Example

from datetime import date
# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
person = Person('Adam', 19)
person.display()
person1 = Person.fromBirthYear('John',  1985)
person1.display()  
```
```
#Output

Adam's age is: 19
John's age is: 31  
```
在這裡我們擁有兩個物件：person以及person1，分別是Adam跟John，接下來我們用他們的姓名來稱呼他們。

Adam是透過標準的建構子(Constructor)來創造的，參數是姓名跟年紀；而John是利用factory method也就是 “frombirthYear” 透過傳入姓名與出生年份來創造。

在程式碼中我們可以看到回傳cls(name, date.today.year - birthYear)，這樣的寫法其實就是創造一個物件並回傳，等價於
Person(name, date.today().year - birthYear)。

透過這種方式來讓你能夠有彈性的創造物件，不局限於限定的建構子參數，也省下建立Factory的步驟。

2. 在繼承時創建正確的物件
承接上面的Factory 範例，如果用staticmethod可不可以做factory？

也可以。
```
#Example

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherBirthYear, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherBirthYear -fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))
```
```
#Output

True
False
```
在範例裡面我們多用了一個從爸爸出生年份與兒子年齡差距來建立物件的方法 — fromFathersAge，直接看到最後回傳的部分，是直接寫死 Person 類別，沒辦法像classmethod一樣利用cls來呼叫自身類別。

兩者的做法差別最大的地方在於：當你利用子類別(sub class)呼叫來自父類別(parent class)函數時，你創造出來的物件會被限定在父類別這個階層，而不是你呼叫的子類別。

因為你當初寫死類別了，staticmethod無法自動衍生至子類別。這點從我們的測試結果就可以看的出來。  


參考 : https://ji3g4zo6qi6.medium.com/python-tips-5d36df9f6ad5