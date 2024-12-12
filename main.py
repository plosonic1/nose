meme_dict = {
            "FR": "es una abreviatura de for real, que se usa en mensajes de texto para enfatizar que lo que se dice es verdad",
            "EZ": "FORMA DE BURLARSE DE ALGUIEN EN UNA PELEA",
            "SKIBIDI": "PALABRA SIN SIGNIFICADO",
            "INGATURRUÑA": "es un ejemplo de humor absurdo y sin sentido",
            "OAL": "es hola mal escrito",
            "NOBODY CAN BEAT ME BEACUSE I AM SUPER 17": "DIALOGO DE SUPER 17 DE DRAGON BALL GT"
            
            
            
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("NO AHI DATO DE ESE MOMAZO EN LA BASE")
