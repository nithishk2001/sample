import streamlit as st
import random

# Sample questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "F. Scott Fitzgerald"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Great White Shark", "Giraffe"],
        "answer": "Blue Whale"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Pb"],
        "answer": "Au"
    },
]

# Initialize the quiz score
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Function to display questions
def display_question(question):
    st.subheader(question["question"])
    options = question["options"]
    user_answer = st.radio("Choose your answer:", options)
    
    if st.button("Submit Answer"):
        if user_answer == question["answer"]:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {question['answer']}")
        
        st.session_state.question_index += 1

# Function to display the final score
def display_score():
    st.title("Quiz Complete!")
    st.write(f"Your final score is: {st.session_state.score} out of {len(quiz_questions)}")
    st.button("Restart Quiz", on_click=reset_quiz)

# Function to reset the quiz
def reset_quiz():
    st.session_state.score = 0
    st.session_state.question_index = 0

# Main quiz logic
st.title("Quiz App")

if st.session_state.question_index < len(quiz_questions):
    current_question = quiz_questions[st.session_state.question_index]
    display_question(current_question)
else:
    display_score()
