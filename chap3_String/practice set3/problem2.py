# write a program to fill in a letter template given below with name and date.

letter =''' 
        Dear <|name|>,
         you are selected!
        <|Date|>
'''
print(letter.replace("<|name|>","Maheen").replace("<|Date|>","30-octuber-2023"))
