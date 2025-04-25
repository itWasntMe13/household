# ui/streamlit_app/main.py
import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from core.utils.db import init_db
from ui.streamlit_app import login_view, shopping_list_view

# 🛠️ Inicjalizacja bazy danych
init_db()

# 📚 Sidebar – Nawigacja
st.sidebar.title("🛒 Nawigacja")
page = st.sidebar.radio("Wybierz ekran:", ["🔑 Logowanie", "🛍️ Lista zakupów"])

# 🖥️ Widoki
if page == "🔑 Logowanie":
    login_view.show()
elif page == "🛍️ Lista zakupów":
    shopping_list_view.show()
