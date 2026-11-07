import streamlit as st

## Page configuration
st.set_page_config(
    page_title="Python crash course",
    page_icon="🐍",
    layout="wide"
)

## Title, header, sub-header and text
st.title("Pyhton Applications crash course")
st.header("Streamlit Basics")
st.subheader("Build simple web application with python")
st.write("Streamlit lets us turn Python code into interactive web application")

st.markdown("### Markdown also works")
st.caption("This is a small caption.")

### Code, JSON and metric
st.code("print('Hello, Streamlit!!')", language="python")
st.json({
    "Course": "Python",
    "Level": "Beginner"
})

st.metric("Students", 25, "+5")

## Sidebar
st.sidebar.title("Course Menu")
st.sidebar.write("Choose an option below.")
topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Pyhton", "Pandas", "Numpy", "AI Applications"]
)
st.write("Selected topic:", topic)

## Text input
name = st.text_input("What is your name:")
if name:
    st.write(f"Hello, {name}!")


## Number input
age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100,
    value=32
)
st.write(f"Your age is: ", age)


## Slider
confidence = st.slider(
    "Choose a confidence score",
    min_value=1,
    max_value=100,
    value=50
)
st.write("Confidence:", confidence)

## Checkbox
show_detail = st.checkbox("Show course details")
if show_detail:
    st.info("This course you prepares to build python applications for AI")

## Radio buttons
experience = st.radio(
    "Your python experience",
    ["Beginner", "Intermediate", "Advanced"]
)
st.write("Selected: ", experience)

## Selectbox and multi-select
language = st.selectbox(
    "Choose your programming language",
    ["Python", "Java", "Java-script", "C++"]
)

skills = st.multiselect(
    "Choose your skills",
    ["Pyhton", "Pandas", "Numpy", "Streamlit", "gen-ai"]
)

st.write("Langauage:", language)
st.write("Skills:", skills)

## Button
if st.button("Click me"):
    st.success("Button clicked successfully!!")


## Form
with st.form("student_form"):
    st.write("Student Ragistration")

    student_name = st.text_input("Student name")
    student_email = st.write("Email")
    submitted = st.form_submit_button("Ragistration")

    if submitted:
        st.success(f"Ragistration received for {student_name}")

## Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.info("Python")

with col2:
    st.info("Pandas")

with col3:
    st.info("NumPy")

# ------------------------------------------------------------
# 14. Expander
# ------------------------------------------------------------
with st.expander("Show more information"):
    st.write("Expanders are useful when we want to hide details until needed.")


## File uploader
uploaded_file = st.file_uploader(
    "Upload a text file",
    type=["txt"]
)

if uploaded_file not in None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("Uploaded content", content, height=150)
