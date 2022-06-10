## Java 特性  
1. OOP
2. 跨平台特性: 一個編譯好的.class文件可以在多個系統下運行，只要安裝好JVM即可運行(ex:windows、Linux、Mac)  
3. 解釋性語言:  

    + 解釋性語言: 經編譯後的class文件還需要一個解釋器。  
    ex : javascript,php,java  
    + 編譯性語言: 編譯後可直接被機器使用。  
    ex : c,c++  

4. 強類型機制、異常處理、垃圾回收等  

------------------------  
## Java底層環境
JVM => java virtual machine  
JVM具有指令及且有不同的存儲空間。負責執行指令、管理數據、內存、寄存器，使包含在JDK中的。  
不同平台即有不同的JVM。  
編譯好class文件在哪都能運行。  

---
JDK => java development kit(JAVA開發工具包)  
JDK=JRE+JAVA的開發工具(java,javac,javadoc,javap等)  
+ JDK提供給開發人云使用，其中包含JAVA開發工具，也包含JRE。因此裝好JDK就不用再安裝JRE。
-------------------------
JRE => java rumtime environment (java運行環境)  
JRE = JVM + JAVA的核心類庫(類) 
+ JRE包括JVM和JAVA城市所需的核心涵式庫。如果想運行開發好的JAVA城市，只需在計算機中安裝JRE即可。
-------------------------
# 懶人包  
JDK = JRE + 開發工具即(ex : Javac,java編譯工具等)  
JRE = JVM + Java SE標準類庫(Java核心類庫)  
JDK = JVM + Java SE標準類庫 + 開發工具集  
如果只想運行開發好的.class文件，只需要JRE