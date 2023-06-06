#!/usr/bin/python3


"""


The module contains function that prints a text indentation


"""
def text_indentation(text):
    """ the function prints a text and 2 new lines after each of the characters (. , ? and :)
    
    Args:
        text (int): represent the text to be printed

    Raises:
        TypeError: If text is not a string
        
        """
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1

