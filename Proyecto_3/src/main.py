import requests

def almacenar_libro(libro:str):
    """
    """
    with open("libros.txt", "a", encoding="utf-8") as archivo:
        archivo.write(libro)
        archivo.write("\n \n")  # Agrega un separador entre libros para facilitar la lectura
        

for i in range(1316,2500):

    link_base=f'https://www.gutenberg.org/cache/epub/{i}/pg{i}.txt'
    print(link_base)
    response=requests.get(link_base)

    if response.status_code==200:
        print('libro almacenado')
        almacenar_libro(response.text)
    else:
        print('fallo')