# SSM框架 = Spring + Spring MVC + MyBatis
(補充:SSH = Spring + Spring MVC + Hibernate)   

## Spring簡單介紹
--------------------

簡單來說:  
Spring(輕量級的容器框架)  
SpringMVC(分層的web開發框架)  
Mybatis(持久化框架)  
## Spring(整合型框架)
* 已包含SpringMVC
* 依賴注入(DI--Dependency Injection):，反轉控制(IOC)的實現，物件管理
面向切面編程:AOP(Aspect Oriented Programming)，對OOP做補充
## SpringMVC(表述層)

* Spring MVC屬於SpringFrameWork的後續產品，已經融合在Spring Web Flow裡面。Spring MVC 分離了控制器、模型對象、分派器以及處理程序對象的角色，這種分離讓它們更容易進行定製。

## MyBatis(持久層框架)

* 其實MyBatis本是apache的一個開源項目iBatis,後來由於種種原因遷移到了google code，並且改名為MyBatis 。MyBatis是一個基於Java的持久層框架。
* iBATIS提供的持久層框架包括SQL Maps和Data Access Objects（DAO）MyBatis消除了幾乎所有的JDBC代碼和參數的手工設置以及結果集的檢索。
* MyBatis使用簡單的XML或註解用於配置和原始映射，將接口和Java的POJOs（Plain Old Java Objects，普通的 Java對象）映射成資料庫中的記錄。可以這麼理解，MyBatis是一個用來幫你管理數據增刪改查的框架。

參考資料:https://www.itread01.com/content/1547467745.html
參考資料：https://kknews.cc/code/j2eq99p.html

簡易使用vscode建置Spring環境：https://www.796t.com/article.php?id=20366


--------------------------------
# Spring

## 靜態代理

* 抽象腳色 : 一般會使用街口或者抽象類來解決
* 真實腳色 : 被代理的腳色
* 代理腳色 : 代理真實腳色，代理真實腳色後，我們一般會做一些附屬操作。
* 客戶 : 訪問代理對象的人