import streamlit as st

# Set the title of the app
st.title("Space Adventure Mad Libs 🚀")

# Define the story template
story = """
In the year {year}, a {adjective} astronaut named {name} set out on a mission to explore the {planet}. 
Their spaceship, the {spaceship_name}, was equipped with a {adjective2} {object} that could {verb} anything in its path. 
But when they landed on {planet}, they were greeted by a group of {plural_noun} who {verb2} them to a {adjective3} {place}. 
There, they discovered a {adjective4} {animal} that could {verb3}. Together, they {verb4} back to Earth and celebrated with {food}.
"""

# Step 2: Create input fields for user words
st.header("Fill in the blanks!")
year = st.text_input("Enter a year:", key="year")
adjective = st.text_input("Enter an adjective:", key="adjective")
name = st.text_input("Enter an astronaut's name:", key="name")
planet = st.text_input("Enter a planet:", key="planet")
spaceship_name = st.text_input("Enter a spaceship name:", key="spaceship_name")
adjective2 = st.text_input("Enter another adjective:", key="adjective2")
object_ = st.text_input("Enter an object:", key="object")
verb = st.text_input("Enter a verb:", key="verb")
plural_noun = st.text_input("Enter a plural noun:", key="plural_noun")
verb2 = st.text_input("Enter another verb:", key="verb2")
adjective3 = st.text_input("Enter one more adjective:", key="adjective3")
place = st.text_input("Enter a place:", key="place")
adjective4 = st.text_input("Enter another adjective:", key="adjective4")
animal = st.text_input("Enter an animal:", key="animal")
verb3 = st.text_input("Enter another verb:", key="verb3")
verb4 = st.text_input("Enter one more verb:", key="verb4")
food = st.text_input("Enter a food:", key="food")

# Step 3: Generate the story when the user clicks a button
if st.button("Generate Story"):
    if all([year, adjective, name, planet, spaceship_name, adjective2, object_, verb, plural_noun, verb2, adjective3, place, adjective4, animal, verb3, verb4, food]):
        # Insert the words into the story
        completed_story = story.format(
            year=year,
            adjective=adjective,
            name=name,
            planet=planet,
            spaceship_name=spaceship_name,
            adjective2=adjective2,
            object=object_,
            verb=verb,
            plural_noun=plural_noun,
            verb2=verb2,
            adjective3=adjective3,
            place=place,
            adjective4=adjective4,
            animal=animal,
            verb3=verb3,
            verb4=verb4,
            food=food
        )
        # Display the final story
        st.header("Your Space Adventure Story:")
        st.write(completed_story)
    else:
        st.error("Please fill in all the fields!")