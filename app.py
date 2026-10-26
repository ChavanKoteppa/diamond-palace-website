import base64
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent
VIDEO_PATH = BASE_DIR / "assets" / "diamond-palace-background.mp4"
if not VIDEO_PATH.exists():
    VIDEO_PATH = BASE_DIR / "diamond-palace-background.mp4"
MAPS_URL = "https://maps.app.goo.gl/BhoKTmAhCCnToEUp8"

st.set_page_config(page_title="Diamond Palace Convention Hall", page_icon="💎", layout="wide", initial_sidebar_state="collapsed")

# Premium dark-and-gold style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@400;500;600&display=swap');
:root { --gold:#d8b36a; --cream:#fff8eb; --dark:#17120f; }
html, body, [data-testid="stAppViewContainer"] { background:var(--dark); color:var(--cream); }
[data-testid="stHeader"] { background:transparent; }
.block-container { padding-top:0.5rem; padding-bottom:0; max-width:100%; }
#MainMenu, footer {visibility:hidden;}
.hero { min-height:78vh; position:relative; display:flex; align-items:center; justify-content:center; text-align:center; overflow:hidden; padding:5rem 1rem; margin:0 -1rem; isolation:isolate; }
.hero video { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; z-index:-3; }
.hero::before { content:''; position:absolute; inset:0; z-index:-2; background:linear-gradient(180deg,rgba(10,8,6,.58),rgba(10,8,6,.34) 42%,rgba(10,8,6,.82)); }
.hero::after { content:''; position:absolute; inset:16px; border:1px solid rgba(216,179,106,.55); z-index:-1; pointer-events:none; }
.eyebrow { font:600 .78rem Montserrat,sans-serif; color:var(--gold); text-transform:uppercase; letter-spacing:.25em; }
.hero h1 { font:400 clamp(3rem,8vw,6.6rem) 'Cormorant Garamond',serif; line-height:1; margin:.6rem 0; color:#fff8eb; }
.subtitle { font:500 .9rem Montserrat,sans-serif; letter-spacing:.17em; color:#f5e8d2; }
.section { padding:4.5rem 1rem; text-align:center; }
.section-label { color:var(--gold); font:600 .75rem Montserrat,sans-serif; text-transform:uppercase; letter-spacing:.22em; }
.section h2 { font:400 clamp(2.2rem,5vw,3.6rem) 'Cormorant Garamond',serif; color:var(--cream); margin:.5rem 0 1rem; }
.section p { color:#e3d6c5; font:400 .98rem/1.9 Montserrat,sans-serif; max-width:780px; margin:0 auto; }
.feature { border:1px solid rgba(216,179,106,.35); padding:1.6rem 1rem; min-height:160px; }
.feature .num { color:var(--gold); font: .8rem Montserrat,sans-serif; }
.feature h3 { font:400 1.65rem 'Cormorant Garamond',serif; color:var(--cream); }
.feature p { font-size:.85rem; line-height:1.7; }
.stButton>button, .stLinkButton>a { border:1px solid var(--gold)!important; border-radius:0!important; background:var(--gold)!important; color:#1b130b!important; font:600 .78rem Montserrat,sans-serif!important; letter-spacing:.12em; text-transform:uppercase; }
.stLinkButton>a { display:inline-flex; align-items:center; text-decoration:none!important; }
.contact { background:#211914; }
.small-note { font: .75rem Montserrat,sans-serif; color:#bcae9b; }
@media(max-width:640px) { .hero {min-height:72vh;} .hero::after {inset:9px;} .section {padding:3.5rem .5rem;} }
</style>
""", unsafe_allow_html=True)

# Encode video as a data URL so the video background works without a separate web server.
video_src = ""
if VIDEO_PATH.exists():
    encoded = base64.b64encode(VIDEO_PATH.read_bytes()).decode("ascii")
    video_src = f"data:video/mp4;base64,{encoded}"

st.markdown(f"""
<div class="hero">
  {f'<video autoplay muted loop playsinline preload="metadata"><source src="{video_src}" type="video/mp4"></video>' if video_src else ''}
  <div>
    <div class="eyebrow">A place for your special moments</div>
    <h1>Diamond Palace</h1>
    <div class="subtitle">CONVENTION HALL · RANEBENNUR</div>
  </div>
</div>
""", unsafe_allow_html=True)

# CTA row
left, middle, right = st.columns([1, 1, 1])
with middle:
    st.link_button("Get Directions", MAPS_URL, use_container_width=True)

st.markdown("""
<div class="section">
  <div class="section-label">Your celebration starts here</div>
  <h2>Make moments memorable.</h2>
  <p>Welcome to Diamond Palace Convention Hall on Hunasikatti Road, Ranebennur — a place to bring family and friends together for life's important celebrations. Contact us to discuss your event requirements and make your occasion special.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-label" style="text-align:center">At a glance</div><h2 style="text-align:center;font:400 clamp(2.2rem,5vw,3.6rem) \'Cormorant Garamond\',serif;margin:.5rem 0 1.5rem">Highlights</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
for col, num, title, description in [
    (c1, "01", "Weddings", "A welcoming setting for your wedding celebration and family gathering."),
    (c2, "02", "Special occasions", "Bring everyone together for meaningful milestones and celebrations."),
    (c3, "03", "Enquiries", "Ask about availability, venue details and booking arrangements.")
]:
    with col:
        st.markdown(f'<div class="feature"><div class="num">{num}</div><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section contact"><div class="section-label">We’d love to hear from you</div><h2>Plan your occasion.</h2><p><strong>Diamond Palace Convention Hall</strong><br>Hunasikatti Road, Ranebennur<br>Contact us to book your event.</p></div>', unsafe_allow_html=True)
a, b, c = st.columns([1, 1, 1])
with b:
    st.link_button("Open Google Maps", MAPS_URL, use_container_width=True)
st.markdown('<p class="small-note" style="text-align:center;margin:2rem 0 1rem">Phone and WhatsApp contact details are placeholders and can be updated later.</p><hr style="border-color:#59452b"><p style="text-align:center;color:#d5c0a0;font:400 .9rem Montserrat,sans-serif;">Diamond Palace Convention Hall — Ranebennur</p>', unsafe_allow_html=True)
