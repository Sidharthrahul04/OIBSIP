# Voice Assistant

A Python-based desktop voice assistant that accepts spoken commands, converts speech to text, identifies the user's intent, and performs different tasks such as checking the weather, searching the web, setting reminders, sending emails, answering general knowledge questions, and executing user-defined custom commands.

The project was developed as part of a Python programming internship and follows a modular, service-based architecture instead of keeping all functionality inside a single Python file.

---

## Features

* Voice-based command input
* Speech-to-text conversion
* Text-to-speech responses
* Greeting support
* Current time and date
* Weather information using a weather API
* Web search using Google
* Voice-based reminders
* Email sending through Gmail SMTP
* General knowledge Q&A using gemini api
* Custom commands using a JSON configuration file
* Rule-based intent detection
* Speech recognition error handling
* Microphone error handling
* API and network error handling
* Application logging
* Environment-based configuration using `.env`
* Secure handling of credentials
* Modular service-based architecture

---

## Tech Stack

### Programming Language

* Python 3

### Libraries and Packages

* SpeechRecognition
* PyAudio
* pyttsx3
* requests
* python-dotenv
* pypiwin32
* pywin32
* comtypes

### External Services

* Google Speech Recognition
* Weather API
* gemini API
* Gmail SMTP
* Google Search

### Development Tools

* Visual Studio Code
* PowerShell
* Git
* GitHub
* Python Virtual Environment (`venv`)

---

## Project Architecture

The application follows a modular architecture where different responsibilities are separated into individual modules and services.

### Project Structure

```text
Python-Task1-VoiceAssistant/
│
├── main.py
├── intents.py
├── weather.py
├── reminders.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
│
├── config/
│   └── custom_commands.json
│
├── services/
│   ├── __init__.py
│   ├── voice_service.py
│   ├── email_service.py
│   ├── email_utils.py
│   ├── qa_service.py
│   ├── command_service.py
│   └── logger.py
│
├── logs/
│   └── assistant.log
│
└── test files
```

### Processing Flow

```text
User
  |
  v
Microphone Input
  |
  v
Speech Recognition
  |
  v
Recognized Text
  |
  v
Intent Detection
  |
  v
Appropriate Service
  |
  +----> Weather ------> Weather API
  |
  +----> Reminder -----> Reminder Service
  |
  +----> Email --------> Gmail SMTP
  |
  +----> Q&A ----------> gemini
  |
  +----> Search -------> Google
  |
  +----> Custom -------> JSON Configuration
  |
  v
Response
  |
  v
Text-to-Speech
  |
  v
User
```

The main processing pipeline is:

1. The user speaks a command.
2. The microphone captures the audio.
3. Speech recognition converts the audio into text.
4. The intent detection module analyzes the recognized text.
5. The appropriate service is selected.
6. The selected service performs the requested operation.
7. The assistant generates a response.
8. Text-to-speech converts the response into spoken output.

---

## Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Python-Task1-VoiceAssistant
```

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If activation is successful, the terminal should display:

```text
(.venv)
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

The application uses environment variables for sensitive configuration such as email credentials and API keys.

Create a file named:

```text
.env
```

Example:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
WEATHER_API_KEY=your_weather_api_key
```

The actual `.env` file must **not** be committed to GitHub.

A safe template is provided in:

```text
.env.example
```

---

## Gmail Configuration

The email feature uses Gmail SMTP.

A normal Gmail account password should not be stored directly in the application.

Instead:

1. Enable two-step verification on the Google account.
2. Create a Google App Password.
3. Store the generated App Password in `.env`.
4. Never upload `.env` to GitHub.

Example:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

The email service uses these values to authenticate with Gmail SMTP.

---

## Weather API Configuration

The weather feature requires a weather API key.

Add the API key to the `.env` file:

```env
WEATHER_API_KEY=your_weather_api_key
```

The key is loaded through environment variables rather than being hard-coded into the Python source code.

---

## Running the Application

First, activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Then start the assistant:

```bash
python main.py
```

The assistant will begin listening for commands.

Example:

```text
Listening...
You said: what time is it
Assistant: The current time is 08:30 PM.
```

---

# Supported Commands

## 1. Greeting

The assistant supports basic greetings.

Examples:

```text
Hello
Hi
Hey
Good morning
Good evening
```

---

## 2. Time

The assistant can provide the current time.

Examples:

```text
What time is it?
Tell me the current time
What is the time?
```

---

## 3. Date

The assistant can provide the current date.

Examples:

```text
What's today's date?
What is the current date?
Tell me today's date
```

---

## 4. Weather

The assistant can retrieve weather information for a requested city.

Examples:

```text
What's the weather in Dubai?
Weather in Kochi
What is the temperature in Noida?
```

The city is extracted from the user's command and sent to the configured weather service.

---

## 5. Web Search

The assistant can perform web searches using Google.

Examples:

```text
Search Python decorators
Search for machine learning
Look up Python
Google artificial intelligence
```

The search results are opened in the default web browser.

---

## 6. Reminders

The assistant supports voice-based reminders.

Examples:

```text
Remind me in 10 seconds to check my assignment
Remind me in 5 minutes to call my father
Remind me in 1 hour to attend the meeting
```

The reminder service extracts the requested time interval and reminder message before scheduling the reminder.

---

## 7. Email

The assistant can send emails through Gmail SMTP.

Say:

```text
Send an email
```

The assistant asks for:

* Recipient
* Subject
* Message
* Confirmation

Example interaction:

```text
Assistant: Who would you like to send the email to?

You: example@gmail.com

Assistant: What should the subject be?

You: Project Update

Assistant: What should I say in the email?

You: The project has been completed.

Assistant: Should I send it?

You: Yes, send it.
```

The email is sent only after user confirmation.

### Canceling an Email

The email operation can be canceled using commands such as:

```text
Cancel
Cancel email
Cancel it
Never mind
Don't send
```

---

## 8. General Knowledge Q&A

The assistant can answer general knowledge questions using gemini api.

Examples:

```text
Who invented Python?
What is artificial intelligence?
Who was Albert Einstein?
What is photosynthesis?
What is the capital of France?
```

The Q&A service searches online via gemini and extracts a short introductory answer.

If the external service is unavailable, the assistant reports the failure instead of crashing.

---

## 9. Custom Commands

The assistant supports user-defined commands through:

```text
config/custom_commands.json
```

Example:

```json
{
    "commands": [
        {
            "name": "open github",
            "action": "https://github.com"
        },
        {
            "name": "open linkedin",
            "action": "https://www.linkedin.com"
        },
        {
            "name": "open youtube",
            "action": "https://www.youtube.com"
        }
    ]
}
```

After adding a command, the user can say:

```text
Open GitHub
```

and the configured URL will be opened in the web browser.

The main advantage of this approach is that users can add supported custom commands without modifying the Python source code.

---

# Intent Detection

The assistant uses rule-based intent detection.

The recognized speech is converted into text and passed to:

```text
intents.py
```

The system identifies the appropriate intent from the user's command.

Supported intents include:

```text
GREETING
GET_TIME
GET_DATE
WEATHER
WEB_SEARCH
SET_REMINDER
SEND_EMAIL
GENERAL_QA
EXIT
UNKNOWN
```

The system also extracts entities when required.

### Example 1: Weather

Input:

```text
What's the weather in Dubai?
```

Intent:

```text
WEATHER
```

Entity:

```text
city = Dubai
```

### Example 2: Reminder

Input:

```text
Remind me in 10 minutes to check my assignment
```

Intent:

```text
SET_REMINDER
```

Entities:

```text
seconds = 600
message = check my assignment
```

---

# Error Handling

The application includes error handling for common runtime and external-service problems.

Examples include:

* Microphone unavailable
* Speech not understood
* Speech recognition service unavailable
* Network connection failure
* API timeout
* Invalid API response
* Invalid email address
* Email authentication failure
* Missing environment variables
* Invalid configuration
* Invalid custom command JSON

The goal is to prevent external service failures or invalid user input from immediately terminating the application.

---

# Logging

Important application events are recorded in:

```text
logs/assistant.log
```

Examples of logged events include:

* Speech recognized
* Intent detected
* Email sent successfully
* Q&A request completed
* API errors
* Microphone errors
* Configuration errors
* Custom command matches

Logging helps with debugging and makes it easier to understand application behavior without displaying every internal detail to the user.

---

# Configuration Management

Sensitive configuration is separated from the application code.

The project uses:

```text
.env
```

for values such as:

* Email address
* Gmail App Password
* Weather API key

The project also provides:

```text
.env.example
```

as a safe configuration template.

This approach prevents credentials from being hard-coded into Python source files.

---

# Privacy and Data Processing

This application processes different types of information depending on the command being used.

## Voice Data

The microphone captures the user's speech.

Speech is converted into text using the configured speech recognition service.

The application primarily works with the resulting text for intent detection and command processing.

Users should avoid speaking sensitive or confidential information into the assistant.

## Commands

Recognized commands are processed by the local Python application.

Commands are used to determine which feature should be executed.

## Weather Requests

When the user requests weather information, the requested city is sent to the configured weather API.

The application does not intentionally send unrelated voice or personal information to the weather service.

## Q&A Requests

Questions submitted to the Q&A feature are sent to gemini to retrieve relevant information.

Users should avoid submitting confidential information as questions.

## Email Data

When using the email feature, the following information is required:

* Recipient email address
* Email subject
* Email message

This information is sent through Gmail SMTP when the user confirms the email.

## Credentials

Email credentials and API keys are stored in `.env`.

They should never be committed to the repository.

The `.gitignore` file excludes `.env` from Git tracking.

## Logs

Application logs are stored locally in:

```text
logs/assistant.log
```

Logs may contain operational information such as recognized commands, detected intents, and service errors.

Sensitive information should not intentionally be logged.

## Third-Party Services

Depending on the feature being used, the application communicates with:

* Google Speech Recognition
* Weather API
* Wikipedia
* Gmail SMTP
* Google Search

The privacy policies and data-handling practices of these third-party services apply when information is sent to them.

---

# Security Considerations

The project follows several basic security practices:

* API keys are stored in environment variables.
* Gmail App Passwords are stored in `.env`.
* `.env` is excluded from Git tracking.
* Credentials are not hard-coded into source files.
* Email sending requires explicit user confirmation.
* External API failures are handled gracefully.
* Sensitive configuration is separated from application logic.
* Sensitive information should not intentionally be written to logs.

This project is intended as an educational and internship project and is **not presented as a production-grade security system**.

---

# Testing

Individual components can be tested independently before running the complete assistant.

Example test files include:

```bash
python test_email.py
python test_email_utils.py
python test_qa.py
python test_qa_intent.py
python test_custom_commands.py
python test_config.py
```

The tests verify individual components and services such as:

* Email sending
* Email normalization
* Q&A
* Intent detection
* Custom commands
* Configuration handling

---

# Example Workflow

A typical interaction follows this workflow:

```text
User speaks
     |
     v
SpeechRecognition
     |
     v
Text Command
     |
     v
Intent Detection
     |
     +----> Weather ------> Weather API
     |
     +----> Email --------> Gmail SMTP
     |
     +----> Q&A ----------> Wikipedia
     |
     +----> Search -------> Google
     |
     +----> Reminder -----> Reminder Service
     |
     +----> Custom -------> JSON Configuration
     |
     v
Response
     |
     v
Text-to-Speech
     |
     v
User hears response
```

---

# Future Improvements

Possible future improvements include:

* More natural language understanding
* More robust intent classification
* Additional API integrations
* Calendar integration
* Music playback
* Application launching
* Better reminder management
* Conversation history
* Improved testing coverage
* Graphical user interface
* Database-backed user preferences
* More advanced authentication and security

---



# Conclusion

The Voice Assistant demonstrates how Python can be used to integrate speech recognition, text-to-speech, APIs, email communication, web search, reminders, configuration management, logging, and modular service design into a single desktop application.

The project also demonstrates practical software development concepts such as separation of responsibilities, environment-based configuration, error handling, external API integration, testing, and basic security practices.
