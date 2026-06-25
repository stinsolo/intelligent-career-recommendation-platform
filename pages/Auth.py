from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

import streamlit as st
import json
import hashlib
from datetime import datetime

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def show():
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding: 2rem 0 1rem;">
            <div style="font-size: 3.5rem;">🚀</div>
            <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem; margin:0;">
                CareerAI
            </h1>
            <p style="color:#888; margin-top:0.5rem;">Your Intelligent Career Recommendation Platform</p>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔑 Login", "✨ Register"])

        users = load_users()

        with tab1:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("login_form"):
                email = st.text_input("📧 Email", placeholder="your@email.com")
                password = st.text_input("🔒 Password", type="password", placeholder="••••••••")
                submitted = st.form_submit_button("Login →", use_container_width=True)

                if submitted:
                    if email in users:
                        if users[email]["password"] == hash_password(password):
                            st.session_state.authenticated = True
                            st.session_state.user = users[email]
                            st.session_state.current_page = "dashboard"
                            st.success("✅ Welcome back!")
                            st.rerun()
                        else:
                            st.error("❌ Incorrect password.")
                    else:
                        st.error("❌ Account not found. Please register.")

            st.markdown("""
            <div style="text-align:center; margin-top:1rem;">
                <p style="color:#555; font-size:0.85rem;">Demo: use any registered account</p>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.form("register_form"):
                name = st.text_input("👤 Full Name", placeholder="John Doe")
                email_reg = st.text_input("📧 Email", placeholder="your@email.com", key="reg_email")
                password_reg = st.text_input("🔒 Password", type="password", placeholder="Min 6 characters", key="reg_pass")
                password_confirm = st.text_input("🔒 Confirm Password", type="password", placeholder="Repeat password", key="reg_confirm")
                role = st.selectbox("🎯 I am a...", ["Job Seeker", "Recent Graduate", "Career Changer", "Professional"])
                submitted_reg = st.form_submit_button("Create Account →", use_container_width=True)

                if submitted_reg:
                    if not all([name, email_reg, password_reg, password_confirm]):
                        st.error("❌ Please fill in all fields.")
                    elif len(password_reg) < 6:
                        st.error("❌ Password must be at least 6 characters.")
                    elif password_reg != password_confirm:
                        st.error("❌ Passwords do not match.")
                    elif email_reg in users:
                        st.error("❌ Email already registered.")
                    else:
                        users[email_reg] = {
                            "name": name,
                            "email": email_reg,
                            "password": hash_password(password_reg),
                            "role": role,
                            "created_at": datetime.now().isoformat(),
                            "resume_uploaded": False
                        }
                        save_users(users)
                        st.session_state.authenticated = True
                        st.session_state.user = users[email_reg]
                        st.session_state.current_page = "dashboard"
                        st.success("✅ Account created! Welcome to CareerAI!")
                        st.rerun()

        st.markdown("""
        <div style="margin-top: 2rem; padding: 1rem; background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
            border: 1px solid rgba(102,126,234,0.3); border-radius: 12px;">
            <p style="color:#888; font-size:0.8rem; margin:0; text-align:center;">
                🔒 Your data is stored locally and securely hashed.<br>
                API keys are never stored permanently.
            </p>
        </div>
        """, unsafe_allow_html=True)