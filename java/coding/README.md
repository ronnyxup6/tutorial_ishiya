# coding注意事項
1. class, function的註釋,以javadoc的方式來寫  
2. 非javadoc的註釋,通常是給維護者看的，著重編寫理由及如何修改，該注意的問題等  
3. 使用tab/shift+tab左/右移動code  
4. 應講求方便閱讀  
5. 用utf-8進行編碼  
6. 對兩個浮點數進行相等判斷時，請小心處理  
7. char類型的底層為ACSII碼，因此為數值，也能夠進行運算。若以(int)強行轉換，將會輸出相應的unicode碼。
8. JAVA不能使用0 or 非0 表示boolean類型的true or false

char => int => long => float => double  
byte => short => int => long => float => double  
(byte,short)與char之間無法自動轉換  
* 請熟記JAVA的自動類型轉換，及精度小轉精度大(容量大小)  
* 以及自動提升原則 : 將表達式結果自動提升為容量最大的類型 
# 