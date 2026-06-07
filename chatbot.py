

# Project: Rule-Based AI Chatbot
# Internship: DecodeLabs - Artificial Intelligence
# Developer: Krishna
# College: GWECA - B.Tech IT
# Date: June 2026


import random
from datetime import datetime

# ── All Rules Function

def get_response(user_input):
    msg = user_input.lower()

    # Greetings
    if "hi" in msg or "hello" in msg or "hey" in msg:
        return"Hey there! i'm ByteBot How can i help you"

    # How are you
    elif "how are you" in msg or "how r u" in msg:
        return "I'm doing great! Thanks for asking 😊"# Bot name
    elif "your name" in msg or "who are you" in msg:
        return "I'm ByteBot, your rule-based AI assistant!"

    # Help
    elif "help" in msg or "what can you do" in msg:
        return "I can chat, tell jokes, answer AI questions and more! Try me 😄"

    # Joke
    elif "joke" in msg or "funny" in msg:
        jokes = [
            "Why did the programmer quit? Because he didn't get arrays 😂",
            "Why do Java developers wear glasses? Because they don't C# 😄",
            "A SQL query walks into a bar, walks up to two tables and asks... Can I JOIN you? 😂"
        ]
        return random.choice(jokes)

    # Age
    elif "your age" in msg or "how old" in msg:
        return "I'm just a few days old! Still learning 😄"

    # Creator
    elif "who made you" in msg or "who created you" in msg or "who built you" in msg:
        return "I was built by Krishna as part of DecodeLabs AI Internship! 💻"

    # Favourite color
    elif "colour" in msg or "color" in msg:
        return "I love blue 💙 like the sky and the ocean!"

    # About AI
    elif "what is ai" in msg or "artificial intelligence" in msg:
        return "AI is making machines smart enough to think and learn like humans!"

    # Machine Learning
    elif "machine learning" in msg or "ml" in msg:
        return "Machine Learning is teaching computers to learn from data without being explicitly programmed!"

    # Deep Learning
    elif "deep learning" in msg or "dl" in msg:
        return "Deep Learning uses neural networks inspired by the human brain!"

    # Python
    elif "python" in msg:
        return "Python is the most popular programming language for AI and ML! 🐍"

    # Chatbot
    elif "what is chatbot" in msg or "what are you" in msg:
        return "A chatbot is a program that simulates conversation with humans using rules or AI!"

    # Robot
    elif "robot" in msg:
        return "Robots use AI to sense, think and act in the real world! 🤖"

    # Data Science
    elif "data science" in msg:
        return "Data Science is extracting useful insights from large amounts of data!"

    # Neural Network
    elif "neural network" in msg:
        return "Neural networks are computing systems inspired by biological neural networks in our brains!"

    # About internship
    elif "internship" in msg or "decodelabs" in msg:
        return "DecodeLabs is where I was born! Great place to learn AI 🚀"

    # Compliment to bot
    elif "good bot" in msg or "nice" in msg or "awesome" in msg or "great" in msg:
        return "Thank you so much! That means a lot to me 😊🙏"

    # Feeling sad
    elif "sad" in msg or "unhappy" in msg or "depressed" in msg:
        return "Aww don't be sad! I'm here to chat and cheer you up 😊💙"

    # Feeling happy
    elif "happy" in msg or "excited" in msg or "great" in msg:
        return "That's amazing! Happiness is contagious 😄🎉"

    # Weather
    elif "weather" in msg:
        return "I can't check live weather yet, but I hope it's sunny where you are! ☀️"

    # Time
    elif "time" in msg:
        now = datetime.now().strftime("%I:%M %p")
        return f"Current time is {now} ⏰"

    # Date
    elif "date" in msg or "today" in msg:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today} 📅"

    # Thanks
    elif "thank" in msg or "thanks" in msg or "thankyou" in msg:
        return "You're welcome! Always happy to help 😊"

    # Bye
    elif "bye" in msg or "goodbye" in msg or "exit" in msg or "quit" in msg:
        return "quit"

    # Default fallback
    else:
        fallbacks = [
            "Hmm, I don't know that yet! Try asking something else 🤔",
            "I'm still learning! Can you ask differently?",
            "That's beyond my knowledge for now 😅",
            "Interesting question! I don't have an answer yet 🤖",
            "I didn't understand that. Can you rephrase?"
        ]
        return random.choice(fallbacks)
        # Main Program
print("=" * 45)
print("        Welcome to ByteBot 🤖")
print("   Rule-Based AI Chatbot | DecodeLabs")
print("        Type 'bye' to exit")
print("=" * 45)

name = input("\nByteBot: Hey! What's your name? ")
print(f"ByteBot: Nice to meet you, {name}! Let's chat 😊\n")

# Chat log setup
log = []
log.append(f"Chat Log - {datetime.now().strftime('%d %B %Y, %I:%M %p')}")
log.append("=" * 45)

# ── Chat Loop ─────────────────────────────────────

while True:
    user_msg = input(f"{name}: ")

    # Empty input check
    if user_msg.strip() == "":
        print("ByteBot: Please type something! 😄\n")
        continue

    # Save user message to log
    log.append(f"{name}: {user_msg}")

    # Get bot response
    response = get_response(user_msg)

    # Exit condition
    if response == "quit":
        farewell = f"ByteBot: Goodbye {name}! It was great chatting with you 👋"
        print(farewell)
        log.append(farewell)
        log.append("--- Chat Ended ---")
        break
  # Print and log response
    print(f"ByteBot: {response}\n")
    log.append(f"ByteBot: {response}")

# ── Save Chat Log ─────────────────────────────────

with open("chat_log.txt", "w") as f:
    for line in log:
        f.write(line + "\n")

print("\n💾 Chat saved to chat_log.txt")
print("✅ Thank you for using ByteBot!")  