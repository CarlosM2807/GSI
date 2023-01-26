### BUILDHASH
## Carlos Martín Sanz
## 4º Mención Computación

import sys, hashlib, os

# 1º Argumento --> Archivo del que vamos a leer las lineas a encriptar
# 2º Argumento --> Fichero de salida

entrada = sys.argv[1]
salida = sys.argv[2]

# Fichero de entrada en modo lectura
with open(entrada,'r') as fich:   

    # Fichero de salida en modo escritura 
    ficheroSalida = open(salida,'w')                                   

    # Leo linea a linea del fichero y sustituyo los retornos de carro por '' 
    for ruta in fich:                                          
        ruta = ruta.replace('\n', '')      

        # He indicado en el informe utilizo SHA-256 y el porque           
        hash = hashlib.sha256()

        # Ahora leemos la ruta en binario
        with open(ruta, 'rb') as binfile: 
            texto = 1                     
            while texto:

                    # Vamos leyendo
                    texto = binfile.read(1024) 
                    hash.update(texto)

                    # Genero el codigo hash de la ruta
                    textoHash = hash.hexdigest()                 
                                  

        # Obtengo las propiedades
        prop = os.stat(ruta)                                  
        prop = repr(prop).encode()

        # Codigo hash generado para las propiedades
        propHash = hash.hexdigest()     

        # Escribo en el fichero de salida la ruta, el hashd de la ruta, y hash de las propiedades                      
        ficheroSalida.write(ruta+';'+textoHash+';'+propHash+'\n') 

# Cierro el fichero      
ficheroSalida.close()

