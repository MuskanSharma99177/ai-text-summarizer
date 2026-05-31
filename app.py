import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# -------------------
# Page Config
# -------------------
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="wide"
)

# -------------------
# Custom CSS
# -------------------
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.stButton > button {
    width: 100%;
    height: 3rem;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #f5f5f5;
    border-left: 6px solid #4CAF50;
    color: black;
}

.header {
    text-align: center;
    padding: 10px;
}

.small-text {
    color: gray;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------
# Load Environment
# -------------------
load_dotenv(dotenv_path="../.env")

# -------------------
# LLM
# -------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -------------------
# Sidebar
# -------------------
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("Model: Llama 3.3 70B")
    st.success("Powered by Groq")
    st.divider()

    summary_type = st.selectbox(
        "Summary Style",
        ["Short", "Detailed", "Bullet Points"]
    )

# -------------------
# Main Header
# -------------------
st.markdown("""
<div class='header'>
    <h1>🤖 AI Text Summarizer</h1>
    <p class='small-text'>
        Paste any text and generate an instant summary
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------
# Input
# -------------------
user_input = st.text_area(
    "Enter your text",
    height=300,
    placeholder="Paste your article, notes, document, blog..."
)

# -------------------
# Button
# -------------------
if st.button("🚀 Summarize"):

    if not user_input.strip():
        st.warning("Please enter some text.")
    else:

        if summary_type == "Short":
            prompt = f"Summarize this text in 3-4 lines:\n\n{user_input}"

        elif summary_type == "Detailed":
            prompt = f"Provide a detailed summary:\n\n{user_input}"

        else:
            prompt = f"Summarize in bullet points:\n\n{user_input}"

        with st.spinner("Generating Summary..."):

            response = llm.invoke(prompt)

        st.markdown("### 📄 Summary")

        st.markdown(
            f"""
            <div class='result-box'>
                {response.content}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("Summary Generated Successfully!")