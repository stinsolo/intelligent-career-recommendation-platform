from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

import streamlit as st
from datetime import datetime

def show():
    user = st.session_state.user
    hour = datetime.now().hour
    greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 17 else "Good evening"

    st.markdown(f"""
    <div style="padding: 2rem 0 1rem;">
        <h1 style="font-family:'Syne',sans-serif; color:#e8e8f0; margin:0;">
            {greeting}, <span style="background: linear-gradient(135deg, #667eea, #f093fb);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{user['name'].split()[0]}</span> 👋
        </h1>
        <p style="color:#888; margin-top:0.25rem;">Here's your career intelligence overview</p>
    </div>
    """, unsafe_allow_html=True)

    # Status cards
    has_resume = bool(st.session_state.resume_text)
    has_analysis = bool(st.session_state.resume_analysis)
    has_jobs = bool(st.session_state.job_results)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:2rem;">📄</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.5rem;">Resume Status</div>
            <div style="font-size:1.1rem; font-weight:700; color:{'#38ef7d' if has_resume else '#f45c43'}; margin-top:0.25rem;">
                {'Uploaded ✓' if has_resume else 'Not Uploaded'}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        score = st.session_state.resume_analysis.get("overall_score", "—") if has_analysis else "—"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:2rem;">🧠</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.5rem;">Resume Score</div>
            <div style="font-size:1.5rem; font-weight:700; color:#667eea; margin-top:0.25rem;">{score}/10</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        job_count = len(st.session_state.job_results)
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:2rem;">💼</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.5rem;">Jobs Found</div>
            <div style="font-size:1.5rem; font-weight:700; color:#f093fb; margin-top:0.25rem;">{job_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        api_status = "Connected ✓" if st.session_state.openai_api_key else "Not Set"
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:2rem;">🔑</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.5rem;">OpenAI API</div>
            <div style="font-size:1.1rem; font-weight:700; color:{'#38ef7d' if st.session_state.openai_api_key else '#f45c43'}; margin-top:0.25rem;">
                {api_status}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # Quick actions
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">⚡ Quick Actions</h3>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card" style="text-align:center; cursor:pointer;">
            <div style="font-size:2.5rem;">📤</div>
            <div style="font-weight:600; margin-top:0.5rem; color:#e8e8f0;">Upload Resume</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.25rem;">Start your analysis journey</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Resume Upload →", key="quick_resume", use_container_width=True):
            st.session_state.current_page = "resume"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="metric-card" style="text-align:center; cursor:pointer;">
            <div style="font-size:2.5rem;">🔍</div>
            <div style="font-weight:600; margin-top:0.5rem; color:#e8e8f0;">Analyze Resume</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.25rem;">Get AI-powered insights</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to AI Insights →", key="quick_insights", use_container_width=True):
            st.session_state.current_page = "insights"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="metric-card" style="text-align:center; cursor:pointer;">
            <div style="font-size:2.5rem;">🎯</div>
            <div style="font-weight:600; margin-top:0.5rem; color:#e8e8f0;">Find Jobs</div>
            <div style="color:#888; font-size:0.85rem; margin-top:0.25rem;">Personalized job matching</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Jobs →", key="quick_jobs", use_container_width=True):
            st.session_state.current_page = "jobs"
            st.rerun()

    # How it works section
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🗺️ How CareerAI Works</h3>', unsafe_allow_html=True)

    steps = [
        ("1", "Upload Resume", "Upload your PDF or paste your resume text for processing", "#667eea"),
        ("2", "AI Analysis", "Our LLM engine extracts skills, strengths, and improvement areas", "#764ba2"),
        ("3", "Job Scraping", "Selenium scrapes LinkedIn for relevant, real-time job postings", "#f093fb"),
        ("4", "Smart Matching", "Jobs are ranked by compatibility with your unique profile", "#38ef7d"),
    ]

    cols = st.columns(4)
    for col, (num, title, desc, color) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="width:40px; height:40px; border-radius:50%; background:{color};
                    display:flex; align-items:center; justify-content:center; margin:0 auto;
                    font-weight:800; color:white; font-size:1.1rem;">{num}</div>
                <div style="font-weight:600; margin-top:0.75rem; color:#e8e8f0;">{title}</div>
                <div style="color:#888; font-size:0.82rem; margin-top:0.25rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # Recent analysis preview
    if has_analysis:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">📊 Latest Analysis Snapshot</h3>', unsafe_allow_html=True)

        analysis = st.session_state.resume_analysis
        col1, col2 = st.columns(2)

        with col1:
            strengths = analysis.get("strengths", [])
            if strengths:
                st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                st.markdown("**💪 Top Strengths**")
                for s in strengths[:3]:
                    st.markdown(f"✅ {s}")
                st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            gaps = analysis.get("gaps", [])
            if gaps:
                st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                st.markdown("**⚠️ Areas to Improve**")
                for g in gaps[:3]:
                    st.markdown(f"🔸 {g}")
                st.markdown('</div>', unsafe_allow_html=True)