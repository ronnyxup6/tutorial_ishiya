## python底線的使用  
1. foo_  
沒屁用
2. _foo  
類似於private的用法，可用於function  

為何說類似而不是等於呢? 
因為python當中沒有private，以下插入一段官方說明 : 
```
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member).
```
* 在某些情況你會使用到此種命名方式 :  
    - 你不希望它被直接訪問  
    - 它可能只是個測試中的 function  
    - 不希望它被直接 import  

但是在一種情況就會被import到
就是被定義在\_\_all\_\_裡的時候：
```
__all__  = ['public_func', '_private_func']
def public_func():
    print("I'm available.")
def _private_func():
    print("I'm not available")
```  
```
>>> from test import *
>>> _private_func()
I'm not available.
```  
可以看到還是被import到了  

3. \_\_foo\_\_  
通常，看到前後都有雙底線時，就要知道這個東東為class中的保留字，ex : \_\_init\_\_。  

但其實此種方式，可用在任何function或varible  

4. __foo  
無法被子類別使用，可使用於functoin、varible

參考 :  
https://medium.com/ai%E5%8F%8D%E6%96%97%E5%9F%8E/python-%E5%BA%95%E7%B7%9A-%E4%BB%8B%E7%B4%B9-%E8%BD%89%E9%8C%84-5b0349efdf52  
https://iter01.com/118529.html