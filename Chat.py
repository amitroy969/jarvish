import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from voice import speak
from listen import listen
from mtranslate import translate
# Initialize the device (GPU or CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents and model data
with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"

# Load the model and data, forcing the model to load on CPU
data = torch.load(FILE, map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialize the model and load the trained weights
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

model.eval()

import random
import torch

def Chat(st: str):
    print("Chatbot is active. Say 'exit' to quit.")
    while True:
        try:
            # Listen for input
            listen_input = listen()  # Assuming 'listen' function captures user speech
            Q = translate(listen_input, 'en', 'auto')  # Translate to English if needed
            QL = Q.lower()
            print(f"User said: {QL}")

            if QL == "exit":
                print("Exiting chatbot. Have a great day!")
                break

            # Tokenize and process the sentence
            sentence = tokenize(QL)
            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0])  # Ensure it's 2D (1, input_size)
            X = torch.from_numpy(X).to(device)

            # Get the model's prediction
            output = model(X)
            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]
            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.60:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        response = random.choice(intent['responses'])
                        print(f"Chatbot: {response}")
                        speak(response)  # Assuming 'speak' generates voice output
                        break
            
            elif "terminate" in QL :
                speak("as you wish , enjoy sir")
                break

            else:
                fallback_response = "I do not understand..."
                print(f"Chatbot: {fallback_response}")
                #speak(fallback_response)

        except Exception as e:
            print(f"An error occurred: {e}")
            #speak("Oops, something went wrong. Let's try again!")

























# def Chat(st: str):
#     while True :
#      try:

#         listen=listen()
#         Q=listen
#         Q=translate(Q,'en','auto')
#         QL=Q.lower()
#         print(f"{QL}")
#         getchat=Chat(QL)
#         speak( getchat)
        
#         sentence = st
#         # Tokenize and process the sentence
#         sentence = tokenize(sentence)
#         X = bag_of_words(sentence, all_words)  
#         X = X.reshape(1, X.shape[0])  # Ensure it's 2D (1, input_size)
#         X = torch.from_numpy(X).to(device)

#         # Get the model's prediction
#         output = model(X)
#         _, predicted = torch.max(output, dim=1)

#         tag = tags[predicted.item()]
#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]

#         if prob.item() > 0.60:
#             # witty_closings = [
#             #     "Anything else, boss?",
#             #     "At your service, as always.",
#             #     "Let me know if there's more brilliance required.",
#             #     "Shall I prepare the systems for your next genius idea?",
#             # ]
#             for intent in intents['intents']:
#                 if tag == intent["tag"]:
#                     response = random.choice(intent['responses'])
#                     # witty_response = random.choice(witty_closings)
#                     # final_response = f"{response} {witty_response}"
#                     # print(final_response)
#                     # speak(final_response)  # Assuming 'speak' generates voice output
#                     # return final_response
#                     return response
#         else:
#             fallback_response = "I do not understand..."
#             print(fallback_response)
#             #speak(fallback_response)
#             #return fallback_response

#      except Exception as e:
#         print(" error; {0}".format(e)) 
        








































# import random
# import json
# import torch
# from model import NeuralNet
# from nltk_utils import bag_of_words, tokenize
# from voice import speak
# from listen import listen
# # Initialize the device (GPU or CPU)
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# # Load intents and model data
# """with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)"""

# with open('intents.json', 'r', encoding='utf-8') as json_data:
#     intents = json.load(json_data)

# FILE = "data.pth"

# # Load the model and data, forcing the model to load on CPU
# data = torch.load(FILE, map_location=torch.device('cpu'))

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# # Initialize the model and load the trained weights
# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# def Chat(st:str):
#     sentence = st
#     # Tokenize and process the sentence
#     sentence = tokenize(sentence)
#     # Ensure bag_of_words is using the correct all_words list
#     X = bag_of_words(sentence, all_words)  
#     X = X.reshape(1, X.shape[0])  # Ensure it's 2D (1, input_size)
#     X = torch.from_numpy(X).to(device)

#     # Get the model's prediction
#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]

#     if prob.item() > 0.60:
#         witty_closings = [
#                         "Anything else, boss?",
#                         "At your service, as always.",
#                         "Let me know if there's more brilliance required.",
#                         "Shall I prepare the systems for your next genius idea?",
#                     ]
#         witty_response = random.choice(witty_closings)
#         response = f"{response} {witty_response}"
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                return random.choice(intent['responses'])
       
#     else:
#         print(" I do not understand...")
        
