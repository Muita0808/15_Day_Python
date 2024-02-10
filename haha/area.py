#!/usr/bin/python3
def arearec(leng=0, wid=0):
    if type(leng) is not int or type(wid) is not int:
        raise TypeError
    else:
        return (leng * wid)
