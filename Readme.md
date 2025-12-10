# 🤖 WhatsApp Auto-Reply Chatbot using Google Gemini

This is a simple Python automation bot that:

- Reads WhatsApp messages from the screen  
- Sends the text to Google Gemini  
- Gets a reply  
- Automatically types and sends the message back in WhatsApp  

No WhatsApp API — only Python + PyAutoGUI + Gemini.

---

## 📌 Features

- AI-generated replies using Gemini  
- Automatically copies incoming chat text  
- Automatically pastes + sends reply  
- Simple GUI automation  
- No API keys exposed (uses .env file)  

---

## 📁 Project Files

main.py
client.py
reply.py
cursor_position.py
requirements.txt
.env.example
README.md


Copy code

---

## 🚀 Setup

### 1️⃣ Install requirements

pip install -r requirements.txt


Copy code

### 2️⃣ Create a `.env` file (copy from `.env.example`)

GEMINI_API_KEY=your_api_key_here

Copy code

### 3️⃣ Run the bot

python main.py


Copy code

---

## 🖱 Get Cursor Positions (for PyAutoGUI)

Run:

python cursor_position.py


Copy code

Move your mouse where needed → coordinates will print.

---

## ⚠ Important

- Do **NOT** upload `.env` to GitHub  
- Do **NOT** move your mouse while the bot runs  
- Press mouse to top-left corner to stop the script instantly  

---

## ✨ Author

Project created by **Bhavish**  
Simple Python automation + AI reply system.
