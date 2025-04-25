# ui/streamlit_app/shopping_list_view.py
import streamlit as st

def show():
    if "user" not in st.session_state:
        st.warning("🔒 Musisz być zalogowany, aby przeglądać listę zakupów!")
        return

    st.title(f"🛍️ Lista zakupów ({st.session_state['user']})")
    st.write("Tu pojawi się Twoja lista zakupów! ✏️")
