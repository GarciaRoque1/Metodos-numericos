import numpy as np
import os
import matplotlib.pyplot as mpl

def Spline():
    while True:
        
        number_p= int(input("Ingrese el numero de puntos a usar(Nota: Deben de ser mas de 4 punto, sino no tendria tanto sentidos hacer tal operacion): "))
        while(number_p<=3):
            number_p= int(input("Ingrese un valor valido de puntos"))
            
        xi=["xi"]
        yi=["yi"]
        valx= 0.0
        valy= 0.0
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
            print("\n")
            print(table1)
            resp1=int(input("¿Son los datos correctos? (Luego los datos seran ordenados para su mejor manejo, asi que no se preocupe si no los dejo en orden) (1->SI, 0->NO): "))
            if(resp1==0 or resp1==1):
                break
            else:
                print("Seleccione un valor valido") 
                
        if(resp1==0):
            while True:
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
                print(f"Valor x{fila} corregido")
                resp2=int(input("¿Desea corregir mas datos? (1->SI, 0->NO): "))
                veri1=0
                while True:
                    if(resp2==1 or resp2==0):
                        if(resp2==1):
                            veri1=1
                            break
                        elif(resp2==0):
                            veri1=0
                            break
                    else:
                        resp2=int(input("Seleccione una opcion valida"))
                if(veri1==1):
                    continue
                elif(veri1==0):
                    break
            
        elif(resp1==1):
            table1=np.delete(table1,0,axis=0)
            table1=np.asarray(table1,dtype=float)
            table1=table1[table1[:,0].argsort(kind='stable')]
            table1=np.asarray(table1,dtype=str)
            table1=np.insert(table1,0,("xi","yi"),axis=0)
            
        hi=[]
        difdiv=[]
        ordx=[]
        ordy=[]
        aux1=0
        aux2=0
        ordx=table1[1:, 0]
        ordy=table1[1:, 1]
        ordx=np.asarray(ordx,dtype=float)
        ordy=np.asarray(ordy,dtype=float)
        for i in range(number_p):
            if(i<number_p-1):
                hi.append(ordx[i+1]-ordx[i])
                difdiv.append((ordy[i+1]-ordy[i])/hi[i])
                continue
            else:
                break
            
            
        hi=np.array(hi)
        difdiv=np.array(difdiv)
        hi1=hi
        difdiv1=difdiv
        hi1=np.transpose(hi1)
        difdiv1=np.transpose(difdiv1)
        print("hi's: \n")
        print(hi1)
        print("Diferencias Divididas: \n")
        print(difdiv1)
        n=number_p-1
        necua1=n-1
        izq=0
        der=number_p-3
        k=0
        l=0
        A=[]
        for i in range(necua1):
            A.append([])
            
            for j in range(number_p):    
                if(i==0):
                    A[i].append(hi[j])
                    A[i].append((2*(hi[j]+hi[j+1])))
                    A[i].append(hi[j+1])
                    while True:
                        k+=1
                        A[i].append(0.0)
                        if(k==der):
                            break
                        
                    izq+=1
                    der-=1
                    k=0
                    break
                elif(i!=0):
                    while True:
                        l+=1
                        A[i].append(0.0)
                        if(l==izq):
                            break
                    
                    A[i].append(hi[j])
                    A[i].append((2*(hi[j]+hi[j+1])))
                    A[i].append(hi[j+1])
                    
                    while True:
                        if(k<der):
                            k+=1
                            A[i].append(0.0)
                            if(k==der):
                                break
                        else:
                            break
                    
                    izq+=1
                    der-=1
                    k=0
                    l=0
                    break
        A=np.array(A)
        A=np.delete(A,0,axis=1)
        A=np.delete(A,len(A),axis=1)
        B=[]
        for i in range(necua1):
            B.append(6*(difdiv[i+1]-difdiv[i]))
        
        B=np.array(B)

        X0=[]
        for i in range(necua1):
            X0.append(1.0)
            
        X0=np.array(X0)

        tolera = 0.00000000000000000001
        iteramax = 100

        # PROCEDIMIENTO

        # Gauss-Seidel
        tamano = np.shape(A)
        n = tamano[0]
        m = tamano[1]
        #  valores iniciales
        X = np.copy(X0)
        diferencia = np.ones(n, dtype=float)
        errado = 2*tolera

        itera = 0
        while not(errado<=tolera or itera>iteramax):
            # por fila
            for i in range(0,n,1):
                # por columna
                suma = 0 
                for j in range(0,m,1):
                    # excepto diagonal de A
                    if (i!=j): 
                        suma = suma-A[i,j]*X[j]
                
                nuevo = (B[i]+suma)/A[i,i]
                diferencia[i] = np.abs(nuevo-X[i])
                X[i] = nuevo
            errado = np.max(diferencia)
            itera = itera + 1

        # Respuesta X en columna
        X = np.transpose([X])

        # revisa si NO converge
        if (itera>iteramax):
            X=0
        # revisa respuesta
        verifica = np.dot(A,X)

        # SALIDA
        """
        print('respuesta X: ')
        print(X)
        """
        """
        print('verificar A.X=B: ')
        print(verifica)
        """
        X=np.asarray(X,dtype=float)
        X=np.transpose(X)
        X1=X[0]
        X=np.transpose(X)
        Si=[]
        Si.append(0.0)
        i=0
        while True:
            aux=X1[i]
            Si.append(aux)
            i+=1
            if(i>=len(X1)):
                break
        Si.append(0.0)
        Si=np.array(Si)
        Si=np.asarray(Si,dtype=float)
        
        Ai=[]
        Bi=[]
        Ci=[]
        
        for i in range(number_p-1):
            Ai.append((Si[i+1]-Si[i])/(6*hi[i]))
            Bi.append((Si[i]/2))
            Ci.append(((difdiv[i])-((Si[i+1]+2*Si[i])/(6))*hi[i]))
            
        i=1
        j=0
        interx=[]
        xin=0
        print("Conjunto de polinomios que pasan por el intervalo:")
        a=[]
        while True:
            a.append(f"g{i}(x)={Ai[i-1]}(x-{table1[i][0]})^3 + {Bi[i-1]}(x-{table1[i][0]})^2 + {Ci[i-1]}(x-{table1[i][0]}) + {table1[i][1]}    si {table1[i][0]} <= x <= {table1[i+1][0]}")
            interx.append(table1[i][0])
            i+=1
            j+=1
            if(i==number_p):
                interx.append(table1[i][0])
                break
        a=np.transpose(a)
        print(a)
        print("\n Grafica del Splin Cubico\n")
        i=0
        aux3=0
        aux4=0
        aiaux=0
        biaux=0
        ciaux=0
        xiaux=0
        yiaux=0
        while True:
            aux3=float(interx[i])
            aux4=float(interx[i+1])
            aiaux=float(Ai[i])
            biaux=float(Bi[i])
            ciaux=float(Ci[i])
            xiaux=float(table1[i+1][0])
            yiaux=float(table1[i+1][1])
            xin=np.linspace(aux3, aux4,10,dtype=float)
            mpl.plot(xin,[aiaux*(x-xiaux)**3 + biaux*(x-xiaux)**2 + ciaux*(x-xiaux) + yiaux for x in xin], 'r', label=f"g(x)={Ai[i-1]}(x-{table1[i][0]})**3 + {Bi[i-1]}(x-{table1[i][0]})**2 + {Ci[i-1]}(x-{table1[i][0]}) + {table1[i+1][1]}    si {table1[i+1][0]} <= x <= {table1[i+2][0]}")
            i+=1
            if(i==number_p-1):
                """
                aux3=float(interx[i])
                aux4=float(interx[i+1])
                aiaux=float(Ai[i])
                biaux=float(Bi[i])
                ciaux=float(Ci[i])
                xiaux=float(table1[i+1][0])
                yiaux=float(table1[i+1][1])
                xin=np.linspace(aux3, aux4,10,dtype=float)
                mpl.plot(xin,[aiaux*(x-xiaux)**3 + biaux*(x-xiaux)**2 + ciaux*(x-xiaux) + yiaux for x in xin], 'r')
                """
                break

        mpl.legend(bbox_to_anchor=(0., 1.02, 2.5, .302), loc='lower left',ncol=1, mode="expand", borderaxespad=0.)
        mpl.grid()
        mpl.show()
        resp3=0      
        print(" --- Nota, si no lee una entrada despues de mostrar la grafica, solo debe de entrar en el entorno de ejecucion que se encuantra arriba del la barra de opciones y dar click en reiniciar y ejecutar todo --- ")
        resp3=int(input("¿Desea realizar otro ajuste con otra tabla[Si->1, No->0]?: "))
        if(resp3 == 0):
            senti3=0
        elif(resp3 == 1):
            senti3=1
        else:
            while True:
              resp3=int(input("Eliga una opcion valida: "))
              if(resp3 == 0):
                senti3=0
                break
              elif(resp3 == 1):
                senti3=1
                break
              else:
                pass
                        
        
        if(senti3==0):
            os.system("cls")
            break
        elif(senti3==1):
            os.system("cls")
            continue
        
    print("Vuelva pronto")
    os.system("cls")

if __name__ == '__main__':
    print("Universidad Nacional Autonoma de Mexico")
    print("Grupo: 2401")
    print("Participantes:")
    print("Garcia Roque Andres Yair")
    print("Rodriguez Peña Atziri Alejandra")
    print("Guodge Moncada Marian")
    print("Quiñones Valles Pamela")
    print("Grupo: 2401")
    print("\n\nSpline Cubico Metodos Numericos II")
    Spline()