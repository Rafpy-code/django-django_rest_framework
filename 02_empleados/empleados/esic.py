# num1 = input('Ingrese el primer número: ')
# num2 = input('Ingrese el segundo número: ')
# suma = int(num1) + int(num2)
# print('La suma de los dos números es:', suma)

# ====================================

# Determinar su un número es positivo, negativo o cero
# num = int(input('Ingrese un número: '))
# if num > 0:
#     print('El número es positivo')
# elif num < 0:
#     print('El número es negativo')
# else:
#     print('El número es cero') 

# El mayor de 3 números
# numeros = input("Ingrese 3 números separados por espacios: ").split()

# ==================================

# # Convierte los valores ingresados a enteros
# num1, num2, num3 = int(numeros[0]), int(numeros[1]), int(numeros[2])

# ==================================

# # Operadores ternarios para encontrar el mayor de los tres números
# mayor = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
# # Verifica si hay dos o tres números iguales
# if num1 == num2 == num3:
#     print("Los tres números son iguales.")
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print(f"El mayor número es: {mayor}, y hay números iguales.")
# else:
#     print(f"El mayor número es: {mayor}")

# ==================================

# # Verificar si un número es par o impar
# num = int(input('Ingrese un número: '))
# if num % 2 == 0:
#     print('El número es par')
# else:
#     print('El número es impar')

# ==================================

# Imprimir los 10 primeros numeros usando un bucle while
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# ==================================

# Calcular la suma de los numeros de una lista
# numeros = [numero for numero in range(30)]  # Lista de números
# print(numeros)
# suma = 0
# for num in numeros:
#     suma += num
# print('La suma de los números es:', suma)

# ==================================

# Contar cuantas veces aparece un elemento en una lista
# lista = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
# elemento = 1
# contador = 0
# for num in lista:
#     if num == elemento:
#         contador += 1
# print(f'El elemento {elemento} aparece {contador} veces en la lista')

# ==================================

# # Calculadora básica usando match case
# def calculadora_basica():
#     num1 = float(input('Ingrese el primer número: '))
#     num2 = float(input('Ingrese el segundo número: '))
#     operacion = input('Ingrese la operación (+, -, *, /): ')
    
#     match operacion:
#         case '+':
#             return num1 + num2
#         case '-':
#             return num1 - num2
#         case '*':
#             return num1 * num2
#         case '/':
#             try:
#                 num1 / num2
#             except ZeroDivisionError as zde:
#                 return f"No se puede dividir por cero. -> {zde}"
#             return num1 / num2
#         case _:
#             return "Operación no válida"
        
# print(calculadora_basica())

# ==================================

# # Función que lea un archivo y cuente las palabras controlando errores
# def contar_palabras(archivo):
#     try:
#         with open(archivo, 'r') as file:
#             contenido = file.read()
#             palabras = contenido.split()
#             return len(palabras)
#     except FileNotFoundError:
#         return f"El archivo {archivo} no existe."
#     except Exception as e:
#         return f"Ocurrió un error: {e}"
    
# print(contar_palabras('archivo_palabras.txt'))

# ==================================

# Funcion para escribir un archivo ingresando el nombre del archivo y texto por la consola, controlar si el archivo existe, además controlar que los campos no estén vacios y controlar los posibles errores
def escribir_archivo():
    import os
    try:
        # Solicitar el nombre del archivo, se repetirá hasta que no esté vacío
        nombre_archivo = ""
        while not nombre_archivo:
            nombre_archivo = input("Ingresa el nombre del archivo: ").strip()
            if not nombre_archivo:
                print("El nombre del archivo no puede estar vacío. Por favor, inténtalo de nuevo.")
        # Agrego la extensión al archivo
        nombre_archivo += ".txt"        
        # Verificar si el archivo ya existe
        if os.path.exists(nombre_archivo):
            print(f"El archivo '{nombre_archivo}' ya existe.")
            respuesta = input("¿Quieres sobrescribirlo? (s/n): ").strip().lower()
            if respuesta != 's':
                print("Operación cancelada.")
                return

        # Solicitar el texto para escribir en el archivo, se repetirá hasta que no esté vacío
        texto = ""
        while not texto:
            texto = input("Ingresa el texto para escribir en el archivo: ").strip()
            if not texto:
                print("El texto no puede estar vacío. Por favor, inténtalo de nuevo.")
        
        # Escribir en el archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(texto)
        
        print(f"El archivo '{nombre_archivo}' ha sido escrito con éxito.") 
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

# Llamar a la función
# escribir_archivo()

# ==================================

# Crear un servidor socket
def crear_socket():
    import socket
    try:
        # Crear un socket
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket creado correctamente.")

        # Asignar ip y puerto
        servidor_socket.bind(('localhost', 8000)) 

        # Escuchar conexiones
        servidor_socket.listen(5)
        print("Servidor escuchando en localhost:8000")

        # Bucle infinito para aceptar conexiones
        while True:
            # Aceptar conexiones
            print("Esperando conexiones...")
            cliente_socket, direccion = servidor_socket.accept()
            print(f"Conexión establecida desde {direccion}")
            # Enviar un mensaje al cliente
            cliente_socket.sendall(b'Hola cliente, desde el servidor!')
            # Cerrar la conexión
            cliente_socket.close()

            return servidor_socket
    except socket.error as e:
        print(f"Error al crear el socket: {e}")
        return None

# Llamar a la función
# crear_socket()

# ==================================
    
# Crear un socket de tipo TCP/IP
def escanear_puertos():
    import socket
    try:
        # Crear un socket
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket TCP creado correctamente.")

        # Solicitar al usuario que ingrese la dirección IP
        direccion_ip = input("Ingrese la dirección IP a escanear: ")

        # Solicitar al usuario que ingrese el rango de puertos a escanear
        rango_puertos = input("Ingrese el rango de puertos a escanear (ejemplo: 80-100): ")
        inicio, fin = map(int, rango_puertos.split('-'))

        # Escanear los puertos
        for puerto in range(inicio, fin + 1):
            try:
                socket_tcp.connect((direccion_ip, puerto))
                print(f"El puerto {puerto} está abierto.")
            except socket.error:
                print(f"El puerto {puerto} está cerrado o no existe.")

        # Cerrar el socket
        socket_tcp.close()
    except socket.error as e:
        print(f"Error al crear el socket: {e}")

# Llamar a la función
# escanear_puertos()

# ==================================

# Sniffer con scapy y además guardar los resultados en un archivo
def sniffer(nombre_archivo="resultados_sniffer.txt"):
    import scapy.all as scapy
    try:
        # Crear un objeto de captura
        captura = scapy.sniff(count=10)  # Capturar 10 paquetes

        # Abrir (o crear) el archivo donde se escribirán los resultados
        with open(nombre_archivo, 'w') as archivo:
            # Iterar sobre los paquetes capturados
            for paquete in captura:
                resumen = paquete.summary()
                print(resumen)  # Imprimir en consola (opcional)
                archivo.write(resumen + "\n")  # Escribir cada paquete en el archivo
            
        print(f"Resultados escritos en {nombre_archivo}")
    
    except Exception as e:
        print(f"Error al capturar paquetes: {e}")

# Llamar a la función para probar
# sniffer()


# Función para escribir los resultados de sniffer en un archivo
# def escribir_resultados(resultados):
#     try:
#         with open("resultados_sniffer.txt", "w") as archivo:
#             archivo.write(resultados)
#         print("Resultados guardados en 'resultados_sniffer.txt'")
#     except Exception as e:
#         print(f"Error al guardar los resultados: {e}")


# ==================================

# Funcíon para mostrar la información de los paquetes capturados
from scapy.all import sniff
def mostrar_paquetes(paquete):    
    paquete.show()

# sniff(prn=mostrar_paquetes, count=10)

# ==================================

# Función para hacer ping
def hacer_ping(direccion_ip):
    from scapy.all import sr1, IP, ICMP
    paquete_ping = IP(dst=direccion_ip) / ICMP()
    respuesta = sr1(paquete_ping, timeout=5, verbose=False)
    if respuesta is None:
        print(f"No se recibió respuesta de {direccion_ip}")
    else:
        print(f"Respuesta recibida de {direccion_ip}")
        print(respuesta.show())
        print(respuesta.summary())
        print(respuesta.src)
        print(respuesta.dst)
        print(respuesta.id)
        print(respuesta.seq)
        print(respuesta.ttl)
        print(respuesta.data)
        print(respuesta.chksum)
        print(respuesta.len)
        print(respuesta.version)
        print(respuesta.ihl)
        print(respuesta.tos)
        print(respuesta.flags)
        print(respuesta.frag)
        print(respuesta.ttl)
        print(respuesta.proto)
        print(respuesta.opts)
        print(respuesta.length)
        print(respuesta.version)

# ==================================

# Función para obtener información del sistema operativo
def obtener_informacion_sistema():
    import os
    import platform
    try:
        informacion = {
            "sistema_operativo": platform.system(),
            "nodo": platform.node(),
            "version_sistema": platform.release(),
            "version_python": platform.python_version(),
            "arquitectura": platform.machine(),
            "procesador": platform.processor(),
            "nombre_usuario": os.getenv("USERNAME") or os.getenv("USER"),
            "directorio_actual": os.getcwd(),
            "lista_directorios": [d for d in os.listdir(".") if os.path.isdir(d)],
            "lista_archivos": [a for a in os.listdir(".") if os.path.isfile(a)],
            "puertos_abiertos": [p for p in range(1024) if os.path.exists(f"/proc/{p}/status")],            
        }
        return informacion
    except Exception as e:
        print(f"Error al obtener información del sistema: {e}")
        return None
    

    # ==================================

# Función para obtener información de una URL
def obtener_informacion_url(url):
    import requests
    import socket
    from urllib.parse import urlparse

    if not url.startswith("http://", "https://"):
        url = "http://" + url

    try:
        # Obtener la información de la URL
        respuesta = requests.get(url)
        codigo_estado = respuesta.status_code
        encabezados = respuesta.headers
        direccion_ip = socket.gethostbyname(urlparse(url).hostname)
        parsed_url = urlparse(url)
        dominio = parsed_url.netloc

        #
        try:
            requests.get("https" + dominio)
            url_segura = True
            print("La URL es segura")
        except requests.exceptions.SSLError:
            url_segura = False
            print("La URL no es segura")


        # Imprimir la información
        print(f"Código de estado: {codigo_estado}")
        print(f"Encabezados: {encabezados}")
        print(f"Dirección IP: {direccion_ip}")
        print(f"URL: {url}")
        print(f"Protocolo: {urlparse(url).scheme}")
        print(f"Dominio: {dominio}")
        print(f"URL segura: {url_segura}")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener información de la URL: {e}")
        return None
    
# ==================================

# Función para obtener información de una IP
def obtener_informacion_ip(ip):
    import requests
    try:
        # Obtener la información de la IP
        direccion_ip = ip
        respuesta = requests.get(f"XXXXXXXXXXXXXXXXXXXXXXX{ip}")
        datos = respuesta.json()
        pais = datos["country"]
        ciudad = datos["city"]
        region = datos["regionName"]
        latitud = datos["lat"]
        longitud = datos["lon"]
        codigo_postal = datos["zip"]
        zona_horaria = datos["timezone"]
        isp = datos["isp"]
        organizacion = datos["org"]
        as_ = datos["as"]

        # Obtener la dirección IP pública
        ip_publica = requests.get('XXXXXXXXXXXXXXXXXXXXX').text

        # Obtener la ubicación geográfica
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip)
        ubicacion_geografica = response.location

        # Imprimir la información
        print(f"Dirección IP: {direccion_ip}")
        print(f"Pais: {pais}")
        print(f"Ciudad: {ciudad}")
        print(f"Region: {region}")
        print(f"Latitud: {latitud}")
        print(f"Longitud: {longitud}")
        print(f"Codigo postal: {codigo_postal}")
        print(f"Zona horaria: {zona_horaria}")
        print(f"ISP: {isp}")
        print(f"Organizacion: {organizacion}")
        print(f"AS: {as_}")
        print(f"IP pública: {ip_publica}")
        print(f"Ubicacion geografica: {ubicacion_geografica}")

        return datos
    except Exception as e:
        print(f"Error al obtener información de la IP: {e}")
        return None
    
# ==================================

# Función para listar las aplicaiones instaladas en el sistema linux
def listar_aplicaciones_linux():
    import os
    try:
        # Obtener la lista de aplicaciones instaladas
        aplicaciones = [a for a in os.listdir("/usr/bin") if os.path.isfile(f"/usr/bin/{a}")]
        return aplicaciones
    except Exception as e:
        print(f"Error al listar las aplicaciones: {e}")
        return None
    
# ==================================

# Función para listar las aplicaciones instaladas en el sistema windows
def listar_aplicaciones_windows():
    import winreg
    claves_registro = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    aplicaciones = []

    try:
        for clave in claves_registro:
            # Abrir la clave de registro en la ubicación especificada
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, clave) as key:
                # Iterar sobre todas las subclaves de la clave abierta
                for i in range(0, winreg.QueryInfoKey(key)[0]):
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            # Leer el valor "DisplayName" de cada subclave (nombre de la aplicación)
                            app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            aplicaciones.append(app_name)
                        except FileNotFoundError:
                            # Si no hay "DisplayName" en la subclave, ignorar
                            continue
    except Exception as e:
        print(f"Error al acceder al registro: {e}")
        return

    # Imprimir y devolver las aplicaciones encontradas
    for app in aplicaciones:
        print(app)
    
    return aplicaciones

# Llamar a la función   
#listar_aplicaciones_windows()

# ==================================

def listar_aplicaciones_con_powershell():
    import subprocess
    try:
        # Comando de PowerShell para listar las aplicaciones instaladas
        comando = 'powershell "Get-WmiObject -Class Win32_Product | Select-Object -Property Name Version Vendor"'
        
        # Ejecutar el comando y capturar la salida
        resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)

        # Verificar si el comando se ejecutó correctamente
        if resultado.returncode != 0:
            print("Error al ejecutar el comando PowerShell")
            return
        
        # Mostrar el resultado en la consola
        print(resultado.stdout)
    except Exception as e:
        print(f"Error al ejecutar el comando PowerShell: {e}")

# Llamar a la función
#listar_aplicaciones_con_powershell()

# ==================================
import subprocess
def programas_instalados_pipes():
    try:
        comando = 'powershell "Get-WmiObject -Class Win32_Product | Select-Object -Property Name, Version, Vendor"'
        result = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        error = result.stderr.strip()
        
        print(f"{f'Error: {error}' if error else f'Lista de programas instalados: \n{output}'}")
    
    except Exception as e:
        print(f"Error al intentar obtener los programas: {e}")

# if __name__ == "__main__":
#     print("Obteniendo lista de programas instalados...")
#     programas_instalados_pipes()

# ==================================

def listar_aplicaciones_con_wmic():
    import subprocess
    try:
        # Comando de PowerShell para listar las aplicaciones instaladas
        comando = 'wmic product get name, version, vendor'

        # Ejecutar el comando y capturar la salida
        resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)

        # Verificar si el comando se ejecutó correctamente
        if resultado.returncode != 0:
            print("Error al ejecutar el comando wmic")
            return

        # Mostrar el resultado en la consola
        print(resultado.stdout)
    except Exception as e:
        print(f"Error al ejecutar el comando wmic: {e}")

# listar_aplicaciones_con_wmic()

# ==================================

def sumar_numeros_controlado():
    correcto = False
    while not correcto:
        try:
            # Pedir el primer número
            num1 = float(input("Ingresa el primer número: "))
            while True:
                try:
                    # Pedir el segundo número
                    num2 = float(input("Ingresa el segundo número: "))
                    break
                except ValueError:
                    print("Error: Por favor, ingresa solo números.")
            
            # Sumar los números
            resultado = num1 + num2
            
            # Devolver el resultado
            print(f"El resultado de la suma es: {resultado}")
            correcto = True
        
        except ValueError:
            # Si el usuario ingresa algo que no es un número
            print("Error: Por favor, ingresa solo números.")
        
        except Exception as e:
            # Para cualquier otro tipo de error no esperado
            print(f"Ha ocurrido un error inesperado: {e}")

# Llamar a la función
#sumar_numeros_controlado()

# ==================================

def pedir_numero(mensaje):
    while True:
        try:
            # Pedir el número y convertirlo a float
            numero = float(input(mensaje))
            return numero  # Si se ingresa un número, salimos del ciclo y retornamos
        except ValueError:
            # Si el valor no es un número, mostrar un mensaje de error y volver a pedirlo
            print("Error: Debes ingresar un número válido.")

def sumar_numeros():
    # Pedir los dos números utilizando la función pedir_numero
    num1 = pedir_numero("Ingresa el primer número: ")
    num2 = pedir_numero("Ingresa el segundo número: ")

    # Sumar los números
    resultado = num1 + num2

    # Mostrar el resultado
    print(f"El resultado de la suma es: {resultado}")

# Llamar a la función para iniciar el proceso
#sumar_numeros()

# ==================================

def es_bisiesto():
    while True:
        try:
            # Pedir el año al usuario
            año = int(input("Ingresa un año: "))
            
            # Comprobar si es bisiesto
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                print(f"El año {año} es bisiesto.")
            else:
                print(f"El año {año} no es bisiesto.")
            
            # Salir del ciclo si se ingresó un número válido
            break
        except ValueError:
            # Si el usuario ingresa algo que no es un número entero
            print("Error: Por favor, ingresa un año válido (número entero).")

# Llamar a la función
#es_bisiesto()

# ==================================

# Función que dada una palabra diga cuántas vocales contiene.
def contar_vocales():
    '''Función que dada una palabra te dice cuantas vocales contiene.'''
    # Variables
    palabra = input('Ingresa una palabra: ').split()[0].strip().lower()
    vocales = "aeiou"
    contador = 0
    vocales_existentes = []

    # Recorro la palabra ingresada
    print(f"\tSolo una palabra 😒: {palabra}")
    for caracter in palabra:
        # Verifico si la letra es una vocal
        if caracter in vocales:
            # Si es así, la agrego a la lista de vocales existentes y aumento el contador
            vocales_existentes.append(caracter)
            contador += 1

    # Imprimo el resultado
    print("\tContando vocales...")
    if contador == 0:
        print(f"\tNo hay vocales en {palabra}.")
    else:   
        print(f"\tVocales encontradas: {', '.join(vocales_existentes)}, en total {contador}")
    return contador

#contar_vocales()
# print(3+2*2)
# lista = [1, 2, 3, 4, 5]
# print(len(lista))
# numero = '3'
# print(type(numero) is int)
# print(type(numero))
# print(type(int(numero)))

#======================================

# Pregunta_8
# Lista de diccionarios con información de personas
# personas = [
#     {"nombre": "Ana", "edad": 28},
#     {"nombre": "Luis", "edad": 34},
#     {"nombre": "Carlos", "edad": 22},
#     {"nombre": "Marta", "edad": 31}
# ]

# # Usando un bucle for para iterar sobre la lista de personas
# for persona in personas:
#     nombre = persona["nombre"]
#     edad = persona["edad"]
#     # Imprimiendo el nombre y la edad de cada persona
#     print(f"{nombre} tiene {edad}")

#======================================

# Pregunta_10
# Definimos una calificación
# calificacion = 85

# Usamos if, elif, else para determinar la calificación
# if calificacion >= 90:
#     print("Calificación A: Excelente")
# elif calificacion >= 80:
#     print("Calificación B: Muy Bueno")
# elif calificacion >= 70:
#     print("Calificación C: Bueno")
# elif calificacion >= 60:
#     print("Calificación D: Aprobado")
# else:
#     print("Calificación F: Reprobado")

#======================================

# # Pregunta_12
# # Funcion para dividir con control de errores
# def dividir_por_numero():
#     try:
#         # Solicita al usuario que ingrrese un número
#         numero = float(input("Ingresa un número para dividir 100: "))
#         # Realiza la división
#         resultado = 100 / numero
#         print(f"100 dividido por {numero} es: {resultado}")
#     # Maneja el error si el usuario no ingresa un número válido
#     except ValueError:
#         print("Error: Debes ingresar un número válido.")
#     # Maneja el error si el usuario ingresa 0
#     except ZeroDivisionError:
#         print("Error: No se puede dividir entre cero.")
#     # Maneja cualquier otro tipo de error inesperado
#     except Exception as e:
#         print(f"Ha ocurrido un error inesperado: {e}")

# # Ejecutar la función
# dividir_por_numero()

#======================================

def ip_publica():
    try:
        import requests
    except ImportError:
        print('La librería requests no está instalada. Instálala con "pip install requests"')
        exit(1)

    url = 'https://www.ifconfig.me'
    response = requests.get(url)

    if response.status_code == 200:
        print(f'Status code: {response.status_code}')
        print(f'IP pública: {response.text}')
    else:
        print('Error al obtener la IP pública')

ip_publica()