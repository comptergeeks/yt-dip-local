# yt-dip-local

A minimal Flask web app to download YouTube videos using yt-dlp. Paste a YouTube URL in the form and download the video directly.

## Features
- Simple web interface
- - Uses latest yt-dlp
  - - Download videos as MP4
   
    - ## Setup
    - 1. Clone the repository:
      2.    ```bash
               git clone https://github.com/comptergeeks/yt-dip-local.git
               cd yt-dip-local
               ```
            2. Install dependencies:
            3.    ```bash
                     pip install -r requirements.txt
                     ```
                  3. Run the app:
                  4.    ```bash
                           python app.py
                           ```
                        4. Open your browser and go to `http://localhost:5000`
                    
                        5. ## Usage
                        6. - Paste a YouTube URL in the form and click Download.
                           - - The video will be processed and downloaded as an MP4 file.
                            
                             - ## Requirements
                             - - Python 3.8+
                               - - pip
                                
                                 - ## Notes
                                 - - For local use only. Do not expose to the public internet without proper security.
                                   - - Uses Flask, Flask-Cors, and yt-dlp (see requirements.txt).
                                    
                                     - ---
                                     MIT License
                                     
