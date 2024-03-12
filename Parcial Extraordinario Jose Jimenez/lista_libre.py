def crear_diccionario_libro() -> dict:
    libro_dict = {
        "titulo": "",
        "autor": "",
        "año": 0
    }
    libro_dict["género"] = ""
    return libro_dict

libro = crear_diccionario_libro()
libro["titulo"] = "Matar a un ruiseñor"
libro["autor"] = "Harper Lee"
libro["año"] = 1960
libro["género"] = "Ficción"

print(libro)
