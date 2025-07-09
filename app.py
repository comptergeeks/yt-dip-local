from flask import Flask, request, send_file, render_template
from flask_cors import CORS
import yt_dlp
import os
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
      url = request.form.get('url')
      if not url:
                return 'No URL provided', 400
            outtmpl = f"/tmp/{uuid.uuid4()}.%(ext)s"
    ydl_opts = {
              'outtmpl': outtmpl,
              'format': 'bestvideo+bestaudio/best',
              'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
              info = ydl.extract_info(url, download=True)
              filename = ydl.prepare_filename(info)
              if not filename.endswith('.mp4'):
                            filename = os.path.splitext(filename)[0] + '.mp4'
                    response = send_file(filename, as_attachment=True)
    os.remove(filename)
    return response

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)
