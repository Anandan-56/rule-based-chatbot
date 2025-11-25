"""
Simple rule-based chatbot using if-elif-else (Task 8)
Save as: chatbot_if_else.py
Run: python chatbot_if_else.py
"""

import datetime
import random

# Small knowledge base (keywords mapped to intents/responses)
GREETINGS = ["hi", "hello", "hey", "hola", "good morning", "good afternoon", "good evening"]
FAREWELLS = ["bye", "goodbye", "see you", "exit", "quit", "later"]
THANKS = ["thanks", "thank you", "thx"]
HOW_ARE_YOU = ["how are you", "how's it going", "how are u"]

FAQ = {
    "what is your name": "I'm ChatPy, a simple rule-based chatbot built with if-elif-else.",
    "what can you do": "I can greet you, answer basic questions, tell the current time, and show a simple sample.",
    "how to exit": "Type 'exit' or 'quit' (or any of the words: exit, quit, bye)."
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache."
]

def normalize(text: str) -> str:
    """Lowercase and strip punctuation-ish characters to help matching."""
    return text.strip().lower()

def contains_any(text: str, words: list) -> bool:
    for w in words:
        if w in text:
            return True
    return False

def handle_input(user: str) -> str:
    u = normalize(user)

    # Exit / Farewell
    if contains_any(u, FAREWELLS):
        return "Goodbye! 👋 (type 'restart' to talk again or re-run the program to start fresh.)", True

    # Greetings
    if contains_any(u, GREETINGS):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you?"]), False

    # Thank you
    if contains_any(u, THANKS):
        return "You're welcome! 😊", False

    # How are you
    if contains_any(u, HOW_ARE_YOU):
        return "I'm a program, so I'm always operating normally 😄. How about you?", False

    # FAQ exact-ish matches
    for q, ans in FAQ.items():
        if q in u:
            return ans, False

    # Ask for time
    if "time" in u:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is: {now}", False

    # Joke request
    if "joke" in u or "funny" in u:
        return random.choice(JOKES), False

    # Handling multiple intents (example): "hi, what's the time?"
    # simple approach: check greeting + time
    if any(g in u for g in GREETINGS) and "time" in u:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Hi! The current time is {now}", False

    # Fallback / Unknown intent
    return (
        "Sorry, I didn't understand that. You can ask things like:\n"
        "- 'What is your name?'\n"
        "- 'What can you do?'\n"
        "- 'Tell me a joke'\n"
        "- 'What is the time?'\n"
        "Or type 'exit' to quit.",
        False
    )

def main():
    print("Welcome to ChatPy — a simple rule-based chatbot.")
    print("Type 'exit' or 'quit' to leave.\n")

    # Main input loop
    while True:
        try:
            user = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBye! (caught keyboard interrupt)")
            break

        # allow restart command to re-run conversation in same session
        if normalize(user) == "restart":
            print("Conversation restarted.\n")
            continue

        response, should_exit = handle_input(user)
        print("Bot:", response)

        if should_exit:
            break

if __name__ == "__main__":
    main()
