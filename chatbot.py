# ============================================================
# Project Title : Rule-Based AI Chatbot
# Internship    : DecodeLabs AI Internship

# Description:
# This project is a simple Rule-Based AI Chatbot.
# It responds to predefined user inputs using
# if-elif-else statements and runs continuously
# until the user exits.
# ============================================================

# ---------------- IMPORT LIBRARIES ---------------- #

import datetime
import random

# ---------------- CHATBOT RESPONSES ---------------- #

greetings = [
    "Hello! Nice to meet you.",
    "Hi! How can I help you today?",
    "Hey! Welcome."
]

how_are_you = [
    "I'm doing great. Thanks for asking!",
    "I'm fine. Hope you're doing well too!",
    "Everything is working perfectly!"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer go broke? Because he used up all his cache!",
    "Debugging is like being a detective in a crime movie where you're also the criminal."
]

# ---------------- DISPLAY INTRO ---------------- #

def show_intro():
    print("=" * 60)
    print("            RULE-BASED AI CHATBOT")
    print("=" * 60)
    print("Hello! I am a simple AI Chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' anytime to exit.")
    print("=" * 60)

# ---------------- HELP MENU ---------------- #

def show_help():
    print("\nYou can ask me the following questions:\n")

    print(" hello")
    print(" hi")
    print(" hey")
    print(" how are you")
    print(" your name")
    print(" who made you")
    print(" what is ai")
    print(" what is python")
    print(" tell me a joke")
    print(" date")
    print(" time")
    print(" thank you")
    print(" bye\n")

# ---------------- CHATBOT LOGIC ---------------- #

def chatbot():

    while True:

        user = input("\nYou : ").strip().lower()

        # Empty Input 
        if user == "":
            print("Bot : Please type something.")
            continue

        # Greetings
        elif user in ["hello", "hi", "hey"]:
            print("Bot :", random.choice(greetings))

        # How are you
        elif user == "how are you":
            print("Bot :", random.choice(how_are_you))

        # Name
        elif user in ["your name", "what is your name"]:
            print("Bot : My name is ChatBot.")

        # Creator
        elif user == "who made you":
            print("Bot : I was created as an AI internship project using Python.")

        # AI
        elif user == "what is ai":
            print("Bot : AI stands for Artificial Intelligence.")
            print("Bot : It enables computers to perform tasks that normally require human intelligence.")

        # Python
        elif user == "what is python":
            print("Bot : Python is an easy-to-learn programming language.")
            print("Bot : It is widely used for AI, web development, automation and data science.")

        # Joke
        elif user == "tell me a joke":
            print("Bot :", random.choice(jokes))

        # Date
        elif user == "date":
            today = datetime.date.today()
            print("Bot : Today's date is", today.strftime("%d-%m-%Y"))

        # Time
        elif user == "time":
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print("Bot : Current time is", current_time)

        # Thank You
        elif user in ["thanks", "thank you"]:
            print("Bot : You're welcome! Happy to help.")

        # Help
        elif user == "help":
            show_help()

        # Exit
        elif user in ["bye", "exit", "quit"]:
            print("\nBot : Thank you for chatting with me.")
            print("Bot : Have a wonderful day!")
            break

        # Default Response
        else:
            print("Bot : Sorry, I don't understand that question.")
            print("Bot : Type 'help' to see the available commands.")

# ---------------- MAIN FUNCTION ---------------- #

def main():

    show_intro()

    chatbot()

# ---------------- PROGRAM STARTS HERE ---------------- #

if __name__ == "__main__":
    main()


