import streamlit as st
import random

# Sample vocabulary for the app
vocabulary = {
    "Hello": "Hola",
    "Goodbye": "Adiós",
    "Please": "Por favor",
    "Thank you": "Gracias",
    "Yes": "Sí",
    "No": "No",
    "Excuse me": "Perdón",
    "How are you?": "¿Cómo estás?",
    "I love you": "Te amo",
}

# Function to create a flashcard
def flashcard():
    st.title("Language Learning Flashcards")
    word = random.choice(list(vocabulary.keys()))
    st.subheader(f"Translate this word to Spanish: **{word}**")
    
    user_input = st.text_input("Your answer:")
    
    if st.button("Check Answer"):
        if user_input.lower() == vocabulary[word].lower():
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {vocabulary[word]}")

# Function to create a quiz
def quiz():
    st.title("Language Learning Quiz")
    questions = list(vocabulary.items())
    question = random.choice(questions)
    st.subheader(f"What is the translation of **{question[0]}**?")
    
    options = [question[1]] + random.sample(list(vocabulary.values()), 3)
    random.shuffle(options)
    
    user_answer = st.radio("Choose your answer:", options)
    
    if st.button("Submit Answer"):
        if user_answer == question[1]:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {question[1]}")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the mode", ["Flashcards", "Quiz"])

if app_mode == "Flashcards":
    flashcard()
else:
    quiz()
