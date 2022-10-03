import streamlit as st
import random
from streamlit import cli as stcli
from random import randint
from PIL import Image
import random

def GTN ():
    number = random.randint(1, 10)
    number_of_guesses = 3
    Opt=st.text_input("Pick a number from 1 to 10")
    while number_of_guesses < 5:
        guess = int(Opt)
        number_of_guesses += 1
        if guess < number:
            st.warning('Your guess is too low')
        if guess > number:
            st.warning('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        st.success('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        st.warning('You did not guess the number, The number was ' + str(number))

def RSP ():
    
    t = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']
    computer = t[randint(0,4)]
    imgRock = Image.open ("Others/Rock.png")
    imgScis = Image.open ("Others/Scissors.png")
    imgPap = Image.open ("Others/Paper.png")
    imgLiz = Image.open ("Others/Lizard.png")
    imgSpo = Image.open ("Others/Spock.png")
    col1, col2 = st.columns(2)
             
    with col1:
        player = st.radio('Choose', ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock'])
        st.write('You choose', player)
        st.write('Computer choose', computer)            
    with col2:
        if player == computer:
            st.write("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                st.write("You Loose!", computer, "covers", player)
                st.image(imgPap)
            if computer == "Lizard":
                st.write("You Win!", player, "crushes", computer)
                st.image(imgRock)
            if computer == "Spock":
                st.write("You Lose!", computer, "vaporizes", player)
                st.image(imgSpo)
            if computer == "Scissors":
                st.write("You Win!", player, "crushes", computer)
                st.image(imgRock)
        elif player == "Paper":
            if computer == "Scissors":
                st.write("You Lose!", computer, "cuts", player)
                st.image(imgScis)
            if computer == "Spock":
                st.write("You Win!", player, "disproves", computer)
                st.image(imgPap)
            if computer == "Lizard":
                st.write("You Lose!", computer, "eats", player)
                st.image(imgLiz)
            if computer == "Rock":
                st.write("You Win!", player, "covers", computer)
                st.image(imgPap)
        elif player == "Scissors":
            if computer == "Rock":
                st.write("You Lose!", computer, "crushes", player)
                st.image(imgRock)
            if computer == "Spock":
                st.write("You Lose!", computer, "smashes", player)
                st.image(imgSpo)
            if computer == "Lizard":
                st.write("You Win!", player, "decapitates", computer)
                st.image(imgScis)
            if computer == "Paper":
                st.write("You Win!", player, "cuts", computer)
                st.image(imgScis)
        elif player == "Lizard":
            if computer == "Rock":
                st.write("You Lose!", computer, "crushes", player)
                st.image(imgRock)
            if computer == "Spock":
                st.write("You Win!", player, "poisons", computer)
                st.image(imgLiz)
            if computer == "Scissors":
                st.write("You Lose!", computer, "decapitates", player)
                st.image(imgScis)
            if computer =="Paper":
                st.write("You Win!", player, "eats", computer)
                st.image(imgLiz)
        elif player == "Spock":
            if computer == "Rock":
                st.write("You Win!", player, "vaporizes", computer)
                st.image(imgSpo)
            if computer == "Paper":
                st.write("You Lose!", computer, "disproves", player)
                st.image(imgPap)
            if computer == "Lizard":
                st.write("You Lose!", computer, "poisons", player)
                st.image(imgLiz)
            if computer =="Scissors":
                st.write("You Win!", player, "smashes", computer)
                st.image(imgSpo)

def CACHO ():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    dado3=random.randint(1,6)
    dado4=random.randint(1,6)
    dado5=random.randint(1,6)
    dado6=random.randint(1,6)
    imgd1=Image.open ("Others/dado1.png")
    imgd2=Image.open ("Others/dado2.png")
    imgd3=Image.open ("Others/dado3.png")
    imgd4=Image.open ("Others/dado4.png")
    imgd5=Image.open ("Others/dado5.png")
    imgd6=Image.open ("Others/dado6.png")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    if st.button("Throw the dices"):
        with col1:
            st.write(dado1)
            if dado1 == 1:
                st.image(imgd1)
            if dado1 == 2:
                st.image(imgd2)
            if dado1 == 3:
                st.image(imgd3)
            if dado1 == 4:
                st.image(imgd4)
            if dado1 == 5:
                st.image(imgd5)
            if dado1 == 6:
                st.image(imgd6)
        with col2:
            st.write(dado2)
            if dado2 == 1:
                st.image(imgd1)
            if dado2 == 2:
                st.image(imgd2)
            if dado2 == 3:
                st.image(imgd3)
            if dado2 == 4:
                st.image(imgd4)
            if dado2 == 5:
                st.image(imgd5)
            if dado2 == 6:
                st.image(imgd6)
        with col3:
            st.write(dado3)
            if dado3 == 1:
                st.image(imgd1)
            if dado3 == 2:
                st.image(imgd2)
            if dado3 == 3:
                st.image(imgd3)
            if dado3 == 4:
                st.image(imgd4)
            if dado3 == 5:
                st.image(imgd5)
            if dado3 == 6:
                st.image(imgd6)
        with col4:
            st.write(dado4)
            if dado4 == 1:
                st.image(imgd1)
            if dado4 == 2:
                st.image(imgd2)
            if dado4 == 3:
                st.image(imgd3)
            if dado4 == 4:
                st.image(imgd4)
            if dado4 == 5:
                st.image(imgd5)
            if dado4 == 6:
                st.image(imgd6)
        with col5:
            st.write(dado5)
            if dado5 == 1:
                st.image(imgd1)
            if dado5 == 2:
                st.image(imgd2)
            if dado5 == 3:
                st.image(imgd3)
            if dado5 == 4:
                st.image(imgd4)
            if dado5 == 5:
                st.image(imgd5)
            if dado5 == 6:
                st.image(imgd6)
        with col6:
            st.write(dado6)
            if dado6 == 1:
                st.image(imgd1)
            if dado6 == 2:
                st.image(imgd2)
            if dado6 == 3:
                st.image(imgd3)
            if dado6 == 4:
                st.image(imgd4)
            if dado6 == 5:
                st.image(imgd5)
            if dado6 == 6:
                st.image(imgd6)

def CMS ():
    carta1 = random.randint(1,13)
    carta2 = random.randint(1,13)
    imgc1=Image.open ("Others/c1.png")
    imgc2=Image.open ("Others/c2.png")
    imgc3=Image.open ("Others/c3.png")
    imgc4=Image.open ("Others/c4.png")
    imgc5=Image.open ("Others/c5.png")
    imgc6=Image.open ("Others/c6.png")
    imgc7=Image.open ("Others/c7.png")
    imgc8=Image.open ("Others/c8.png")
    imgc9=Image.open ("Others/c9.png")
    imgc10=Image.open ("Others/c10.png")
    imgc11=Image.open ("Others/c11.png")
    imgc12=Image.open ("Others/c12.png")
    imgc13=Image.open ("Others/c13.png")
    col1,col2 = st.columns(2)

    if st.button ("Play"):
        with col1:
            st.write("Player")
            if carta1 == 1:
                st.image(imgc1)
            if carta1 == 2:
                st.image(imgc2)
            if carta1 == 3:
                st.image(imgc3)
            if carta1 == 4:
                st.image(imgc4)
            if carta1 == 5:
                st.image(imgc5)
            if carta1 == 6:
                st.image(imgc6)
            if carta1 == 7:
                st.image(imgc7)
            if carta1 == 8:
                st.image(imgc8)
            if carta1 == 9:
                st.image(imgc9)
            if carta1 == 10:
                st.image(imgc10)
            if carta1 == 11:
                st.image(imgc11)
            if carta1 == 12:
                st.image(imgc12)
            if carta1 == 13:
                st.image(imgc13)
        with col2:
            st.write("Computer")
            if carta2 == 1:
                st.image(imgc1)
            if carta2 == 2:
                st.image(imgc2)
            if carta2 == 3:
                st.image(imgc3)
            if carta2 == 4:
                st.image(imgc4)
            if carta2 == 5:
                st.image(imgc5)
            if carta2 == 6:
                st.image(imgc6)
            if carta2 == 7:
                st.image(imgc7)
            if carta2 == 8:
                st.image(imgc8)
            if carta2 == 9:
                st.image(imgc9)
            if carta2 == 10:
                st.image(imgc10)
            if carta2 == 11:
                st.image(imgc11)
            if carta2 == 12:
                st.image(imgc12)
            if carta2 == 13:
                st.image(imgc13)
        if carta1 > carta2:
            st.write("You win!")
        if carta1 < carta2:
            st.write("You Lose!")
        if carta1 == carta2:
            st.write("It is a tie")