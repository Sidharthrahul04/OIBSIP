# Voice Assistant

A Python-based desktop voice assistant that accepts spoken commands, converts speech to text, identifies the user's intent, and performs different tasks such as checking weather, searching the web, setting reminders, sending emails, answering general knowledge questions, and executing user-defined custom commands.

The project was developed as a Python programming internship project and follows a modular service-based structure instead of keeping all functionality inside a single Python file.

---

## Features

- Voice-based command input
- Text-to-speech responses
- Greeting support
- Current time and date
- Weather information using a weather API
- Web search using Google
- Reminders
- Email sending through Gmail SMTP
- General knowledge Q&A using Wikipedia
- Custom commands using a JSON configuration file
- Speech recognition error handling
- Microphone error handling
- API/network error handling
- Logging of important application events
- Environment-based configuration using `.env`
- Privacy-conscious handling of credentials
- Modular service-based architecture

---

## Tech Stack

### Programming Language

- Python 3

### Libraries and Packages

- SpeechRecognition
- PyAudio
- pyttsx3
- requests
- python-dotenv
- pypiwin32
- pywin32
- comtypes

### External Services

- Google Speech Recognition
- Weather API
- Wikipedia API
- Gmail SMTP

### Development Tools

- Visual Studio Code
- PowerShell
- Git
- GitHub
- Python Virtual Environment (`venv`)

---

## Project Architecture

The application follows a modular architecture where different responsibilities are separated into individual modules and services.

```text
                         User
                           |
                           v
                    Microphone Input
                           |
                           v
                  +------------------+
                  |  voice_service   |
                  | Speech-to-Text   |
                  +------------------+
                           |
                           v
                     Recognized Text
                           |
                           v
                  +------------------+
                  |    intents.py    |
                  | Intent Detection |
                  +------------------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       Weather          Reminder           Email
          |                |                |
          v                v                v
    weather.py       reminders.py     email_service.py

          +----------------+----------------+
          |                |                |
          v                v                v
     Web Search         Q&A             Custom Commands
          |                |                |
          v                v                v
       Google         Wikipedia       JSON Configuration

                           |
                           v
                  +------------------+
                  |  Text-to-Speech  |
                  |   pyttsx3        |
                  +------------------+
                           |
                           v
                         User
