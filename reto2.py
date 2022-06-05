def cliente (informacion:dict):
    
    boletaXT= 20000 
    boletaCC = 5000
    boletaSV = 10000
    
    if informacion['edad'] > 18:
        atraccion = "X-Treme"
        apto = True
        if informacion['primer_ingreso'] == True:
           boleta_total = boletaXT - (boletaXT * 0.05)
        else: 
            boleta_total = boletaXT
         
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = "Carros chocones"
        apto = True
        if informacion['primer_ingreso'] == True:
            boleta_total = boletaCC - (boletaCC * 0.07)
        else: 
            boleta_total = boletaCC  
   
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion ="Sillas voladoras"
        apto = True
        if informacion['primer_ingreso'] == True:
            boleta_total = boletaSV - (boletaSV * 0.05)
        else: 
            boleta_total = boletaSV
         
    else: 
        atraccion = 'N/A'
        apto = False
        boleta_total = 'N/A'
        
    datos = {
        "nombre" : informacion['nombre'],
        "edad" : informacion['edad'],
        "atraccion": atraccion,
        "apto": apto,
        "primer_ingreso": informacion['primer_ingreso'],
        "total_boleta": boleta_total
    }
    
    return datos
    
    
cliente1 = {'id_cliente':1,'nombre':'Johana Fernandez', 'edad': 20,'primer_ingreso': True}
cliente2 = {'id_cliente':1,'nombre':'Johana Fernandez', 'edad': 20,'primer_ingreso': False}
cliente3 = {'id_cliente':2,'nombre':'Gloria Suarez', 'edad': 3,'primer_ingreso': True}
cliente4 = {'id_cliente':3,'nombre':'Tatiana Suarez', 'edad': 17,'primer_ingreso': True}
cliente5 = {'id_cliente':3,'nombre':'Tatiana Suarez', 'edad': 17,'primer_ingreso': False}
cliente6 = {'id_cliente':4,'nombre':'Tatiana Ruiz', 'edad': 8,'primer_ingreso': True}
cliente7 = {'id_cliente':4,'nombre':'Tatiana Ruiz', 'edad': 8,'primer_ingreso': False}

print(cliente(cliente1))
print(cliente(cliente2))
print(cliente(cliente3))
print(cliente(cliente4))
print(cliente(cliente5))
print(cliente(cliente6))
print(cliente(cliente7))

    


        