from dotenv import load_dotenv
import os
import sys
import importlib.util
import streamlit as st

# Load environment variables
load_dotenv()

# Validate required variables
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

# ── Fix: always add the folder that contains app.py to sys.path ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ── Helper: load any module from the pages/ sub-folder by name ──
def load_module(name):
    module_path = os.path.join(BASE_DIR, "pages", f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, module_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

st.set_page_config(
    page_title="CareerAI - Intelligent Career Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&display=swap');

    * { font-family: 'Space Grotesk', sans-serif; }
    h1, h2, h3 { font-family: 'Syne', sans-serif; }
    .stApp { background: #0a0a0f; color: #e8e8f0; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%);
        border-right: 1px solid #2a2a4a;
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        font-family: 'Syne', sans-serif;
    }

    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #2a2a4a;
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }

    .metric-card:hover {
        border-color: #667eea;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        font-family: 'Space Grotesk', sans-serif;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }

    .success-badge {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white; padding: 0.3rem 1rem;
        border-radius: 20px; font-size: 0.85rem; font-weight: 600;
    }

    .warning-badge {
        background: linear-gradient(135deg, #f7971e, #ffd200);
        color: #1a1a2e; padding: 0.3rem 1rem;
        border-radius: 20px; font-size: 0.85rem; font-weight: 600;
    }

    .danger-badge {
        background: linear-gradient(135deg, #eb3349, #f45c43);
        color: white; padding: 0.3rem 1rem;
        border-radius: 20px; font-size: 0.85rem; font-weight: 600;
    }

    .job-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 1px solid #2a2a4a; border-radius: 16px;
        padding: 1.5rem; margin-bottom: 1rem; transition: all 0.3s ease;
    }

    .job-card:hover {
        border-color: #667eea;
        box-shadow: 0 0 25px rgba(102, 126, 234, 0.15);
    }

    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }

    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: #1a1a2e; border: 1px solid #2a2a4a;
        color: #e8e8f0; border-radius: 10px;
    }

    .stSelectbox > div > div {
        background: #1a1a2e; border: 1px solid #2a2a4a; color: #e8e8f0;
    }

    .sidebar-nav-item {
        padding: 0.75rem 1rem; border-radius: 10px;
        margin: 0.25rem 0; cursor: pointer; transition: all 0.2s ease;
    }

    .sidebar-nav-item:hover { background: rgba(102, 126, 234, 0.2); }

    div[data-testid="stForm"] {
        background: #1a1a2e; border: 1px solid #2a2a4a;
        border-radius: 16px; padding: 2rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: #1a1a2e; border-radius: 10px; padding: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent; color: #888; border-radius: 8px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea, #764ba2); color: white;
    }

    .progress-bar-custom {
        background: linear-gradient(90deg, #667eea, #f093fb);
        height: 8px; border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ── Session state initialization ──
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user" not in st.session_state:
    st.session_state.user = None
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "resume_analysis" not in st.session_state:
    st.session_state.resume_analysis = None
if "job_results" not in st.session_state:
    st.session_state.job_results = []
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = os.getenv("OPENAI_API_KEY", "")

# ── Sidebar navigation ──
def show_sidebar():
    with st.sidebar:
        st.markdown('<p class="main-header" style="font-size:1.8rem;">🚀 CareerAI</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:#888; font-size:0.85rem; margin-top:-10px;">Intelligent Career Platform</p>', unsafe_allow_html=True)
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

        if st.session_state.authenticated:
            st.markdown(f'<p style="color:#667eea; font-weight:600;">👤 {st.session_state.user["name"]}</p>', unsafe_allow_html=True)
            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

            nav_pages = {
                "🏠 Dashboard": "dashboard",
                "📄 Resume Upload": "resume",
                "🧠 AI Insights": "insights",
                "💼 Job Recommendations": "jobs",
                "⚙️ Settings": "settings",
            }

            if "current_page" not in st.session_state:
                st.session_state.current_page = "dashboard"

            for label, page_id in nav_pages.items():
                if st.button(label, key=f"nav_{page_id}", use_container_width=True):
                    st.session_state.current_page = page_id
                    st.rerun()

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.user = None
                st.session_state.current_page = "login"
                st.rerun()
        else:
            if st.button("🔑 Login / Register", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()

        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#555; font-size:0.75rem; text-align:center;">Powered by OpenAI + Selenium<br/>© 2025 CareerAI</p>', unsafe_allow_html=True)

# ── Main routing ──
show_sidebar()

if not st.session_state.authenticated:
    auth = load_module("auth")
    auth.show()
else:
    page = st.session_state.get("current_page", "dashboard")
    if page == "dashboard":
        load_module("dashboard").show()
    elif page == "resume":
        load_module("resume").show()
    elif page == "insights":
        load_module("insights").show()
    elif page == "jobs":
        load_module("jobs").show()
    elif page == "settings":
        load_module("settings").show()
