import random
import pickle
import keyboard
import threading

# Fonction pour créer ou récupérer le fichier de scores avec pickle
def get_scores():
    try:
        with open("scores.pkl", "rb") as scores_file:
            scores = pickle.load(scores_file)
    except (FileNotFoundError, EOFError):
        # Si le fichier n'existe pas ou est vide, créez un nouveau dictionnaire
        scores = {}
        with open("scores.pkl", "wb") as scores_file:
            pickle.dump(scores, scores_file)
    return scores

# Fonction pour arrêter le jeu lorsque la touche 'K' est enfoncée
def check_for_pause():
    while True:
        if keyboard.is_pressed('k'):
            print("Jwèt la kanpe!")
            break

# Fonction pour jouer au jeu
def joue_jeu(utilizate, scores):
    epsedo = {'min': 0, 'max': 100}
    nimewo_kache = random.randint(epsedo['min'], epsedo['max'])
    chans_rete = 5

    # Créez un thread pour surveiller la touche 'K'
    pause_thread = threading.Thread(target=check_for_pause)
    pause_thread.start()

    while chans_rete > 0:
        try:
            nimewo_tape = int(input("Tape yon nimewo: "))
            if nimewo_tape < 0 or nimewo_tape > 100:
                print("Nimewo a dwe ant 0 ak 100.")
                continue
            if nimewo_tape == nimewo_kache:
                print("BRAVO! Ou genyen pati a!")
                ancien_sko = scores.get(utilizate, 0)
                bonus = chans_rete * 30
                nouvo_sko = ancien_sko + bonus
                scores[utilizate] = nouvo_sko
                enregistre_scores(scores)
                print(f"Ancien skò: {ancien_sko}, Nouvo skò: {nouvo_sko}")
                break
            elif nimewo_tape < nimewo_kache:
                print("Nimewo wap chèche a pi gran.")
            elif nimewo_tape > nimewo_kache:
                print("Nimewo chèche a pi piti.")
            chans_rete -= 1
            print(f"Chans ki rete: {chans_rete}")
        except ValueError:
            print("Mete yon nimewo valab, tanpri")

    if chans_rete == 0:
        print(f"Ou pèdi! Nimewo kache a te {nimewo_kache}")

    # Attendez que le thread de pause se termine
    pause_thread.join()

# Fonction pour enregistrer les scores avec pickle
def enregistre_scores(scores):
    with open("scores.pkl", "wb") as scores_file:
        pickle.dump(scores, scores_file)

# Fonction principale
def main():
    print("Byenvini nan Lawoulèt!")
    epsedo = {'min': 0, 'max': 100}
    scores = get_scores()
    utilizate = input("Antre epsedo ou: ").strip()
    utilizate = utilizate.lower()
    
    jwe = True
    while jwe:
        joue_jeu(utilizate, scores)
        reponse = input("Vle ou rejwe? (O/N): ").strip().lower()
        if reponse != 'o':
            jwe = False

    print("Mèsi pou jwe Lawoulèt!")

if __name__ == "__main__":
    main()
