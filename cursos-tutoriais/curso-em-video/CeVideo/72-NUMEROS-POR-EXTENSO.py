numeros_escritos = "zero", "UM", "DOIS",  "TRES", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE"



num = int(input("numero "))

      
if len(str(num)) > 1:
    transformes = str(num)
    
    for i in range(len(transformes)):
        separado = int(transformes[i])    
      
        print(f'{numeros_escritos[separado]}', end=' ')
        
else:            
    print(numeros_escritos[num])


