def Reverse(resw): 
    w = resw.split(' ')
    chg = ' '.join(reversed(w))
    return chg  
if __name__ == "__main__": 
    sw = 'geeks quiz practice code'
    print(sw)
    print()
    print(Reverse(sw))
    print()