import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to reset the game
def reset_game():
    st.session_state.random_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.history = []

# Main title and instructions
st.title("🎮 Number Guessing Game")
st.markdown("""
Try to guess the number between 1 and 10!
I'll give you hints along the way.
""")

# Game interface
col1, col2 = st.columns([3, 1])

with col1:
    # Input for user's guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input", disabled=st.session_state.game_over)

with col2:
    # Button to submit guess
    if st.button("Guess!", disabled=st.session_state.game_over):
        st.session_state.attempts += 1
        
        # Check the guess
        if guess < st.session_state.random_number:
            st.session_state.message = f"Too low! Try a higher number."
            st.session_state.history.append(f"Guess {st.session_state.attempts}: {guess} - Too low!")
        elif guess > st.session_state.random_number:
            st.session_state.message = f"Too high! Try a lower number."
            st.session_state.history.append(f"Guess {st.session_state.attempts}: {guess} - Too high!")
        else:
            st.session_state.message = f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!"
            st.session_state.game_over = True
            st.session_state.history.append(f"Guess {st.session_state.attempts}: {guess} - Correct!")

# Display message
if st.session_state.message:
    if st.session_state.game_over:
        st.success(st.session_state.message)
    else:
        st.info(st.session_state.message)

# Display attempts
if st.session_state.attempts > 0:
    st.write(f"Attempts: {st.session_state.attempts}")

# Display guess history
if st.session_state.history:
    st.subheader("Guess History")
    for entry in st.session_state.history:
        st.write(entry)

# Reset button
if st.button("New Game"):
    reset_game()

# Display the secret number (for debugging)
# st.sidebar.write(f"Secret number: {st.session_state.random_number}")

# Add some styling
st.markdown("""
<style>
    .stButton button {
        width: 100%;
    }
    .css-1d391kg {
        padding-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


