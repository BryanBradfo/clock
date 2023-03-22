import tkinter as tk
import time

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.configure(bg='black')  # Changement de la couleur de fond en noir
fenetre.title("Horloge")

# Mise en plein écran
fenetre.attributes("-fullscreen", True)

# Création de l'horloge
horloge = tk.Label(fenetre, font=('times', 72, 'bold'), bg='black', fg='white')  # Changement de la police de caractères et de la couleur de texte
horloge.pack(fill=tk.BOTH, expand=1)

# Fonction pour mettre à jour l'horloge toutes les secondes
def tick():
    heure_actuelle = time.strftime("%I:%M:%S %p")
    horloge.config(text=heure_actuelle)
    horloge.after(200, tick)

# Mise à jour de l'horloge pour la première fois
tick()

# Création du bouton "Quitter"
bouton_quitter = tk.Button(fenetre, text="Quitter", bg='red', fg='white', command=fenetre.destroy)
bouton_quitter.pack(side='right', anchor='ne')  # Placement du bouton en haut à droite de la fenêtre

# Démarrage de la boucle principale de Tkinter
fenetre.mainloop()
