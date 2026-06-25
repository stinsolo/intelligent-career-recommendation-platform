from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing")

# # # # import os
# # # # import streamlit as st
# # # # import json
# # # # import time
# # # # import random
# # # # import re

# # # # def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
# # # #     """Scrape LinkedIn jobs using Selenium."""
# # # #     try:
# # # #         from selenium import webdriver
# # # #         from selenium.webdriver.common.by import By
# # # #         from selenium.webdriver.chrome.options import Options
# # # #         from selenium.webdriver.support.ui import WebDriverWait
# # # #         from selenium.webdriver.support import expected_conditions as EC
# # # #         from selenium.common.exceptions import TimeoutException, NoSuchElementException
# # # #         import urllib.parse

# # # #         options = Options()
# # # #         options.add_argument("--headless")
# # # #         options.add_argument("--no-sandbox")
# # # #         options.add_argument("--disable-dev-shm-usage")
# # # #         options.add_argument("--disable-gpu")
# # # #         options.add_argument("--window-size=1920,1080")
# # # #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# # # #         options.add_argument("--disable-blink-features=AutomationControlled")
# # # #         options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # # #         options.add_experimental_option("useAutomationExtension", False)

# # # #         driver = webdriver.Chrome(options=options)
# # # #         driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# # # #         encoded_keywords = urllib.parse.quote(keywords)
# # # #         encoded_location = urllib.parse.quote(location)
# # # #         url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_keywords}&location={encoded_location}&f_TPR=r86400&sortBy=R"

# # # #         driver.get(url)
# # # #         time.sleep(3)

# # # #         jobs = []
# # # #         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.base-card")

# # # #         for card in job_cards[:num_jobs]:
# # # #             try:
# # # #                 title = card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text.strip()
# # # #                 company = card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text.strip()
# # # #                 location_el = card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text.strip()
# # # #                 try:
# # # #                     link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
# # # #                 except:
# # # #                     link = ""
# # # #                 try:
# # # #                     posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
# # # #                 except:
# # # #                     posted = "Recently"

# # # #                 jobs.append({
# # # #                     "title": title,
# # # #                     "company": company,
# # # #                     "location": location_el,
# # # #                     "url": link,
# # # #                     "posted": posted,
# # # #                     "description": "",
# # # #                     "match_score": random.randint(65, 95)
# # # #                 })
# # # #             except Exception:
# # # #                 continue

# # # #         driver.quit()
# # # #         return jobs, None

# # # #     except ImportError:
# # # #         return None, "selenium_not_installed"
# # # #     except Exception as e:
# # # #         return None, str(e)


# # # # def get_ai_job_matches(resume_analysis, job_title, location, api_key, num_jobs=8):
# # # #     """Use AI to generate relevant job recommendations when scraping is unavailable."""
# # # #     try:
# # # #         from openai import OpenAI
# # # #         client = OpenAI(api_key=os.getenv("GROQ_API_KEY", "") or api_key, base_url="https://api.groq.com/openai/v1")

# # # #         target_roles = resume_analysis.get('target_roles', [job_title])
# # # #         skills = resume_analysis.get('skills', {}).get('technical', [])
# # # #         industry = resume_analysis.get('industry_fit', ['Technology'])

# # # #         prompt = f"""You are a job market expert. Generate {num_jobs} realistic job listings for a candidate with this profile:
# # # # - Target roles: {', '.join(target_roles[:3])}
# # # # - Skills: {', '.join(skills[:8])}
# # # # - Industries: {', '.join(industry[:2])}
# # # # - Preferred location: {location}
# # # # - Job search query: {job_title}

# # # # Return ONLY a JSON array with this exact structure:
# # # # [
# # # #   {{
# # # #     "title": "Job Title",
# # # #     "company": "Company Name",
# # # #     "location": "{location}",
# # # #     "description": "2-3 sentence job description mentioning key responsibilities",
# # # #     "requirements": ["requirement1", "requirement2", "requirement3"],
# # # #     "salary_range": "$XX,000 - $XX,000",
# # # #     "match_score": 85,
# # # #     "match_reasons": ["reason1", "reason2"],
# # # #     "posted": "2 days ago",
# # # #     "job_type": "Full-time",
# # # #     "url": "https://linkedin.com/jobs/view/sample"
# # # #   }}
# # # # ]

# # # # Make companies and roles realistic and diverse. Match scores should be 60-95 based on skill alignment."""

# # # #         response = client.chat.completions.create(
# # # #             model="llama3-8b-8192",
# # # #             messages=[{"role": "user", "content": prompt}],
# # # #             temperature=0.7,
# # # #             max_tokens=3000
# # # #         )

# # # #         raw = response.choices[0].message.content.strip()
# # # #         raw = re.sub(r'^```json\s*', '', raw)
# # # #         raw = re.sub(r'\s*```$', '', raw)
# # # #         jobs = json.loads(raw)
# # # #         return jobs, None

# # # #     except Exception as e:
# # # #         return None, str(e)


# # # # def show():
# # # #     st.markdown("""
# # # #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# # # #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# # # #         💼 Job Recommendations
# # # #     </h1>
# # # #     <p style="color:#888;">AI-powered job matching with LinkedIn data extraction</p>
# # # #     """, unsafe_allow_html=True)

# # # #     if not st.session_state.resume_text:
# # # #         st.markdown("""
# # # #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# # # #             border-radius: 12px; padding: 2rem; text-align:center;">
# # # #             <div style="font-size:3rem;">📄</div>
# # # #             <h3 style="color:#f45c43;">No Resume Found</h3>
# # # #             <p style="color:#888;">Upload your resume first to get personalized job recommendations.</p>
# # # #         </div>
# # # #         """, unsafe_allow_html=True)
# # # #         if st.button("📤 Upload Resume", use_container_width=True):
# # # #             st.session_state.current_page = "resume"
# # # #             st.rerun()
# # # #         return

# # # #     # Search configuration
# # # #     st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
# # # #     st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:0;">🔍 Job Search Configuration</h4>', unsafe_allow_html=True)

# # # #     col1, col2, col3 = st.columns(3)

# # # #     # Auto-fill from analysis
# # # #     default_title = ""
# # # #     if st.session_state.resume_analysis:
# # # #         roles = st.session_state.resume_analysis.get('target_roles', [])
# # # #         if roles:
# # # #             default_title = roles[0]

# # # #     with col1:
# # # #         job_title = st.text_input("🎯 Job Title / Keywords", value=default_title or "Software Engineer", placeholder="e.g. Data Scientist, Product Manager")
# # # #     with col2:
# # # #         location = st.text_input("📍 Location", value="United States", placeholder="e.g. New York, Remote, San Francisco")
# # # #     with col3:
# # # #         num_jobs = st.slider("📊 Number of Jobs", min_value=5, max_value=20, value=8)

# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         search_mode = st.selectbox("🛠️ Search Mode", [
# # # #             "AI-Generated Recommendations (Recommended)",
# # # #             "LinkedIn Selenium Scraping (Requires Chrome Driver)"
# # # #         ])

# # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # #     use_selenium = "Selenium" in search_mode

# # # #     col1, col2 = st.columns([3, 1])
# # # #     with col1:
# # # #         search_btn = st.button("🚀 Find Matching Jobs", use_container_width=True)
# # # #     with col2:
# # # #         if st.session_state.job_results:
# # # #             if st.button("🗑️ Clear Results", use_container_width=True):
# # # #                 st.session_state.job_results = []
# # # #                 st.rerun()

# # # #     if search_btn:
# # # #         if not st.session_state.openai_api_key and not use_selenium:
# # # #             st.error("❌ Please add your OpenAI API key in Settings for AI-generated recommendations.")
# # # #         else:
# # # #             with st.spinner(f"{'🤖 Generating AI job recommendations' if not use_selenium else '🌐 Scraping LinkedIn'}... Please wait..."):
# # # #                 if use_selenium:
# # # #                     jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
# # # #                     if error == "selenium_not_installed":
# # # #                         st.warning("⚠️ Selenium not installed. Switching to AI recommendations.")
# # # #                         jobs, error = get_ai_job_matches(
# # # #                             st.session_state.resume_analysis or {},
# # # #                             job_title, location,
# # # #                             st.session_state.openai_api_key, num_jobs
# # # #                         )
# # # #                     if error:
# # # #                         st.error(f"❌ Scraping failed: {error}")
# # # #                         jobs = []
# # # #                 else:
# # # #                     if st.session_state.resume_analysis:
# # # #                         jobs, error = get_ai_job_matches(
# # # #                             st.session_state.resume_analysis,
# # # #                             job_title, location,
# # # #                             st.session_state.openai_api_key, num_jobs
# # # #                         )
# # # #                     else:
# # # #                         st.warning("⚠️ Run AI Resume Analysis first for better matches! Using basic search.")
# # # #                         jobs, error = get_ai_job_matches(
# # # #                             {"target_roles": [job_title], "skills": {"technical": []}, "industry_fit": []},
# # # #                             job_title, location,
# # # #                             st.session_state.openai_api_key, num_jobs
# # # #                         )
# # # #                     if error:
# # # #                         st.error(f"❌ Error: {error}")
# # # #                         jobs = []

# # # #                 if jobs:
# # # #                     st.session_state.job_results = jobs
# # # #                     st.success(f"✅ Found {len(jobs)} job matches!")
# # # #                     st.rerun()

# # # #     # Display job results
# # # #     if st.session_state.job_results:
# # # #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # # #         jobs = st.session_state.job_results
# # # #         # Sort by match score
# # # #         jobs_sorted = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)

# # # #         # Summary stats
# # # #         col1, col2, col3, col4 = st.columns(4)
# # # #         avg_score = sum(j.get('match_score', 0) for j in jobs) / len(jobs)
# # # #         high_match = sum(1 for j in jobs if j.get('match_score', 0) >= 80)

# # # #         with col1:
# # # #             st.markdown(f"""
# # # #             <div class="metric-card" style="text-align:center;">
# # # #                 <div style="color:#888; font-size:0.8rem;">TOTAL JOBS</div>
# # # #                 <div style="font-size:2rem; font-weight:800; color:#667eea;">{len(jobs)}</div>
# # # #             </div>
# # # #             """, unsafe_allow_html=True)
# # # #         with col2:
# # # #             st.markdown(f"""
# # # #             <div class="metric-card" style="text-align:center;">
# # # #                 <div style="color:#888; font-size:0.8rem;">AVG MATCH</div>
# # # #                 <div style="font-size:2rem; font-weight:800; color:#f093fb;">{avg_score:.0f}%</div>
# # # #             </div>
# # # #             """, unsafe_allow_html=True)
# # # #         with col3:
# # # #             st.markdown(f"""
# # # #             <div class="metric-card" style="text-align:center;">
# # # #                 <div style="color:#888; font-size:0.8rem;">HIGH MATCH (80%+)</div>
# # # #                 <div style="font-size:2rem; font-weight:800; color:#38ef7d;">{high_match}</div>
# # # #             </div>
# # # #             """, unsafe_allow_html=True)
# # # #         with col4:
# # # #             top_score = max(j.get('match_score', 0) for j in jobs)
# # # #             st.markdown(f"""
# # # #             <div class="metric-card" style="text-align:center;">
# # # #                 <div style="color:#888; font-size:0.8rem;">TOP MATCH</div>
# # # #                 <div style="font-size:2rem; font-weight:800; color:#ffd200;">{top_score}%</div>
# # # #             </div>
# # # #             """, unsafe_allow_html=True)

# # # #         st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
# # # #         st.markdown(f'<h3 style="font-family:Syne,sans-serif; color:#e8e8f0;">🎯 {len(jobs)} Job Matches</h3>', unsafe_allow_html=True)

# # # #         for i, job in enumerate(jobs_sorted):
# # # #             score = job.get('match_score', 0)
# # # #             score_col = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
# # # #             score_label = "🔥 Top Match" if score >= 85 else "✅ Good Match" if score >= 70 else "🔵 Fair Match"

# # # #             with st.expander(f"{score_label} | {job.get('title', 'Job')} at {job.get('company', 'Company')} — {score}% match", expanded=(i < 2)):
# # # #                 col1, col2 = st.columns([3, 1])

# # # #                 with col1:
# # # #                     st.markdown(f"""
# # # #                     <div style="margin-bottom:1rem;">
# # # #                         <h3 style="color:#e8e8f0; font-family:Syne,sans-serif; margin:0;">{job.get('title', '')}</h3>
# # # #                         <div style="color:#667eea; font-weight:600; margin:0.25rem 0;">{job.get('company', '')}</div>
# # # #                         <div style="color:#888; font-size:0.85rem;">
# # # #                             📍 {job.get('location', '')} &nbsp;•&nbsp;
# # # #                             🕐 {job.get('job_type', 'Full-time')} &nbsp;•&nbsp;
# # # #                             📅 {job.get('posted', 'Recently')}
# # # #                             {f"&nbsp;•&nbsp; 💰 {job.get('salary_range', '')}" if job.get('salary_range') else ''}
# # # #                         </div>
# # # #                     </div>
# # # #                     """, unsafe_allow_html=True)

# # # #                     if job.get('description'):
# # # #                         st.markdown(f'<p style="color:#888; font-size:0.9rem;">{job["description"]}</p>', unsafe_allow_html=True)

# # # #                     reqs = job.get('requirements', [])
# # # #                     if reqs:
# # # #                         st.markdown("**📋 Key Requirements:**")
# # # #                         for req in reqs[:4]:
# # # #                             st.markdown(f'<span style="color:#888; font-size:0.85rem;">• {req}</span>', unsafe_allow_html=True)

# # # #                     match_reasons = job.get('match_reasons', [])
# # # #                     if match_reasons:
# # # #                         reasons_html = " ".join([f'<span style="background:rgba(56,239,125,0.15); color:#38ef7d; padding:0.2rem 0.6rem; border-radius:12px; font-size:0.8rem; margin:2px; display:inline-block;">✓ {r}</span>' for r in match_reasons])
# # # #                         st.markdown(f"**Why you're a match:** {reasons_html}", unsafe_allow_html=True)

# # # #                 with col2:
# # # #                     st.markdown(f"""
# # # #                     <div style="text-align:center; padding:1rem; background:rgba(26,26,46,0.8); border-radius:12px; border:1px solid {score_col}33;">
# # # #                         <div style="color:#888; font-size:0.8rem;">MATCH SCORE</div>
# # # #                         <div style="font-size:3rem; font-weight:800; color:{score_col}; line-height:1.1;">{score}%</div>
# # # #                         <div style="margin-top:0.5rem; font-size:0.8rem; color:{score_col};">{score_label}</div>
# # # #                     </div>
# # # #                     """, unsafe_allow_html=True)

# # # #                     if job.get('url') and job['url'].startswith('http'):
# # # #                         st.markdown(f'<a href="{job["url"]}" target="_blank" style="display:block; text-align:center; margin-top:0.75rem; background:linear-gradient(135deg,#667eea,#764ba2); color:white; padding:0.5rem; border-radius:8px; text-decoration:none; font-weight:600; font-size:0.85rem;">Apply Now →</a>', unsafe_allow_html=True)



# # # # import os
# # # # import streamlit as st
# # # # import json
# # # # import time
# # # # import random
# # # # import re


# # # # def clean_html(text):
# # # #     """Strip all HTML tags from a string."""
# # # #     if not text:
# # # #         return ""
# # # #     clean = re.sub(r'<[^>]+>', '', str(text))
# # # #     clean = re.sub(r'&nbsp;', ' ', clean)
# # # #     clean = re.sub(r'&amp;', '&', clean)
# # # #     clean = re.sub(r'&lt;', '<', clean)
# # # #     clean = re.sub(r'&gt;', '>', clean)
# # # #     clean = re.sub(r'\s+', ' ', clean).strip()
# # # #     return clean


# # # # def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
# # # #     """Scrape LinkedIn jobs using Selenium."""
# # # #     try:
# # # #         from selenium import webdriver
# # # #         from selenium.webdriver.common.by import By
# # # #         from selenium.webdriver.chrome.options import Options
# # # #         import urllib.parse

# # # #         options = Options()
# # # #         options.add_argument("--headless")
# # # #         options.add_argument("--no-sandbox")
# # # #         options.add_argument("--disable-dev-shm-usage")
# # # #         options.add_argument("--disable-gpu")
# # # #         options.add_argument("--window-size=1920,1080")
# # # #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
# # # #         options.add_argument("--disable-blink-features=AutomationControlled")
# # # #         options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # # #         options.add_experimental_option("useAutomationExtension", False)

# # # #         driver = webdriver.Chrome(options=options)
# # # #         driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# # # #         encoded_keywords = urllib.parse.quote(keywords)
# # # #         encoded_location = urllib.parse.quote(location)
# # # #         url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_keywords}&location={encoded_location}&f_TPR=r86400&sortBy=R"

# # # #         driver.get(url)
# # # #         time.sleep(3)

# # # #         jobs = []
# # # #         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.base-card")

# # # #         for card in job_cards[:num_jobs]:
# # # #             try:
# # # #                 title   = clean_html(card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text.strip())
# # # #                 company = clean_html(card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text.strip())
# # # #                 loc     = clean_html(card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text.strip())
# # # #                 try:
# # # #                     link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
# # # #                 except Exception:
# # # #                     link = ""
# # # #                 try:
# # # #                     posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
# # # #                 except Exception:
# # # #                     posted = "Recently"

# # # #                 if not title or not company:
# # # #                     continue

# # # #                 jobs.append({
# # # #                     "title": title,
# # # #                     "company": company,
# # # #                     "location": loc,
# # # #                     "url": link,
# # # #                     "posted": posted,
# # # #                     "description": "",
# # # #                     "requirements": [],
# # # #                     "job_type": "Full-time",
# # # #                     "salary_range": "",
# # # #                     "match_reasons": [],
# # # #                     "match_score": random.randint(65, 95)
# # # #                 })
# # # #             except Exception:
# # # #                 continue

# # # #         driver.quit()
# # # #         return jobs, None

# # # #     except ImportError:
# # # #         return None, "selenium_not_installed"
# # # #     except Exception as e:
# # # #         return None, str(e)


# # # # def get_ai_job_matches(resume_analysis, job_title, location, api_key, num_jobs=8):
# # # #     """Use Groq AI to generate relevant job recommendations."""
# # # #     try:
# # # #         from openai import OpenAI
# # # #         groq_key = os.getenv("GROQ_API_KEY", "") or api_key
# # # #         client = OpenAI(
# # # #             api_key=groq_key,
# # # #             base_url="https://api.groq.com/openai/v1"
# # # #         )

# # # #         target_roles = resume_analysis.get('target_roles', [job_title])
# # # #         skills       = resume_analysis.get('skills', {}).get('technical', [])
# # # #         industry     = resume_analysis.get('industry_fit', ['Technology'])

# # # #         prompt = f"""You are a job market expert. Generate {num_jobs} realistic job listings for a candidate.

# # # # Candidate profile:
# # # # - Target roles: {', '.join(target_roles[:3])}
# # # # - Technical skills: {', '.join(skills[:8])}
# # # # - Industries: {', '.join(industry[:2])}
# # # # - Location preference: {location}
# # # # - Search query: {job_title}

# # # # Return ONLY a valid JSON array. No markdown, no explanation, no code fences.
# # # # Each object must have ALL of these fields:

# # # # [
# # # #   {{
# # # #     "title": "Exact Job Title",
# # # #     "company": "Real Company Name",
# # # #     "location": "City, State/Country",
# # # #     "description": "2-3 sentences describing the role and key responsibilities clearly.",
# # # #     "requirements": ["Requirement 1", "Requirement 2", "Requirement 3", "Requirement 4"],
# # # #     "salary_range": "₹X LPA - ₹Y LPA",
# # # #     "match_score": 85,
# # # #     "match_reasons": ["Reason why candidate matches 1", "Reason 2"],
# # # #     "posted": "2 days ago",
# # # #     "job_type": "Full-time",
# # # #     "url": "https://linkedin.com/jobs/view/123456"
# # # #   }}
# # # # ]

# # # # Rules:
# # # # - Every job MUST have a non-empty title, company, location, and description
# # # # - Do NOT include any HTML tags in any field — plain text only
# # # # - Make companies realistic (use real company names like Google, Infosys, Wipro, TCS, etc.)
# # # # - match_score must be an integer between 60 and 95
# # # # - Generate exactly {num_jobs} jobs"""

# # # #         response = client.chat.completions.create(
# # # #             model="llama-3.3-70b-versatile",
# # # #             messages=[{"role": "user", "content": prompt}],
# # # #             temperature=0.7,
# # # #             max_tokens=4000
# # # #         )

# # # #         raw = response.choices[0].message.content.strip()
# # # #         # Strip markdown code fences if present
# # # #         raw = re.sub(r'^```json\s*', '', raw)
# # # #         raw = re.sub(r'^```\s*', '', raw)
# # # #         raw = re.sub(r'\s*```$', '', raw)
# # # #         raw = raw.strip()

# # # #         jobs = json.loads(raw)

# # # #         # Sanitize every field — strip any HTML that slipped through
# # # #         clean_jobs = []
# # # #         for job in jobs:
# # # #             if not job.get('title') or not job.get('company'):
# # # #                 continue
# # # #             clean_jobs.append({
# # # #                 "title":        clean_html(job.get("title", "")),
# # # #                 "company":      clean_html(job.get("company", "")),
# # # #                 "location":     clean_html(job.get("location", location)),
# # # #                 "description":  clean_html(job.get("description", "")),
# # # #                 "requirements": [clean_html(r) for r in job.get("requirements", [])],
# # # #                 "salary_range": clean_html(job.get("salary_range", "")),
# # # #                 "match_score":  int(job.get("match_score", 75)),
# # # #                 "match_reasons":[clean_html(r) for r in job.get("match_reasons", [])],
# # # #                 "posted":       clean_html(job.get("posted", "Recently")),
# # # #                 "job_type":     clean_html(job.get("job_type", "Full-time")),
# # # #                 "url":          job.get("url", ""),
# # # #             })

# # # #         return clean_jobs, None

# # # #     except json.JSONDecodeError as e:
# # # #         return None, f"Failed to parse AI response as JSON: {str(e)}"
# # # #     except Exception as e:
# # # #         return None, str(e)


# # # # def show():
# # # #     st.markdown("""
# # # #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# # # #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# # # #         💼 Job Recommendations
# # # #     </h1>
# # # #     <p style="color:#888;">AI-powered job matching based on your resume profile</p>
# # # #     """, unsafe_allow_html=True)

# # # #     if not st.session_state.resume_text:
# # # #         st.markdown("""
# # # #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# # # #             border-radius: 12px; padding: 2rem; text-align:center;">
# # # #             <div style="font-size:3rem;">📄</div>
# # # #             <h3 style="color:#f45c43;">No Resume Found</h3>
# # # #             <p style="color:#888;">Upload your resume first to get personalized job recommendations.</p>
# # # #         </div>
# # # #         """, unsafe_allow_html=True)
# # # #         if st.button("📤 Upload Resume", use_container_width=True):
# # # #             st.session_state.current_page = "resume"
# # # #             st.rerun()
# # # #         return

# # # #     # ── Search Configuration ──
# # # #     st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
# # # #     st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:0;">🔍 Job Search Configuration</h4>', unsafe_allow_html=True)

# # # #     default_title = ""
# # # #     if st.session_state.resume_analysis:
# # # #         roles = st.session_state.resume_analysis.get('target_roles', [])
# # # #         if roles:
# # # #             default_title = roles[0]

# # # #     col1, col2, col3 = st.columns(3)
# # # #     with col1:
# # # #         job_title = st.text_input("🎯 Job Title / Keywords", value=default_title or "Software Engineer")
# # # #     with col2:
# # # #         location = st.text_input("📍 Location", value="India")
# # # #     with col3:
# # # #         num_jobs = st.slider("📊 Number of Jobs", min_value=5, max_value=20, value=8)

# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         search_mode = st.selectbox("🛠️ Search Mode", [
# # # #             "AI-Generated Recommendations (Recommended)",
# # # #             "LinkedIn Selenium Scraping (Requires Chrome Driver)"
# # # #         ])
# # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # #     use_selenium = "Selenium" in search_mode

# # # #     col1, col2 = st.columns([3, 1])
# # # #     with col1:
# # # #         search_btn = st.button("🚀 Find Matching Jobs", use_container_width=True)
# # # #     with col2:
# # # #         if st.session_state.job_results:
# # # #             if st.button("🗑️ Clear Results", use_container_width=True):
# # # #                 st.session_state.job_results = []
# # # #                 st.rerun()

# # # #     if search_btn:
# # # #         groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
# # # #         if not groq_key and not use_selenium:
# # # #             st.error("❌ Please add your GROQ_API_KEY in the .env file.")
# # # #         else:
# # # #             with st.spinner("🤖 Finding matching jobs... Please wait..."):
# # # #                 if use_selenium:
# # # #                     jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
# # # #                     if error == "selenium_not_installed" or error:
# # # #                         st.warning("⚠️ Selenium unavailable. Switching to AI recommendations.")
# # # #                         jobs, error = get_ai_job_matches(
# # # #                             st.session_state.resume_analysis or {},
# # # #                             job_title, location, groq_key, num_jobs
# # # #                         )
# # # #                 else:
# # # #                     analysis = st.session_state.resume_analysis or {
# # # #                         "target_roles": [job_title],
# # # #                         "skills": {"technical": []},
# # # #                         "industry_fit": []
# # # #                     }
# # # #                     if not st.session_state.resume_analysis:
# # # #                         st.warning("⚠️ Run AI Resume Analysis first for better matches!")
# # # #                     jobs, error = get_ai_job_matches(analysis, job_title, location, groq_key, num_jobs)

# # # #                 if error:
# # # #                     st.error(f"❌ Error: {error}")
# # # #                 elif jobs:
# # # #                     st.session_state.job_results = jobs
# # # #                     st.success(f"✅ Found {len(jobs)} job matches!")
# # # #                     st.rerun()

# # # #     # ── Display Results ──
# # # #     if not st.session_state.job_results:
# # # #         return

# # # #     jobs = st.session_state.job_results
# # # #     jobs_sorted = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)

# # # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # # #     # Summary stats
# # # #     avg_score  = sum(j.get('match_score', 0) for j in jobs) / len(jobs)
# # # #     high_match = sum(1 for j in jobs if j.get('match_score', 0) >= 80)
# # # #     top_score  = max(j.get('match_score', 0) for j in jobs)

# # # #     col1, col2, col3, col4 = st.columns(4)
# # # #     with col1:
# # # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOTAL JOBS</div><div style="font-size:2rem;font-weight:800;color:#667eea;">{len(jobs)}</div></div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">AVG MATCH</div><div style="font-size:2rem;font-weight:800;color:#f093fb;">{avg_score:.0f}%</div></div>', unsafe_allow_html=True)
# # # #     with col3:
# # # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">HIGH MATCH (80%+)</div><div style="font-size:2rem;font-weight:800;color:#38ef7d;">{high_match}</div></div>', unsafe_allow_html=True)
# # # #     with col4:
# # # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOP MATCH</div><div style="font-size:2rem;font-weight:800;color:#ffd200;">{top_score}%</div></div>', unsafe_allow_html=True)

# # # #     st.markdown(f'<h3 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:1.5rem;">🎯 {len(jobs)} Job Matches</h3>', unsafe_allow_html=True)

# # # #     for i, job in enumerate(jobs_sorted):
# # # #         score       = job.get('match_score', 0)
# # # #         score_col   = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
# # # #         score_label = "🔥 Top Match" if score >= 85 else "✅ Good Match" if score >= 70 else "🔵 Fair Match"
# # # #         title       = job.get('title', 'Job Title')
# # # #         company     = job.get('company', 'Company')
# # # #         location_   = job.get('location', '')
# # # #         description = job.get('description', '')
# # # #         job_type    = job.get('job_type', 'Full-time')
# # # #         posted      = job.get('posted', 'Recently')
# # # #         salary      = job.get('salary_range', '')
# # # #         reqs        = job.get('requirements', [])
# # # #         reasons     = job.get('match_reasons', [])
# # # #         url         = job.get('url', '')

# # # #         expander_label = f"{score_label} | {title} at {company} — {score}% match"

# # # #         with st.expander(expander_label, expanded=(i < 2)):
# # # #             col1, col2 = st.columns([3, 1])

# # # #             with col1:
# # # #                 # Job header — all plain text, no HTML injection
# # # #                 st.markdown(f"""
# # # #                 <div style="margin-bottom:1rem;">
# # # #                     <h3 style="color:#e8e8f0; font-family:Syne,sans-serif; margin:0 0 0.25rem;">{title}</h3>
# # # #                     <div style="color:#667eea; font-weight:600; font-size:1rem; margin-bottom:0.4rem;">🏢 {company}</div>
# # # #                     <div style="color:#888; font-size:0.88rem; display:flex; flex-wrap:wrap; gap:0.75rem;">
# # # #                         <span>📍 {location_}</span>
# # # #                         <span>🕐 {job_type}</span>
# # # #                         <span>📅 {posted}</span>
# # # #                         {"<span>💰 " + salary + "</span>" if salary else ""}
# # # #                     </div>
# # # #                 </div>
# # # #                 """, unsafe_allow_html=True)

# # # #                 # Description
# # # #                 if description:
# # # #                     st.markdown(f"""
# # # #                     <div style="background:rgba(102,126,234,0.07); border-left:3px solid #667eea;
# # # #                         border-radius:0 8px 8px 0; padding:0.75rem 1rem; margin:0.75rem 0; color:#ccc; font-size:0.9rem;">
# # # #                         {description}
# # # #                     </div>
# # # #                     """, unsafe_allow_html=True)

# # # #                 # Requirements
# # # #                 if reqs:
# # # #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">📋 Key Requirements</p>', unsafe_allow_html=True)
# # # #                     req_html = "".join([
# # # #                         f'<div style="color:#888; font-size:0.85rem; padding:0.25rem 0; border-bottom:1px solid #1a1a2e;">• {r}</div>'
# # # #                         for r in reqs[:5]
# # # #                     ])
# # # #                     st.markdown(f'<div style="margin-bottom:0.75rem;">{req_html}</div>', unsafe_allow_html=True)

# # # #                 # Match reasons
# # # #                 if reasons:
# # # #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">✅ Why You Match</p>', unsafe_allow_html=True)
# # # #                     badges = " ".join([
# # # #                         f'<span style="background:rgba(56,239,125,0.15); color:#38ef7d; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.8rem; display:inline-block; margin:2px;">✓ {r}</span>'
# # # #                         for r in reasons
# # # #                     ])
# # # #                     st.markdown(f'<div style="margin-bottom:0.5rem;">{badges}</div>', unsafe_allow_html=True)

# # # #             with col2:
# # # #                 st.markdown(f"""
# # # #                 <div style="text-align:center; padding:1.25rem 1rem; background:rgba(26,26,46,0.9);
# # # #                     border-radius:12px; border:2px solid {score_col}44; margin-bottom:0.75rem;">
# # # #                     <div style="color:#888; font-size:0.75rem; letter-spacing:1px;">MATCH SCORE</div>
# # # #                     <div style="font-size:3.5rem; font-weight:800; color:{score_col}; line-height:1.1;">{score}%</div>
# # # #                     <div style="font-size:0.82rem; color:{score_col}; margin-top:0.25rem;">{score_label}</div>
# # # #                 </div>
# # # #                 """, unsafe_allow_html=True)

# # # #                 if url and url.startswith("http"):
# # # #                     st.markdown(f"""
# # # #                     <a href="{url}" target="_blank"
# # # #                         style="display:block; text-align:center; background:linear-gradient(135deg,#667eea,#764ba2);
# # # #                         color:white; padding:0.6rem; border-radius:8px; text-decoration:none;
# # # #                         font-weight:600; font-size:0.85rem;">
# # # #                         Apply Now →
# # # #                     </a>
# # # #                     """, unsafe_allow_html=True)


# # # import os
# # # import streamlit as st
# # # import json
# # # import time
# # # import random
# # # import re


# # # def clean_html(text):
# # #     """Strip all HTML tags from a string."""
# # #     if not text:
# # #         return ""
# # #     clean = re.sub(r'<[^>]+>', '', str(text))
# # #     clean = re.sub(r'&nbsp;', ' ', clean)
# # #     clean = re.sub(r'&amp;', '&', clean)
# # #     clean = re.sub(r'&lt;', '<', clean)
# # #     clean = re.sub(r'&gt;', '>', clean)
# # #     clean = re.sub(r'\s+', ' ', clean).strip()
# # #     return clean


# # # def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
# # #     """Scrape LinkedIn jobs using Selenium."""
# # #     try:
# # #         from selenium import webdriver
# # #         from selenium.webdriver.common.by import By
# # #         from selenium.webdriver.chrome.options import Options
# # #         import urllib.parse

# # #         options = Options()
# # #         options.add_argument("--headless")
# # #         options.add_argument("--no-sandbox")
# # #         options.add_argument("--disable-dev-shm-usage")
# # #         options.add_argument("--disable-gpu")
# # #         options.add_argument("--window-size=1920,1080")
# # #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
# # #         options.add_argument("--disable-blink-features=AutomationControlled")
# # #         options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # #         options.add_experimental_option("useAutomationExtension", False)

# # #         driver = webdriver.Chrome(options=options)
# # #         driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# # #         encoded_keywords = urllib.parse.quote(keywords)
# # #         encoded_location = urllib.parse.quote(location)
# # #         url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_keywords}&location={encoded_location}&f_TPR=r86400&sortBy=R"

# # #         driver.get(url)
# # #         time.sleep(3)

# # #         jobs = []
# # #         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.base-card")

# # #         for card in job_cards[:num_jobs]:
# # #             try:
# # #                 title   = clean_html(card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text.strip())
# # #                 company = clean_html(card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text.strip())
# # #                 loc     = clean_html(card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text.strip())
# # #                 try:
# # #                     link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
# # #                 except Exception:
# # #                     link = ""
# # #                 try:
# # #                     posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
# # #                 except Exception:
# # #                     posted = "Recently"

# # #                 if not title or not company:
# # #                     continue

# # #                 jobs.append({
# # #                     "title": title,
# # #                     "company": company,
# # #                     "location": loc,
# # #                     "url": link,
# # #                     "posted": posted,
# # #                     "description": "",
# # #                     "requirements": [],
# # #                     "job_type": "Full-time",
# # #                     "salary_range": "",
# # #                     "match_reasons": [],
# # #                     "match_score": random.randint(65, 95)
# # #                 })
# # #             except Exception:
# # #                 continue

# # #         driver.quit()
# # #         return jobs, None

# # #     except ImportError:
# # #         return None, "selenium_not_installed"
# # #     except Exception as e:
# # #         return None, str(e)


# # # def get_ai_job_matches(resume_analysis, job_title, location, api_key, num_jobs=10):
# # #     """Use Groq AI to generate relevant job recommendations."""
# # #     try:
# # #         from openai import OpenAI
# # #         groq_key = os.getenv("GROQ_API_KEY", "") or api_key
# # #         client = OpenAI(
# # #             api_key=groq_key,
# # #             base_url="https://api.groq.com/openai/v1"
# # #         )

# # #         target_roles = resume_analysis.get('target_roles', [job_title])
# # #         skills       = resume_analysis.get('skills', {}).get('technical', [])
# # #         industry     = resume_analysis.get('industry_fit', ['Technology'])

# # #         prompt = f"""You are a job market expert. Generate exactly {num_jobs} realistic job listings for a candidate.

# # # Candidate profile:
# # # - Target roles: {', '.join(target_roles[:3])}
# # # - Technical skills: {', '.join(skills[:8])}
# # # - Industries: {', '.join(industry[:2])}
# # # - Location preference: {location}
# # # - Search query: {job_title}

# # # Return ONLY a valid JSON array. No markdown, no explanation, no code fences.
# # # Each object must have ALL of these fields:

# # # [
# # #   {{
# # #     "title": "Exact Job Title",
# # #     "company": "Real Company Name",
# # #     "location": "City, State/Country",
# # #     "description": "2-3 sentences describing the role and key responsibilities clearly.",
# # #     "requirements": ["Requirement 1", "Requirement 2", "Requirement 3", "Requirement 4"],
# # #     "salary_range": "₹X LPA - ₹Y LPA",
# # #     "match_score": 85,
# # #     "match_reasons": ["Reason why candidate matches 1", "Reason 2"],
# # #     "posted": "2 days ago",
# # #     "job_type": "Full-time",
# # #     "url": "https://linkedin.com/jobs/view/123456"
# # #   }}
# # # ]

# # # Rules:
# # # - You MUST generate exactly {num_jobs} job objects in the array — no more, no less
# # # - Every job MUST have a non-empty title, company, location, and description
# # # - Do NOT include any HTML tags in any field — plain text only
# # # - Use real Indian company names like TCS, Infosys, Wipro, HCL, Accenture, Google, Amazon, Flipkart, Zomato, Swiggy etc.
# # # - match_score must be an integer between 60 and 95
# # # - Vary the companies and roles — do not repeat the same company twice"""

# # #         response = client.chat.completions.create(
# # #             model="llama-3.3-70b-versatile",
# # #             messages=[{"role": "user", "content": prompt}],
# # #             temperature=0.7,
# # #             max_tokens=6000
# # #         )

# # #         raw = response.choices[0].message.content.strip()
# # #         raw = re.sub(r'^```json\s*', '', raw)
# # #         raw = re.sub(r'^```\s*', '', raw)
# # #         raw = re.sub(r'\s*```$', '', raw)
# # #         raw = raw.strip()

# # #         jobs = json.loads(raw)

# # #         # Sanitize every field
# # #         clean_jobs = []
# # #         for job in jobs:
# # #             if not job.get('title') or not job.get('company'):
# # #                 continue
# # #             clean_jobs.append({
# # #                 "title":         clean_html(job.get("title", "")),
# # #                 "company":       clean_html(job.get("company", "")),
# # #                 "location":      clean_html(job.get("location", location)),
# # #                 "description":   clean_html(job.get("description", "")),
# # #                 "requirements":  [clean_html(r) for r in job.get("requirements", [])],
# # #                 "salary_range":  clean_html(job.get("salary_range", "")),
# # #                 "match_score":   int(job.get("match_score", 75)),
# # #                 "match_reasons": [clean_html(r) for r in job.get("match_reasons", [])],
# # #                 "posted":        clean_html(job.get("posted", "Recently")),
# # #                 "job_type":      clean_html(job.get("job_type", "Full-time")),
# # #                 "url":           job.get("url", ""),
# # #             })

# # #         return clean_jobs, None

# # #     except json.JSONDecodeError as e:
# # #         return None, f"Failed to parse AI response as JSON: {str(e)}"
# # #     except Exception as e:
# # #         return None, str(e)


# # # def show():
# # #     st.markdown("""
# # #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# # #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# # #         💼 Job Recommendations
# # #     </h1>
# # #     <p style="color:#888;">AI-powered job matching based on your resume profile</p>
# # #     """, unsafe_allow_html=True)

# # #     if not st.session_state.resume_text:
# # #         st.markdown("""
# # #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# # #             border-radius: 12px; padding: 2rem; text-align:center;">
# # #             <div style="font-size:3rem;">📄</div>
# # #             <h3 style="color:#f45c43;">No Resume Found</h3>
# # #             <p style="color:#888;">Upload your resume first to get personalized job recommendations.</p>
# # #         </div>
# # #         """, unsafe_allow_html=True)
# # #         if st.button("📤 Upload Resume", use_container_width=True):
# # #             st.session_state.current_page = "resume"
# # #             st.rerun()
# # #         return

# # #     # ── Search Configuration ──
# # #     st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
# # #     st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:0;">🔍 Job Search Configuration</h4>', unsafe_allow_html=True)

# # #     default_title = ""
# # #     if st.session_state.resume_analysis:
# # #         roles = st.session_state.resume_analysis.get('target_roles', [])
# # #         if roles:
# # #             default_title = roles[0]

# # #     col1, col2, col3 = st.columns(3)
# # #     with col1:
# # #         job_title = st.text_input("🎯 Job Title / Keywords", value=default_title or "Software Engineer")
# # #     with col2:
# # #         location = st.text_input("📍 Location", value="India")
# # #     with col3:
# # #         num_jobs = st.slider("📊 Number of Jobs", min_value=10, max_value=30, value=10)

# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         search_mode = st.selectbox("🛠️ Search Mode", [
# # #             "AI-Generated Recommendations (Recommended)",
# # #             "LinkedIn Selenium Scraping (Requires Chrome Driver)"
# # #         ])
# # #     st.markdown('</div>', unsafe_allow_html=True)

# # #     use_selenium = "Selenium" in search_mode

# # #     col1, col2 = st.columns([3, 1])
# # #     with col1:
# # #         search_btn = st.button("🚀 Find Matching Jobs", use_container_width=True)
# # #     with col2:
# # #         if st.session_state.job_results:
# # #             if st.button("🗑️ Clear Results", use_container_width=True):
# # #                 st.session_state.job_results = []
# # #                 st.rerun()

# # #     if search_btn:
# # #         groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
# # #         if not groq_key and not use_selenium:
# # #             st.error("❌ Please add your GROQ_API_KEY in the .env file.")
# # #         else:
# # #             with st.spinner(f"🤖 Generating {num_jobs} job matches... Please wait..."):
# # #                 if use_selenium:
# # #                     jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
# # #                     if error == "selenium_not_installed" or error:
# # #                         st.warning("⚠️ Selenium unavailable. Switching to AI recommendations.")
# # #                         jobs, error = get_ai_job_matches(
# # #                             st.session_state.resume_analysis or {},
# # #                             job_title, location, groq_key, num_jobs
# # #                         )
# # #                 else:
# # #                     analysis = st.session_state.resume_analysis or {
# # #                         "target_roles": [job_title],
# # #                         "skills": {"technical": []},
# # #                         "industry_fit": []
# # #                     }
# # #                     if not st.session_state.resume_analysis:
# # #                         st.warning("⚠️ Run AI Resume Analysis first for better matches!")
# # #                     jobs, error = get_ai_job_matches(analysis, job_title, location, groq_key, num_jobs)

# # #                 if error:
# # #                     st.error(f"❌ Error: {error}")
# # #                 elif jobs:
# # #                     st.session_state.job_results = jobs
# # #                     st.success(f"✅ Found {len(jobs)} job matches!")
# # #                     st.rerun()
# # #                 else:
# # #                     st.error("❌ No jobs returned. Please try again.")

# # #     # ── Display Results ──
# # #     if not st.session_state.job_results:
# # #         return

# # #     jobs = st.session_state.job_results
# # #     jobs_sorted = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)

# # #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# # #     # Summary stats
# # #     avg_score  = sum(j.get('match_score', 0) for j in jobs) / len(jobs)
# # #     high_match = sum(1 for j in jobs if j.get('match_score', 0) >= 80)
# # #     top_score  = max(j.get('match_score', 0) for j in jobs)

# # #     col1, col2, col3, col4 = st.columns(4)
# # #     with col1:
# # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOTAL JOBS</div><div style="font-size:2rem;font-weight:800;color:#667eea;">{len(jobs)}</div></div>', unsafe_allow_html=True)
# # #     with col2:
# # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">AVG MATCH</div><div style="font-size:2rem;font-weight:800;color:#f093fb;">{avg_score:.0f}%</div></div>', unsafe_allow_html=True)
# # #     with col3:
# # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">HIGH MATCH (80%+)</div><div style="font-size:2rem;font-weight:800;color:#38ef7d;">{high_match}</div></div>', unsafe_allow_html=True)
# # #     with col4:
# # #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOP MATCH</div><div style="font-size:2rem;font-weight:800;color:#ffd200;">{top_score}%</div></div>', unsafe_allow_html=True)

# # #     st.markdown(f'<h3 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:1.5rem;">🎯 {len(jobs)} Job Matches</h3>', unsafe_allow_html=True)

# # #     for i, job in enumerate(jobs_sorted):
# # #         score       = job.get('match_score', 0)
# # #         score_col   = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
# # #         score_label = "🔥 Top Match" if score >= 85 else "✅ Good Match" if score >= 70 else "🔵 Fair Match"
# # #         title       = job.get('title', 'Job Title')
# # #         company     = job.get('company', 'Company')
# # #         location_   = job.get('location', '')
# # #         description = job.get('description', '')
# # #         job_type    = job.get('job_type', 'Full-time')
# # #         posted      = job.get('posted', 'Recently')
# # #         salary      = job.get('salary_range', '')
# # #         reqs        = job.get('requirements', [])
# # #         reasons     = job.get('match_reasons', [])
# # #         url         = job.get('url', '')

# # #         expander_label = f"{score_label} | {title} at {company} — {score}% match"

# # #         with st.expander(expander_label, expanded=(i < 2)):
# # #             col1, col2 = st.columns([3, 1])

# # #             with col1:
# # #                 st.markdown(f"""
# # #                 <div style="margin-bottom:1rem;">
# # #                     <h3 style="color:#e8e8f0; font-family:Syne,sans-serif; margin:0 0 0.25rem;">{title}</h3>
# # #                     <div style="color:#667eea; font-weight:600; font-size:1rem; margin-bottom:0.4rem;">🏢 {company}</div>
# # #                     <div style="color:#888; font-size:0.88rem; display:flex; flex-wrap:wrap; gap:0.75rem;">
# # #                         <span>📍 {location_}</span>
# # #                         <span>🕐 {job_type}</span>
# # #                         <span>📅 {posted}</span>
# # #                         {"<span>💰 " + salary + "</span>" if salary else ""}
# # #                     </div>
# # #                 </div>
# # #                 """, unsafe_allow_html=True)

# # #                 if description:
# # #                     st.markdown(f"""
# # #                     <div style="background:rgba(102,126,234,0.07); border-left:3px solid #667eea;
# # #                         border-radius:0 8px 8px 0; padding:0.75rem 1rem; margin:0.75rem 0; color:#ccc; font-size:0.9rem;">
# # #                         {description}
# # #                     </div>
# # #                     """, unsafe_allow_html=True)

# # #                 if reqs:
# # #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">📋 Key Requirements</p>', unsafe_allow_html=True)
# # #                     req_html = "".join([
# # #                         f'<div style="color:#888; font-size:0.85rem; padding:0.25rem 0; border-bottom:1px solid #1a1a2e;">• {r}</div>'
# # #                         for r in reqs[:5]
# # #                     ])
# # #                     st.markdown(f'<div style="margin-bottom:0.75rem;">{req_html}</div>', unsafe_allow_html=True)

# # #                 if reasons:
# # #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">✅ Why You Match</p>', unsafe_allow_html=True)
# # #                     badges = " ".join([
# # #                         f'<span style="background:rgba(56,239,125,0.15); color:#38ef7d; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.8rem; display:inline-block; margin:2px;">✓ {r}</span>'
# # #                         for r in reasons
# # #                     ])
# # #                     st.markdown(f'<div style="margin-bottom:0.5rem;">{badges}</div>', unsafe_allow_html=True)

# # #             with col2:
# # #                 st.markdown(f"""
# # #                 <div style="text-align:center; padding:1.25rem 1rem; background:rgba(26,26,46,0.9);
# # #                     border-radius:12px; border:2px solid {score_col}44; margin-bottom:0.75rem;">
# # #                     <div style="color:#888; font-size:0.75rem; letter-spacing:1px;">MATCH SCORE</div>
# # #                     <div style="font-size:3.5rem; font-weight:800; color:{score_col}; line-height:1.1;">{score}%</div>
# # #                     <div style="font-size:0.82rem; color:{score_col}; margin-top:0.25rem;">{score_label}</div>
# # #                 </div>
# # #                 """, unsafe_allow_html=True)

# # #                 if url and url.startswith("http"):
# # #                     st.markdown(f"""
# # #                     <a href="{url}" target="_blank"
# # #                         style="display:block; text-align:center; background:linear-gradient(135deg,#667eea,#764ba2);
# # #                         color:white; padding:0.6rem; border-radius:8px; text-decoration:none;
# # #                         font-weight:600; font-size:0.85rem;">
# # #                         Apply Now →
# # #                     </a>
# # #                     """, unsafe_allow_html=True)



# # import os
# # import streamlit as st
# # import json
# # import time
# # import random
# # import re


# # def clean_html(text):
# #     """Strip all HTML tags from a string."""
# #     if not text:
# #         return ""
# #     clean = re.sub(r'<[^>]+>', '', str(text))
# #     clean = re.sub(r'&nbsp;', ' ', clean)
# #     clean = re.sub(r'&amp;', '&', clean)
# #     clean = re.sub(r'&lt;', '<', clean)
# #     clean = re.sub(r'&gt;', '>', clean)
# #     clean = re.sub(r'\s+', ' ', clean).strip()
# #     return clean


# # def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
# #     """Scrape LinkedIn jobs using Selenium."""
# #     try:
# #         from selenium import webdriver
# #         from selenium.webdriver.common.by import By
# #         from selenium.webdriver.chrome.options import Options
# #         import urllib.parse

# #         options = Options()
# #         options.add_argument("--headless")
# #         options.add_argument("--no-sandbox")
# #         options.add_argument("--disable-dev-shm-usage")
# #         options.add_argument("--disable-gpu")
# #         options.add_argument("--window-size=1920,1080")
# #         options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
# #         options.add_argument("--disable-blink-features=AutomationControlled")
# #         options.add_experimental_option("excludeSwitches", ["enable-automation"])
# #         options.add_experimental_option("useAutomationExtension", False)

# #         driver = webdriver.Chrome(options=options)
# #         driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# #         encoded_keywords = urllib.parse.quote(keywords)
# #         encoded_location = urllib.parse.quote(location)
# #         url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_keywords}&location={encoded_location}&f_TPR=r86400&sortBy=R"

# #         driver.get(url)
# #         time.sleep(3)

# #         jobs = []
# #         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.base-card")

# #         for card in job_cards[:num_jobs]:
# #             try:
# #                 title   = clean_html(card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text.strip())
# #                 company = clean_html(card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text.strip())
# #                 loc     = clean_html(card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text.strip())
# #                 try:
# #                     link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
# #                 except Exception:
# #                     link = ""
# #                 try:
# #                     posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
# #                 except Exception:
# #                     posted = "Recently"

# #                 if not title or not company:
# #                     continue

# #                 jobs.append({
# #                     "title": title,
# #                     "company": company,
# #                     "location": loc,
# #                     "url": link,
# #                     "posted": posted,
# #                     "description": "",
# #                     "requirements": [],
# #                     "job_type": "Full-time",
# #                     "salary_range": "",
# #                     "match_reasons": [],
# #                     "match_score": random.randint(65, 95)
# #                 })
# #             except Exception:
# #                 continue

# #         driver.quit()
# #         return jobs, None

# #     except ImportError:
# #         return None, "selenium_not_installed"
# #     except Exception as e:
# #         return None, str(e)


# # def get_ai_job_matches(resume_analysis, job_title, location, api_key, num_jobs=10):
# #     """Use Groq AI to generate relevant job recommendations."""
# #     try:
# #         from openai import OpenAI
# #         groq_key = os.getenv("GROQ_API_KEY", "") or api_key
# #         client = OpenAI(
# #             api_key=groq_key,
# #             base_url="https://api.groq.com/openai/v1"
# #         )

# #         target_roles = resume_analysis.get('target_roles', [job_title])
# #         skills       = resume_analysis.get('skills', {}).get('technical', [])
# #         industry     = resume_analysis.get('industry_fit', ['Technology'])

# #         # ── Helpers ──────────────────────────────────────────────────────────────

# #         def build_prompt(count, exclude_companies=None):
# #             encoded_kw  = job_title.replace(' ', '%20')
# #             encoded_loc = location.replace(' ', '%20')
# #             exclude_note = ""
# #             if exclude_companies:
# #                 exclude_note = (
# #                     f"- Do NOT use these companies (already used): "
# #                     f"{', '.join(exclude_companies)}\n"
# #                 )
# #             return f"""You are a job market expert. Generate exactly {count} realistic job listings for a candidate.

# # Candidate profile:
# # - Target roles: {', '.join(target_roles[:3])}
# # - Technical skills: {', '.join(skills[:8])}
# # - Industries: {', '.join(industry[:2])}
# # - Location preference: {location}
# # - Search query: {job_title}

# # Return ONLY a valid JSON array with exactly {count} objects. No markdown, no explanation, no code fences.
# # Each object must have ALL of these fields:

# # [
# #   {{
# #     "title": "Exact Job Title",
# #     "company": "Real Company Name",
# #     "location": "City, State/Country",
# #     "description": "2-3 sentences describing the role and key responsibilities clearly.",
# #     "requirements": ["Requirement 1", "Requirement 2", "Requirement 3", "Requirement 4"],
# #     "salary_range": "₹X LPA - ₹Y LPA",
# #     "match_score": 85,
# #     "match_reasons": ["Reason why candidate matches 1", "Reason 2"],
# #     "posted": "2 days ago",
# #     "job_type": "Full-time",
# #     "url": "https://www.linkedin.com/jobs/search/?keywords={encoded_kw}&location={encoded_loc}"
# #   }}
# # ]

# # CRITICAL RULES — the output is invalid if any rule is broken:
# # - The JSON array MUST contain exactly {count} job objects — count them before returning
# # - Every job MUST have a non-empty title, company, location, and description
# # - Do NOT include any HTML tags in any field — plain text only
# # - Use real Indian company names: TCS, Infosys, Wipro, HCL, Accenture, Google India, Amazon India,
# #   Microsoft India, Flipkart, Zomato, Swiggy, Paytm, Razorpay, HDFC, ICICI, Deloitte, IBM India,
# #   Oracle India, SAP Labs, Cognizant, Tech Mahindra, Capgemini, Mphasis, Hexaware, L&T Infotech, etc.
# # - match_score must be an integer between 60 and 95
# # - Each job must be at a DIFFERENT company — no two jobs can share the same company name
# # {exclude_note}- Vary the seniority levels: include a mix of junior, mid-level, and senior roles"""

# #         def parse_and_clean(raw, fallback_location):
# #             raw = re.sub(r'^```json\s*', '', raw.strip())
# #             raw = re.sub(r'^```\s*', '', raw)
# #             raw = re.sub(r'\s*```$', '', raw)
# #             raw = raw.strip()
# #             jobs = json.loads(raw)
# #             cleaned = []
# #             for job in jobs:
# #                 title   = clean_html(job.get("title", "")).strip()
# #                 company = clean_html(job.get("company", "")).strip()
# #                 if not title or not company:
# #                     continue
# #                 cleaned.append({
# #                     "title":         title,
# #                     "company":       company,
# #                     "location":      clean_html(job.get("location", fallback_location)),
# #                     "description":   clean_html(job.get("description", "")),
# #                     "requirements":  [clean_html(r) for r in job.get("requirements", [])],
# #                     "salary_range":  clean_html(job.get("salary_range", "")),
# #                     "match_score":   int(job.get("match_score", 75)),
# #                     "match_reasons": [clean_html(r) for r in job.get("match_reasons", [])],
# #                     "posted":        clean_html(job.get("posted", "Recently")),
# #                     "job_type":      clean_html(job.get("job_type", "Full-time")),
# #                     "url":           job.get("url", ""),
# #                 })
# #             return cleaned

# #         # ── First call: request num_jobs + 5 buffer to absorb any filtered duds ─
# #         request_count = num_jobs + 5
# #         # ~400 tokens per job is a safe estimate
# #         max_tokens = max(6000, request_count * 450)

# #         response = client.chat.completions.create(
# #             model="llama-3.3-70b-versatile",
# #             messages=[{"role": "user", "content": build_prompt(request_count)}],
# #             temperature=0.7,
# #             max_tokens=max_tokens
# #         )

# #         clean_jobs = parse_and_clean(response.choices[0].message.content, location)

# #         # ── Retry loop: top up if still short ───────────────────────────────────
# #         max_retries = 3
# #         attempt = 0
# #         while len(clean_jobs) < num_jobs and attempt < max_retries:
# #             shortfall       = num_jobs - len(clean_jobs)
# #             used_companies  = [j["company"] for j in clean_jobs]
# #             attempt        += 1

# #             retry_response = client.chat.completions.create(
# #                 model="llama-3.3-70b-versatile",
# #                 messages=[{
# #                     "role": "user",
# #                     "content": build_prompt(shortfall + 2, exclude_companies=used_companies)
# #                 }],
# #                 temperature=0.9,          # higher temp → more variety on retry
# #                 max_tokens=max(3000, (shortfall + 2) * 450)
# #             )

# #             extra_jobs = parse_and_clean(retry_response.choices[0].message.content, location)

# #             # Deduplicate by company name before merging
# #             existing = {j["company"].lower() for j in clean_jobs}
# #             for j in extra_jobs:
# #                 if j["company"].lower() not in existing:
# #                     clean_jobs.append(j)
# #                     existing.add(j["company"].lower())
# #                 if len(clean_jobs) >= num_jobs:
# #                     break

# #         # Trim surplus from buffer and return exactly num_jobs
# #         return clean_jobs[:num_jobs], None

# #     except json.JSONDecodeError as e:
# #         return None, f"Failed to parse AI response as JSON: {str(e)}"
# #     except Exception as e:
# #         return None, str(e)


# # def show():
# #     st.markdown("""
# #     <h1 style="font-family:'Syne',sans-serif; background: linear-gradient(135deg, #667eea, #f093fb);
# #         -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
# #         💼 Job Recommendations
# #     </h1>
# #     <p style="color:#888;">AI-powered job matching based on your resume profile</p>
# #     """, unsafe_allow_html=True)

# #     if not st.session_state.resume_text:
# #         st.markdown("""
# #         <div style="background: rgba(244,92,67,0.1); border: 1px solid rgba(244,92,67,0.3);
# #             border-radius: 12px; padding: 2rem; text-align:center;">
# #             <div style="font-size:3rem;">📄</div>
# #             <h3 style="color:#f45c43;">No Resume Found</h3>
# #             <p style="color:#888;">Upload your resume first to get personalized job recommendations.</p>
# #         </div>
# #         """, unsafe_allow_html=True)
# #         if st.button("📤 Upload Resume", use_container_width=True):
# #             st.session_state.current_page = "resume"
# #             st.rerun()
# #         return

# #     # ── Search Configuration ──
# #     st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
# #     st.markdown('<h4 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:0;">🔍 Job Search Configuration</h4>', unsafe_allow_html=True)

# #     default_title = ""
# #     if st.session_state.resume_analysis:
# #         roles = st.session_state.resume_analysis.get('target_roles', [])
# #         if roles:
# #             default_title = roles[0]

# #     col1, col2, col3 = st.columns(3)
# #     with col1:
# #         job_title = st.text_input("🎯 Job Title / Keywords", value=default_title or "Software Engineer")
# #     with col2:
# #         location = st.text_input("📍 Location", value="India")
# #     with col3:
# #         num_jobs = st.slider("📊 Number of Jobs", min_value=10, max_value=30, value=10)

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         search_mode = st.selectbox("🛠️ Search Mode", [
# #             "AI-Generated Recommendations (Recommended)",
# #             "LinkedIn Selenium Scraping (Requires Chrome Driver)"
# #         ])
# #     st.markdown('</div>', unsafe_allow_html=True)

# #     use_selenium = "Selenium" in search_mode

# #     col1, col2 = st.columns([3, 1])
# #     with col1:
# #         search_btn = st.button("🚀 Find Matching Jobs", use_container_width=True)
# #     with col2:
# #         if st.session_state.job_results:
# #             if st.button("🗑️ Clear Results", use_container_width=True):
# #                 st.session_state.job_results = []
# #                 st.rerun()

# #     if search_btn:
# #         groq_key = os.getenv("GROQ_API_KEY", "") or st.session_state.get("openai_api_key", "")
# #         if not groq_key and not use_selenium:
# #             st.error("❌ Please add your GROQ_API_KEY in the .env file.")
# #         else:
# #             with st.spinner(f"🤖 Generating {num_jobs} job matches... Please wait..."):
# #                 if use_selenium:
# #                     jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
# #                     if error == "selenium_not_installed" or error:
# #                         st.warning("⚠️ Selenium unavailable. Switching to AI recommendations.")
# #                         jobs, error = get_ai_job_matches(
# #                             st.session_state.resume_analysis or {},
# #                             job_title, location, groq_key, num_jobs
# #                         )
# #                 else:
# #                     analysis = st.session_state.resume_analysis or {
# #                         "target_roles": [job_title],
# #                         "skills": {"technical": []},
# #                         "industry_fit": []
# #                     }
# #                     if not st.session_state.resume_analysis:
# #                         st.warning("⚠️ Run AI Resume Analysis first for better matches!")
# #                     jobs, error = get_ai_job_matches(analysis, job_title, location, groq_key, num_jobs)

# #                 if error:
# #                     st.error(f"❌ Error: {error}")
# #                 elif jobs:
# #                     st.session_state.job_results = jobs
# #                     st.success(f"✅ Found {len(jobs)} job matches!")
# #                     st.rerun()
# #                 else:
# #                     st.error("❌ No jobs returned. Please try again.")

# #     # ── Display Results ──
# #     if not st.session_state.job_results:
# #         return

# #     jobs = st.session_state.job_results
# #     jobs_sorted = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)

# #     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# #     # Summary stats
# #     avg_score  = sum(j.get('match_score', 0) for j in jobs) / len(jobs)
# #     high_match = sum(1 for j in jobs if j.get('match_score', 0) >= 80)
# #     top_score  = max(j.get('match_score', 0) for j in jobs)

# #     col1, col2, col3, col4 = st.columns(4)
# #     with col1:
# #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOTAL JOBS</div><div style="font-size:2rem;font-weight:800;color:#667eea;">{len(jobs)}</div></div>', unsafe_allow_html=True)
# #     with col2:
# #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">AVG MATCH</div><div style="font-size:2rem;font-weight:800;color:#f093fb;">{avg_score:.0f}%</div></div>', unsafe_allow_html=True)
# #     with col3:
# #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">HIGH MATCH (80%+)</div><div style="font-size:2rem;font-weight:800;color:#38ef7d;">{high_match}</div></div>', unsafe_allow_html=True)
# #     with col4:
# #         st.markdown(f'<div class="metric-card" style="text-align:center;"><div style="color:#888;font-size:0.8rem;">TOP MATCH</div><div style="font-size:2rem;font-weight:800;color:#ffd200;">{top_score}%</div></div>', unsafe_allow_html=True)

# #     st.markdown(f'<h3 style="font-family:Syne,sans-serif; color:#e8e8f0; margin-top:1.5rem;">🎯 {len(jobs)} Job Matches</h3>', unsafe_allow_html=True)

# #     for i, job in enumerate(jobs_sorted):
# #         score       = job.get('match_score', 0)
# #         score_col   = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
# #         score_label = "🔥 Top Match" if score >= 85 else "✅ Good Match" if score >= 70 else "🔵 Fair Match"
# #         title       = job.get('title', 'Job Title')
# #         company     = job.get('company', 'Company')
# #         location_   = job.get('location', '')
# #         description = job.get('description', '')
# #         job_type    = job.get('job_type', 'Full-time')
# #         posted      = job.get('posted', 'Recently')
# #         salary      = job.get('salary_range', '')
# #         reqs        = job.get('requirements', [])
# #         reasons     = job.get('match_reasons', [])
# #         url         = job.get('url', '')

# #         expander_label = f"{score_label} | {title} at {company} — {score}% match"

# #         with st.expander(expander_label, expanded=(i < 2)):
# #             col1, col2 = st.columns([3, 1])

# #             with col1:
# #                 st.markdown(f"""
# #                 <div style="margin-bottom:1rem;">
# #                     <h3 style="color:#e8e8f0; font-family:Syne,sans-serif; margin:0 0 0.25rem;">{title}</h3>
# #                     <div style="color:#667eea; font-weight:600; font-size:1rem; margin-bottom:0.4rem;">🏢 {company}</div>
# #                     <div style="color:#888; font-size:0.88rem; display:flex; flex-wrap:wrap; gap:0.75rem;">
# #                         <span>📍 {location_}</span>
# #                         <span>🕐 {job_type}</span>
# #                         <span>📅 {posted}</span>
# #                         {"<span>💰 " + salary + "</span>" if salary else ""}
# #                     </div>
# #                 </div>
# #                 """, unsafe_allow_html=True)

# #                 if description:
# #                     st.markdown(f"""
# #                     <div style="background:rgba(102,126,234,0.07); border-left:3px solid #667eea;
# #                         border-radius:0 8px 8px 0; padding:0.75rem 1rem; margin:0.75rem 0; color:#ccc; font-size:0.9rem;">
# #                         {description}
# #                     </div>
# #                     """, unsafe_allow_html=True)

# #                 if reqs:
# #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">📋 Key Requirements</p>', unsafe_allow_html=True)
# #                     req_html = "".join([
# #                         f'<div style="color:#888; font-size:0.85rem; padding:0.25rem 0; border-bottom:1px solid #1a1a2e;">• {r}</div>'
# #                         for r in reqs[:5]
# #                     ])
# #                     st.markdown(f'<div style="margin-bottom:0.75rem;">{req_html}</div>', unsafe_allow_html=True)

# #                 if reasons:
# #                     st.markdown('<p style="color:#e8e8f0; font-weight:600; margin:0.75rem 0 0.4rem;">✅ Why You Match</p>', unsafe_allow_html=True)
# #                     badges = " ".join([
# #                         f'<span style="background:rgba(56,239,125,0.15); color:#38ef7d; padding:0.25rem 0.75rem; border-radius:20px; font-size:0.8rem; display:inline-block; margin:2px;">✓ {r}</span>'
# #                         for r in reasons
# #                     ])
# #                     st.markdown(f'<div style="margin-bottom:0.5rem;">{badges}</div>', unsafe_allow_html=True)

# #             with col2:
# #                 st.markdown(f"""
# #                 <div style="text-align:center; padding:1.25rem 1rem; background:rgba(26,26,46,0.9);
# #                     border-radius:12px; border:2px solid {score_col}44; margin-bottom:0.75rem;">
# #                     <div style="color:#888; font-size:0.75rem; letter-spacing:1px;">MATCH SCORE</div>
# #                     <div style="font-size:3.5rem; font-weight:800; color:{score_col}; line-height:1.1;">{score}%</div>
# #                     <div style="font-size:0.82rem; color:{score_col}; margin-top:0.25rem;">{score_label}</div>
# #                 </div>
# #                 """, unsafe_allow_html=True)

# #                 if url and url.startswith("http"):
# #                     st.markdown(f"""
# #                     <a href="{url}" target="_blank"
# #                         style="display:block; text-align:center; background:linear-gradient(135deg,#667eea,#764ba2);
# #                         color:white; padding:0.6rem; border-radius:8px; text-decoration:none;
# #                         font-weight:600; font-size:0.85rem;">
# #                         Apply Now →
# #                     </a>
# #                     """, unsafe_allow_html=True)



# import os
# import re
# import time
# import random
# import requests
# import streamlit as st


# # ─────────────────────────────────────────────────────────────────────────────
# #  Helpers
# # ─────────────────────────────────────────────────────────────────────────────

# def clean_html(text):
#     """Strip HTML tags and normalise whitespace."""
#     if not text:
#         return ""
#     text = re.sub(r"<[^>]+>", " ", str(text))
#     for entity, replacement in [("&nbsp;", " "), ("&amp;", "&"),
#                                  ("&lt;", "<"), ("&gt;", ">"), ("&#39;", "'")]:
#         text = text.replace(entity, replacement)
#     return re.sub(r"\s+", " ", text).strip()


# def time_ago(timestamp):
#     """Convert a UTC epoch timestamp to a human-readable string."""
#     if not timestamp:
#         return "Recently"
#     try:
#         diff = int(time.time()) - int(timestamp)
#         if diff < 3600:
#             return "Just now"
#         if diff < 86400:
#             return f"{diff // 3600}h ago"
#         days = diff // 86400
#         if days == 1:
#             return "1 day ago"
#         if days < 30:
#             return f"{days} days ago"
#         months = days // 30
#         return f"{months} month{'s' if months > 1 else ''} ago"
#     except Exception:
#         return "Recently"


# def score_job(job, resume_analysis):
#     """Rough match score based on resume keywords found in job text."""
#     if not resume_analysis:
#         return random.randint(60, 85)
#     target_roles = [r.lower() for r in resume_analysis.get("target_roles", [])]
#     tech_skills  = [s.lower() for s in resume_analysis.get("skills", {}).get("technical", [])]
#     soft_skills  = [s.lower() for s in resume_analysis.get("skills", {}).get("soft", [])]
#     all_keywords = target_roles + tech_skills + soft_skills
#     text = (job.get("title", "") + " " + job.get("description", "")).lower()
#     hits = sum(1 for kw in all_keywords if kw in text)
#     base = min(95, 50 + hits * 5)
#     return max(40, base + random.randint(-5, 5))


# def match_reasons(job, resume_analysis):
#     """Return up to 4 strings explaining why the candidate matches."""
#     if not resume_analysis:
#         return []
#     tech_skills = resume_analysis.get("skills", {}).get("technical", [])
#     text = (job.get("title", "") + " " + job.get("description", "")).lower()
#     matched = [s for s in tech_skills if s.lower() in text][:4]
#     return [f"{s} skill matches" for s in matched]


# # ─────────────────────────────────────────────────────────────────────────────
# #  JSearch API  (RapidAPI)
# #  Free key: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch
# #  Free tier: 200 requests / month  (~10 jobs per call → 2 000 jobs/month free)
# # ─────────────────────────────────────────────────────────────────────────────

# JSEARCH_URL  = "https://jsearch.p.rapidapi.com/search"
# JSEARCH_HOST = "jsearch.p.rapidapi.com"


# def fetch_jsearch_page(query, location, page, rapidapi_key, date_posted="month"):
#     """Fetch one page (≤10 results) from JSearch."""
#     headers = {
#         "X-RapidAPI-Key":  rapidapi_key,
#         "X-RapidAPI-Host": JSEARCH_HOST,
#     }
#     params = {
#         "query":       f"{query} in {location}",
#         "page":        str(page),
#         "num_pages":   "1",
#         "date_posted": date_posted,
#         "country":     "in",
#     }
#     resp = requests.get(JSEARCH_URL, headers=headers, params=params, timeout=15)
#     if resp.status_code == 429:
#         time.sleep(6)
#         resp = requests.get(JSEARCH_URL, headers=headers, params=params, timeout=15)
#     if resp.status_code == 403:
#         raise RuntimeError(
#             "Invalid or missing RAPIDAPI_KEY. "
#             "Get a free key at https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch"
#         )
#     resp.raise_for_status()
#     return resp.json().get("data", [])


# def jsearch_jobs(query, location, num_jobs, rapidapi_key, resume_analysis):
#     """
#     Fetch `num_jobs` real jobs from JSearch across multiple pages.
#     Returns (jobs_list, error_or_None).
#     """
#     all_raw  = []
#     seen_ids = set()
#     # Fetch extra pages as buffer; JSearch returns ~10 per page
#     max_pages = max(3, (num_jobs // 10) + 3)

#     for page in range(1, max_pages + 1):
#         if len(all_raw) >= num_jobs:
#             break
#         try:
#             page_data = fetch_jsearch_page(query, location, page, rapidapi_key)
#         except RuntimeError as e:
#             return None, str(e)
#         except Exception as e:
#             return None, f"Network error: {e}"

#         # If first page returns nothing, try a wider date range
#         if not page_data and page == 1:
#             try:
#                 page_data = fetch_jsearch_page(
#                     query, location, 1, rapidapi_key, date_posted="year"
#                 )
#             except Exception:
#                 pass

#         if not page_data:
#             break   # no more results

#         for raw in page_data:
#             jid = raw.get("job_id", "")
#             if jid in seen_ids:
#                 continue
#             seen_ids.add(jid)
#             all_raw.append(raw)

#         time.sleep(0.4)  # be polite

#     if not all_raw:
#         return None, (
#             "No real jobs found for those keywords. "
#             "Try different terms or a broader date range."
#         )

#     jobs = []
#     for raw in all_raw[:num_jobs]:
#         apply_url = raw.get("job_apply_link") or raw.get("job_google_link") or ""

#         # Salary
#         salary = ""
#         s_min = raw.get("job_min_salary")
#         s_max = raw.get("job_max_salary")
#         s_cur = raw.get("job_salary_currency", "INR")
#         s_per = raw.get("job_salary_period", "")
#         if s_min and s_max:
#             salary = f"{s_cur} {int(s_min):,} \u2013 {int(s_max):,} / {s_per}".strip(" /")
#         elif s_min:
#             salary = f"{s_cur} {int(s_min):,}+ / {s_per}".strip(" /")

#         # Job type
#         emp_type  = (raw.get("job_employment_type") or "").replace("_", " ").title() or "Full-time"
#         is_remote = raw.get("job_is_remote", False)
#         job_type  = emp_type + (" (Remote)" if is_remote else "")

#         # Location
#         city    = raw.get("job_city", "") or ""
#         state   = raw.get("job_state", "") or ""
#         country = raw.get("job_country", "") or ""
#         loc     = ", ".join(filter(None, [city, state, country])) or location

#         # Description (capped at 600 chars)
#         desc = clean_html(raw.get("job_description", ""))[:600]
#         if len(desc) == 600:
#             desc = desc.rsplit(" ", 1)[0] + "\u2026"

#         # Requirements from highlights
#         qualifs = (raw.get("job_highlights") or {}).get("Qualifications", []) or []
#         reqs    = [clean_html(q) for q in qualifs[:5]]

#         job = {
#             "title":         clean_html(raw.get("job_title", "Unknown Role")),
#             "company":       clean_html(raw.get("employer_name", "Unknown Company")),
#             "location":      loc,
#             "description":   desc,
#             "requirements":  reqs,
#             "salary_range":  salary,
#             "job_type":      job_type,
#             "posted":        time_ago(raw.get("job_posted_at_timestamp")),
#             "url":           apply_url,
#             "publisher":     raw.get("job_publisher", ""),
#             "logo":          raw.get("employer_logo", ""),
#             "match_score":   0,
#             "match_reasons": [],
#         }
#         job["match_score"]   = score_job(job, resume_analysis)
#         job["match_reasons"] = match_reasons(job, resume_analysis)
#         jobs.append(job)

#     return jobs, None


# # ─────────────────────────────────────────────────────────────────────────────
# #  Fallback: Selenium LinkedIn scraper
# # ─────────────────────────────────────────────────────────────────────────────

# def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
#     try:
#         from selenium import webdriver
#         from selenium.webdriver.common.by import By
#         from selenium.webdriver.chrome.options import Options
#         import urllib.parse

#         options = Options()
#         for arg in ["--headless", "--no-sandbox", "--disable-dev-shm-usage",
#                     "--disable-gpu", "--window-size=1920,1080",
#                     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
#                     "--disable-blink-features=AutomationControlled"]:
#             options.add_argument(arg)
#         options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         options.add_experimental_option("useAutomationExtension", False)

#         driver = webdriver.Chrome(options=options)
#         driver.execute_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")

#         url = (
#             f"https://www.linkedin.com/jobs/search/"
#             f"?keywords={urllib.parse.quote(keywords)}"
#             f"&location={urllib.parse.quote(location)}&f_TPR=r86400&sortBy=R"
#         )
#         driver.get(url)
#         time.sleep(3)

#         jobs = []
#         for card in driver.find_elements(By.CSS_SELECTOR, "div.base-card")[:num_jobs]:
#             try:
#                 title   = clean_html(card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text)
#                 company = clean_html(card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text)
#                 loc     = clean_html(card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text)
#                 try:
#                     link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
#                 except Exception:
#                     link = ""
#                 try:
#                     posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
#                 except Exception:
#                     posted = "Recently"
#                 if title and company:
#                     jobs.append({
#                         "title": title, "company": company, "location": loc,
#                         "url": link, "posted": posted, "description": "",
#                         "requirements": [], "job_type": "Full-time",
#                         "salary_range": "", "match_reasons": [],
#                         "match_score": random.randint(65, 95),
#                         "publisher": "LinkedIn", "logo": "",
#                     })
#             except Exception:
#                 continue
#         driver.quit()
#         return jobs, None
#     except ImportError:
#         return None, "selenium_not_installed"
#     except Exception as e:
#         return None, str(e)


# # ─────────────────────────────────────────────────────────────────────────────
# #  Streamlit page
# # ─────────────────────────────────────────────────────────────────────────────

# def show():
#     st.markdown("""
#     <h1 style="font-family:'Syne',sans-serif;
#                background:linear-gradient(135deg,#667eea,#f093fb);
#                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
#         💼 Job Recommendations
#     </h1>
#     <p style="color:#888;">Real-time job listings from LinkedIn, Indeed, Glassdoor &amp; more</p>
#     """, unsafe_allow_html=True)

#     # Guard: resume required
#     if not st.session_state.get("resume_text"):
#         st.markdown("""
#         <div style="background:rgba(244,92,67,0.1);border:1px solid rgba(244,92,67,0.3);
#             border-radius:12px;padding:2rem;text-align:center;">
#             <div style="font-size:3rem;">📄</div>
#             <h3 style="color:#f45c43;">No Resume Found</h3>
#             <p style="color:#888;">Upload your resume first to get personalised job recommendations.</p>
#         </div>
#         """, unsafe_allow_html=True)
#         if st.button("📤 Upload Resume", use_container_width=True):
#             st.session_state.current_page = "resume"
#             st.rerun()
#         return

#     # API key
#     rapidapi_key = (
#         os.getenv("RAPIDAPI_KEY", "")
#         or st.session_state.get("rapidapi_key", "")
#     )
#     if not rapidapi_key:
#         st.info(
#             "🔑 **JSearch API key required for real jobs.**\n\n"
#             "Get a **free** key (200 req/month) → "
#             "https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch\n\n"
#             "Then add `RAPIDAPI_KEY=your_key` to your `.env` file, or enter it below."
#         )
#         entered = st.text_input(
#             "Enter RapidAPI Key (JSearch)", type="password",
#             placeholder="paste your key here"
#         )
#         if entered:
#             st.session_state.rapidapi_key = entered
#             rapidapi_key = entered

#     # Search config
#     st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
#     st.markdown(
#         '<h4 style="font-family:Syne,sans-serif;color:#e8e8f0;margin-top:0;">'
#         '🔍 Job Search Configuration</h4>',
#         unsafe_allow_html=True
#     )

#     default_title = ""
#     if st.session_state.get("resume_analysis"):
#         roles = st.session_state.resume_analysis.get("target_roles", [])
#         if roles:
#             default_title = roles[0]

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         job_title = st.text_input("🎯 Job Title / Keywords",
#                                   value=default_title or "Software Engineer")
#     with col2:
#         location = st.text_input("📍 Location", value="India")
#     with col3:
#         num_jobs = st.slider("📊 Number of Jobs", min_value=5, max_value=50, value=15)

#     col1, col2 = st.columns(2)
#     with col1:
#         date_filter = st.selectbox("📅 Date Posted",
#                                    ["Past Month", "Past Week", "Past 3 Days", "Today"])
#     with col2:
#         search_mode = st.selectbox("🛠️ Search Mode", [
#             "JSearch API – Real Jobs (LinkedIn, Indeed, Glassdoor…)",
#             "LinkedIn Selenium Scraping (Requires Chrome Driver)",
#         ])

#     st.markdown('</div>', unsafe_allow_html=True)

#     date_map    = {"Today": "today", "Past 3 Days": "3days",
#                    "Past Week": "week", "Past Month": "month"}
#     date_posted = date_map.get(date_filter, "month")
#     use_selenium = "Selenium" in search_mode

#     col1, col2 = st.columns([3, 1])
#     with col1:
#         search_btn = st.button("🚀 Find Real Jobs", use_container_width=True)
#     with col2:
#         if st.session_state.get("job_results"):
#             if st.button("🗑️ Clear", use_container_width=True):
#                 st.session_state.job_results = []
#                 st.rerun()

#     if search_btn:
#         if not use_selenium and not rapidapi_key:
#             st.error("❌ Enter your RapidAPI key above to fetch real jobs.")
#         else:
#             with st.spinner(f"🔍 Fetching up to {num_jobs} real jobs… please wait…"):
#                 if use_selenium:
#                     jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
#                     if error:
#                         st.warning(f"⚠️ Selenium failed ({error}). Falling back to JSearch API…")
#                         if rapidapi_key:
#                             jobs, error = jsearch_jobs(
#                                 job_title, location, num_jobs, rapidapi_key,
#                                 st.session_state.get("resume_analysis") or {}
#                             )
#                         else:
#                             st.error("❌ No RapidAPI key available for fallback.")
#                             return
#                 else:
#                     jobs, error = jsearch_jobs(
#                         job_title, location, num_jobs, rapidapi_key,
#                         st.session_state.get("resume_analysis") or {}
#                     )

#                 if error:
#                     st.error(f"❌ {error}")
#                 elif jobs:
#                     st.session_state.job_results = jobs
#                     st.success(f"✅ Found {len(jobs)} real job listings!")
#                     st.rerun()
#                 else:
#                     st.error("❌ No jobs returned. Try different keywords or a broader date range.")

#     # Display results
#     if not st.session_state.get("job_results"):
#         return

#     jobs        = st.session_state.job_results
#     jobs_sorted = sorted(jobs, key=lambda x: x.get("match_score", 0), reverse=True)

#     st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

#     avg_score  = sum(j.get("match_score", 0) for j in jobs) / len(jobs)
#     high_match = sum(1 for j in jobs if j.get("match_score", 0) >= 80)
#     top_score  = max(j.get("match_score", 0) for j in jobs)

#     c1, c2, c3, c4 = st.columns(4)
#     for col, label, value, color in [
#         (c1, "TOTAL JOBS",     len(jobs),          "#667eea"),
#         (c2, "AVG MATCH",      f"{avg_score:.0f}%", "#f093fb"),
#         (c3, "HIGH MATCH 80+", high_match,           "#38ef7d"),
#         (c4, "TOP MATCH",      f"{top_score}%",     "#ffd200"),
#     ]:
#         col.markdown(
#             f'<div class="metric-card" style="text-align:center;">'
#             f'<div style="color:#888;font-size:0.8rem;">{label}</div>'
#             f'<div style="font-size:2rem;font-weight:800;color:{color};">{value}</div>'
#             f'</div>',
#             unsafe_allow_html=True
#         )

#     st.markdown(
#         f'<h3 style="font-family:Syne,sans-serif;color:#e8e8f0;margin-top:1.5rem;">'
#         f'🎯 {len(jobs)} Real Job Matches</h3>',
#         unsafe_allow_html=True
#     )

#     for i, job in enumerate(jobs_sorted):
#         score       = job.get("match_score", 0)
#         score_col   = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
#         score_label = ("🔥 Top Match" if score >= 85
#                        else "✅ Good Match" if score >= 70 else "🔵 Fair Match")

#         title     = job.get("title", "Job Title")
#         company   = job.get("company", "Company")
#         loc_      = job.get("location", "")
#         desc      = job.get("description", "")
#         job_type  = job.get("job_type", "Full-time")
#         posted    = job.get("posted", "Recently")
#         salary    = job.get("salary_range", "")
#         reqs      = job.get("requirements", [])
#         reasons   = job.get("match_reasons", [])
#         url       = job.get("url", "")
#         publisher = job.get("publisher", "")

#         with st.expander(
#             f"{score_label} | {title} at {company} — {score}% match",
#             expanded=(i < 2)
#         ):
#             left, right = st.columns([3, 1])

#             with left:
#                 src_badge = (
#                     f'<span style="background:rgba(102,126,234,0.2);color:#667eea;'
#                     f'padding:2px 8px;border-radius:10px;font-size:0.75rem;">'
#                     f'📡 {publisher}</span>'
#                     if publisher else ""
#                 )
#                 st.markdown(f"""
#                 <div style="margin-bottom:1rem;">
#                     <h3 style="color:#e8e8f0;font-family:Syne,sans-serif;margin:0 0 0.25rem;">{title}</h3>
#                     <div style="color:#667eea;font-weight:600;font-size:1rem;margin-bottom:0.4rem;">🏢 {company}</div>
#                     <div style="color:#888;font-size:0.88rem;display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:0.4rem;">
#                         <span>📍 {loc_}</span>
#                         <span>🕐 {job_type}</span>
#                         <span>📅 {posted}</span>
#                         {"<span>💰 " + salary + "</span>" if salary else ""}
#                     </div>
#                     {src_badge}
#                 </div>
#                 """, unsafe_allow_html=True)

#                 if desc:
#                     st.markdown(f"""
#                     <div style="background:rgba(102,126,234,0.07);border-left:3px solid #667eea;
#                         border-radius:0 8px 8px 0;padding:0.75rem 1rem;margin:0.75rem 0;
#                         color:#ccc;font-size:0.9rem;">{desc}</div>
#                     """, unsafe_allow_html=True)

#                 if reqs:
#                     st.markdown('<p style="color:#e8e8f0;font-weight:600;margin:0.75rem 0 0.4rem;">📋 Key Requirements</p>', unsafe_allow_html=True)
#                     req_html = "".join(
#                         f'<div style="color:#888;font-size:0.85rem;padding:0.25rem 0;'
#                         f'border-bottom:1px solid #1a1a2e;">• {r}</div>'
#                         for r in reqs[:5]
#                     )
#                     st.markdown(f'<div style="margin-bottom:0.75rem;">{req_html}</div>', unsafe_allow_html=True)

#                 if reasons:
#                     st.markdown('<p style="color:#e8e8f0;font-weight:600;margin:0.75rem 0 0.4rem;">✅ Why You Match</p>', unsafe_allow_html=True)
#                     badges = " ".join(
#                         f'<span style="background:rgba(56,239,125,0.15);color:#38ef7d;'
#                         f'padding:0.25rem 0.75rem;border-radius:20px;font-size:0.8rem;'
#                         f'display:inline-block;margin:2px;">✓ {r}</span>'
#                         for r in reasons
#                     )
#                     st.markdown(f'<div style="margin-bottom:0.5rem;">{badges}</div>', unsafe_allow_html=True)

#             with right:
#                 st.markdown(f"""
#                 <div style="text-align:center;padding:1.25rem 1rem;background:rgba(26,26,46,0.9);
#                     border-radius:12px;border:2px solid {score_col}44;margin-bottom:0.75rem;">
#                     <div style="color:#888;font-size:0.75rem;letter-spacing:1px;">MATCH SCORE</div>
#                     <div style="font-size:3.5rem;font-weight:800;color:{score_col};line-height:1.1;">{score}%</div>
#                     <div style="font-size:0.82rem;color:{score_col};margin-top:0.25rem;">{score_label}</div>
#                 </div>
#                 """, unsafe_allow_html=True)

#                 if url and url.startswith("http"):
#                     st.markdown(f"""
#                     <a href="{url}" target="_blank"
#                         style="display:block;text-align:center;
#                         background:linear-gradient(135deg,#667eea,#764ba2);
#                         color:white;padding:0.6rem;border-radius:8px;
#                         text-decoration:none;font-weight:600;font-size:0.85rem;">
#                         Apply Now →
#                     </a>
#                     """, unsafe_allow_html=True)
#                 else:
#                     import urllib.parse as _up
#                     q  = _up.quote(f"{title} {company} jobs")
#                     fb = f"https://www.google.com/search?q={q}"
#                     st.markdown(f"""
#                     <a href="{fb}" target="_blank"
#                         style="display:block;text-align:center;
#                         background:rgba(102,126,234,0.2);color:#667eea;
#                         padding:0.6rem;border-radius:8px;text-decoration:none;
#                         font-weight:600;font-size:0.85rem;border:1px solid #667eea44;">
#                         Search Online →
#                     </a>
#                     """, unsafe_allow_html=True)



import os
import re
import time
import random
import requests
import streamlit as st


# ─────────────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────────────

def clean_html(text):
    """Strip HTML tags and normalise whitespace."""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", str(text))
    for entity, replacement in [("&nbsp;", " "), ("&amp;", "&"),
                                 ("&lt;", "<"), ("&gt;", ">"), ("&#39;", "'")]:
        text = text.replace(entity, replacement)
    return re.sub(r"\s+", " ", text).strip()


def time_ago(timestamp):
    """Convert a UTC epoch timestamp to a human-readable string."""
    if not timestamp:
        return "Recently"
    try:
        diff = int(time.time()) - int(timestamp)
        if diff < 3600:
            return "Just now"
        if diff < 86400:
            return f"{diff // 3600}h ago"
        days = diff // 86400
        if days == 1:
            return "1 day ago"
        if days < 30:
            return f"{days} days ago"
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    except Exception:
        return "Recently"


def score_job(job, resume_analysis):
    """Rough match score based on resume keywords found in job text."""
    if not resume_analysis:
        return random.randint(60, 85)
    target_roles = [r.lower() for r in resume_analysis.get("target_roles", [])]
    tech_skills  = [s.lower() for s in resume_analysis.get("skills", {}).get("technical", [])]
    soft_skills  = [s.lower() for s in resume_analysis.get("skills", {}).get("soft", [])]
    all_keywords = target_roles + tech_skills + soft_skills
    text = (job.get("title", "") + " " + job.get("description", "")).lower()
    hits = sum(1 for kw in all_keywords if kw in text)
    base = min(95, 50 + hits * 5)
    return max(40, base + random.randint(-5, 5))


def match_reasons(job, resume_analysis):
    """Return up to 4 strings explaining why the candidate matches."""
    if not resume_analysis:
        return []
    tech_skills = resume_analysis.get("skills", {}).get("technical", [])
    text = (job.get("title", "") + " " + job.get("description", "")).lower()
    matched = [s for s in tech_skills if s.lower() in text][:4]
    return [f"{s} skill matches" for s in matched]


# ─────────────────────────────────────────────────────────────────────────────
#  JSearch API  (RapidAPI)
#  Free key: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch
#  Free tier: 200 requests / month  (~10 jobs per call → 2 000 jobs/month free)
# ─────────────────────────────────────────────────────────────────────────────

JSEARCH_URL  = "https://jsearch.p.rapidapi.com/search"
JSEARCH_HOST = "jsearch.p.rapidapi.com"


def fetch_jsearch_page(query, location, page, rapidapi_key, date_posted="month"):
    """Fetch one page (≤10 results) from JSearch."""
    headers = {
        "X-RapidAPI-Key":  rapidapi_key,
        "X-RapidAPI-Host": JSEARCH_HOST,
    }
    params = {
        "query":       f"{query} in {location}",
        "page":        str(page),
        "num_pages":   "1",
        "date_posted": date_posted,
        "country":     "in",
    }
    resp = requests.get(JSEARCH_URL, headers=headers, params=params, timeout=15)
    if resp.status_code == 429:
        time.sleep(6)
        resp = requests.get(JSEARCH_URL, headers=headers, params=params, timeout=15)
    if resp.status_code == 403:
        raise RuntimeError(
            "Invalid or missing RAPIDAPI_KEY. "
            "Get a free key at https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch"
        )
    resp.raise_for_status()
    return resp.json().get("data", [])


def jsearch_jobs(query, location, num_jobs, rapidapi_key, resume_analysis):
    """
    Fetch `num_jobs` real jobs from JSearch across multiple pages.
    Returns (jobs_list, error_or_None).
    """
    all_raw  = []
    seen_ids = set()
    # Fetch extra pages as buffer; JSearch returns ~10 per page
    max_pages = max(3, (num_jobs // 10) + 3)

    for page in range(1, max_pages + 1):
        if len(all_raw) >= num_jobs:
            break
        try:
            page_data = fetch_jsearch_page(query, location, page, rapidapi_key)
        except RuntimeError as e:
            return None, str(e)
        except Exception as e:
            return None, f"Network error: {e}"

        # If first page returns nothing, try a wider date range
        if not page_data and page == 1:
            try:
                page_data = fetch_jsearch_page(
                    query, location, 1, rapidapi_key, date_posted="year"
                )
            except Exception:
                pass

        if not page_data:
            break   # no more results

        for raw in page_data:
            jid = raw.get("job_id", "")
            if jid in seen_ids:
                continue
            seen_ids.add(jid)
            all_raw.append(raw)

        time.sleep(0.4)  # be polite

    if not all_raw:
        return None, (
            "No real jobs found for those keywords. "
            "Try different terms or a broader date range."
        )

    jobs = []
    for raw in all_raw[:num_jobs]:
        apply_url = raw.get("job_apply_link") or raw.get("job_google_link") or ""

        # Salary
        salary = ""
        s_min = raw.get("job_min_salary")
        s_max = raw.get("job_max_salary")
        s_cur = raw.get("job_salary_currency", "INR")
        s_per = raw.get("job_salary_period", "")
        if s_min and s_max:
            salary = f"{s_cur} {int(s_min):,} \u2013 {int(s_max):,} / {s_per}".strip(" /")
        elif s_min:
            salary = f"{s_cur} {int(s_min):,}+ / {s_per}".strip(" /")

        # Job type
        emp_type  = (raw.get("job_employment_type") or "").replace("_", " ").title() or "Full-time"
        is_remote = raw.get("job_is_remote", False)
        job_type  = emp_type + (" (Remote)" if is_remote else "")

        # Location
        city    = raw.get("job_city", "") or ""
        state   = raw.get("job_state", "") or ""
        country = raw.get("job_country", "") or ""
        loc     = ", ".join(filter(None, [city, state, country])) or location

        # Description (capped at 600 chars)
        desc = clean_html(raw.get("job_description", ""))[:600]
        if len(desc) == 600:
            desc = desc.rsplit(" ", 1)[0] + "\u2026"

        # Requirements from highlights
        qualifs = (raw.get("job_highlights") or {}).get("Qualifications", []) or []
        reqs    = [clean_html(q) for q in qualifs[:5]]

        job = {
            "title":         clean_html(raw.get("job_title", "Unknown Role")),
            "company":       clean_html(raw.get("employer_name", "Unknown Company")),
            "location":      loc,
            "description":   desc,
            "requirements":  reqs,
            "salary_range":  salary,
            "job_type":      job_type,
            "posted":        time_ago(raw.get("job_posted_at_timestamp")),
            "url":           apply_url,
            "publisher":     raw.get("job_publisher", ""),
            "logo":          raw.get("employer_logo", ""),
            "match_score":   0,
            "match_reasons": [],
        }
        job["match_score"]   = score_job(job, resume_analysis)
        job["match_reasons"] = match_reasons(job, resume_analysis)
        jobs.append(job)

    return jobs, None


# ─────────────────────────────────────────────────────────────────────────────
#  Fallback: Selenium LinkedIn scraper
# ─────────────────────────────────────────────────────────────────────────────

def scrape_linkedin_jobs_selenium(keywords, location, num_jobs=10):
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        import urllib.parse

        options = Options()
        for arg in ["--headless", "--no-sandbox", "--disable-dev-shm-usage",
                    "--disable-gpu", "--window-size=1920,1080",
                    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "--disable-blink-features=AutomationControlled"]:
            options.add_argument(arg)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")

        url = (
            f"https://www.linkedin.com/jobs/search/"
            f"?keywords={urllib.parse.quote(keywords)}"
            f"&location={urllib.parse.quote(location)}&f_TPR=r86400&sortBy=R"
        )
        driver.get(url)
        time.sleep(3)

        jobs = []
        for card in driver.find_elements(By.CSS_SELECTOR, "div.base-card")[:num_jobs]:
            try:
                title   = clean_html(card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text)
                company = clean_html(card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text)
                loc     = clean_html(card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text)
                try:
                    link = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")
                except Exception:
                    link = ""
                try:
                    posted = card.find_element(By.CSS_SELECTOR, "time").text.strip()
                except Exception:
                    posted = "Recently"
                if title and company:
                    jobs.append({
                        "title": title, "company": company, "location": loc,
                        "url": link, "posted": posted, "description": "",
                        "requirements": [], "job_type": "Full-time",
                        "salary_range": "", "match_reasons": [],
                        "match_score": random.randint(65, 95),
                        "publisher": "LinkedIn", "logo": "",
                    })
            except Exception:
                continue
        driver.quit()
        return jobs, None
    except ImportError:
        return None, "selenium_not_installed"
    except Exception as e:
        return None, str(e)


# ─────────────────────────────────────────────────────────────────────────────
#  Streamlit page
# ─────────────────────────────────────────────────────────────────────────────

def show():
    st.markdown("""
    <h1 style="font-family:'Syne',sans-serif;
               background:linear-gradient(135deg,#667eea,#f093fb);
               -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
        💼 Job Recommendations
    </h1>
    <p style="color:#888;">Real-time job listings from LinkedIn, Indeed, Glassdoor &amp; more</p>
    """, unsafe_allow_html=True)

    # Guard: resume required
    if not st.session_state.get("resume_text"):
        st.markdown("""
        <div style="background:rgba(244,92,67,0.1);border:1px solid rgba(244,92,67,0.3);
            border-radius:12px;padding:2rem;text-align:center;">
            <div style="font-size:3rem;">📄</div>
            <h3 style="color:#f45c43;">No Resume Found</h3>
            <p style="color:#888;">Upload your resume first to get personalised job recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📤 Upload Resume", use_container_width=True):
            st.session_state.current_page = "resume"
            st.rerun()
        return

    # API key
    rapidapi_key = (
        os.getenv("RAPIDAPI_KEY", "")
        or st.session_state.get("rapidapi_key", "")
    )
    if not rapidapi_key:
        st.info(
            "🔑 **JSearch API key required for real jobs.**\n\n"
            "Get a **free** key (200 req/month) → "
            "https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch\n\n"
            "Then add `RAPIDAPI_KEY=your_key` to your `.env` file, or enter it below."
        )
        entered = st.text_input(
            "Enter RapidAPI Key (JSearch)", type="password",
            placeholder="paste your key here"
        )
        if entered:
            st.session_state.rapidapi_key = entered
            rapidapi_key = entered

    # Search config
    st.markdown('<div class="metric-card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
    st.markdown(
        '<h4 style="font-family:Syne,sans-serif;color:#e8e8f0;margin-top:0;">'
        '🔍 Job Search Configuration</h4>',
        unsafe_allow_html=True
    )

    default_title = ""
    if st.session_state.get("resume_analysis"):
        roles = st.session_state.resume_analysis.get("target_roles", [])
        if roles:
            default_title = roles[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        job_title = st.text_input("🎯 Job Title / Keywords",
                                  value=default_title or "Software Engineer")
    with col2:
        location = st.text_input("📍 Location", value="India")
    with col3:
        num_jobs = st.slider("📊 Number of Jobs", min_value=5, max_value=50, value=15)

    col1, col2 = st.columns(2)
    with col1:
        date_filter = st.selectbox("📅 Date Posted",
                                   ["Past Month", "Past Week", "Past 3 Days", "Today"])
    with col2:
        search_mode = st.selectbox("🛠️ Search Mode", [
            "JSearch(LinkedIn, Indeed, Glassdoor…)",
        #     "LinkedIn Selenium Scraping (Requires Chrome Driver)",
         ])

    st.markdown('</div>', unsafe_allow_html=True)

    date_map    = {"Today": "today", "Past 3 Days": "3days",
                   "Past Week": "week", "Past Month": "month"}
    date_posted = date_map.get(date_filter, "month")
    use_selenium = "Selenium" in search_mode

    col1, col2 = st.columns([3, 1])
    with col1:
        search_btn = st.button("🚀 Find Real Jobs", use_container_width=True)
    with col2:
        if st.session_state.get("job_results"):
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.job_results = []
                st.rerun()

    if search_btn:
        if not use_selenium and not rapidapi_key:
            st.error("❌ Enter your RapidAPI key above to fetch real jobs.")
        else:
            with st.spinner(f"🔍 Fetching up to {num_jobs} real jobs… please wait…"):
                if use_selenium:
                    jobs, error = scrape_linkedin_jobs_selenium(job_title, location, num_jobs)
                    if error:
                        st.warning(f"⚠️ Selenium failed ({error}). Falling back to JSearch API…")
                        if rapidapi_key:
                            jobs, error = jsearch_jobs(
                                job_title, location, num_jobs, rapidapi_key,
                                st.session_state.get("resume_analysis") or {}
                            )
                        else:
                            st.error("❌ No RapidAPI key available for fallback.")
                            return
                else:
                    jobs, error = jsearch_jobs(
                        job_title, location, num_jobs, rapidapi_key,
                        st.session_state.get("resume_analysis") or {}
                    )

                if error:
                    st.error(f"❌ {error}")
                elif jobs:
                    st.session_state.job_results = jobs
                    st.success(f"✅ Found {len(jobs)} real job listings!")
                    st.rerun()
                else:
                    st.error("❌ No jobs returned. Try different keywords or a broader date range.")

    # Display results
    if not st.session_state.get("job_results"):
        return

    jobs        = st.session_state.job_results
    jobs_sorted = sorted(jobs, key=lambda x: x.get("match_score", 0), reverse=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    avg_score  = sum(j.get("match_score", 0) for j in jobs) / len(jobs)
    high_match = sum(1 for j in jobs if j.get("match_score", 0) >= 80)
    top_score  = max(j.get("match_score", 0) for j in jobs)

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value, color in [
        (c1, "TOTAL JOBS",     len(jobs),          "#667eea"),
        (c2, "AVG MATCH",      f"{avg_score:.0f}%", "#f093fb"),
        (c3, "HIGH MATCH 80+", high_match,           "#38ef7d"),
        (c4, "TOP MATCH",      f"{top_score}%",     "#ffd200"),
    ]:
        col.markdown(
            f'<div class="metric-card" style="text-align:center;">'
            f'<div style="color:#888;font-size:0.8rem;">{label}</div>'
            f'<div style="font-size:2rem;font-weight:800;color:{color};">{value}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<h3 style="font-family:Syne,sans-serif;color:#e8e8f0;margin-top:1.5rem;">'
        f'🎯 {len(jobs)} Real Job Matches</h3>',
        unsafe_allow_html=True
    )

    for i, job in enumerate(jobs_sorted):
        score       = job.get("match_score", 0)
        score_col   = "#38ef7d" if score >= 80 else "#ffd200" if score >= 60 else "#f45c43"
        score_label = ("🔥 Top Match" if score >= 85
                       else "✅ Good Match" if score >= 70 else "🔵 Fair Match")

        title     = job.get("title", "Job Title")
        company   = job.get("company", "Company")
        loc_      = job.get("location", "")
        desc      = job.get("description", "")
        job_type  = job.get("job_type", "Full-time")
        posted    = job.get("posted", "Recently")
        salary    = job.get("salary_range", "")
        reqs      = job.get("requirements", [])
        reasons   = job.get("match_reasons", [])
        url       = job.get("url", "")
        publisher = job.get("publisher", "")

        with st.expander(
            f"{score_label} | {title} at {company} — {score}% match",
            expanded=(i < 2)
        ):
            left, right = st.columns([3, 1])

            with left:
                salary_html    = f'<span>💰 {salary}</span>' if salary else ""
                publisher_html = (
                    f'<span style="background:rgba(102,126,234,0.2);color:#667eea;'
                    f'padding:2px 8px;border-radius:10px;font-size:0.75rem;'
                    f'display:inline-block;margin-top:0.3rem;">📡 {publisher}</span>'
                    if publisher else ""
                )
                header_html = (
                    '<div style="margin-bottom:1rem;">'
                    f'<h3 style="color:#e8e8f0;font-family:Syne,sans-serif;margin:0 0 0.25rem;">{title}</h3>'
                    f'<div style="color:#667eea;font-weight:600;font-size:1rem;margin-bottom:0.4rem;">🏢 {company}</div>'
                    '<div style="color:#888;font-size:0.88rem;display:flex;flex-wrap:wrap;gap:0.75rem;margin-bottom:0.4rem;">'
                    f'<span>📍 {loc_}</span>'
                    f'<span>🕐 {job_type}</span>'
                    f'<span>📅 {posted}</span>'
                    f'{salary_html}'
                    '</div>'
                    f'{publisher_html}'
                    '</div>'
                )
                st.markdown(header_html, unsafe_allow_html=True)

                if desc:
                    st.markdown(f"""
                    <div style="background:rgba(102,126,234,0.07);border-left:3px solid #667eea;
                        border-radius:0 8px 8px 0;padding:0.75rem 1rem;margin:0.75rem 0;
                        color:#ccc;font-size:0.9rem;">{desc}</div>
                    """, unsafe_allow_html=True)

                if reqs:
                    st.markdown('<p style="color:#e8e8f0;font-weight:600;margin:0.75rem 0 0.4rem;">📋 Key Requirements</p>', unsafe_allow_html=True)
                    req_html = "".join(
                        f'<div style="color:#888;font-size:0.85rem;padding:0.25rem 0;'
                        f'border-bottom:1px solid #1a1a2e;">• {r}</div>'
                        for r in reqs[:5]
                    )
                    st.markdown(f'<div style="margin-bottom:0.75rem;">{req_html}</div>', unsafe_allow_html=True)

                if reasons:
                    st.markdown('<p style="color:#e8e8f0;font-weight:600;margin:0.75rem 0 0.4rem;">✅ Why You Match</p>', unsafe_allow_html=True)
                    badges = " ".join(
                        f'<span style="background:rgba(56,239,125,0.15);color:#38ef7d;'
                        f'padding:0.25rem 0.75rem;border-radius:20px;font-size:0.8rem;'
                        f'display:inline-block;margin:2px;">✓ {r}</span>'
                        for r in reasons
                    )
                    st.markdown(f'<div style="margin-bottom:0.5rem;">{badges}</div>', unsafe_allow_html=True)

            with right:
                st.markdown(f"""
                <div style="text-align:center;padding:1.25rem 1rem;background:rgba(26,26,46,0.9);
                    border-radius:12px;border:2px solid {score_col}44;margin-bottom:0.75rem;">
                    <div style="color:#888;font-size:0.75rem;letter-spacing:1px;">MATCH SCORE</div>
                    <div style="font-size:3.5rem;font-weight:800;color:{score_col};line-height:1.1;">{score}%</div>
                    <div style="font-size:0.82rem;color:{score_col};margin-top:0.25rem;">{score_label}</div>
                </div>
                """, unsafe_allow_html=True)

                if url and url.startswith("http"):
                    st.markdown(f"""
                    <a href="{url}" target="_blank"
                        style="display:block;text-align:center;
                        background:linear-gradient(135deg,#667eea,#764ba2);
                        color:white;padding:0.6rem;border-radius:8px;
                        text-decoration:none;font-weight:600;font-size:0.85rem;">
                        Apply Now →
                    </a>
                    """, unsafe_allow_html=True)
                else:
                    import urllib.parse as _up
                    q  = _up.quote(f"{title} {company} jobs")
                    fb = f"https://www.google.com/search?q={q}"
                    st.markdown(f"""
                    <a href="{fb}" target="_blank"
                        style="display:block;text-align:center;
                        background:rgba(102,126,234,0.2);color:#667eea;
                        padding:0.6rem;border-radius:8px;text-decoration:none;
                        font-weight:600;font-size:0.85rem;border:1px solid #667eea44;">
                        Search Online →
                    </a>
                    """, unsafe_allow_html=True)

