import streamlit as st
from config import *
from chatgpt import run_completion

st.set_page_config(
    page_title="Streamlit App",
    page_icon="📝",
)

def init_session_state():
    """Initialize the session state variables."""
    return    

# Main application logic
def main():
    init_session_state()
        
    st.title("Welcome to Streamlit App")
    user_input = st.text_area("Enter your text:")
    submit_btn = st.button('Submit', key='submit_btn')
    if submit_btn:
        completion_text = run_completion(user_input)
        st.write(completion_text)    

if __name__ == '__main__':
    main()
