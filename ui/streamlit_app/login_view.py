# ui/streamlit_app/login_view.py
import streamlit as st
from core.services.auth_service import AuthService

def show():
    st.title("🔑 Logowanie / Rejestracja")

    tab1, tab2 = st.tabs(["🔐 Zaloguj się", "📝 Zarejestruj się"])

    with tab1:
        st.subheader("🔐 Logowanie")
        name = st.text_input("Nazwa użytkownika", key="login_name")
        password = st.text_input("Hasło", type="password", key="login_password")

        if st.button("Zaloguj się"):
            if AuthService.authenticate_user(name, password):
                st.session_state["user"] = name
                st.success(f"Zalogowano jako {name} ✅")
            else:
                st.error("Nieprawidłowe dane logowania ❌")

    with tab2:
        st.subheader("📝 Rejestracja")
        name = st.text_input("Nazwa użytkownika", key="register_name")
        password = st.text_input("Hasło", type="password", key="register_password")

        if st.button("Zarejestruj się"):
            if AuthService.register_user(name, password):
                st.success("Użytkownik zarejestrowany! 🎉")
            else:
                st.error("Taka nazwa już istnieje ❌")
