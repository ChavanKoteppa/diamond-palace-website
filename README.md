# Diamond Palace Convention Hall — Streamlit website

## Run locally (Windows)
1. Install Python if needed.
2. Open Command Prompt or the VS Code terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the site:
   ```bash
   streamlit run app.py
   ```
5. Streamlit will open the website in your browser.

## Included
- `app.py` — Streamlit website
- `assets/diamond-palace-background.mp4` — uploaded video used as looping muted homepage background
- Google Maps directions button
- `XXXX` placeholder for phone/WhatsApp details

## Before publishing
Replace `XXXX` with the real contact number and test the page on mobile. The uploaded video is embedded as a base64 data URL to support the background video in the custom HTML; this makes the HTML payload large. For production hosting, consider serving the video as a normal static asset or hosting it on a video CDN.
