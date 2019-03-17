def check_proposition(list):
    x=[]
    for el in list:
        if el%2 is 0 and el>0 and el<=50:
            x= el
            break
    for el in list :
        if el*2 is x and el>0 and el<=50:
            return True
    return False