#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
       
        nb_print = 0
        i = 0

       
        while nb_print < x and i < len(my_list):
           
            if isinstance(my_list[i], int):
               
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1

   
            i += 1

       
        print()

        
        return nb_print

    except IndexError:
        
        raise
