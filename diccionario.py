#diccionario:
#colección de datos
#los almacena en pares
#clave - valor
#un diccionario comienza y termina
#con llaves (curly braces)
#la clave se separa del valor
#cada elemento (propiedad) del
#diccionario se separa por una coma.

#ejemplo

pais1 = {
            'nombre': 'Argentina',
            'capital': 'Buenos aires',
            'moneda' : 'peso argentino',
            'ciudades': [
                        "Cordoba",
                        "Rosario",
                        "Mendoza"
                ],
            'poblacion': {
                "censo": 46,
                "densidad": 16
            }
        }

pais2 = {
            'nombre': 'Ecuador',
            'capital': 'Quito',
            'moneda' : 'Dolar',
            'ciudades': [
                            "Cordoba",
                            "Rosario",
                            "Mendoza"
                        ],
            'poblacion': {
                "censo": 46,
                "densidad": 16
            }
        }

pais3 = {
            'nombre': 'Paraguay',
            'capital': 'Asunción',
            'moneda' : 'Guaraní',
            'ciudades': [
                            "Luque",
                            "Lambaré",
                            "Limpio",
                            "Itaguá",
                            "Caaguazú"
                        ],
            'poblacion': {
                "censo": 46,
                "densidad": 16
            }
        }
#acceder a la info
print(pais2 ['nombre'])
print(pais1 ['ciudades'])
print(pais2 ['moneda'])

for ciudad in pais1 ['ciudades']:
    print ("censo", pais1['poblacion']['censo'], "millones de habitantes")
    print (
        "densidad: ",
        pais1['poblacion']['densidad'], "por km2" 
    )