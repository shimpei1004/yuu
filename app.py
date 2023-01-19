import streamlit as st
from PIL import Image

# List of countries and their corresponding flag images
countries = {
    "Afghanistan": "afghanistan.png",
    "Albania": "albania.png",
    "Algeria": "algeria.png",
    # ... add more countries here
}

# Function to check if the user's guess is correct
def check_answer(guess):
    if guess == correct_answer:
        st.success("Correct!")
    else:
        st.error("Incorrect. The correct answer is: " + correct_answer)

st.title("Guess the Country Flag")

# Show a random flag image
correct_answer, flag_file = random.choice(list(countries.items()))
img = Image.open(flag_file)
st.image(img, width=300)

# Get user's guess
guess = st.selectbox("Which country's flag is this?", list(countries.keys()))

# Check the answer
if st.button("Submit"):
    check_answer(guess)
