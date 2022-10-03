import streamlit as st
import sys
from streamlit import cli as stcli
from PIL import Image
from Juego import *

def main():
    st.title("Juegos Cortos")
    menu = ["Adivinar el Numero", "Rock, Scissors, Paper, Lizard, Spock", "Cacho","Carta mas alta"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Adivinar el Numero":
        st.subheader("Adivina un numero del 1 al 10")
        GTN ()
    
    elif choice == "Rock, Scissors, Paper, Lizard, Spock":
        st.subheader("Rock, Scissors, Paper, Lizard, Spock")
        image = Image.open("Others/Game1.png")
        st.image(image)
        RSP ()

    elif choice == "Cacho":
        st.subheader("Cacho")
        CACHO ()
    
    elif choice == "Carta mas alta":
        st.subheader ("Carta mas alta")
        CMS ()
            
    
if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
