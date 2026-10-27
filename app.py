import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOCAL_VIDEO_PATH = BASE_DIR / "assets" / "diamond-palace-background.mp4"
if not LOCAL_VIDEO_PATH.exists():
    LOCAL_VIDEO_PATH = BASE_DIR / "diamond-palace-background.mp4"

VIDEO_URL = "https://raw.githubusercontent.com/ChavanKoteppa/diamond-palace-website/main/diamond-palace-background.mp4"
MAPS_URL = "https://maps.app.goo.gl/BhoKTmAhCCnToEUp8"

st.set_page_config(
    page_title="Diamond Palace Convention Hall",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');

    :root {
        --bg: #120f0d;
        --bg-soft: #1a1512;
        --panel: rgba(255,255,255,0.03);
        --panel-strong: rgba(255,255,255,0.06);
        --line: rgba(216,179,106,0.28);
        --gold: #d8b36a;
        --gold-soft: #f0d7a6;
        --cream: #fff8eb;
        --muted: #d9c8b1;
        --text: #f5efe6;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: var(--bg);
        color: var(--cream);
        font-family: 'Montserrat', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }
    #MainMenu, footer { visibility: hidden; }

    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin: 0;
        max-width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }

    .topbar {
        position: sticky;
        top: 0;
        z-index: 50;
        background: rgba(18, 15, 13, 0.80);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding: 1rem 2rem;
    }

    .topbar-inner {
        max-width: 1280px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }

    .brand {
        font-family: 'Cormorant Garamond', serif;
        letter-spacing: 0.08em;
        font-size: 2.1rem;
        color: var(--gold-soft);
        font-weight: 600;
    }

    .nav {
        display: flex;
        gap: 1.35rem;
        flex-wrap: wrap;
        justify-content: center;
        color: var(--text);
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
    }

    .nav a {
        color: var(--text);
        text-decoration: none;
        opacity: 0.86;
    }

    .nav a:hover { color: var(--gold); }

    .nav-button {
        border: 1px solid var(--gold);
        background: rgba(216,179,106,0.05);
        color: var(--gold-soft);
        padding: 0.8rem 1.2rem;
        text-transform: uppercase;
        font-size: 0.72rem;
        letter-spacing: 0.15em;
        border-radius: 999px;
        text-decoration: none;
        white-space: nowrap;
    }

    .hero {
        position: relative;
        min-height: 82vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 5rem 1rem 3rem;
        overflow: hidden;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        background: linear-gradient(180deg, rgba(18,15,13,0.22), rgba(18,15,13,0.7));
        isolation: isolate;
    }

    .hero-video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 0;
        filter: brightness(0.72) saturate(0.8);
        pointer-events: none;
    }

    .hero::after {
        content: '';
        position: absolute;
        inset: 18px;
        border: 1px solid rgba(216,179,106,0.5);
        pointer-events: none;
        z-index: 2;
    }

    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 1100px;
        text-align: center;
        padding: 1rem 0 2rem;
    }

    .eyebrow {
        margin-bottom: 1rem;
        font-size: 0.78rem;
        letter-spacing: 0.32em;
        text-transform: uppercase;
        color: var(--gold-soft);
        font-weight: 600;
    }

    .hero h1 {
        margin: 0;
        color: #fffaf2;
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(3.2rem, 7vw, 7rem);
        line-height: 0.92;
        letter-spacing: 0.02em;
        text-shadow: 0 12px 24px rgba(0,0,0,0.32);
    }

    .subtitle {
        margin-top: 1rem;
        font-size: 0.9rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: #f5ead2;
    }

    .cta-row {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 2rem;
    }

    .button-primary, .button-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 180px;
        padding: 0.95rem 1.45rem;
        border-radius: 999px;
        font-size: 0.72rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        text-decoration: none;
        font-weight: 700;
    }

    .button-primary {
        background: linear-gradient(135deg, #d8b36a 0%, #f0d7a6 100%);
        color: #18110d;
        border: 1px solid rgba(255,255,255,0.18);
    }

    .button-secondary {
        border: 1px solid rgba(255,255,255,0.5);
        background: rgba(255,255,255,0.04);
        color: #fff;
    }

    .section {
        padding: 5rem 1rem;
    }

    .container {
        max-width: 1280px;
        margin: 0 auto;
    }

    .section-heading {
        text-align: center;
        margin-bottom: 2.5rem;
    }

    .section-heading .label {
        color: var(--gold);
        font-size: 0.75rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
        font-weight: 700;
    }

    .section-heading h2 {
        margin: 0;
        color: var(--cream);
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.4rem, 4vw, 4rem);
        font-weight: 400;
    }

    .story-grid {
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 2rem;
        align-items: center;
    }

    .story-card, .feature-box, .info-card, .gallery-tile, .cta-box, .tour-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--line);
        box-shadow: 0 14px 28px rgba(0,0,0,0.16);
    }

    .story-card {
        padding: 2rem;
    }

    .story-card p {
        margin: 0;
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.9;
    }

    .story-visual {
        min-height: 360px;
        background: linear-gradient(135deg, rgba(26,20,15,0.45), rgba(26,20,15,0.22)),
                    url('https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
        border: 1px solid var(--line);
        position: relative;
        overflow: hidden;
    }

    .story-visual::after {
        content: 'Diamond Palace';
        position: absolute;
        left: 1.4rem;
        bottom: 1.2rem;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        letter-spacing: 0.06em;
        color: rgba(255,248,235,0.92);
    }

    .stats {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }

    .info-card {
        padding: 1.5rem 1rem;
        text-align: center;
    }

    .info-card .number {
        color: var(--gold);
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.3rem;
        line-height: 1;
        margin-bottom: 0.45rem;
    }

    .info-card .text {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--cream);
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1.2rem;
    }

    .feature-box {
        padding: 2rem 1.5rem;
        min-height: 220px;
    }

    .feature-box .num {
        color: var(--gold);
        font-size: 0.76rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .feature-box h3 {
        font-family: 'Cormorant Garamond', serif;
        color: #fff9f1;
        font-size: 2rem;
        margin: 0 0 0.8rem;
    }

    .feature-box p {
        font-size: 0.92rem;
        line-height: 1.8;
        color: var(--muted);
        margin: 0;
    }

    .tour-wrap {
        background: rgba(255,255,255,0.015);
        border-top: 1px solid rgba(255,255,255,0.06);
        border-bottom: 1px solid rgba(255,255,255,0.06);
    }

    .tour-grid {
        display: grid;
        grid-template-columns: 1.3fr 0.9fr;
        gap: 1.2rem;
    }

    .tour-image {
        min-height: 420px;
        background-size: cover;
        background-position: center;
        border: 1px solid var(--line);
    }

    .tour-card {
        padding: 2rem;
    }

    .tour-card h3 {
        margin: 0 0 1rem;
        color: #fff9f3;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.3rem;
    }

    .tour-card p {
        color: var(--muted);
        font-size: 0.98rem;
        line-height: 1.9;
        margin: 0;
    }

    .amenities-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 1rem;
    }

    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
    }

    .gallery-tile {
        min-height: 260px;
        position: relative;
        overflow: hidden;
        background-size: cover;
        background-position: center;
        border: 1px solid var(--line);
    }

    .gallery-tile::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(18,15,13,0.12), rgba(18,15,13,0.72));
    }

    .gallery-tile span {
        position: absolute;
        left: 1.2rem;
        bottom: 1.2rem;
        font-size: 0.8rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--cream);
        z-index: 1;
    }

    .cta-box {
        padding: 2.2rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
        background: linear-gradient(135deg, rgba(216,179,106,0.12), rgba(255,255,255,0.02));
    }

    .cta-box h3 {
        margin: 0;
        color: #fff9f3;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.2rem;
    }

    .cta-box p {
        margin: 0.7rem 0 0;
        color: var(--muted);
    }

    .footer-note {
        text-align: center;
        color: #bcae9b;
        font-size: 0.8rem;
        padding: 1rem 1rem 2rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        line-height: 1.8;
    }

    @media (max-width: 980px) {
        .story-grid, .features-grid, .gallery-grid, .amenities-grid, .tour-grid { grid-template-columns: 1fr 1fr; }
        .story-grid, .tour-grid { grid-template-columns: 1fr; }
        .topbar-inner { flex-direction: column; text-align: center; }
    }

    @media (max-width: 640px) {
        .nav { gap: 0.7rem; }
        .hero { min-height: 72vh; }
        .section { padding: 4rem 0.7rem; }
        .features-grid, .gallery-grid, .amenities-grid, .stats { grid-template-columns: 1fr; }
        .cta-box { padding: 1.5rem; }
        .cta-box h3 { font-size: 1.8rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
      <div class="topbar-inner">
        <div class="brand">Diamond Palace</div>
        <div class="nav">
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#spaces">Spaces</a>
          <a href="#events">Events</a>
          <a href="#gallery">Gallery</a>
          <a href="#contact">Contact</a>
        </div>
        <a class="nav-button" href="https://maps.app.goo.gl/BhoKTmAhCCnToEUp8" target="_blank" rel="noopener noreferrer">Get Directions</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_video = f"""
<video class="hero-video" autoplay muted loop playsinline preload="auto" poster="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1600&q=80">
  <source src="{VIDEO_URL}" type="video/mp4" />
</video>
"""

st.markdown(
    f"""
    <div class="hero" id="home">
      {hero_video}
      <div class="hero-content">
        <div class="eyebrow">A place for your special moments</div>
        <h1>Diamond Palace</h1>
        <div class="subtitle">Convention Hall • Ranebennur</div>
        <div class="cta-row">
          <a class="button-primary" href="{MAPS_URL}" target="_blank" rel="noopener noreferrer">Plan Your Event</a>
          <a class="button-secondary" href="#contact">Contact Us</a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section" id="about">
      <div class="container">
        <div class="section-heading">
          <div class="label">Welcome</div>
          <h2>Where celebrations feel truly grand.</h2>
        </div>
        <div class="story-grid">
          <div class="story-card">
            <p>
              Diamond Palace Convention Hall is designed for joyful family moments and unforgettable events.
              From weddings and receptions to birthdays, engagements, corporate gatherings, and community celebrations,
              every occasion is shaped with elegance, warmth, and thoughtful planning.
            </p>
            <div class="stats">
              <div class="info-card">
                <div class="number">500+</div>
                <div class="text">Guests</div>
              </div>
              <div class="info-card">
                <div class="number">3</div>
                <div class="text">Event Styles</div>
              </div>
              <div class="info-card">
                <div class="number">24/7</div>
                <div class="text">Support</div>
              </div>
            </div>
          </div>
          <div class="story-visual"></div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
      <div class="container">
        <div class="section-heading">
          <div class="label">Your occasion, our attention</div>
          <h2>Everything you need under one roof.</h2>
        </div>
        <div class="features-grid">
          <div class="feature-box">
            <div class="num">01</div>
            <h3>Weddings</h3>
            <p>Elegant settings for sacred rituals, ceremonies, and joyful reception evenings that your family will remember forever.</p>
          </div>
          <div class="feature-box">
            <div class="num">02</div>
            <h3>Corporate Events</h3>
            <p>Professional, polished spaces for conferences, launches, seminars, and product showcases that feel premium from start to finish.</p>
          </div>
          <div class="feature-box">
            <div class="num">03</div>
            <h3>Family Gatherings</h3>
            <p>Comfortable and welcoming arrangements for birthdays, engagements, anniversaries, and intimate celebrations.</p>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section tour-wrap" id="spaces">
      <div class="container">
        <div class="section-heading">
          <div class="label">Explore the venue</div>
          <h2>Take a virtual tour through our spaces.</h2>
        </div>
        <div class="tour-grid">
          <div class="tour-image" style="background-image: url('https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=1200&q=80');"></div>
          <div class="tour-card">
            <h3>Designed for grand experiences</h3>
            <p>
              From the dining hall to the stage and seating arrangements, every space is curated to offer comfort,
              elegance, and seamless guest flow. The venue combines beauty with practicality for memorable celebrations.
            </p>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
      <div class="container">
        <div class="section-heading">
          <div class="label">Venue highlights</div>
          <h2>Designed for ease, comfort, and beauty.</h2>
        </div>
        <div class="amenities-grid">
          <div class="feature-box">
            <div class="num">A</div>
            <h3>Spacious Hall</h3>
            <p>Comfortably accommodates large guest lists while preserving an elegant, uncluttered ambience.</p>
          </div>
          <div class="feature-box">
            <div class="num">B</div>
            <h3>Lighting & Decor</h3>
            <p>Warm and premium styling that creates a memorable atmosphere for every celebration and ceremony.</p>
          </div>
          <div class="feature-box">
            <div class="num">C</div>
            <h3>Parking</h3>
            <p>Convenient access for guests, making arrivals and departures smooth and stress-free.</p>
          </div>
          <div class="feature-box">
            <div class="num">D</div>
            <h3>Guest Experience</h3>
            <p>Friendly service and functional planning ensure every guest feels welcome from beginning to end.</p>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section" id="gallery">
      <div class="container">
        <div class="section-heading">
          <div class="label">Gallery</div>
          <h2>Moments that feel extraordinary.</h2>
        </div>
        <div class="gallery-grid">
          <div class="gallery-tile" style="background-image: url('https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=900&q=80');"><span>Wedding</span></div>
          <div class="gallery-tile" style="background-image: url('https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=900&q=80');"><span>Reception</span></div>
          <div class="gallery-tile" style="background-image: url('https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=900&q=80');"><span>Gathering</span></div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section" id="events">
      <div class="container">
        <div class="cta-box">
          <div>
            <h3>Book your celebration with us.</h3>
            <p>Let’s plan a memorable occasion in a venue built for joy, comfort, and elegance.</p>
          </div>
          <div class="cta-row" style="margin-top:0; justify-content:flex-end;">
            <a class="button-primary" href="https://maps.app.goo.gl/BhoKTmAhCCnToEUp8" target="_blank" rel="noopener noreferrer">Get Directions</a>
            <a class="button-secondary" href="tel:+919999999999">Call Now</a>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="footer-note" id="contact">Diamond Palace Convention Hall • Hunasikatti Road, Ranebennur<br>Developed and Managed by Chavan Koteppa</div>',
    unsafe_allow_html=True,
)
