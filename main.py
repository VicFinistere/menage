import os
import gtts

print("Salut !")
print("Vous avez un peu de temps ?") 
for r in [os.path.splitext(filename)[0] for filename in os.listdir()]:
    if r not in 'main':
        print(r)
room = input("Quelle pièce souhaitez-vous remettre en ordre ?")
print(open(room + '.txt', mode='r',encoding="utf-8").read())

# Sélectionner l'action parmi la liste proposée de la salle 
instruction = "En avant ta da da da da !"
tts = gtts.gTTS(instruction, lang="fr")
tts.save("sound.mp3")
os.system("sound.mp3")

