import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Helpster Chatbot")

        # Zufällige Antworten für unerkannte Fragen
        self.random_answers = [
            "Das weiß ich leider nicht.",
            "Könntest du dein Problem nochmals genauer beschreiben?",
            "Leider kann ich dir bei deinem Problem nicht helfen, bitte verständige unseren Support."
        ]

        # Bibliothek für Antworten, wenn Stichwörter in der Frage implementiert sind
        self.intent_answers = {
            'hallo': 'Hey, wie kann ich dir helfen?',
            'passwort': 'Wenn Sie Ihr Passwort vergessen haben, klicken Sie auf \"Passwort vergessen\" auf der Anmeldeseite.',
            'internet': 'Bitte überprüfen Sie, ob Ihr Router eingeschaltet ist und ob die Kabel richtig angeschlossen sind.',
            'drucker': 'Überprüfen Sie, ob der Drucker eingeschaltet ist und Papier sowie Toner vorhanden sind.',
            'email': 'Bitte prüfen Sie, ob Ihre Internetverbindung stabil ist und Sie die richtigen Zugangsdaten verwenden.',
            'software': 'Haben Sie die Software aktualisiert? Falls nicht, führen Sie bitte ein Update durch.',
            'bildschirm': 'Bitte prüfen Sie, ob der Monitor eingeschaltet ist, und ob alle Kabel eingesteckt sind.',
            'hilfe': 'Zu diesen Themen kannst du mich Fragen: Passwort, internet, drucker, email, software, bildschirm'
        }

        # Synonyme für Stichwörter
        self.synonyms = {
            'hallo': ['hi', 'hey'],
            'passwort': ['password', 'kennwort'],
            'internet': ['netzwerk', 'wifi', 'wlan'],
            'email': ['mail', 'nachrichten'],
            'software': ['programm', 'anwendung'],
            'bildschirm': ['monitor']
        }

        # Anzeige für den Chatverlauf
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state='normal', font=("Arial", 12))
        self.chat_display.pack(pady=10)
        self.chat_display.insert(tk.END, f"{self.get_timestamp()} Chatbot: Hallo, ich bin dein persönlicher Chatbot, der dir bei deinen Problemen helfen soll. Für eine Übersicht, schreib einfach Hilfe.\n")

        # Eingabefeld und Senden-Button
        self.user_entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.user_entry.pack(pady=5)
        self.user_entry.bind("<Return>", lambda event: self.process_input())

        self.send_button = tk.Button(root, text="Senden", command=self.process_input, font=("Arial", 12), bg="lightblue")
        self.send_button.pack(pady=5)

    def get_timestamp(self):
        # Gibt den aktuellen Zeitstempel zurück
        return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    def find_intent(self, word):
        # Prüfe, ob das Wort direkt ein Intent ist
        if word in self.intent_answers:
            return word
        # Prüfe, ob das Wort ein Synonym ist
        for key, values in self.synonyms.items():
            if word in values:
                return key  # Gib den passenden Schlüssel zurück
        return None

    def auto_save_chat(self):
        chat_log = self.chat_display.get("1.0", tk.END).strip()
        if chat_log:
            with open("chat_log.txt", "w", encoding="utf-8") as file:
                file.write(chat_log)

    def process_input(self):
        user_input = self.user_entry.get().strip().lower()  # Holen und formatieren der Benutzereingabe
        self.user_entry.delete(0, tk.END)  # Eingabefeld leeren
        self.chat_display.insert(tk.END, f"{self.get_timestamp()} Du: {user_input}\n")  # Eingabe in der Anzeige anzeigen

        if user_input == "bye":
            self.chat_display.insert(tk.END, f"{self.get_timestamp()} Chatbot: Ich wünsche dir einen schönen Tag und bis zum nächsten Mal!\n")
            self.auto_save_chat()
            self.root.quit()
            return

        user_words = user_input.split()
        found_answer = False

        for word in user_words:
            intent = self.find_intent(word)  # Prüfe auf passende Intents oder Synonyme
            if intent:
                self.chat_display.insert(tk.END, f"{self.get_timestamp()} Chatbot: {self.intent_answers[intent]}\n")
                found_answer = True
                break

        if not found_answer:
            self.chat_display.insert(tk.END, f"{self.get_timestamp()} Chatbot: {random.choice(self.random_answers)}\n")

        self.auto_save_chat()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
