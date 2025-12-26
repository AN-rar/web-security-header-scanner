import requests

D_URL = input("URL objetivo: ")

try:
    
    Respuesta = requests.get(D_URL)

    
    if "Server" in Respuesta.headers:
       
        print(f"Software del servidor: {Respuesta.headers['Server']}")

    if "X-Powered-By" in Respuesta.headers:
       
        print(f"Lenguaje detectado: {Respuesta.headers['X-Powered-By']}")

    if "Strict-Transport-Security" in Respuesta.headers:
        print("HSTS Activo: El sitio obliga a usar conexiones seguras.")
    else:
        print("Vulnerabilidad: Falta la cabecera Strict-Transport-Security (HSTS).")

except:
   
    print("Algo salió mal: No se pudo conectar con la URL, verifique si inicia con: http// o https//")