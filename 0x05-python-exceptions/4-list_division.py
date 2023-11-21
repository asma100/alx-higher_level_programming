#!/usr/bin/python3
    
       
    def list_division(my_l_1, my_l_2, list_length):
    x = []

    for i in range(list_length):
        try:
            div_re = my_l_1[i] / my_l_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_re = 0
        except TypeError:
            print("wrong type")
            div_re = 0
        except IndexError:
            print("out of range")
            div_re = 0
        finally:
            x.append(div_re)

    return x
