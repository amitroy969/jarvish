
import json
import pyttsx3
import speech_recognition as sr
import colorama
from colorama import Fore, Style
from hugchat import hugchat
import threading
import time
import random
from listen import listen
colorama.init(autoreset=True)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=4)
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query
        except Exception as e:
            print("Could not understand audio, please say that again.")
            return "I didn't understand. Please try again."  # Replace None with default response
query=takecommand().lower()
# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 165)
engine.setProperty('voice', voices[11].id)  # Choose a suitable voice index.

# Define speak function
def speak(*args, **kwargs):
    # Concatenate all arguments into a single string
    audio = " ".join(str(arg) for arg in args)
    print(Fore.CYAN + audio)  # Print the text in cyan
    engine.say(audio)         # Send the text to the TTS engine
    engine.runAndWait()       # Wait for the speech to finish
    return audio              # Return the concatenated string

# Global memory and conversation context
memory = {}
conversation_context = ""  # Holds the entire conversation for continuity

# Event to handle listening state
# stop_event = threading.Event()

# Function to save memory to a file
def save_memory():
    with open("memory.json", "w") as file:
        json.dump(memory, file)

# Function to load memory from a file
def load_memory():
    global memory
    try:
        with open("memory.json", "r") as file:
            memory = json.load(file)
    except FileNotFoundError:
        memory = {}


# Function to speak and handle interruption
def speak_response(response):
    engine.say(response)
    engine.runAndWait()  # Ensure speech is completed before continuing

# Main function to handle speech recognition and responses
def chatBot(query):
    global conversation_context

    # # Start the listening thread for the 'stop' command
    # listener_thread = threading.Thread(target=listen_for_stop)
    # listener_thread.daemon = True
    # listener_thread.start()

    # Initialize speech recognizer
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

   # speak_response(Fore.MAGENTA + Style.BRIGHT + "Hello I am Jarvis , Ready to assist! sir")

    speak_response("welcome back , Ready to assist! sir")

    while True:
            # Listen for the user command
        try:
            with microphone as source:
                print("Listening for your command...")
                # audio = recognizer.listen(source, timeout=5)
                # query = recognizer.recognize_google(audio).lower()
                query=listen().lower()
                print(Fore.GREEN + "You said: " + query)

                if "exit" in query or "quit" in query or "bye" in query:
                    print(Fore.YELLOW + "Jarvis: Shutting down, boss. Catch you later!")
                    engine.say("Shutting down, boss. Catch you later!")
                    engine.runAndWait()
                    break  # Exit the loop if the user says exit/quit/bye

                # Process the query and get the response
                chatbot = hugchat.ChatBot(cookie_path="cookies.json")
                chatbot.change_conversation(chatbot.new_conversation())

                # Handle memory commands
                if "remember" in query:
                    key, _, value = query.partition("remember ")
                    memory[key.strip()] = value.strip()
                    save_memory()
                    response = f"I've noted that down: '{key.strip()}'."
                elif "recall" in query:
                    key = query.partition("recall ")[2].strip()
                    response = memory.get(key, f"Sorry, I don't recall anything about '{key}'.")
                else:
                    # Add the query to the conversation context
                    conversation_context += f"\nUser: {query}\nJarvis:"

                    # Get response from the chatbot
                    raw_response = chatbot.chat(conversation_context)
                    response_text = str(raw_response).strip()

                    # Add Jarvis's response to the conversation context
                    conversation_context += f" {response_text}"

                    # Add Jarvis-style flair
                    witty_closings = [
                        "Anything else, boss?",
                        "At your service, as always.",
                        "Let me know if there's more brilliance required.",
                        "Shall I prepare the systems for your next genius idea?",
                    ]
                    witty_response = random.choice(witty_closings)
                    response = f"{response_text} {witty_response}"

                    # Speak the response and allow interruption
                    print(Fore.CYAN + "Jarvis: " + response)
                    # stop_event.clear()  # Reset the stop event to allow listening again
                    speak_response(response)

        except sr.UnknownValueError:
            print(Fore.RED + "Sorry, I could not understand that.")
        except sr.RequestError as e:
            print(Fore.RED + f"Could not request results from Google Speech Recognition service; {e}")
        except KeyboardInterrupt:
            break

# Load memory at startup
load_memory()


if __name__ == "__main__":
    chatBot(query)
  


































# from hugchat import hugchat
# import pyttsx3
# Function to recognize speech continuously and listen for 'stop' command
# def listen_for_stop():
#     recognizer = sr.Recognizer()

#     while True:
#         if not stop_event.is_set():  # Continue listening if stop event is not set
#             try:
#                 # Use `with` to safely manage the microphone
#                 with sr.Microphone() as source:
#                     print("Listening for 'stop' command...")
#                     audio = recognizer.listen(source, timeout=5)
#                     try:
#                         command = recognizer.recognize_google(audio).lower()
#                         if "stop" in command:
#                             print(Fore.RED + "Stop command received. Stopping speech...")
#                             engine.stop()  # Stop the speech immediately
#                             stop_event.set()  # Set the stop event to indicate listening should stop
#                     except sr.UnknownValueError:
#                         pass
#                     except sr.RequestError as e:
#                         print(f"Could not request results; {e}")
#             except AssertionError:
#                 print("Microphone not properly initialized. Retrying...")
# import colorama
# from colorama import Fore, Back, Style










# # colorama.init(autoreset=True)

# # Initialize pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('rate', 165)
# engine.setProperty('voice', voices[11].id)  # Choose the voice
# # Example: brian1, emma2, giant3, etc.

# # Define speak function
# def speak(*args, **kwargs):
#     # Concatenate all arguments into a single string
#     audio = " ".join(str(arg) for arg in args)
#     print(Fore.CYAN + audio)  # Print the text in cyan
#     engine.say(audio)         # Send the text to the TTS engine
#     engine.runAndWait()       # Wait for the speech to finish
#     return audio              # Return the concatenated string

# # Example usage
# #spoken_text = speak("Hello,", "this is your assistant,", "how can I help you today?")
# #print(Fore.GREEN + "Spoken text:", spoken_text)



# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path="cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response

