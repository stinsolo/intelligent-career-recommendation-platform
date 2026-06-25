from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

# # # import streamlit as st
# # # import json
# # # import re

# # # def call_openai_analysis(resume_text, api_key):
# # #     """Call OpenAI API for resume analysis."""
# # #     try:
# # #         from openai import OpenAI
# # #         client = OpenAI(api_key=api_key)

# # #         prompt = f"""You are an expert career counselor and resume analyst. Analyze the following resume comprehensively and return a JSON object with this exact structure:

# # # {{
# # #   "candidate_name": "extracted name or 'Not found'",
# # #   "current_role": "current or most recent job title",
# # #   "experience_years": number (integer estimate),
# # #   "overall_score": number (1-10),
# # #   "summary": "2-3 sentence professional summary",
# # #   "skills": {{
# # #     "technical": ["skill1", "skill2", ...],
# # #     "soft": ["skill1", "skill2", ...],
# # #     "tools": ["tool1", "tool2", ...]
# # #   }},
# # #   "strengths": ["strength1", "strength2", "strength3", "strength4", "strength5"],
# # #   "gaps": ["gap1", "gap2", "gap3", "gap4"],
# # #   "recommendations": [
# # #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "High/Medium/Low"}},
# # #     ...at least 5 recommendations
# # #   ],
# # #   "target_roles": ["role1", "role2", "role3", "role4", "role5"],
# # #   "industry_fit": ["industry1", "industry2", "industry3"],
# # #   "education": "highest education level and field",
# # #   "ats_score": number (1-10, ATS compatibility),
# # #   "formatting_score": number (1-10),
# # #   "content_score": number (1-10),
# # #   "keywords_missing": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
# # #   "certifications_recommended": ["cert1", "cert2", "cert3"]
# # # }}

# # # Return ONLY valid JSON, no markdown, no explanation.

# # # RESUME:
# # # {resume_text[:4000]}"""

# # #         response = client.chat.completions.create(
# # #             model="gpt-4o-mini",
# # #             messages=[{"role": "user", "content": prompt}],
# # #             temperature=0.3,
# # #             max_tokens=2000
# # #         )

# # #         raw = response.choices[0].message.content.strip()
# # #         # Clean JSON
# # #         raw = re.sub(r'^```json\s*', '', raw)
# # #         raw = re.sub(r'\s*```$', '', raw)
# # #         return json.loads(raw), None

# # #     except ImportError:
# # #         return None, "OpenAI library not installed. Run: pip install openai"
# # #     except json.JSONDecodeError as e:
# # #         return None, f"Failed to parse AI response: {str(e)}"
# # #     except Exception as e:
# # #         return None, str(e)


# # # def score_color(score, max_score=10):
# # #     pct = score / max_score
# # #     if pct >= 0.75:
# # #         return "#38ef7d"
# # #     elif pct >= 0.5:
# # #         return "#ffd200"
# # #     else:
# # #         return "#f45c43"


# # # def score_bar(score, max_score=10, label=""):
# # #     pct = (score / max_score) * 100
# # #     color = score_color(score, max_score)
# # #     return f"""
# # #     <div style="margin-bottom:1rem;">
# # #         <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
# # #             <span style="color:#e8e8f0; font-size:0.9rem;">{label}</span>
# # #             <span style="color:{color}; font-weight:700;">{score}/{max_score}</span>
# # #         </div>
# # #         <div style="background:#1a1a2e; border-radius:4px; height:8px; overflow:hidden;">
# # #             <div style="width:{pct}%; background:linear-gradient(90deg, #667eea, {color}); height:100%; border-radius:4px; transition:width 1s ease;"></div>
# # #         </div>
# # #     </div>
# # #     """


# # # def show():
# # #     st.markdown("""
# # #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# # #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# # #         🧠 AI-Powered Resume Insights
# # #     </h1>
# # #     <p style="color:#888;">Comprehensive AI analysis of your resume with actionable recommendations</p>
# # #     """, unsafe_allow_html=True)

# # #     if not st.session_state.resume_text:
# # #         st.markdown("""
# # #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# # #             border-radius: 12px; padding: 2rem; text-align:center; margin-top:2rem;">
# # #             <div style="font-size:3rem;">📄</div>
# # #             <h3 style="color:#f45c43; font-family:Syne,sans-serif;">No Resume Found</h3>
# # #             <p style="color:#888;">Please upload your resume first before running the analysis.</p>
# # #         </div>
# # #         """, unsafe_allow_html=True)
# # #         if st.button("📤 Go to Resume Upload", use_container_width=True):
# # #             st.session_state.current_page = "resume"
# # #             st.rerun()
# # #         return

# # #     if not st.session_state.openai_api_key:
# # #         st.markdown("""
# # #         <div style="background: rgba(255,210,0,0.1); border: 1px solid rgba(255,210,0,0.4);
# # #             border-radius: 12px; padding: 1.5rem; margin-bottom:1rem;">
# # #             <p style="color:#ffd200; font-weight:600; margin:0 0 0.5rem;">⚠️ OpenAI API Key Required</p>
# # #             <p style="color:#888; margin:0; font-size:0.9rem;">Please add your OpenAI API key in Settings to enable AI analysis.</p>
# # #         </div>
# # #         """, unsafe_allow_html=True)
# # #         if st.button("⚙️ Go to Settings", use_container_width=True):
# # #             st.session_state.current_page = "settings"
# # #             st.rerun()
# # #         return

# # #     # Analyze button
# # #     col1, col2 = st.columns([3, 1])
# # #     with col1:
# # #         if st.button("🚀 Run Full AI Analysis", use_container_width=True):
# # #             with st.spinner("🧠 Analyzing your resume with AI... This may take 15-30 seconds..."):
# # #                 analysis, error = call_openai_analysis(
# # #                     st.session_state.resume_text,
# # #                     st.session_state.openai_api_key
# # #                 )
# # #                 if error:
# # #                     st.error(f"❌ Analysis failed: {error}")
# # #                 else:
# # #                     st.session_state.resume_analysis = analysis
# # #                     st.success("✅ Analysis complete!")
# # #                     st.rerun()

# # #     with col2:
# # #         if st.session_state.resume_analysis and st.button("🔄 Re-analyze", use_container_width=True):
# # #             st.session_state.resume_analysis = None
# # #             st.rerun()

# # #     # Show results
# # #     if not st.session_state.resume_analysis:
# # #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# # #         st.markdown("""
# # #         <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
# # #             border: 1px solid rgba(102,126,234,0.2); border-radius: 16px; padding: 2rem; text-align:center;">
# # #             <div style="font-size:3rem;">✨</div>
# # #             <h3 style="color:#e8e8f0; font-family:Syne,sans-serif;">Ready to Analyze</h3>
# # #             <p style="color:#888;">Click the button above to get your comprehensive AI-powered resume analysis.</p>
# # #             <p style="color:#667eea; font-size:0.85rem;">Resume loaded: {chars} characters</p>
# # #         </div>
# # #         """.replace("{chars}", f"{len(st.session_state.resume_text):,}"), unsafe_allow_html=True)
# # #         return

# # #     a = st.session_state.resume_analysis

# # #     # Header info
# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns([2, 1])
# # #     with col1:
# # #         st.markdown(f"""
# # #         <div class="metric-card">
# # #             <h2 style="font-family:Syne,sans-serif; color:#e8e8f0; margin:0 0 0.25rem;">{a.get('candidate_name', 'Candidate')}</h2>
# # #             <p style="color:#667eea; font-weight:600; margin:0 0 0.75rem;">{a.get('current_role', 'Professional')}</p>
# # #             <p style="color:#888; font-size:0.9rem; margin:0;">{a.get('summary', '')}</p>
# # #             <div style="margin-top:1rem; display:flex; gap:1rem; flex-wrap:wrap;">
# # #                 <span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
# # #                     🎓 {a.get('education', 'N/A')}
# # #                 </span>
# # #                 <span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
# # #                     ⏱️ {a.get('experience_years', 0)} years exp.
# # #                 </span>
# # #             </div>
# # #         </div>
# # #         """, unsafe_allow_html=True)

# # #     with col2:
# # #         overall = a.get('overall_score', 5)
# # #         color = score_color(overall)
# # #         st.markdown(f"""
# # #         <div class="metric-card" style="text-align:center; height:100%;">
# # #             <p style="color:#888; margin:0 0 0.5rem; font-size:0.85rem;">OVERALL SCORE</p>
# # #             <div style="font-size:4rem; font-weight:800; color:{color}; line-height:1;">{overall}</div>
# # #             <div style="color:#888; font-size:1rem;">/10</div>
# # #             <div style="margin-top:1rem; font-size:0.85rem; color:{color};">
# # #                 {'⭐ Excellent' if overall >= 8 else '👍 Good' if overall >= 6 else '⚠️ Needs Work' if overall >= 4 else '❌ Major Revision Needed'}
# # #             </div>
# # #         </div>
# # #         """, unsafe_allow_html=True)

# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # #     # Score breakdown
# # #     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">📊 Score Breakdown</h3>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         scores_html = ""
# # #         scores_html += score_bar(a.get('ats_score', 5), 10, "🤖 ATS Compatibility")
# # #         scores_html += score_bar(a.get('content_score', 5), 10, "📝 Content Quality")
# # #         scores_html += score_bar(a.get('formatting_score', 5), 10, "🎨 Formatting & Structure")
# # #         st.markdown(f'<div class="metric-card">{scores_html}</div>', unsafe_allow_html=True)

# # #     with col2:
# # #         # Skills display
# # #         skills = a.get('skills', {})
# # #         tech_skills = skills.get('technical', [])
# # #         soft_skills = skills.get('soft', [])
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         st.markdown("**🛠️ Technical Skills**")
# # #         if tech_skills:
# # #             badges = " ".join([f'<span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>' for s in tech_skills[:8]])
# # #             st.markdown(badges, unsafe_allow_html=True)
# # #         st.markdown("**🤝 Soft Skills**", unsafe_allow_html=False)
# # #         if soft_skills:
# # #             badges = " ".join([f'<span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>' for s in soft_skills[:6]])
# # #             st.markdown(badges, unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # #     # Strengths & Gaps
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#38ef7d;">💪 Strengths</h3>', unsafe_allow_html=True)
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         for s in a.get('strengths', []):
# # #             st.markdown(f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">✅ {s}</div>', unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     with col2:
# # #         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#ffd200;">⚠️ Gaps & Areas to Improve</h3>', unsafe_allow_html=True)
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         for g in a.get('gaps', []):
# # #             st.markdown(f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">🔸 {g}</div>', unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # #     # Recommendations
# # #     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Personalized Recommendations</h3>', unsafe_allow_html=True)
# # #     recs = a.get('recommendations', [])
# # #     for rec in recs:
# # #         priority = rec.get('priority', 'Medium')
# # #         priority_colors = {"High": "#f45c43", "Medium": "#ffd200", "Low": "#38ef7d"}
# # #         p_color = priority_colors.get(priority, "#888")
# # #         st.markdown(f"""
# # #         <div class="metric-card" style="margin-bottom:0.75rem;">
# # #             <div style="display:flex; justify-content:space-between; align-items:center;">
# # #                 <span style="font-weight:600; color:#e8e8f0;">{rec.get('area', 'General')}</span>
# # #                 <span style="background:{p_color}22; color:{p_color}; padding:0.2rem 0.75rem; border-radius:12px; font-size:0.8rem; font-weight:600;">{priority} Priority</span>
# # #             </div>
# # #             <p style="color:#888; margin: 0.5rem 0 0; font-size:0.9rem;">💡 {rec.get('suggestion', '')}</p>
# # #         </div>
# # #         """, unsafe_allow_html=True)

# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # #     # Target roles & Keywords
# # #     col1, col2, col3 = st.columns(3)
# # #     with col1:
# # #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Target Roles</h4>', unsafe_allow_html=True)
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         for role in a.get('target_roles', []):
# # #             st.markdown(f'<div style="padding:0.4rem 0; color:#667eea; border-bottom:1px solid #2a2a4a;">→ {role}</div>', unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     with col2:
# # #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🏢 Industry Fit</h4>', unsafe_allow_html=True)
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         for ind in a.get('industry_fit', []):
# # #             st.markdown(f'<div style="padding:0.4rem 0; color:#f093fb; border-bottom:1px solid #2a2a4a;">→ {ind}</div>', unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     with col3:
# # #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🔑 Missing Keywords</h4>', unsafe_allow_html=True)
# # #         st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# # #         for kw in a.get('keywords_missing', []):
# # #             st.markdown(f'<div style="padding:0.4rem 0; color:#ffd200; border-bottom:1px solid #2a2a4a;">+ {kw}</div>', unsafe_allow_html=True)
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     # Recommended certs
# # #     certs = a.get('certifications_recommended', [])
# # #     if certs:
# # #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# # #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">📜 Recommended Certifications</h4>', unsafe_allow_html=True)
# # #         cols = st.columns(min(len(certs), 3))
# # #         for i, cert in enumerate(certs[:3]):
# # #             with cols[i]:
# # #                 st.markdown(f"""
# # #                 <div class="metric-card" style="text-align:center;">
# # #                     <div style="font-size:1.5rem;">🏅</div>
# # #                     <div style="color:#e8e8f0; font-weight:600; margin-top:0.5rem; font-size:0.9rem;">{cert}</div>
# # #                 </div>
# # #                 """, unsafe_allow_html=True)

# # #     # CTA
# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# # #     if st.button("💼 Find Matching Jobs →", use_container_width=True):
# # #         st.session_state.current_page = "jobs"
# # #         st.rerun()


# # import streamlit as st
# # import json
# # import re
# # import os

# # def get_groq_client():
# #     """Get Groq client using OpenAI-compatible SDK."""
# #     from openai import OpenAI
# #     api_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
# #     client = OpenAI(
# #         api_key=api_key,
# #         base_url="https://api.groq.com/openai/v1"
# #     )
# #     return client

# # def call_analysis(resume_text):
# #     """Call Groq API for resume analysis."""
# #     try:
# #         client = get_groq_client()

# #         prompt = f"""You are an expert career counselor and resume analyst. Analyze the following resume comprehensively and return a JSON object with this exact structure:

# # {{
# #   "candidate_name": "extracted name or 'Not found'",
# #   "current_role": "current or most recent job title",
# #   "experience_years": 0,
# #   "overall_score": 7,
# #   "summary": "2-3 sentence professional summary",
# #   "skills": {{
# #     "technical": ["skill1", "skill2"],
# #     "soft": ["skill1", "skill2"],
# #     "tools": ["tool1", "tool2"]
# #   }},
# #   "strengths": ["strength1", "strength2", "strength3", "strength4", "strength5"],
# #   "gaps": ["gap1", "gap2", "gap3", "gap4"],
# #   "recommendations": [
# #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "High"}},
# #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Medium"}},
# #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Low"}},
# #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "High"}},
# #     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Medium"}}
# #   ],
# #   "target_roles": ["role1", "role2", "role3", "role4", "role5"],
# #   "industry_fit": ["industry1", "industry2", "industry3"],
# #   "education": "highest education level and field",
# #   "ats_score": 7,
# #   "formatting_score": 7,
# #   "content_score": 7,
# #   "keywords_missing": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
# #   "certifications_recommended": ["cert1", "cert2", "cert3"]
# # }}

# # Return ONLY valid JSON. No markdown, no explanation, no code blocks.

# # RESUME:
# # {resume_text[:4000]}"""

# #         response = client.chat.completions.create(
# #             model="llama3-8b-8192",
# #             messages=[{"role": "user", "content": prompt}],
# #             temperature=0.3,
# #             max_tokens=2000
# #         )

# #         raw = response.choices[0].message.content.strip()
# #         # Clean any accidental markdown
# #         raw = re.sub(r'^```json\s*', '', raw)
# #         raw = re.sub(r'^```\s*', '', raw)
# #         raw = re.sub(r'\s*```$', '', raw)
# #         raw = raw.strip()

# #         return json.loads(raw), None

# #     except ImportError:
# #         return None, "OpenAI library not installed. Run: pip install openai"
# #     except json.JSONDecodeError as e:
# #         return None, f"Failed to parse AI response: {str(e)}"
# #     except Exception as e:
# #         return None, str(e)


# # def score_color(score, max_score=10):
# #     pct = score / max_score
# #     if pct >= 0.75:
# #         return "#38ef7d"
# #     elif pct >= 0.5:
# #         return "#ffd200"
# #     else:
# #         return "#f45c43"


# # def score_bar(score, max_score=10, label=""):
# #     pct = (score / max_score) * 100
# #     color = score_color(score, max_score)
# #     return f"""
# #     <div style="margin-bottom:1rem;">
# #         <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
# #             <span style="color:#e8e8f0; font-size:0.9rem;">{label}</span>
# #             <span style="color:{color}; font-weight:700;">{score}/{max_score}</span>
# #         </div>
# #         <div style="background:#1a1a2e; border-radius:4px; height:8px; overflow:hidden;">
# #             <div style="width:{pct}%; background:linear-gradient(90deg, #667eea, {color}); height:100%; border-radius:4px;"></div>
# #         </div>
# #     </div>
# #     """


# # def show():
# #     st.markdown("""
# #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# #         🧠 AI-Powered Resume Insights
# #     </h1>
# #     <p style="color:#888;">Comprehensive AI analysis of your resume with actionable recommendations</p>
# #     """, unsafe_allow_html=True)

# #     # Check resume
# #     if not st.session_state.resume_text:
# #         st.markdown("""
# #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# #             border-radius: 12px; padding: 2rem; text-align:center; margin-top:2rem;">
# #             <div style="font-size:3rem;">📄</div>
# #             <h3 style="color:#f45c43; font-family:Syne,sans-serif;">No Resume Found</h3>
# #             <p style="color:#888;">Please upload your resume first.</p>
# #         </div>
# #         """, unsafe_allow_html=True)
# #         if st.button("📤 Go to Resume Upload", use_container_width=True):
# #             st.session_state.current_page = "resume"
# #             st.rerun()
# #         return

# #     # Check API key
# #     groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
# #     if not groq_key:
# #         st.markdown("""
# #         <div style="background: rgba(255,210,0,0.1); border: 1px solid rgba(255,210,0,0.4);
# #             border-radius: 12px; padding: 1.5rem; margin-bottom:1rem;">
# #             <p style="color:#ffd200; font-weight:600; margin:0 0 0.5rem;">⚠️ Groq API Key Required</p>
# #             <p style="color:#888; margin:0;">Get a free key at <strong>console.groq.com</strong> and add it to your <code>.env</code> file as:<br/>
# #             <code style="color:#f093fb;">GROQ_API_KEY=gsk_your_key_here</code></p>
# #         </div>
# #         """, unsafe_allow_html=True)
# #         if st.button("⚙️ Go to Settings", use_container_width=True):
# #             st.session_state.current_page = "settings"
# #             st.rerun()
# #         return

# #     # Analyze button
# #     col1, col2 = st.columns([3, 1])
# #     with col1:
# #         if st.button("🚀 Run Full AI Analysis", use_container_width=True):
# #             with st.spinner("🧠 Analyzing your resume with Groq AI... Please wait..."):
# #                 analysis, error = call_analysis(st.session_state.resume_text)
# #                 if error:
# #                     st.error(f"❌ Analysis failed: {error}")
# #                 else:
# #                     st.session_state.resume_analysis = analysis
# #                     st.success("✅ Analysis complete!")
# #                     st.rerun()
# #     with col2:
# #         if st.session_state.resume_analysis:
# #             if st.button("🔄 Re-analyze", use_container_width=True):
# #                 st.session_state.resume_analysis = None
# #                 st.rerun()

# #     # Placeholder before analysis
# #     if not st.session_state.resume_analysis:
# #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# #         st.markdown(f"""
# #         <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
# #             border: 1px solid rgba(102,126,234,0.2); border-radius: 16px; padding: 2rem; text-align:center;">
# #             <div style="font-size:3rem;">✨</div>
# #             <h3 style="color:#e8e8f0; font-family:Syne,sans-serif;">Ready to Analyze</h3>
# #             <p style="color:#888;">Click the button above to get your AI-powered resume analysis.</p>
# #             <p style="color:#667eea; font-size:0.85rem;">Resume loaded: {len(st.session_state.resume_text):,} characters</p>
# #         </div>
# #         """, unsafe_allow_html=True)
# #         return

# #     a = st.session_state.resume_analysis

# #     # ── Header ──
# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# #     col1, col2 = st.columns([2, 1])
# #     with col1:
# #         st.markdown(f"""
# #         <div class="metric-card">
# #             <h2 style="font-family:Syne,sans-serif; color:#e8e8f0; margin:0 0 0.25rem;">{a.get('candidate_name', 'Candidate')}</h2>
# #             <p style="color:#667eea; font-weight:600; margin:0 0 0.75rem;">{a.get('current_role', 'Professional')}</p>
# #             <p style="color:#888; font-size:0.9rem; margin:0;">{a.get('summary', '')}</p>
# #             <div style="margin-top:1rem; display:flex; gap:1rem; flex-wrap:wrap;">
# #                 <span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
# #                     🎓 {a.get('education', 'N/A')}
# #                 </span>
# #                 <span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
# #                     ⏱️ {a.get('experience_years', 0)} years exp.
# #                 </span>
# #             </div>
# #         </div>
# #         """, unsafe_allow_html=True)

# #     with col2:
# #         overall = a.get('overall_score', 5)
# #         color = score_color(overall)
# #         st.markdown(f"""
# #         <div class="metric-card" style="text-align:center;">
# #             <p style="color:#888; margin:0 0 0.5rem; font-size:0.85rem;">OVERALL SCORE</p>
# #             <div style="font-size:4rem; font-weight:800; color:{color}; line-height:1;">{overall}</div>
# #             <div style="color:#888; font-size:1rem;">/10</div>
# #             <div style="margin-top:1rem; font-size:0.85rem; color:{color};">
# #                 {'⭐ Excellent' if overall >= 8 else '👍 Good' if overall >= 6 else '⚠️ Needs Work' if overall >= 4 else '❌ Major Revision'}
# #             </div>
# #         </div>
# #         """, unsafe_allow_html=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# #     # ── Score Breakdown + Skills ──
# #     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">📊 Score Breakdown</h3>', unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         scores_html = (
# #             score_bar(a.get('ats_score', 5), 10, "🤖 ATS Compatibility") +
# #             score_bar(a.get('content_score', 5), 10, "📝 Content Quality") +
# #             score_bar(a.get('formatting_score', 5), 10, "🎨 Formatting & Structure")
# #         )
# #         st.markdown(f'<div class="metric-card">{scores_html}</div>', unsafe_allow_html=True)

# #     with col2:
# #         skills = a.get('skills', {})
# #         tech_skills = skills.get('technical', [])
# #         soft_skills = skills.get('soft', [])
# #         tech_badges = " ".join([
# #             f'<span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>'
# #             for s in tech_skills[:8]
# #         ])
# #         soft_badges = " ".join([
# #             f'<span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>'
# #             for s in soft_skills[:6]
# #         ])
# #         st.markdown(f"""
# #         <div class="metric-card">
# #             <p style="color:#e8e8f0; font-weight:600; margin:0 0 0.5rem;">🛠️ Technical Skills</p>
# #             <div style="margin-bottom:1rem;">{tech_badges}</div>
# #             <p style="color:#e8e8f0; font-weight:600; margin:0 0 0.5rem;">🤝 Soft Skills</p>
# #             <div>{soft_badges}</div>
# #         </div>
# #         """, unsafe_allow_html=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# #     # ── Strengths & Gaps ──
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#38ef7d;">💪 Strengths</h3>', unsafe_allow_html=True)
# #         items = "".join([f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">✅ {s}</div>' for s in a.get('strengths', [])])
# #         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

# #     with col2:
# #         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#ffd200;">⚠️ Gaps to Improve</h3>', unsafe_allow_html=True)
# #         items = "".join([f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">🔸 {g}</div>' for g in a.get('gaps', [])])
# #         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# #     # ── Recommendations ──
# #     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Personalized Recommendations</h3>', unsafe_allow_html=True)
# #     priority_colors = {"High": "#f45c43", "Medium": "#ffd200", "Low": "#38ef7d"}
# #     for rec in a.get('recommendations', []):
# #         p = rec.get('priority', 'Medium')
# #         pc = priority_colors.get(p, "#888")
# #         st.markdown(f"""
# #         <div class="metric-card" style="margin-bottom:0.75rem;">
# #             <div style="display:flex; justify-content:space-between; align-items:center;">
# #                 <span style="font-weight:600; color:#e8e8f0;">{rec.get('area', 'General')}</span>
# #                 <span style="background:{pc}22; color:{pc}; padding:0.2rem 0.75rem; border-radius:12px; font-size:0.8rem; font-weight:600;">{p} Priority</span>
# #             </div>
# #             <p style="color:#888; margin:0.5rem 0 0; font-size:0.9rem;">💡 {rec.get('suggestion', '')}</p>
# #         </div>
# #         """, unsafe_allow_html=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# #     # ── Target Roles / Industries / Keywords ──
# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Target Roles</h4>', unsafe_allow_html=True)
# #         items = "".join([f'<div style="padding:0.4rem 0; color:#667eea; border-bottom:1px solid #2a2a4a;">→ {r}</div>' for r in a.get('target_roles', [])])
# #         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

# #     with col2:
# #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🏢 Industry Fit</h4>', unsafe_allow_html=True)
# #         items = "".join([f'<div style="padding:0.4rem 0; color:#f093fb; border-bottom:1px solid #2a2a4a;">→ {i}</div>' for i in a.get('industry_fit', [])])
# #         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

# #     with col3:
# #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🔑 Missing Keywords</h4>', unsafe_allow_html=True)
# #         items = "".join([f'<div style="padding:0.4rem 0; color:#ffd200; border-bottom:1px solid #2a2a4a;">+ {k}</div>' for k in a.get('keywords_missing', [])])
# #         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

# #     # ── Certifications ──
# #     certs = a.get('certifications_recommended', [])
# #     if certs:
# #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# #         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">📜 Recommended Certifications</h4>', unsafe_allow_html=True)
# #         cols = st.columns(min(len(certs), 3))
# #         for i, cert in enumerate(certs[:3]):
# #             with cols[i]:
# #                 st.markdown(f"""
# #                 <div class="metric-card" style="text-align:center;">
# #                     <div style="font-size:1.5rem;">🏅</div>
# #                     <div style="color:#e8e8f0; font-weight:600; margin-top:0.5rem; font-size:0.9rem;">{cert}</div>
# #                 </div>
# #                 """, unsafe_allow_html=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# #     if st.button("💼 Find Matching Jobs →", use_container_width=True):
# #         st.session_state.current_page = "jobs"
# #         st.rerun()



# import streamlit as st
# import json
# import re
# import os

# def get_groq_client():
#     """Get Groq client using OpenAI-compatible SDK."""
#     from openai import OpenAI
#     api_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
#     client = OpenAI(
#         api_key=api_key,
#         base_url="https://api.groq.com/openai/v1"
#     )
#     return client

# def call_analysis(resume_text):
#     """Call Groq API for resume analysis."""
#     try:
#         client = get_groq_client()

#         prompt = f"""You are an expert career counselor and resume analyst. Analyze the following resume comprehensively and return a JSON object with this exact structure:

# {{
#   "candidate_name": "extracted name or 'Not found'",
#   "current_role": "current or most recent job title",
#   "experience_years": 0,
#   "overall_score": 7,
#   "summary": "2-3 sentence professional summary",
#   "skills": {{
#     "technical": ["skill1", "skill2"],
#     "soft": ["skill1", "skill2"],
#     "tools": ["tool1", "tool2"]
#   }},
#   "strengths": ["strength1", "strength2", "strength3", "strength4", "strength5"],
#   "gaps": ["gap1", "gap2", "gap3", "gap4"],
#   "recommendations": [
#     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "High"}},
#     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Medium"}},
#     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Low"}},
#     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "High"}},
#     {{"area": "area name", "suggestion": "specific actionable suggestion", "priority": "Medium"}}
#   ],
#   "target_roles": ["role1", "role2", "role3", "role4", "role5"],
#   "industry_fit": ["industry1", "industry2", "industry3"],
#   "education": "highest education level and field",
#   "ats_score": 7,
#   "formatting_score": 7,
#   "content_score": 7,
#   "keywords_missing": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
#   "certifications_recommended": ["cert1", "cert2", "cert3"]
# }}

# Return ONLY valid JSON. No markdown, no explanation, no code blocks.

# RESUME:
# {resume_text[:4000]}"""

#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.3,
#             max_tokens=2000
#         )

#         raw = response.choices[0].message.content.strip()
#         # Clean any accidental markdown
#         raw = re.sub(r'^```json\s*', '', raw)
#         raw = re.sub(r'^```\s*', '', raw)
#         raw = re.sub(r'\s*```$', '', raw)
#         raw = raw.strip()

#         return json.loads(raw), None

#     except ImportError:
#         return None, "OpenAI library not installed. Run: pip install openai"
#     except json.JSONDecodeError as e:
#         return None, f"Failed to parse AI response: {str(e)}"
#     except Exception as e:
#         return None, str(e)


# def score_color(score, max_score=10):
#     pct = score / max_score
#     if pct >= 0.75:
#         return "#38ef7d"
#     elif pct >= 0.5:
#         return "#ffd200"
#     else:
#         return "#f45c43"


# def score_bar(score, max_score=10, label=""):
#     pct = (score / max_score) * 100
#     color = score_color(score, max_score)
#     return f"""
#     <div style="margin-bottom:1rem;">
#         <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
#             <span style="color:#e8e8f0; font-size:0.9rem;">{label}</span>
#             <span style="color:{color}; font-weight:700;">{score}/{max_score}</span>
#         </div>
#         <div style="background:#1a1a2e; border-radius:4px; height:8px; overflow:hidden;">
#             <div style="width:{pct}%; background:linear-gradient(90deg, #667eea, {color}); height:100%; border-radius:4px;"></div>
#         </div>
#     </div>
#     """


# def show():
#     st.markdown("""
#     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
#         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
#         🧠 AI-Powered Resume Insights
#     </h1>
#     <p style="color:#888;">Comprehensive AI analysis of your resume with actionable recommendations</p>
#     """, unsafe_allow_html=True)

#     # Check resume
#     if not st.session_state.resume_text:
#         st.markdown("""
#         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
#             border-radius: 12px; padding: 2rem; text-align:center; margin-top:2rem;">
#             <div style="font-size:3rem;">📄</div>
#             <h3 style="color:#f45c43; font-family:Syne,sans-serif;">No Resume Found</h3>
#             <p style="color:#888;">Please upload your resume first.</p>
#         </div>
#         """, unsafe_allow_html=True)
#         if st.button("📤 Go to Resume Upload", use_container_width=True):
#             st.session_state.current_page = "resume"
#             st.rerun()
#         return

#     # Check API key
#     groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
#     if not groq_key:
#         st.markdown("""
#         <div style="background: rgba(255,210,0,0.1); border: 1px solid rgba(255,210,0,0.4);
#             border-radius: 12px; padding: 1.5rem; margin-bottom:1rem;">
#             <p style="color:#ffd200; font-weight:600; margin:0 0 0.5rem;">⚠️ Groq API Key Required</p>
#             <p style="color:#888; margin:0;">Get a free key at <strong>console.groq.com</strong> and add it to your <code>.env</code> file as:<br/>
#             <code style="color:#f093fb;">GROQ_API_KEY=gsk_your_key_here</code></p>
#         </div>
#         """, unsafe_allow_html=True)
#         if st.button("⚙️ Go to Settings", use_container_width=True):
#             st.session_state.current_page = "settings"
#             st.rerun()
#         return

#     # Analyze button
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         if st.button("🚀 Run Full AI Analysis", use_container_width=True):
#             with st.spinner("🧠 Analyzing your resume with Groq AI... Please wait..."):
#                 analysis, error = call_analysis(st.session_state.resume_text)
#                 if error:
#                     st.error(f"❌ Analysis failed: {error}")
#                 else:
#                     st.session_state.resume_analysis = analysis
#                     st.success("✅ Analysis complete!")
#                     st.rerun()
#     with col2:
#         if st.session_state.resume_analysis:
#             if st.button("🔄 Re-analyze", use_container_width=True):
#                 st.session_state.resume_analysis = None
#                 st.rerun()

#     # Placeholder before analysis
#     if not st.session_state.resume_analysis:
#         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#         st.markdown(f"""
#         <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(240,147,251,0.1));
#             border: 1px solid rgba(102,126,234,0.2); border-radius: 16px; padding: 2rem; text-align:center;">
#             <div style="font-size:3rem;">✨</div>
#             <h3 style="color:#e8e8f0; font-family:Syne,sans-serif;">Ready to Analyze</h3>
#             <p style="color:#888;">Click the button above to get your AI-powered resume analysis.</p>
#             <p style="color:#667eea; font-size:0.85rem;">Resume loaded: {len(st.session_state.resume_text):,} characters</p>
#         </div>
#         """, unsafe_allow_html=True)
#         return

#     a = st.session_state.resume_analysis

#     # ── Header ──
#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#     col1, col2 = st.columns([2, 1])
#     with col1:
#         st.markdown(f"""
#         <div class="metric-card">
#             <h2 style="font-family:Syne,sans-serif; color:#e8e8f0; margin:0 0 0.25rem;">{a.get('candidate_name', 'Candidate')}</h2>
#             <p style="color:#667eea; font-weight:600; margin:0 0 0.75rem;">{a.get('current_role', 'Professional')}</p>
#             <p style="color:#888; font-size:0.9rem; margin:0;">{a.get('summary', '')}</p>
#             <div style="margin-top:1rem; display:flex; gap:1rem; flex-wrap:wrap;">
#                 <span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
#                     🎓 {a.get('education', 'N/A')}
#                 </span>
#                 <span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.85rem;">
#                     ⏱️ {a.get('experience_years', 0)} years exp.
#                 </span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         overall = a.get('overall_score', 5)
#         color = score_color(overall)
#         st.markdown(f"""
#         <div class="metric-card" style="text-align:center;">
#             <p style="color:#888; margin:0 0 0.5rem; font-size:0.85rem;">OVERALL SCORE</p>
#             <div style="font-size:4rem; font-weight:800; color:{color}; line-height:1;">{overall}</div>
#             <div style="color:#888; font-size:1rem;">/10</div>
#             <div style="margin-top:1rem; font-size:0.85rem; color:{color};">
#                 {'⭐ Excellent' if overall >= 8 else '👍 Good' if overall >= 6 else '⚠️ Needs Work' if overall >= 4 else '❌ Major Revision'}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # ── Score Breakdown + Skills ──
#     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">📊 Score Breakdown</h3>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         scores_html = (
#             score_bar(a.get('ats_score', 5), 10, "🤖 ATS Compatibility") +
#             score_bar(a.get('content_score', 5), 10, "📝 Content Quality") +
#             score_bar(a.get('formatting_score', 5), 10, "🎨 Formatting & Structure")
#         )
#         st.markdown(f'<div class="metric-card">{scores_html}</div>', unsafe_allow_html=True)

#     with col2:
#         skills = a.get('skills', {})
#         tech_skills = skills.get('technical', [])
#         soft_skills = skills.get('soft', [])
#         tech_badges = " ".join([
#             f'<span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>'
#             for s in tech_skills[:8]
#         ])
#         soft_badges = " ".join([
#             f'<span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">{s}</span>'
#             for s in soft_skills[:6]
#         ])
#         st.markdown(f"""
#         <div class="metric-card">
#             <p style="color:#e8e8f0; font-weight:600; margin:0 0 0.5rem;">🛠️ Technical Skills</p>
#             <div style="margin-bottom:1rem;">{tech_badges}</div>
#             <p style="color:#e8e8f0; font-weight:600; margin:0 0 0.5rem;">🤝 Soft Skills</p>
#             <div>{soft_badges}</div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # ── Strengths & Gaps ──
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#38ef7d;">💪 Strengths</h3>', unsafe_allow_html=True)
#         items = "".join([f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">✅ {s}</div>' for s in a.get('strengths', [])])
#         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown('<h3 style="font-family:Syne,sans-serif; color:#ffd200;">⚠️ Gaps to Improve</h3>', unsafe_allow_html=True)
#         items = "".join([f'<div style="padding:0.5rem 0; border-bottom:1px solid #2a2a4a; color:#e8e8f0;">🔸 {g}</div>' for g in a.get('gaps', [])])
#         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # ── Recommendations ──
#     st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Personalized Recommendations</h3>', unsafe_allow_html=True)
#     priority_colors = {"High": "#f45c43", "Medium": "#ffd200", "Low": "#38ef7d"}
#     for rec in a.get('recommendations', []):
#         p = rec.get('priority', 'Medium')
#         pc = priority_colors.get(p, "#888")
#         st.markdown(f"""
#         <div class="metric-card" style="margin-bottom:0.75rem;">
#             <div style="display:flex; justify-content:space-between; align-items:center;">
#                 <span style="font-weight:600; color:#e8e8f0;">{rec.get('area', 'General')}</span>
#                 <span style="background:{pc}22; color:{pc}; padding:0.2rem 0.75rem; border-radius:12px; font-size:0.8rem; font-weight:600;">{p} Priority</span>
#             </div>
#             <p style="color:#888; margin:0.5rem 0 0; font-size:0.9rem;">💡 {rec.get('suggestion', '')}</p>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     # ── Target Roles / Industries / Keywords ──
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Target Roles</h4>', unsafe_allow_html=True)
#         items = "".join([f'<div style="padding:0.4rem 0; color:#667eea; border-bottom:1px solid #2a2a4a;">→ {r}</div>' for r in a.get('target_roles', [])])
#         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🏢 Industry Fit</h4>', unsafe_allow_html=True)
#         items = "".join([f'<div style="padding:0.4rem 0; color:#f093fb; border-bottom:1px solid #2a2a4a;">→ {i}</div>' for i in a.get('industry_fit', [])])
#         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

#     with col3:
#         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🔑 Missing Keywords</h4>', unsafe_allow_html=True)
#         items = "".join([f'<div style="padding:0.4rem 0; color:#ffd200; border-bottom:1px solid #2a2a4a;">+ {k}</div>' for k in a.get('keywords_missing', [])])
#         st.markdown(f'<div class="metric-card">{items}</div>', unsafe_allow_html=True)

#     # ── Certifications ──
#     certs = a.get('certifications_recommended', [])
#     if certs:
#         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#         st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">📜 Recommended Certifications</h4>', unsafe_allow_html=True)
#         cols = st.columns(min(len(certs), 3))
#         for i, cert in enumerate(certs[:3]):
#             with cols[i]:
#                 st.markdown(f"""
#                 <div class="metric-card" style="text-align:center;">
#                     <div style="font-size:1.5rem;">🏅</div>
#                     <div style="color:#e8e8f0; font-weight:600; margin-top:0.5rem; font-size:0.9rem;">{cert}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
#     if st.button("💼 Find Matching Jobs →", use_container_width=True):
#         st.session_state.current_page = "jobs"
#         st.rerun()

import streamlit as st
import json
import re
import os


def get_groq_client():
    from openai import OpenAI
    api_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    return client


def call_analysis(resume_text):
    try:
        client = get_groq_client()

        prompt = f"""You are an expert career counselor and resume analyst. Analyze the following resume and return ONLY a valid JSON object. No markdown, no explanation, no code blocks — just raw JSON.

{{
  "candidate_name": "Full Name",
  "current_role": "Most recent job title",
  "experience_years": 3,
  "overall_score": 7,
  "summary": "2-3 sentence professional summary of the candidate.",
  "skills": {{
    "technical": ["Python", "SQL"],
    "soft": ["Communication", "Teamwork"],
    "tools": ["Git", "VS Code"]
  }},
  "strengths": ["Strength 1", "Strength 2", "Strength 3", "Strength 4", "Strength 5"],
  "gaps": ["Gap 1", "Gap 2", "Gap 3", "Gap 4"],
  "recommendations": [
    {{"area": "Skills", "suggestion": "Learn Docker for containerization", "priority": "High"}},
    {{"area": "Resume Format", "suggestion": "Add quantified achievements", "priority": "High"}},
    {{"area": "Certifications", "suggestion": "Get AWS Cloud Practitioner", "priority": "Medium"}},
    {{"area": "Projects", "suggestion": "Add 2 personal projects to GitHub", "priority": "Medium"}},
    {{"area": "LinkedIn", "suggestion": "Update LinkedIn with recent experience", "priority": "Low"}}
  ],
  "target_roles": ["Role 1", "Role 2", "Role 3", "Role 4", "Role 5"],
  "industry_fit": ["Industry 1", "Industry 2", "Industry 3"],
  "education": "B.Tech Computer Science",
  "ats_score": 7,
  "formatting_score": 7,
  "content_score": 7,
  "keywords_missing": ["Keyword1", "Keyword2", "Keyword3", "Keyword4", "Keyword5"],
  "certifications_recommended": ["Cert 1", "Cert 2", "Cert 3"]
}}

RESUME TO ANALYZE:
{resume_text[:4000]}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2000
        )

        raw = response.choices[0].message.content.strip()
        raw = re.sub(r'^```json\s*', '', raw)
        raw = re.sub(r'^```\s*', '', raw)
        raw = re.sub(r'\s*```$', '', raw)
        raw = raw.strip()

        return json.loads(raw), None

    except ImportError:
        return None, "OpenAI library not installed. Run: pip install openai"
    except json.JSONDecodeError as e:
        return None, f"Failed to parse AI response: {str(e)}"
    except Exception as e:
        return None, str(e)


def score_color(score, max_score=10):
    pct = score / max_score
    if pct >= 0.75:
        return "#38ef7d"
    elif pct >= 0.5:
        return "#ffd200"
    else:
        return "#f45c43"


def render_score_bar(label, score, max_score=10):
    """Render a single score bar directly using st.markdown with unsafe_allow_html."""
    pct   = (score / max_score) * 100
    color = score_color(score, max_score)
    st.markdown(f"""
    <div style="margin-bottom:1rem;">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem;">
            <span style="color:#e8e8f0; font-size:0.9rem;">{label}</span>
            <span style="color:{color}; font-weight:700; font-size:0.9rem;">{score}/{max_score}</span>
        </div>
        <div style="background:#0a0a0f; border-radius:6px; height:10px; overflow:hidden; border:1px solid #2a2a4a;">
            <div style="width:{pct}%; background:linear-gradient(90deg, #667eea, {color}); height:100%; border-radius:6px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show():
    st.markdown("""
    <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        🧠 AI-Powered Resume Insights
    </h1>
    <p style="color:#888;">Comprehensive AI analysis of your resume with actionable recommendations</p>
    """, unsafe_allow_html=True)

    # ── Guard: no resume ──
    if not st.session_state.resume_text:
        st.markdown("""
        <div style="background:rgba(244,92,67,0.1); border:1px solid rgba(244,92,67,0.3);
            border-radius:12px; padding:2rem; text-align:center; margin-top:2rem;">
            <div style="font-size:3rem;">📄</div>
            <h3 style="color:#f45c43; font-family:Syne,sans-serif;">No Resume Found</h3>
            <p style="color:#888;">Please upload your resume first.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📤 Go to Resume Upload", use_container_width=True):
            st.session_state.current_page = "resume"
            st.rerun()
        return

    # ── Guard: no API key ──
    groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
    if not groq_key:
        st.markdown("""
        <div style="background:rgba(255,210,0,0.1); border:1px solid rgba(255,210,0,0.4);
            border-radius:12px; padding:1.5rem; margin-bottom:1rem;">
            <p style="color:#ffd200; font-weight:600; margin:0 0 0.5rem;">⚠️ Groq API Key Required</p>
            <p style="color:#888; margin:0;">Get a free key at <strong>console.groq.com</strong> and add to <code>.env</code>:<br/>
            <code style="color:#f093fb;">GROQ_API_KEY=gsk_your_key_here</code></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("⚙️ Go to Settings", use_container_width=True):
            st.session_state.current_page = "settings"
            st.rerun()
        return

    # ── Analyze button ──
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("🚀 Run Full AI Analysis", use_container_width=True):
            with st.spinner("🧠 Analyzing your resume with Groq AI..."):
                analysis, error = call_analysis(st.session_state.resume_text)
                if error:
                    st.error(f"❌ Analysis failed: {error}")
                else:
                    st.session_state.resume_analysis = analysis
                    st.success("✅ Analysis complete!")
                    st.rerun()
    with col2:
        if st.session_state.resume_analysis:
            if st.button("🔄 Re-analyze", use_container_width=True):
                st.session_state.resume_analysis = None
                st.rerun()

    if not st.session_state.resume_analysis:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,rgba(102,126,234,0.1),rgba(240,147,251,0.1));
            border:1px solid rgba(102,126,234,0.2); border-radius:16px; padding:2rem; text-align:center; margin-top:1.5rem;">
            <div style="font-size:3rem;">✨</div>
            <h3 style="color:#e8e8f0; font-family:Syne,sans-serif;">Ready to Analyze</h3>
            <p style="color:#888;">Click the button above to get your AI-powered resume analysis.</p>
            <p style="color:#667eea; font-size:0.85rem;">Resume loaded: {len(st.session_state.resume_text):,} characters</p>
        </div>
        """, unsafe_allow_html=True)
        return

    a = st.session_state.resume_analysis

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 1 — Candidate Header + Overall Score
    # ══════════════════════════════════════════
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2 style="font-family:Syne,sans-serif; color:#e8e8f0; margin:0 0 0.25rem;">
                {a.get('candidate_name','Candidate')}
            </h2>
            <p style="color:#667eea; font-weight:600; margin:0 0 0.75rem; font-size:1rem;">
                {a.get('current_role','Professional')}
            </p>
            <p style="color:#aaa; font-size:0.9rem; line-height:1.6; margin:0;">
                {a.get('summary','')}
            </p>
            <div style="margin-top:1rem; display:flex; gap:0.75rem; flex-wrap:wrap;">
                <span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.3rem 0.9rem; border-radius:20px; font-size:0.82rem;">
                    🎓 {a.get('education','N/A')}
                </span>
                <span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.3rem 0.9rem; border-radius:20px; font-size:0.82rem;">
                    ⏱️ {a.get('experience_years',0)} years exp.
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        overall = a.get('overall_score', 5)
        color   = score_color(overall)
        label   = '⭐ Excellent' if overall >= 8 else '👍 Good' if overall >= 6 else '⚠️ Needs Work' if overall >= 4 else '❌ Needs Revision'
        st.markdown(f"""
        <div class="metric-card" style="text-align:center; padding:2rem 1rem;">
            <p style="color:#888; margin:0 0 0.5rem; font-size:0.8rem; letter-spacing:1px;">OVERALL SCORE</p>
            <div style="font-size:4.5rem; font-weight:800; color:{color}; line-height:1;">{overall}</div>
            <div style="color:#555; font-size:1.1rem; margin-bottom:0.5rem;">/10</div>
            <div style="background:{color}22; color:{color}; padding:0.3rem 0.9rem; border-radius:20px; font-size:0.82rem; font-weight:600; display:inline-block;">
                {label}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 2 — Score Breakdown (fixed bars)
    # ══════════════════════════════════════════
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-bottom:1rem;">📊 Score Breakdown</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="metric-card" style="padding:1.5rem;">
            <p style="color:#667eea; font-weight:600; margin:0 0 1rem; font-size:0.85rem; letter-spacing:1px;">RESUME SCORES</p>
        </div>
        """, unsafe_allow_html=True)
        # Render each bar individually — this fixes the raw HTML bug
        with st.container():
            st.markdown('<div style="background:linear-gradient(135deg,#1a1a2e,#16213e); border:1px solid #2a2a4a; border-radius:16px; padding:1.5rem;">', unsafe_allow_html=True)
            render_score_bar("🤖 ATS Compatibility",     a.get('ats_score', 5))
            render_score_bar("📝 Content Quality",       a.get('content_score', 5))
            render_score_bar("🎨 Formatting & Structure", a.get('formatting_score', 5))
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        skills      = a.get('skills', {})
        tech_skills = skills.get('technical', [])
        soft_skills = skills.get('soft', [])
        tools       = skills.get('tools', [])

        st.markdown("""
        <div class="metric-card">
            <p style="color:#667eea; font-weight:600; margin:0 0 0.75rem; font-size:0.85rem; letter-spacing:1px;">SKILLS IDENTIFIED</p>
        """, unsafe_allow_html=True)

        if tech_skills:
            badges = " ".join([
                f'<span style="background:rgba(102,126,234,0.2); color:#667eea; padding:0.25rem 0.65rem; border-radius:12px; font-size:0.8rem; display:inline-block; margin:3px;">{s}</span>'
                for s in tech_skills[:10]
            ])
            st.markdown(f'<p style="color:#aaa; font-size:0.82rem; margin:0.5rem 0 0.3rem;">🛠️ Technical</p>{badges}', unsafe_allow_html=True)

        if soft_skills:
            badges = " ".join([
                f'<span style="background:rgba(240,147,251,0.2); color:#f093fb; padding:0.25rem 0.65rem; border-radius:12px; font-size:0.8rem; display:inline-block; margin:3px;">{s}</span>'
                for s in soft_skills[:6]
            ])
            st.markdown(f'<p style="color:#aaa; font-size:0.82rem; margin:0.75rem 0 0.3rem;">🤝 Soft Skills</p>{badges}', unsafe_allow_html=True)

        if tools:
            badges = " ".join([
                f'<span style="background:rgba(56,239,125,0.15); color:#38ef7d; padding:0.25rem 0.65rem; border-radius:12px; font-size:0.8rem; display:inline-block; margin:3px;">{s}</span>'
                for s in tools[:6]
            ])
            st.markdown(f'<p style="color:#aaa; font-size:0.82rem; margin:0.75rem 0 0.3rem;">🔧 Tools</p>{badges}', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 3 — Strengths & Gaps
    # ══════════════════════════════════════════
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<h3 style="font-family:Syne,sans-serif; color:#38ef7d;">💪 Strengths</h3>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        for s in a.get('strengths', []):
            st.markdown(f'<div style="padding:0.55rem 0; border-bottom:1px solid #1e1e35; color:#ddd; font-size:0.9rem;">✅ {s}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 style="font-family:Syne,sans-serif; color:#ffd200;">⚠️ Gaps to Improve</h3>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        for g in a.get('gaps', []):
            st.markdown(f'<div style="padding:0.55rem 0; border-bottom:1px solid #1e1e35; color:#ddd; font-size:0.9rem;">🔸 {g}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 4 — Recommendations
    # ══════════════════════════════════════════
    st.markdown('<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Personalized Recommendations</h3>', unsafe_allow_html=True)
    priority_colors = {"High": "#f45c43", "Medium": "#ffd200", "Low": "#38ef7d"}

    for rec in a.get('recommendations', []):
        p  = rec.get('priority', 'Medium')
        pc = priority_colors.get(p, "#888")
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom:0.75rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
                <span style="font-weight:600; color:#e8e8f0; font-size:0.95rem;">{rec.get('area','General')}</span>
                <span style="background:{pc}22; color:{pc}; padding:0.2rem 0.75rem; border-radius:20px; font-size:0.78rem; font-weight:600; border:1px solid {pc}44;">
                    {p} Priority
                </span>
            </div>
            <p style="color:#aaa; margin:0; font-size:0.88rem; line-height:1.5;">💡 {rec.get('suggestion','')}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 5 — Target Roles / Industry / Keywords
    # ══════════════════════════════════════════
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 Target Roles</h4>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        for role in a.get('target_roles', []):
            st.markdown(f'<div style="padding:0.4rem 0; color:#667eea; border-bottom:1px solid #1e1e35; font-size:0.88rem;">→ {role}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🏢 Industry Fit</h4>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        for ind in a.get('industry_fit', []):
            st.markdown(f'<div style="padding:0.4rem 0; color:#f093fb; border-bottom:1px solid #1e1e35; font-size:0.88rem;">→ {ind}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">🔑 Missing Keywords</h4>', unsafe_allow_html=True)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        for kw in a.get('keywords_missing', []):
            st.markdown(f'<div style="padding:0.4rem 0; color:#ffd200; border-bottom:1px solid #1e1e35; font-size:0.88rem;">+ {kw}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════
    # SECTION 6 — Certifications
    # ══════════════════════════════════════════
    certs = a.get('certifications_recommended', [])
    if certs:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0;">📜 Recommended Certifications</h4>', unsafe_allow_html=True)
        cols = st.columns(min(len(certs), 3))
        for i, cert in enumerate(certs[:3]):
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card" style="text-align:center; padding:1.25rem;">
                    <div style="font-size:2rem;">🏅</div>
                    <div style="color:#e8e8f0; font-weight:600; margin-top:0.5rem; font-size:0.88rem; line-height:1.4;">{cert}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    if st.button("💼 Find Matching Jobs →", use_container_width=True):
        st.session_state.current_page = "jobs"
        st.rerun()