import streamlit as st



# Diccionario de traducciones de español a inglés
dictionary = {
    "ese": "uán",
    "convertirse": "nduu",
    "amarillo": "kuáán,",
    "alto": "súkú,súkún",
    "tierra": "ñuhu,ñuhun",
    "volver": "nduu",
    "mano": "ndaha",
    "otro": "inga",
    "bien": "vaha",
    "borrego": "rii",
    "cueva": "túnchi",
    "contiene": "ñúhu",
    "fuego": "ñuhú",
    "deidad": "ñuhú",
    # Agrega más palabras y traducciones según sea necesario
}

# Función para traducir una oración

def translate_sentence(sentence):
        translated_words = [dictionary.get(word, word) for word in sentence.lower().split()]
        translated_sentence = ' '.join(translated_words)
        return translated_sentence

# Interfaz de usuario con Streamlit
st.title("Traductor de Español a Mix")
sentence = st.text_input("Escribe una oración en español para traducir:").lower

if st.button("Traducir"):
        translated_sentence = translate_sentence(sentence)
   st.write("Oración traducida al inglés:", translated_sentence)
        
  
