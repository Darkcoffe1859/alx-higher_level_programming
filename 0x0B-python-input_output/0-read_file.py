#!/usr/bin/python


    """ function that reads a textfile and print on STDOUT

    """
     
     def read_file(filename=""):

         with open(filename, encoding = 'utf-8') as file:
             print(file.read(), end=''
