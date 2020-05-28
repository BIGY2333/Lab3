*Yao_Wangze  Sun_wei*

*laboratory work number ———— 1*

*variant description：  Lazy single-linked lists by closures ：In this variant, you should implement a lazy library for a single-linked list. For that, you should use closures. Usage of generators (yield statement) or async (async, await statements) is not allowed. *

## synopsis ##
In this lab,we should implement a lazy library for a single-linked list.And we need to design several APIs for this singly linked list. In addition, we need to verify the unit to verify the test, and also verify his laziness

## contribution summary for each group member ##

Yaowangze's contribution：Completed the implementation of the Lazy single-linked lists by closures

Sunwei's contribution：Design the test unit and test 

## explanation of taken design decisions and analysis ##
We implement a lazy library for a single-linked list.The basis of closures is that the language level allows functions to be nested, that is, a function body can contain another function, and allows the function to be returned as a return value.  The appearance of closures in Python emphasizes the delay in obtaining results, which is consistent with the characteristics of lazy computing.


## operation result ##
![Alt text](/fig/1.png)