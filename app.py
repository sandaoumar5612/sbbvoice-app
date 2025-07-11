from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
from datetime import datetime

# ✅ CORRECT : name utilisé
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']
        tts = gTTS(text=text, lang=lang)
        filename = f"static/audio/voice_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
        tts.save(filename)
        audio_file = filename
    return render_template('index.html', audio_file=audio_file)

@app.route('/download/<filename>')
def download(filename):
    return send_file(f'static/audio/{filename}', as_attachment=True)

# ⚠️ PAS DE app.run() ICI — Render utilise gunicorn pour lancer l'app