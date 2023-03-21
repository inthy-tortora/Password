import re
import hashlib
import json

def mdp_valide(mdp):
    if len(mdp) < 8:
        return False
    if not re.search("[a-z]", mdp):
        return False
    if not re.search("[A-Z]", mdp):
        return False
    if not re.search("[0-9]", mdp):
        return False
    if not re.search("[!@#$%^&*]", mdp):
        return False
    return True


def mdp_crypter(mdp):
    mdp_a_crypter = mdp.encode()
    hachage = hashlib.sha256(mdp_a_crypter)
    mdp_digest = hachage.hexdigest()
    return mdp_digest


def mdp_identique(mdp_digest, mdp_liste):
    for x in mdp_liste:
        if mdp_digest == x["Mot_de_passe_crypte"]:
            return True
    return False


while True:
    mdp = input("Entrer un mot de passe valide: ")
    if mdp_valide(mdp):
        mdp_crypter_final = mdp_crypter(mdp)
        with open("mdp.txt", "r") as file:
            mdp_liste = [json.loads(line) for line in file.readlines()]
        if mdp_identique(mdp_crypter_final, mdp_liste):
            print("Le mot de passe existe déjà. Veuillez entrer un nouveau mot de passe.")
        else:
            print("Le mot de passe est valide.")
            print("Mot de passe crypté:", mdp_crypter_final)
            with open("mdp.txt", "a") as file:
                file.write(json.dumps({"Mot_de_passe": mdp, "Mot_de_passe_crypte": mdp_crypter_final}) + "\n")
            break
    else:
        print("Le mot de passe n'est pas valide. Veuillez entrer un mot de passe valide.")

with open("mdp.txt", "r") as file:
    mdps = [json.loads(line) for line in file.readlines()]
    print(mdps)