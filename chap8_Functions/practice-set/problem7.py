# write a python function to remove a given word from a list ad strip it at the same time.


def word(list_word,x):
    n = []

    for item in list_word:
        if not(item == x):
            n.append(item.strip(x))
        return n

list_word = ["Maheen", "advice", "admire", "admit"]
    
print(word(list_word,"an"))