def Mbappe(x) :
    CR7 = []
    for Neymar in range(len(x) ):
        for Neuer in range(len(x[Neymar])) :
            if x[Neymar][Neuer]<10 :
                CR7.append(x[Neymar][Neuer])
    return(CR7)           
def main():
    lista = []
    fila = int(input())
    columna = int(input())
    for Neymar in range (fila) :
        lista.append([])
        for Neuer in range (columna) :
            Benzema = int(input())
            lista[Neymar].append(Benzema)
    Messi = Mbappe(lista)
    print(Messi)
   
if __name__=='__main__':
    main()
