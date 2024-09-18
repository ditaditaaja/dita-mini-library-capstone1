Hi I’m Dita and this is my first ever project in stepping into a whole new world called Data Science. This program was created as Capstone project of 1st Modul in Data Science by Purwadhika. Fairly far from perfect, some might see all codes in here as inefficient as well, but this is my take as a beginner on understanding all regular functions in Python and I hope you can forgive that :D. I will also feel very lucky if you willing to give some valuable inputs. In the end of this road, hopefully I can look back on this and make amend with better coding approach. Anyway, lets jump right in!

This program was created with Python in Visual Studio for my mini library interfaced in Bahasa Indonesia (however, I also acknowledged that some keys are in English, pardon my confused minds). I try to create program with CRUD functionalities. Besides, I also try to make something that I feel similar to what I usually used in campus library system, hence, you will find it split into two menus: for Members and Administrators. 
Basically, Members only able to read and search all books collection, while Administrators can modify through it. Both members and administrators are required to input personal ID. I do have in mind to connect this ID to other database that will verify you before you can going through the system, but that is another room for improvement next time.

Let’s dissect the feature one by one.
1.	Showing all books collection
All books collection are hard coded in the program and not connected to any clouds or databases. Hence, all additions and amendments that was made only exist while the program running. After every turn off, collections will restart to initial collection. After done running the function, system will always ask you whether you want to get back to main menu or user menu (members/admins).
Codes notes: sets of data was created with list and presented in table with the help of tabulate (thanks to my mentor who suggesting tabulate). In here, SN served as primary key, so every title per author will have specific SN.
2.	Finding books collection
Users will have 5 different options to search, which is by SN, Title, Author, Language, and Status.
a.	Search by SN
b.	Search by Title
c.	Search by Author
d.	Search by Language
e.	Search by status
System will give feedback on what its defined as incorrect input, whether it does not exist, only input partially, or input was not initially defined. Another room for improvement is on how system can be more flexible on the case of partial title or author input.
Codes notes: in ‘find’ function, I mainly use for loop, if else, append, and continue function.

3.	Adding new collection
Program will be able to add one book collection at a time for new book collection that is never listed before. Once succeed, program will show all books collection with adding new collection shown in the last. To ensure no duplication, program will verify by SN and ask you to reinput new SN.
It is also apply on the case of title duplication after you input new SN.
As long as program does not get turn off, additions are visible to read and show function.
Codes notes: in ‘adding; function, I mainly use for loop, if else, and global function.

4.	Updating collection 
All information in columns is changeable, hence 5 changing options provided. By Title, Author, Language, quantity, and Status.
System will work based on SN and verify whether SN is available in the collections. 
As long as program does not get turn off, modifications are all visible to read and show function.
For error input, programs will give you feedback.
 
5.	Erasing collection
Program able to erase collection one collection at a time. As of now, it only able to delete collection based on SN, however it can be improved based on title or other information next time. If SN input incorrectly, program will give you feedback.
 




