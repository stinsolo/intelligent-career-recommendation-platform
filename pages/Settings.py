from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

import streamlit as st
import json

def show():
    st.markdown("""
    <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        ⚙️ Settings & Configuration
    </h1>
    <p style="color:#888;">Configure your API keys and preferences</p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # API Keys Section
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🔑 API Configuration</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background: rgba(255,210,0,0.1); border: 1px solid rgba(255,210,0,0.3);
        border-radius: 12px; padding: 1rem; margin-bottom:1.5rem;">
        <p style="color:#ffd200; font-weight:600; margin:0 0 0.25rem;">🔒 Privacy Notice</p>
        <p style="color:#888; margin:0; font-size:0.85rem;">API keys are stored only in your session memory and are never saved to disk or transmitted anywhere except to the respective API providers.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("api_settings"):
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("**🤖 OpenAI API Key**")
        st.markdown('<p style="color:#888; font-size:0.85rem; margin-top:-0.5rem;">Required for AI Resume Analysis and Job Recommendations</p>', unsafe_allow_html=True)

        openai_key = st.text_input(
            "OpenAI API Key",
            value=st.session_state.openai_api_key,
            type="password",
            placeholder="sk-proj-...",
            label_visibility="collapsed"
        )

        st.markdown("**🌐 LinkedIn Configuration** (Optional - for Selenium scraping)")
        linkedin_email = st.text_input("LinkedIn Email (optional)", placeholder="your@email.com")
        linkedin_pass = st.text_input("LinkedIn Password (optional)", type="password", placeholder="For authenticated scraping")

        save_btn = st.form_submit_button("💾 Save Settings", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if save_btn:
            st.session_state.openai_api_key = openai_key
            if linkedin_email:
                st.session_state.linkedin_email = linkedin_email
            if linkedin_pass:
                st.session_state.linkedin_pass = linkedin_pass
            st.success("✅ Settings saved successfully!")

    # API Status
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">📊 Connection Status</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        has_key = bool(st.session_state.openai_api_key)
        status_color = "#38ef7d" if has_key else "#f45c43"
        status_text = "Connected" if has_key else "Not Configured"
        st.markdown(f"""
        <div class="metric-card">
            <div style="display:flex; align-items:center; gap:0.75rem;">
                <div style="width:10px; height:10px; border-radius:50%; background:{status_color};"></div>
                <div>
                    <div style="color:#e8e8f0; font-weight:600;">OpenAI API</div>
                    <div style="color:{status_color}; font-size:0.85rem;">{status_text}</div>
                </div>
            </div>
            {f'<div style="margin-top:0.75rem; color:#888; font-size:0.8rem;">Key: ...{st.session_state.openai_api_key[-8:] if len(st.session_state.openai_api_key) > 8 else "***"}</div>' if has_key else ''}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="display:flex; align-items:center; gap:0.75rem;">
                <div style="width:10px; height:10px; border-radius:50%; background:#ffd200;"></div>
                <div>
                    <div style="color:#e8e8f0; font-weight:600;">Selenium (Chrome)</div>
                    <div style="color:#ffd200; font-size:0.85rem;">Auto-detected at runtime</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Test API
    if st.session_state.openai_api_key:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        if st.button("🧪 Test OpenAI Connection", use_container_width=True):
            with st.spinner("Testing connection..."):
                try:
                    from openai import OpenAI
                    client = OpenAI(api_key=st.session_state.openai_api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": "Say 'Connection successful!' in 5 words or less."}],
                        max_tokens=20
                    )
                    st.success(f"✅ {response.choices[0].message.content}")
                except Exception as e:
                    st.error(f"❌ Connection failed: {str(e)}")

    # System info
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">ℹ️ System Information</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="color:#888; font-size:0.85rem; margin-bottom:0.75rem;">CURRENT SESSION</div>
        """, unsafe_allow_html=True)

        resume_status = "✅ Loaded" if st.session_state.resume_text else "❌ Not loaded"
        analysis_status = "✅ Complete" if st.session_state.resume_analysis else "⏳ Pending"
        jobs_count = len(st.session_state.job_results)

        st.markdown(f"""
            <div style="color:#e8e8f0;">Resume: {resume_status}</div>
            <div style="color:#e8e8f0; margin-top:0.5rem;">Analysis: {analysis_status}</div>
            <div style="color:#e8e8f0; margin-top:0.5rem;">Jobs Found: {jobs_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="color:#888; font-size:0.85rem; margin-bottom:0.75rem;">TECH STACK</div>
            <div style="color:#e8e8f0;">🐍 Python + Streamlit</div>
            <div style="color:#e8e8f0; margin-top:0.5rem;">🤖 OpenAI GPT-4o-mini</div>
            <div style="color:#e8e8f0; margin-top:0.5rem;">🌐 Selenium WebDriver</div>
            <div style="color:#e8e8f0; margin-top:0.5rem;">📦 PyPDF2 / pdfplumber</div>
        </div>
        """, unsafe_allow_html=True)

    # Data management
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🗑️ Data Management</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Clear Resume & Analysis", use_container_width=True):
            st.session_state.resume_text = ""
            st.session_state.resume_analysis = None
            st.session_state.job_results = []
            st.success("✅ Session data cleared.")
    with col2:
        if st.button("👤 Update Profile", use_container_width=True):
            st.info("Profile updates: edit your name/role in the users.json file.")