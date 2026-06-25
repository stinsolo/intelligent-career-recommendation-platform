from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

# import streamlit as st
# import io
# import os

# def extract_text_from_pdf(pdf_file):
#     """Extract text from uploaded PDF file."""
#     try:
#         import PyPDF2
#         pdf_reader = PyPDF2.PdfReader(pdf_file)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text() + "\n"
#         return text.strip()
#     except ImportError:
#         try:
#             import pdfplumber
#             with pdfplumber.open(pdf_file) as pdf:
#                 text = ""
#                 for page in pdf.pages:
#                     text += (page.extract_text() or "") + "\n"
#             return text.strip()
#         except Exception as e:
#             return None
#     except Exception as e:
#         return None

# def show():
#     st.markdown("""
#     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
#         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
#         📄 Resume Upload & Analysis
#     </h1>
#     <p style="color:#888;">Upload your resume to begin the AI-powered career analysis</p>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     tab1, tab2 = st.tabs(["📤 Upload PDF", "✍️ Paste Text"])

#     with tab1:
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
#             border: 2px dashed rgba(102,126,234,0.4); border-radius: 16px; padding: 2rem; text-align:center; margin-bottom:1rem;">
#             <div style="font-size:3rem;">📎</div>
#             <p style="color:#888; margin:0.5rem 0 0;">Drag & drop your resume PDF or click to browse</p>
#         </div>
#         """, unsafe_allow_html=True)

#         uploaded_file = st.file_uploader(
#             "Choose PDF file",
#             type=["pdf"],
#             label_visibility="collapsed"
#         )

#         if uploaded_file:
#             st.markdown(f"""
#             <div style="background: rgba(56, 239, 125, 0.1); border: 1px solid rgba(56,239,125,0.4);
#                 border-radius: 12px; padding: 1rem; margin: 1rem 0;">
#                 <span style="color:#38ef7d;">✅ File uploaded:</span>
#                 <span style="color:#e8e8f0; margin-left:0.5rem; font-weight:600;">{uploaded_file.name}</span>
#                 <span style="color:#888; margin-left:1rem; font-size:0.85rem;">({uploaded_file.size / 1024:.1f} KB)</span>
#             </div>
#             """, unsafe_allow_html=True)

#             if st.button("🔍 Extract & Process Resume", use_container_width=True):
#                 with st.spinner("Extracting text from PDF..."):
#                     text = extract_text_from_pdf(io.BytesIO(uploaded_file.read()))

#                 if text and len(text) > 50:
#                     st.session_state.resume_text = text
#                     st.session_state.resume_analysis = None  # Reset previous analysis
#                     st.success("✅ Resume text extracted successfully!")
#                     st.markdown(f"""
#                     <div class="metric-card" style="margin-top:1rem;">
#                         <div style="color:#888; font-size:0.85rem;">Characters extracted</div>
#                         <div style="font-size:1.5rem; font-weight:700; color:#667eea;">{len(text):,}</div>
#                         <div style="color:#888; font-size:0.85rem; margin-top:0.25rem;">Words: ~{len(text.split()):,}</div>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.error("❌ Could not extract text. Try the 'Paste Text' tab or ensure the PDF contains selectable text.")

#     with tab2:
#         st.markdown('<p style="color:#888; margin-bottom:0.5rem;">Paste your resume content directly:</p>', unsafe_allow_html=True)

#         resume_text_input = st.text_area(
#             "Resume Text",
#             value=st.session_state.resume_text,
#             height=400,
#             placeholder="Paste your complete resume here...\n\nExample:\nJohn Doe\njohn@email.com | LinkedIn: linkedin.com/in/johndoe\n\nEXPERIENCE\nSoftware Engineer at TechCorp (2022-Present)\n- Developed REST APIs using Python/FastAPI\n- Led team of 4 engineers...",
#             label_visibility="collapsed"
#         )

#         col1, col2 = st.columns([3, 1])
#         with col1:
#             if st.button("💾 Save Resume Text", use_container_width=True):
#                 if len(resume_text_input.strip()) < 50:
#                     st.error("❌ Resume text is too short. Please provide more content.")
#                 else:
#                     st.session_state.resume_text = resume_text_input.strip()
#                     st.session_state.resume_analysis = None
#                     st.success("✅ Resume saved!")
#         with col2:
#             if st.button("🗑️ Clear", use_container_width=True):
#                 st.session_state.resume_text = ""
#                 st.session_state.resume_analysis = None
#                 st.rerun()

#     # Show current resume preview
#     if st.session_state.resume_text:
#         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">👁️ Resume Preview</h3>', unsafe_allow_html=True)

#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.markdown(f"""
#             <div class="metric-card" style="text-align:center;">
#                 <div style="color:#888; font-size:0.85rem;">Characters</div>
#                 <div style="font-size:1.5rem; font-weight:700; color:#667eea;">{len(st.session_state.resume_text):,}</div>
#             </div>
#             """, unsafe_allow_html=True)
#         with col2:
#             word_count = len(st.session_state.resume_text.split())
#             st.markdown(f"""
#             <div class="metric-card" style="text-align:center;">
#                 <div style="color:#888; font-size:0.85rem;">Words</div>
#                 <div style="font-size:1.5rem; font-weight:700; color:#764ba2;">{word_count:,}</div>
#             </div>
#             """, unsafe_allow_html=True)
#         with col3:
#             line_count = len(st.session_state.resume_text.splitlines())
#             st.markdown(f"""
#             <div class="metric-card" style="text-align:center;">
#                 <div style="color:#888; font-size:0.85rem;">Lines</div>
#                 <div style="font-size:1.5rem; font-weight:700; color:#f093fb;">{line_count:,}</div>
#             </div>
#             """, unsafe_allow_html=True)

#         with st.expander("📖 View Resume Content", expanded=False):
#             st.text(st.session_state.resume_text[:3000] + ("..." if len(st.session_state.resume_text) > 3000 else ""))

#         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, rgba(102,126,234,0.15), rgba(240,147,251,0.15));
#             border: 1px solid rgba(102,126,234,0.3); border-radius: 12px; padding: 1.25rem;">
#             <p style="color:#e8e8f0; font-weight:600; margin:0 0 0.5rem;">✨ Next Step</p>
#             <p style="color:#888; margin:0; font-size:0.9rem;">Your resume is ready! Head to <strong style="color:#667eea;">AI Insights</strong> to get comprehensive analysis and personalized recommendations.</p>
#         </div>
#         """, unsafe_allow_html=True)

#         if st.button("🧠 Analyze with AI →", use_container_width=True):
#             st.session_state.current_page = "insights"
#             st.rerun()
#     else:
#         st.markdown("""
#         <div style="margin-top:2rem; background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
#             border-radius: 12px; padding: 1.25rem; text-align:center;">
#             <p style="color:#f45c43; margin:0;">⚠️ No resume uploaded yet. Upload a PDF or paste your resume text above to get started.</p>
#         </div>
#         """, unsafe_allow_html=True)

import streamlit as st
import io
import os

def extract_text_from_pdf(pdf_bytes):
    """Try multiple PDF extraction methods for maximum compatibility."""
    text = ""

    # Method 1: pdfplumber (best quality)
    try:
        import pdfplumber
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        if text.strip():
            return text.strip(), "pdfplumber"
    except Exception:
        pass

    # Method 2: PyPDF2
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        if text.strip():
            return text.strip(), "PyPDF2"
    except Exception:
        pass

    # Method 3: pymupdf (fitz)
    try:
        import fitz
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            text += page.get_text() + "\n"
        doc.close()
        if text.strip():
            return text.strip(), "pymupdf"
    except Exception:
        pass

    # Method 4: pdfminer
    try:
        from pdfminer.high_level import extract_text_to_fp
        from pdfminer.layout import LAParams
        output = io.StringIO()
        extract_text_to_fp(io.BytesIO(pdf_bytes), output, laparams=LAParams())
        text = output.getvalue()
        if text.strip():
            return text.strip(), "pdfminer"
    except Exception:
        pass

    return None, None


def show():
    st.markdown("""
    <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        📄 Resume Upload & Analysis
    </h1>
    <p style="color:#888;">Upload your resume to begin the AI-powered career analysis</p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📤 Upload PDF", "✍️ Paste Text"])

    with tab1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
            border: 2px dashed rgba(102,126,234,0.4); border-radius: 16px; padding: 2rem; text-align:center; margin-bottom:1rem;">
            <div style="font-size:3rem;">📎</div>
            <p style="color:#888; margin:0.5rem 0 0;">Drag & drop your resume PDF or click to browse</p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose PDF file",
            type=["pdf"],
            label_visibility="collapsed"
        )

        if uploaded_file:
            st.markdown(f"""
            <div style="background: rgba(56, 239, 125, 0.1); border: 1px solid rgba(56,239,125,0.4);
                border-radius: 12px; padding: 1rem; margin: 1rem 0;">
                <span style="color:#38ef7d;">✅ File uploaded:</span>
                <span style="color:#e8e8f0; margin-left:0.5rem; font-weight:600;">{uploaded_file.name}</span>
                <span style="color:#888; margin-left:1rem; font-size:0.85rem;">({uploaded_file.size / 1024:.1f} KB)</span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🔍 Extract & Process Resume", use_container_width=True):
                pdf_bytes = uploaded_file.read()

                with st.spinner("Extracting text from PDF..."):
                    text, method = extract_text_from_pdf(pdf_bytes)

                if text and len(text.strip()) > 30:
                    st.session_state.resume_text = text.strip()
                    st.session_state.resume_analysis = None
                    st.success(f"✅ Resume extracted successfully using {method}!")
                    st.markdown(f"""
                    <div class="metric-card" style="margin-top:1rem;">
                        <div style="color:#888; font-size:0.85rem;">Characters extracted</div>
                        <div style="font-size:1.5rem; font-weight:700; color:#667eea;">{len(text):,}</div>
                        <div style="color:#888; font-size:0.85rem; margin-top:0.25rem;">Words: ~{len(text.split()):,}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("👁️ Preview extracted text", expanded=True):
                        st.text(text[:1000] + ("..." if len(text) > 1000 else ""))
                else:
                    st.error("❌ Could not extract text from this PDF.")
                    st.markdown("""
                    <div style="background: rgba(255,210,0,0.1); border: 1px solid rgba(255,210,0,0.3);
                        border-radius: 12px; padding: 1rem; margin-top:1rem;">
                        <p style="color:#ffd200; font-weight:600; margin:0 0 0.5rem;">💡 Why this happens:</p>
                        <ul style="color:#888; margin:0; padding-left:1.2rem;">
                            <li>Your PDF is a scanned image (not selectable text)</li>
                            <li>The PDF is password protected</li>
                            <li>The PDF uses an unusual font encoding</li>
                        </ul>
                        <p style="color:#888; margin:0.75rem 0 0;">
                            👉 Use the <strong style="color:#667eea;">Paste Text</strong> tab —
                            open your resume, select all (Ctrl+A), copy (Ctrl+C), paste it there.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("""
                    <div style="background: rgba(102,126,234,0.1); border: 1px solid rgba(102,126,234,0.3);
                        border-radius: 12px; padding: 1rem; margin-top:0.75rem;">
                        <p style="color:#667eea; font-weight:600; margin:0 0 0.5rem;">🛠️ Install better PDF libraries then restart:</p>
                        <code style="color:#f093fb;">pip install pdfplumber PyPDF2 pymupdf pdfminer.six</code>
                    </div>
                    """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<p style="color:#888; margin-bottom:0.5rem;">Paste your resume content directly — this always works!</p>', unsafe_allow_html=True)

        resume_text_input = st.text_area(
            "Resume Text",
            value=st.session_state.resume_text,
            height=400,
            placeholder="""Paste your full resume here...

Example:
surya
surya@email.com | LinkedIn: linkedin.com/in/surya | +91-701133453

SUMMARY
Experienced Software Engineer with 5+ years building scalable web applications...

EXPERIENCE
Software Engineer — TechCorp (2021–Present)
- Built REST APIs using Python/FastAPI serving 1M+ requests/day
- Led a team of 4 engineers to deliver projects on time

EDUCATION
B.S. Computer Science — State University (2019)

SKILLS
Python, JavaScript, React, SQL, Docker, AWS""",
            label_visibility="collapsed"
        )

        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("💾 Save Resume Text", use_container_width=True):
                if len(resume_text_input.strip()) < 30:
                    st.error("❌ Text is too short. Please paste your full resume.")
                else:
                    st.session_state.resume_text = resume_text_input.strip()
                    st.session_state.resume_analysis = None
                    st.success(f"✅ Resume saved! ({len(resume_text_input.split()):,} words)")
        with col2:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.resume_text = ""
                st.session_state.resume_analysis = None
                st.rerun()

    # Show current resume status
    if st.session_state.resume_text:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">✅ Resume Ready</h3>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="color:#888; font-size:0.85rem;">Characters</div>
                <div style="font-size:1.5rem; font-weight:700; color:#667eea;">{len(st.session_state.resume_text):,}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            word_count = len(st.session_state.resume_text.split())
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="color:#888; font-size:0.85rem;">Words</div>
                <div style="font-size:1.5rem; font-weight:700; color:#764ba2;">{word_count:,}</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            line_count = len(st.session_state.resume_text.splitlines())
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="color:#888; font-size:0.85rem;">Lines</div>
                <div style="font-size:1.5rem; font-weight:700; color:#f093fb;">{line_count:,}</div>
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 View Resume Content", expanded=False):
            st.text(st.session_state.resume_text[:3000] + ("..." if len(st.session_state.resume_text) > 3000 else ""))

        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        if st.button("🧠 Analyze with AI →", use_container_width=True):
            st.session_state.current_page = "insights"
            st.rerun()
    else:
        st.markdown("""
        <div style="margin-top:2rem; background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
            border-radius: 12px; padding: 1.25rem; text-align:center;">
            <p style="color:#f45c43; margin:0;">⚠️ No resume uploaded yet. Upload a PDF or paste your resume text above.</p>
        </div>
        """, unsafe_allow_html=True)
