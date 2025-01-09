import tkinter as tk
from tkinter import scrolledtext
import random

# Zufällige Antworten für unerkannte Fragen
random_answers = [
    "Das weiß ich leider nicht.",
    "Könntest du dein Problem nochmals genauer beschreiben?",
    "Leider kann ich dir bei deinem Problem nicht helfen, bitte verständige unseren Support."
]

# Bibliothek für Antworten, wenn Stichwörter in der Frage implementiert sind
intent_answers = {
    'hallo': 'Hey, wie kann ich dir helfen?',
    'passwort': 'Wenn Sie Ihr Passwort vergessen haben, klicken Sie auf "Passwort vergessen" auf der Anmeldeseite.',
    'internet': 'Bitte überprüfen Sie, ob Ihr Router eingeschaltet ist und ob die Kabel richtig angeschlossen sind.',
    'drucker': 'Überprüfen Sie, ob der Drucker eingeschaltet ist und Papier sowie Toner vorhanden sind.',
    'email': 'Bitte prüfen Sie, ob Ihre Internetverbindung stabil ist und Sie die richtigen Zugangsdaten verwenden.',
    'software': 'Haben Sie die Software aktualisiert? Falls nicht, führen Sie bitte ein Update durch.',
    'bildschirm': 'Bitte prüfen Sie, ob der Monitor eingeschaltet ist, und ob alle Kabel eingesteckt sind.',
    'hilfe': 'Zu diesen Themen kannst du mich Fragen: Passwort, internet,drucker,email,software,bildschirm'
}

# Synonyme für Stichwörter
synonyms = {
    'hallo': ['hi', 'hey'],
    'passwort': ['password', 'kennwort'],
    'internet': ['netzwerk', 'wifi', 'wlan'],
    'email': ['mail', 'nachrichten'],
    'software': ['programm', 'anwendung'],
    'bildschirm': ['monitor']
}

# Funktion zur Überprüfung von Synonymen
def find_intent(word):
    # Prüfe, ob das Wort direkt ein Intent ist
    if word in intent_answers:
        return word
    # Prüfe, ob das Wort ein Synonym ist
    for key, values in synonyms.items():
        if word in values:
            return key  # Gib den passenden Schlüssel zurück
    return None

# Funktion zur Verarbeitung der Benutzereingabe
def process_input():
    user_input = user_entry.get().strip().lower()  # Holen und formatieren der Benutzereingabe
    user_entry.delete(0, tk.END)  # Eingabefeld leeren
    chat_display.insert(tk.END, f"Du: {user_input}\n")  # Eingabe in der Anzeige anzeigen

    if user_input == "bye":
        chat_display.insert(tk.END, "Chatbot: Ich wünsche dir einen schönen Tag und bis zum nächsten Mal!\n")
        root.quit()
        return

    user_words = user_input.split()
    found_answer = False

    for word in user_words:
        intent = find_intent(word)  # Prüfe auf passende Intents oder Synonyme
        if intent:
            chat_display.insert(tk.END, f"Chatbot: {intent_answers[intent]}\n")
            found_answer = True
            break

    if not found_answer:
        chat_display.insert(tk.END, f"Chatbot: {random.choice(random_answers)}\n")

# GUI erstellen
root = tk.Tk()
root.title("Chatbot mit Tkinter")

# Anzeige für den Chatverlauf
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state='normal', font=("Arial", 12))
chat_display.pack(pady=10)
chat_display.insert(tk.END, "Chatbot: Hallo, ich bin dein persönlicher Chatbot, der dir bei deinen Problemen helfen soll. Für eine Übersicht, schreib einfach Hilfe.\n")

# Eingabefeld und Senden-Button
user_entry = tk.Entry(root, width=40, font=("Arial", 14))
user_entry.pack(pady=5)
user_entry.bind("<Return>", lambda event: process_input())

send_button = tk.Button(root, text="Senden", command=process_input, font=("Arial", 12), bg="lightblue")
send_button.pack(pady=5)

# Haupt-GUI-Schleife starten
root.mainloop()
