# BrainRotAI 🎬

A Flask-based web application that automatically generates Instagram Reels from images and text using AI-powered text-to-speech technology.

## Features ✨

- **Image Upload**: Upload multiple images to create slideshow-style reels
- **AI Text-to-Speech**: Convert text descriptions into natural-sounding audio using ElevenLabs API
- **Automatic Video Generation**: Combine images and audio into Instagram-ready vertical videos (1080x1920)
- **Gallery View**: Browse and view all generated reels
- **Responsive Design**: Modern, mobile-friendly interface
- **Real-time Processing**: Background processing queue for video generation

## Demo 🎥 https://youtu.be/oRPhnVpP8aQ

Upload your images, add a text description, and let BrainRotAI create engaging Instagram Reels automatically!

## Tech Stack 🛠️

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Text-to-Speech**: ElevenLabs API
- **Video Processing**: FFmpeg
- **File Handling**: Werkzeug

## Installation 📦

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BrainrotAI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   - **macOS**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html)

4. **Set up ElevenLabs API**
   - Get your API key from [ElevenLabs](https://elevenlabs.io/)
   - Update [`config.py`](config.py) with your API key:
     ```python
     ELEVENLABS_API_KEY = "your-api-key-here"
     ```

## Usage 🚀

1. **Start the Flask application**
   ```bash
   python main.py
   ```

2. **Start the background processor** (in a separate terminal)
   ```bash
   python generation.py
   ```

3. **Open your browser** and navigate to `http://localhost:5000`

4. **Create a reel**:
   - Go to "Create Reel" page
   - Upload multiple images (PNG, JPG, JPEG)
   - Add a text description for the voiceover
   - Submit and wait for processing

5. **View your reels** in the Gallery section

## Project Structure 📁

```
BrainrotAI/
├── main.py                 # Flask web application
├── generation.py           # Background video processing
├── text_to_audio.py       # Text-to-speech conversion
├── config.py              # API configuration
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   └── gallery.html
├── static/               # Static assets
│   ├── css/
│   ├── reels/           # Generated videos
│   └── songs/           # Audio files
└── user_uploads/        # Uploaded files and processing
```

## How It Works 🔄

1. **Upload**: Users upload images and text through the web interface
2. **Processing Queue**: [`generation.py`](generation.py) monitors for new uploads
3. **Audio Generation**: Text is converted to speech using [`text_to_audio.py`](text_to_audio.py)
4. **Video Creation**: FFmpeg combines images and audio into a vertical video
5. **Gallery**: Completed reels are displayed in the gallery

## API Configuration 🔧

The project uses ElevenLabs for text-to-speech with the following settings:
- **Voice**: Adam (pNInz6obpgDQGcFmaJgB)
- **Model**: eleven_turbo_v2_5 (for low latency)
- **Output**: MP3 22050Hz 32kbps

## Video Specifications 📹

Generated reels have the following specifications:
- **Resolution**: 1080x1920 (Instagram Reel format)
- **Frame Rate**: 30 FPS
- **Codec**: H.264 (libx264)
- **Audio**: AAC
- **Duration**: Based on image count (1 second per image) and audio length

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📬

- **Instagram**: [@mohammad_humzah](https://instagram.com/mohammad_humzah)
- **LinkedIn**: [mohammadhumzah](https://www.linkedin.com/in/mohammadhumzah)
- **YouTube**: [@mohammadhumzah6236](https://www.youtube.com/@mohammadhumzah6236)

## Acknowledgments 🙏

- [ElevenLabs](https://elevenlabs.io/) for the amazing text-to-speech API
- [FFmpeg](https://ffmpeg.org/) for video processing capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework

---

**Note**: Remember to keep your ElevenLabs API key secure and never commit it to version control!