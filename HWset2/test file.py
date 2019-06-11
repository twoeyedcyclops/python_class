# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:15:19 2019

@author: kevin
"""
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    alphabet=string.ascii_lowercase
    modalphabet=list(alphabet)
    for char1 in alphabet:
        for char2 in letters_guessed:
            if char1==char2:
                
                modalphabet.remove(char1)
    letters_available=''.join(modalphabet)  
    return letters_available

letters_guessed=['e','i','k','p','r','s'] 
print(get_available_letters(letters_guessed))  