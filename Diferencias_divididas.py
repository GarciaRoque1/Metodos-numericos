import numpy as np
import pandas as pd
import os

def DiferenciasD():
    resp2=0
    while True:
    
        number_p= int(input("Ingrese el numero de puntos a usar(Nota: Deben de ser mas de 2 punto, sino no tendria tanto sentidos hacer tal operacion): "))
        while(number_p<=2):
            number_p= int(input("Ingrese un valor valido de puntos"))
        xi=["xi"]
        yi=["yi"]
        valx= 0.0
        valy= 0.0
        interx1=0.0
        interx2=0.0
        for i in range(number_p):
            valx= float(input(f"Valor de x{i} : "))
            xi.append(valx)
            valy= float(input(f"Valor de y{i} : "))
            yi.append(valy)
            
        table=[]
        for i in range(2):
            table.append([])
            
            for j in range(number_p+1):    
                if(i==0):
                    table[i].append(xi[j])
                elif(i==1):
                    table[i].append(yi[j])
                
        
        table1=np.array(table)
        table1=np.transpose(table1)
        while True:
            resp1=int(input("¿Son los datos correctos? (1->SI, 0->NO): "))
            if(resp1==0 or resp1==1):
                break
            else:
                print("Seleccione un valor valido") 
                
        if(resp1==0):
            table1=np.transpose(table1)
            while True:
                fila=int(input("Fila a corregir: "))
                if(fila<=number_p and fila>0):
                    break
                else:
                    print("Seleccione un valor valido")    
            
            valxa=float(input(f"Valor de x{fila} : "))
            valya=float(input(f"Valor de y{fila} : "))
            
            for j in range(fila+1):    
                if(j==fila):
                    table1[0, j]=valxa
                    table1[1, j]=valya
                        
            
            table1=np.transpose(table1)
            table1=np.delete(table1,0,axis=0)
            table1=np.asarray(table1,dtype=float)
            table1=table1[table1[:,0].argsort(kind='stable')]
            table1=np.asarray(table1,dtype=str)
            table1=np.insert(table1,0,("xi","yi"),axis=0)
            
        elif(resp1==1):
            table1=np.delete(table1,0,axis=0)
            table1=np.asarray(table1,dtype=float)
            table1=table1[table1[:,0].argsort(kind='stable')]
            table1=np.asarray(table1,dtype=str)
            table1=np.insert(table1,0,("xi","yi"),axis=0)
        
        listA=[]
        i=0
        j=1
        m=0
        n=0
        o=0
        s=2
        p=number_p-(number_p-s)
        senti=0
        senti2=0
        while(i<number_p):
            
            if(senti==1):
                while(True):
                    
                    n=len(listA)
                    
                    while(n<number_p):
                        listA=np.insert(listA,n,"NaN")
                        n+=1
                    
                    n+=1
                    m+=1
                    i=0
                    j+=1
                    senti=0
                    listA=np.insert(listA,0,o)
                    o+=1
                    listA=np.transpose(listA)
                    table1=np.insert(table1,s,listA,axis=1)
                    listA=np.transpose(listA)
                    s+=1
                    p=number_p-(number_p-s)
                    listA=[]
                    break
            
            while(j<=number_p-1):
                
                if((i+j+1)>number_p):
                    senti=1
                    break
                
                xi1= float( table1[i+1, 0] )
                xi2= float( table1[i+j+1, 0] )
            
                yi1= float( table1[i+1, m+1] )
                yi2= float( table1[i+2, m+1] )
            
                pend=(yi2-yi1)/(xi2-xi1)
            
                listA=np.insert(listA,i,pend)

                i=i+1
                
                if(i==number_p-1):
                    listA
                    break
                
                if(j==number_p):
                    break
            
            col=[0,0]
            col=np.array(col)
            col=np.shape(table1)
            col=list(col)
            col=np.array(col)
            col1= int( col[1] )
            if(col1>number_p):
                break
            
        i=i+1
        j+=1
        
        ord1=[]
        ord1=table1[1:, 0]
        ord1=np.array(ord1)
        ord1=np.asarray(ord1,dtype=float)
        interx1=max(ord1)
        interx2=min(ord1)
        
        poínt=0.0
        resp3=0
        while True:
        
            while(True):
                point=float(input(f"Punto a interpolar: "))
                if(point<=float(interx1) and point>=float(interx2)):
                    break
                else:
                    print("De el punto a interpolar sobre el intervalo de interes")
            
            fila1=[0,0]
            grade=int(input("Grado del polinomio(Nota: El polinomio resultante esta directamente relacionado con la tabla de coeficientes, \nes decir, si elige un grado cualquiera, entonces los coeficientes que se usan son elegidos a partir de la fila que se localizan,\n en donde la fila a usar esta determinado por el grado del polinomio, elija sabiamente el grado): "))
            while(True):
                if(grade>(number_p-1) or grade<=0):
                    print("Los puntos de la tabla no son suficientes para realizar el grado del polinomio o no eligio un valor valido")
                    grade=int(input("Elija nuevamente: "))
                else:
                    break     
            
            x_values=[]
            x_values=table1[1:, 0]
            x_values=np.array(x_values)
            while True:
                if((number_p-1) == grade):
                    break
                else:
                    zz=-(grade+2)
                    x_values=np.delete(x_values,zz)
                    sentencia=len(x_values)
                    if((sentencia) == (grade+1)):
                        break
                    else:
                        pass
                    
            x_values=np.asarray(x_values,dtype=float)
            
            polinomio=[]
            polinomio=table1[-(grade+1)]
            polinomio=np.array(polinomio)
            polinomio=np.delete(polinomio,0)
            z=0
            if('nan' in polinomio):
                n=np.where(polinomio == 'nan')
                if('nan' in polinomio):
                    while True:
                        polinomio=np.delete(polinomio, n[z])
                        if('nan' not in polinomio):
                            break
                        
            
            polinomio=np.asarray(polinomio,dtype=float)
                
            print(f"Tabla de diferencias: \n {table1}")
            table2=pd.DataFrame(table1, index=table1[0])
            print(table2)
            
            ind1=0
            result=0
            result1=1
            while True:
                termino=polinomio[ind1]
                if(ind1 == 0):
                    result= termino
                else:
                    result1*=(point-x_values[(ind1-1)])
                    result+= termino*result1
                
                if(grade == ind1):
                    break
                else:
                    ind1+=1
            
            print(f"\n\nResultado: {result}")
            while True:
                resp3=int(input("¿Desea interpolar otro punto con la misma tabla[Si->1, No->0]?: "))
                if(resp3 == 0):
                    senti3=0
                    break
                elif(resp3 == 1):
                    senti3=1
                    break
                else:
                    resp3=int(input("Eliga una opcion valida: "))
                    
            if(senti3==0):
                break
            elif(senti3==1):
                pass
        
        resp2=int(input("¿Que desea hacer ahora? \n1.-Cambiar los puntos de la tabla \n2.-Ir al menu de opciones \nEliga una opcion[1,2]: "))

        if(resp2==1 or resp2==0):
            if(resp2==1):
                pass
            if(resp2==0):
                break
        else:
            while True:
                resp2=int(input("De una opcion valida: "))
                if(resp2==1):
                    break
                elif(resp2==0):
                    break
                else:
                    pass
        if(resp2==1):
            os.system("cls")
            pass
        if(resp2==0):
            break
    
    
if __name__ == '__main__':
    DiferenciasD()