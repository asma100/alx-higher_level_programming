#!/usr/bin/python3
"""module my list """
class MyList (list):
    """
    MyList is sub class
    """
    
    def print_sorted(self):
        """
        self :
        Returns : None
        """
        sorte = self[:]
        list.sort(sorte)
        print(sorte)
