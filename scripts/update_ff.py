import os  # Importa el módulo 'os', que permite interactuar con el sistema operativo.
import json  # Importa el módulo 'json', que permite trabajar con archivos en formato JSON.

last_version = "0.0.0"  # Declara una variable global 'last_version' para almacenar la versión anterior.
new_version = "0.0.0"  # Declara una variable global 'new_version' para almacenar la nueva versión.

def update_ff():  # Define una función llamada 'update_ff'.
  os.system("npm run update-ff:raw")  # Ejecuta un comando del sistema operativo para correr un script de npm.

def get_version_before():  # Define una función llamada 'get_version_before'.
  global last_version  # Declara que la variable 'last_version' es global para poder modificarla.
  with open("surfer.json", "r") as f:  # Abre el archivo 'surfer.json' en modo de lectura.
    data = json.load(f)  # Carga el contenido del archivo JSON en la variable 'data'.
    last_version = data["version"]["version"]  # Extrae la versión anterior y la asigna a 'last_version'.

def get_version_after():  # Define una función llamada 'get_version_after'.
  global new_version  # Declara que la variable 'new_version' es global para poder modificarla.
  with open("surfer.json", "r") as f:  # Abre el archivo 'surfer.json' en modo de lectura.
    data = json.load(f)  # Carga el contenido del archivo JSON en la variable 'data'.
    new_version = data["version"]["version"]  # Extrae la nueva versión y la asigna a 'new_version'.

def update_readme():  # Define una función llamada 'update_readme'.
  global last_version  # Declara que la variable 'last_version' es global.
  global new_version  # Declara que la variable 'new_version' es global.
  with open("README.md", "r") as f:  # Abre el archivo 'README.md' en modo de lectura.
    data = f.read()  # Lee todo el contenido del archivo y lo almacena en 'data'.
    data = data.replace(last_version, new_version)  # Reemplaza la 'last_version' por la 'new_version' en 'data'.
  with open("README.md", "w") as f:  # Abre el archivo 'README.md' en modo de escritura.
    f.write(data)  # Escribe el contenido modificado de 'data' en el archivo.

if __name__ == "__main__":  # Verifica si este script se está ejecutando directamente.
  get_version_before()  # Llama a la función para obtener la versión anterior.
  update_ff()  # Llama a la función para ejecutar el script de npm.
  get_version_after()  # Llama a la función para obtener la nueva versión.
  update_readme()  # Llama a la función para actualizar el archivo README.md.
  print("Updated from version {} to version {}".format(last_version, new_version))  # Imprime un mensaje indicando la actualización de versión.