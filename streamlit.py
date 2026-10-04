import streamlit as st

st.set_page_config(
    page_title="Python Crash Course",
    page_icon="🐍",
    layout="wide"
)

st.title("Python Applications Crash Course")
st.header("Streamlit Basics")
st.subheader("Build simple web applications with Python")

st.write("Streamlit lets us turn Python code into an interactive web application.")

st.markdown("### Markdown also works")
st.caption("This is a small caption.")

# ------------------------------------------------------------
# 3. Code, JSON and metric
# ------------------------------------------------------------
st.code("print('Hello, Streamlit!')", language="python")

st.json({
    "course": "Python",
    "level": "Beginner"
})

st.metric("Students", 25, "+5")

# ------------------------------------------------------------
# 4. Sidebar
# ------------------------------------------------------------
st.sidebar.title("Course Menu")
st.sidebar.write("Choose an option below.")

topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Python", "Pandas", "NumPy", "AI Applications"]
)

st.write("Selected topic:", topic)


# ------------------------------------------------------------
# 5. Text input
# ------------------------------------------------------------
name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}!")

# ------------------------------------------------------------
# 6. Number input
# ------------------------------------------------------------
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)

st.write("Your age is:", age)

# ------------------------------------------------------------
# 7. Slider
# ------------------------------------------------------------
confidence = st.slider(
    "Choose a confidence score",
    min_value=0,
    max_value=100,
    value=50
)

st.write("Confidence:", confidence)

# ------------------------------------------------------------
# 8. Checkbox
# ------------------------------------------------------------
show_details = st.checkbox("Show course details")

if show_details:
    st.info("This course prepares you to build Python applications for AI.")

# ------------------------------------------------------------
# 9. Radio buttons
# ------------------------------------------------------------
experience = st.radio(
    "Your Python experience",
    ["Beginner", "Intermediate", "Advanced"]
)

st.write("Selected:", experience)

# ------------------------------------------------------------
# 10. Selectbox and multiselect
# ------------------------------------------------------------
language = st.selectbox(
    "Choose a programming language",
    ["Python", "Java", "JavaScript", "C++"]
)

skills = st.multiselect(
    "Choose your skills",
    ["Python", "Pandas", "NumPy", "Streamlit", "Git"]
)

st.write("Language:", language)
st.write("Skills:", skills)

# ------------------------------------------------------------
# 11. Button
# ------------------------------------------------------------
if st.button("Click Me"):
    st.success("Button clicked successfully!")

# ------------------------------------------------------------
# 12. Form
# ------------------------------------------------------------
with st.form("student_form"):
    st.write("Student Registration")

    student_name = st.text_input("Student name")
    student_email = st.text_input("Email")
    submitted = st.form_submit_button("Register")

    if submitted:
        st.success(f"Registration received for {student_name}")

# ------------------------------------------------------------
# 13. Columns
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# 15. Status messages
# ------------------------------------------------------------
st.success("Success message")
st.info("Information message")
st.warning("Warning message")
st.error("Error message")

# ------------------------------------------------------------
# 16. Progress bar
# ------------------------------------------------------------
st.progress(70)

# ------------------------------------------------------------
# 17. File uploader
# ------------------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a text file",
    type=["txt"]
)

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("Uploaded content", content, height=150)

# ------------------------------------------------------------
# 18. Download button
# ------------------------------------------------------------
sample_text = "Hello from our Python application!"

st.download_button(
    label="Download sample text",
    data=sample_text,
    file_name="sample.txt",
    mime="text/plain"
)

# ------------------------------------------------------------
# 19. Simple practical Streamlit app
# ------------------------------------------------------------
st.header("Mini App: Student Score Calculator")

student = st.text_input("Student name", key="score_student")
math_score = st.number_input("Math", 0, 100, 50, key="math")
python_score = st.number_input("Python", 0, 100, 50, key="python")
ai_score = st.number_input("AI", 0, 100, 50, key="ai")

if st.button("Calculate Result", key="calculate"):
    total = math_score + python_score + ai_score
    average = total / 3

    st.write("Student:", student)
    st.write("Total:", total)
    st.write("Average:", average)

    if average >= 50:
        st.success("Result: Pass")
    else:
        st.error("Result: Fail")
