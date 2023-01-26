### BUILDHASH
## Carlos Martín Sanz
## 4º Mención Computación

import sys, hashlib, os

# 1º Argumento --> Archivo del que vamos a leer las lineas a encriptar
# Salida --> indica la modificacion o no por consola

entrada = sys.argv[1]

# Fichero de entrada en modo lectura
with open(entrada,'r') as fich:

        # Leo linea a linea del fichero y sustituyo los retornos de carro por '' 
    for ruta in fich:                                          
        ruta = ruta.replace('\n', '')  

        # En partes almaceno cada parte separada por ;
        # partes[0] = ruta fichero, partes[1] = codigo hash fichero, partes[2] = propiedades fichero
        partes = ruta.split(";")

        # Utilizo la misma funcion que he usado en BUILDHASH.py          
        hash = hashlib.sha256()

        # Generar el codigo hash de la ruta que hay en el fichero
        with open(partes[0], 'rb') as binfile: 
            texto = 1                     
            while texto:

                 # Vamos leyendo
                texto = binfile.read(1024) 
                hash.update(texto)

                # Genero el codigo hash de la ruta
                textoHash = hash.hexdigest()
        
        # Obtengo las propiedades
        prop = os.stat(partes[0])                                  
        prop = repr(prop).encode()

        # Codigo hash generado para las propiedades
        propHash = hash.hexdigest()     

        # Condiciones modificacion 
        
        if(textoHash != partes[1]):
            print("Se ha modificado el fichero")
        if(propHash != partes[2]):
            print("Se ha modificado las propiedades del fichero")
        if(propHash != partes[2] and textoHash != partes[1]):
            print("Se han modificado tanto el archivo como sus propiedades")
        else: 
            print("No se ha modificado ni el archivo ni las propiedades")