import base64
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent
VIDEO_PATH = BASE_DIR / "assets" / "diamond-palace-background.mp4"
if not VIDEO_PATH.exists():
    VIDEO_PATH = BASE_DIR / "diamond-palace-background.mp4"
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
        --gold: #d8b36a;
        --gold-soft: #f0d7a6;
        --cream: #fff8eb;
        --dark: #120f0d;
        --muted: #d9c8b1;
        --line: rgba(216,179,106,0.35);
        --panel: rgba(255,255,255,0.02);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: var(--dark);
        color: var(--cream);
        font-family: 'Montserrat', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0;
        max-width: 100%;
        padding-left: 0;
        padding-right: 0;
    }
    #MainMenu, footer { visibility: hidden; }

    .topbar {
        position: sticky;
        top: 0;
        z-index: 20;
        background: rgba(18, 15, 13, 0.72);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255,255,255,0.06);
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
        font-size: 2rem;
        color: var(--gold-soft);
        font-weight: 600;
    }

    .nav {
        display: flex;
        gap: 1.4rem;
        flex-wrap: wrap;
        justify-content: center;
        color: #f4e9d4;
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
    }

    .nav a {
        color: #f4e9d4;
        text-decoration: none;
        opacity: 0.88;
        transition: 0.2s ease;
    }

    .nav a:hover { color: var(--gold); }

    .nav-button {
        border: 1px solid var(--gold);
        background: transparent;
        color: var(--gold);
        padding: 0.8rem 1.2rem;
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 0.15em;
        border-radius: 999px;
        text-decoration: none;
        transition: all 0.2s ease;
    }

    .nav-button:hover {
        background: var(--gold);
        color: #1b130b;
    }

    .hero {
        position: relative;
        min-height: 82vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        overflow: hidden;
        padding: 5rem 1rem 2rem;
        margin: 0;
        isolation: isolate;
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .hero video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -4;
        filter: saturate(0.8) contrast(1.1);
    }

    .hero::before {
        content: '';
        position: absolute;
        inset: 0;
        z-index: -3;
        background: linear-gradient(180deg, rgba(14,10,8,0.45), rgba(14,10,8,0.35) 40%, rgba(14,10,8,0.76));
    }

    .hero::after {
        content: '';
        position: absolute;
        inset: 18px;
        border: 1px solid rgba(216,179,106,0.55);
        z-index: -2;
        pointer-events: none;
    }

    .hero-content {
        max-width: 1100px;
        position: relative;
        z-index: 1;
        padding: 1rem 0 2rem;
    }

    .eyebrow {
        font: 600 0.78rem 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.30em;
        color: var(--gold-soft);
        margin-bottom: 1rem;
    }

    .hero h1 {
        font: 700 clamp(3.2rem, 7vw, 7rem) 'Cormorant Garamond', serif;
        line-height: 0.92;
        margin: 0 0 0.7rem;
        color: #fffaf2;
        text-shadow: 0 12px 24px rgba(0,0,0,0.35);
    }

    .subtitle {
        font: 500 0.9rem 'Montserrat', sans-serif;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: #f5ead2;
        margin-bottom: 2rem;
    }

    .cta-row {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 1rem;
    }

    .button-primary, .button-secondary {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        min-width: 180px;
        padding: 0.95rem 1.4rem;
        border-radius: 999px;
        font-size: 0.72rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        text-decoration: none;
        transition: all 0.2s ease;
        font-weight: 700;
    }

    .button-primary {
        background: linear-gradient(135deg, #d8b36a 0%, #f0d7a6 100%);
        color: #18110d;
        border: 1px solid rgba(255,255,255,0.18);
    }

    .button-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 25px rgba(216,179,106,0.2);
    }

    .button-secondary {
        border: 1px solid rgba(255,255,255,0.4);
        color: #fff;
        background: rgba(255,255,255,0.03);
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
        font: 600 0.75rem 'Montserrat', sans-serif;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .section-heading h2 {
        font: 400 clamp(2.4rem, 4vw, 4rem) 'Cormorant Garamond', serif;
        margin: 0;
        color: var(--cream);
    }

    .story-grid {
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 2rem;
        align-items: center;
    }

    .story-card, .info-card, .feature-box, .gallery-tile, .cta-box, .tour-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--line);
        box-shadow: 0 14px 28px rgba(0,0,0,0.15);
    }

    .story-card {
        padding: 2rem;
    }

    .story-card p {
        font-size: 1rem;
        line-height: 1.9;
        color: var(--muted);
        margin: 0;
    }

    .story-visual {
        min-height: 360px;
        background:
            linear-gradient(135deg, rgba(26,20,15,0.45), rgba(26,20,15,0.2)),
            url('https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
        border: 1px solid var(--line);
        position: relative;
        overflow: hidden;
    }

    .story-visual::after {
        content: 'Diamond Palace';
        position: absolute;
        left: 1.5rem;
        bottom: 1.5rem;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        letter-spacing: 0.06em;
        color: rgba(255,248,235,0.9);
    }

    .stats {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }

    .info-card {
        padding: 1.6rem 1.1rem;
        text-align: center;
    }

    .info-card .number {
        color: var(--gold);
        font-size: 2rem;
        font-family: 'Cormorant Garamond', serif;
        line-height: 1;
        margin-bottom: 0.4rem;
    }

    .info-card .text {
        font-size: 0.72rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--cream);
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1.2rem;
    }

    .feature-box {
        padding: 2rem 1.5rem;
        min-height: 240px;
    }

    .feature-box .num {
        color: var(--gold);
        font-size: 0.76rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 1rem;
        font-weight: 700;
    }

    .feature-box h3 {
        font: 400 2rem 'Cormorant Garamond', serif;
        margin: 0 0 0.8rem;
        color: #fff9f1;
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
        align-items: stretch;
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
        font: 400 2.3rem 'Cormorant Garamond', serif;
        margin: 0 0 1rem;
        color: #fff9f3;
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
    }

    .gallery-tile::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(18,15,13,0.1), rgba(18,15,13,0.7));
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
        font: 400 2.2rem 'Cormorant Garamond', serif;
        margin: 0;
        color: #fff9f3;
    }

    .cta-box p {
        color: var(--muted);
        margin: 0.6rem 0 0;
    }

    .footer-note {
        text-align: center;
        color: #bcae9b;
        font-size: 0.8rem;
        padding: 1rem 1rem 2rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    @media (max-width: 980px) {
        .story-grid, .features-grid, .gallery-grid, .amenities-grid, .tour-grid {
            grid-template-columns: 1fr 1fr;
        }

        .story-grid, .tour-grid {
            grid-template-columns: 1fr;
        }

        .topbar-inner {
            flex-direction: column;
            text-align: center;
        }
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
        <a class="nav-button" href="https://maps.app.goo.gl/BhoKTmAhCCnToEUp8" target="_blank">Get Directions</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

video_src = ""
if VIDEO_PATH.exists():
    encoded = base64.b64encode(VIDEO_PATH.read_bytes()).decode("ascii")
    video_src = f"data:video/mp4;base64,{encoded}"

st.markdown(
    f"""
    <div class="hero" id="home">
      {f'<video autoplay muted loop playsinline preload="metadata"><source src="{video_src}" type="video/mp4"></video>' if video_src else ''}
      <div class="hero-content">
        <div class="eyebrow">A place for your special moments</div>
        <h1>Diamond Palace</h1>
        <div class="subtitle">Convention Hall • Ranebennur</div>
        <div class="cta-row">
          <a class="button-primary" href="https://maps.app.goo.gl/BhoKTmAhCCnToEUp8" target="_blank">Plan Your Event</a>
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
            <p>Diamond Palace Convention Hall is designed for joyful family moments and unforgettable events. From weddings and receptions to birthdays, engagements, and community gatherings, our venue brings a graceful atmosphere with thoughtful hospitality and spacious comfort.</p>
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
            <p>Professional, polished spaces for conferences, launches, seminars, and product showcases with a premium presentation.</p>
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
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

space_data = [
    (
        "Dining Hall",
        "Our dining hall is designed for comfort, elegance, and smooth guest flow. With warm lighting, refined decor, and a smart layout, it creates an inviting atmosphere for celebrations, receptions, and family gatherings.",
        "https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&w=1200&q=80",
    ),
    (
        "Stage",
        "Designed to stand out, our stage offers the perfect focal point for cultural performances, wedding rituals, speeches, and live events. It blends elegance with practical setup for lighting, stage decor, and audience visibility.",
        "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1200&q=80",
    ),
    (
        "Seating Area",
        "Guest comfort is central to our layout. The seating area is arranged to maintain clear views of the stage, easy movement between sections, and a balanced, welcoming experience for every visitor.",
        "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=1200&q=80",
    ),
    (
        "Exterior View",
        "The outside look of the venue reflects the premium experience waiting inside. With a dignified facade and welcoming presence, the building creates a memorable first impression for your guests.",
        "https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=1200&q=80",
    ),
    (
        "Rooms",
        "Our rooms offer flexible support spaces for preparation, rest, and event planning. Ideal for family gatherings, ceremonies, or behind-the-scenes coordination, they provide privacy and convenience.",
        "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80",
    ),
]

space_tabs = st.tabs([item[0] for item in space_data])
for tab, (title, description, image_url) in zip(space_tabs, space_data):
    with tab:
        st.image(image_url, use_container_width=True)
        st.markdown(f"### {title}")
        st.write(description)

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
            <a class="button-primary" href="https://maps.app.goo.gl/BhoKTmAhCCnToEUp8" target="_blank">Get Directions</a>
            <a class="button-secondary" href="tel:+919999999999">Call Now</a>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="footer-note" id="contact">Diamond Palace Convention Hall • Hunasikatti Road, Ranebennur</div>',
    unsafe_allow_html=True,
)
