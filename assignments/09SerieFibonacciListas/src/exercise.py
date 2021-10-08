def main():
    a = -1
    x = 1
    y = 1
    s = 0
    lista = []
    while a <= -1 :
        a = int(input())
    if a == 0 :
        print(lista)
    elif a==1 :
        lista.append(0)
        print(lista)
    elif a==2 :
        lista.append(0)
        lista.append(1)
        print(lista)
    else :
        lista.append(0)
        lista.append(1)
        lista.append(1)
        for i in range(a-3) :
            s = x + y
            y = x
            x = s
            lista.append(s)
        print(lista)

if __name__=='__main__':
    main()
