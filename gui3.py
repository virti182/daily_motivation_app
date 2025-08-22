# Creating the Daily Motivation App using streamlit

import streamlit as st
import random

# Input the title 
st.title("Daily Motivation App")

# add the header and subheader you want 
st.header("Encourage positive thoughts and embrace a goal getter mindset with Motivation")
st.subheader("Welcome to your daily source of inspiration! ")
 

 # Now ask the user to enter the name
name = st.text_input("Enter your name! ")

# Now add some benefits to know why daily motivation is useful
st.markdown("### Benefits of Daily motivtion! ")
st.write("01. Stay inspired and Focused ")
st.caption("Embrace a positive, motivated mindset by reading powerful, encouraging quotes throughout your day.")
st.write("02. Build resilience")
st.caption("Cultivate resilience by reminding yourself that challenges are opportunities for growth and setbacks are just part of your comeback.")
st.write("03. Take action toward your goals")
st.caption("Stay determined and driven with motivational quotes that encourage you to take actionable steps and celebrate your wins.")
st.write("04. Nurture your mental well-being")
st.caption("Foster a positive mindset, reduce stress and anxiety, and boost your self-confidence thanks to the power of daily motivational quotes.")


# Now lets go for the selection box and ask user what they wanna hear today like motivation type
motivation_type = st.selectbox("What kind of motivation you wanna hear today?: ", ["Select an option", "Sucess", "Romantic", "Growth", "Positivity"])

# now add the quotes for each thing
quotes = { "Sucess": ["The first step towards sucess is taken when you rufuse to be a captive of the environment in which you first find yourself",
                      "Success seems to be connected with action. Successful people keep moving. They make mistakes, but they don't quit.",
                      "Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, vision cleared, ambition inspired and success achieved.",
                      "The most certain way to succeed is always to try just one more time.",
                      "A little more persistence, a little more effort and what seemed hopeless failure may turn to glorious success.",
                      "Perseverance is the hard work you do after you get tired of doing the hard work you already did."], 
            "Romantic": ["To the world you may be one person, but to one person you are the world.",
                         "Love is that condition in which the happiness of another person is essential to your own.",
                         "If you live to be a hundred, I want to live to be a hundred minus one day so I never have to live without you.",
                         "You are the closest to heaven that I will ever be.",
                         "It is always better when we aretogether.",
                         "You know you are in love when you cant fall asleep because reality is finally better than your dreams."],
            "Growth": ["Do the best you can until you know better. Then when you know better, do better.", 
                       "Stay afraid, but do it anyway. Whats important is the action. You dont have to wait to be confident. Just do it and eventually the confidence will follow.",
                       "We cant become what we need to be by remaining what we are.",
                       "When we are growing up there are all sorts of people telling us what to do when really what we need is space to work out who to be.",
                       "Be not afraid of growing slowly; be afraid only of standing still.",
                       "Permit yourself to change your mind when something is no longer working for you."],
            "Positivity": ["Kindness is one thing you cant give away. It always comes back.",
                           "Great things happen to those who don't stop believing, trying, learning, and being grateful.",
                           "Fight for the things that you care about, but do it in a way that will lead others to join you.",
                           "Extraordinary things are always hiding in places people never think to look.",
                           "Nothing is impossible, the word itself says I am possible.",
                           "Once you replace negative thoughts with positive ones, you will start having positive results."]}


#main body
# button for quote
if st.button("Inspire Me"):
    if name.strip() == "":
        st.warning("Pkease enter your name first to get personalised quotes! ")
    elif motivation_type == "Select an option":
        st.warning("Please select the type of motivation you want! ")
    else:
        quote = random.choice(quotes[motivation_type])
        st.success(f"Hey {name}, here is your {motivation_type.lower()} motivation:\n\n{quote}")