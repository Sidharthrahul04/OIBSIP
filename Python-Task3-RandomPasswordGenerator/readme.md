# 🔐 Random Password Generator

A Python-based desktop application that generates secure and customizable passwords based on user-selected requirements.

The application provides a graphical user interface where users can choose the password length, character types, and whether ambiguous characters should be excluded. It also evaluates password strength, allows passwords to be copied to the clipboard, and maintains a session history of the last five generated passwords.

---

## 📌 Features

- Generate random passwords using Python's `secrets` module
- Select password length
- Include or exclude uppercase letters
- Include or exclude lowercase letters
- Include or exclude numbers
- Include or exclude symbols
- Exclude ambiguous characters such as `0`, `O`, `l`, and `1`
- Guarantee at least one character from each selected character type
- Password strength evaluation
- Copy generated passwords to the system clipboard
- Maintain the last five generated passwords during the current session
- Input validation and error handling
- Desktop graphical user interface using Tkinter

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Application programming language |
| Tkinter    | Graphical user interface |
| secrets    | Secure random password generation |
| string     | Standard character sets |
| Pyperclip  | Clipboard functionality |

---

## 🏗️ Project Architecture

The project follows a simple modular structure, separating the graphical interface from the password-generation logic.

```text
                    ┌─────────────────────┐
                    │        User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      main.py         │
                    │    GUI / Tkinter     │
                    └──────────┬──────────┘
                               │
                    Calls password logic
                               │
                               ▼
                    ┌─────────────────────┐
                    │    generator.py      │
                    │                       │
                    │ • Character Sets      │
                    │ • Password Generator  │
                    │ • Strength Checker    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Generated Password  │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
              GUI Display            Clipboard
                                     (Pyperclip)
```

---

## 🔄 Application Workflow

```text
Start Application
       ↓
Open Tkinter GUI
       ↓
Enter Password Length
       ↓
Select Character Types
       ↓
Choose Ambiguous Character Option
       ↓
Click Generate Password
       ↓
Validate User Input
       ↓
Build Character Sets
       ↓
Generate Password Using secrets
       ↓
Calculate Password Strength
       ↓
Display Password and Strength
       ↓
Store Password in Session History
       ↓
User Can Copy Password
```

---

## 📁 Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── .venv/                     # Virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── __pycache__/                # Compiled Python cache files
│
├── screenshots/                # Application screenshots used in this README
│   ├── screenshot1.png
│   ├── screenshot2.png
│   ├── screenshot3.png
│   └── screenshot4.png
│
├── .gitignore                  # Files and folders excluded from Git
├── generator.py                 # Password generation and strength evaluation logic
├── main.py                      # Tkinter GUI and application logic
├── readme.md                    # Project documentation
└── requirements.txt              # External Python dependencies
```

---

## 🔐 Password Generation

The application uses Python's built-in `secrets` module for password generation.

Instead of using the standard `random` module, the application uses:

```python
secrets.choice()
```

for selecting characters, ensuring the process is cryptographically secure.

The generated password is then securely shuffled using:

```python
secrets.SystemRandom().shuffle()
```

This makes the password generation suitable for security-sensitive use cases.

---

## 🎯 Character Selection

Users can customize the password by selecting from the following categories:

- Uppercase letters: `A-Z`
- Lowercase letters: `a-z`
- Numbers: `0-9`
- Symbols

The application ensures that **at least one character from each selected category** is included in the generated password.

For example, if the user selects Uppercase, Lowercase, Numbers, and Symbols, the generated password will contain at least one character from each of those four categories.

---

## 👁️ Ambiguous Character Exclusion

The application provides an option to exclude visually confusing characters:

- `0` (zero)
- `O` (capital O)
- `l` (lowercase L)
- `1` (one)

Excluding these characters makes passwords easier to read and manually type or enter.

---

## 💪 Password Strength

The application evaluates the generated password based on:

- Password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of symbols

The result is displayed as one of the following:

- **Weak**
- **Medium**
- **Strong**

---

## 📋 Clipboard Support

The **Copy Password** button uses the `Pyperclip` library to copy the currently generated password to the system clipboard, allowing the user to paste it directly into another application.

---

## 🕘 Password History

The application maintains a session-based history of the last five generated passwords.

```text
New Password
     ↓
Add to History
     ↓
Keep Maximum of 5
     ↓
Remove Oldest if Necessary
```

The history is stored only while the application is running and is **not saved permanently to disk**.

---

## ✅ Input Validation

The application validates user input before generating a password. Examples include:

- Invalid or non-numeric password length
- Password length below the minimum
- Too few character categories selected
- Password length shorter than the number of selected character categories

Error messages are displayed through Tkinter message boxes.

---

## 📦 Requirements

- Python 3.10 or newer
- Tkinter
- Pyperclip

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone <your-github-repository-url>
```

**2. Open the project directory**
```bash
cd Python-Task3-RandomPasswordGenerator
```

**3. Create a virtual environment**
```bash
python -m venv .venv
```

**4. Activate the virtual environment**

Windows PowerShell:
```bash
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```bash
.venv\Scripts\activate
```

**5. Install dependencies**
```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Application

After activating the virtual environment:

```bash
python main.py
```

The Random Password Generator GUI will open.

---

## 🖥️ How to Use

1. Enter the required password length.
2. Select the character types you want.
3. Enable ambiguous-character exclusion if required.
4. Click **Generate Password**.
5. Review the generated password.
6. Check the displayed password strength.
7. Click **Copy Password** if you want to copy it.
8. View previously generated passwords in the session history.

---

## 🔒 Security Considerations

- The application uses Python's `secrets` module rather than the standard `random` module for password generation.
- Passwords are generated in memory, and the application does not store them permanently in a file or database.
- The password history is maintained only for the current application session.

---

## 🚀 Future Improvements

Possible future enhancements include:

- Password visibility toggle
- Custom password patterns
- Password strength meter with more detailed scoring
- Securely clearing clipboard contents after a configurable period
- Option to clear password history
- Dark mode
- Password generation presets
- Export or password-manager integration

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/screenshot1.png)

### Password Generation
![Password Generation](screenshots/screenshot2.png)

### Copy to Clipboard
![Copy to Clipboard](screenshots/screenshot3.png)

### Input Validation
![Input Validation](screenshots/screenshot4.png)