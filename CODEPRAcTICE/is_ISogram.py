def is_isogram(string):
    str=string.lower()
    letter_list=[]
    for letter in str:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True
print(is_isogram(string=input("write the word here: ")))