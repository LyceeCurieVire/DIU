#!/usr/bin/python3

import sqlite3

def afficher_menu():
    print('1.Ajouter une région')
    print("2.Ajout d'un département")
    print("3.Ajout d'une ville")
    print('4.Affichage de la liste des régions')
    print('5.Affichage de la liste des départements')
    print('6.Afficher la liste des villes d''une région donnée')
    print('7.Affichage de la liste des villes')
    print('8.Suppression d''une ville')
    print('9.Suppression d''un départment')

def lire_action():
    reponse=0
    while reponse not in range(1,10):
        afficher_menu()
        reponseTexte=input("Votre choix :")
        reponse=int(reponseTexte)
    return(reponse)

def action_ajouter_region():
    nom_region=input("Nom de la nouvelle région : ")
    curseurId=connexion.execute('SELECT max(idRegion) FROM Region')
    tupleId=curseurId.__next__()
    idMax=int(tupleId[0])
    nouvel_id=idMax+1
    connexion.execute('INSERT INTO Region (idRegion,Nom) VALUES (?,?)',(nouvel_id,nom_region))
    connexion.commit()

def action_ajouter_departement():
    nom_departement=input("Nom du nouveau département : ")
    numero=int(input("Code département : "))
    pref=input("Nom de la préfecture : ")
    prefCP=int(input("Code postal prfecture : "))
    regio=input("Région du département : ")
    connexion.execute('INSERT INTO Departement (Nom,Numero,Prefecture,PrefectureCP,Region) VALUES (?,?,?,?,?)',(nom_departement,numero,pref,prefCP,regio))
    connexion.commit()

def action_ajouter_ville():
    nom_ville=input("Nom de la nouvelle ville : ")
    cp=int(input('Code postal :'))
    popu=int(input('Population : '))
    dpt=int(input('Numéro du département : '))
    connexion.execute('INSERT INTO Villes (Nom,CP,Population,Dpt) VALUES (?,?,?,?)',(nom_ville,cp,popu,dpt))
    connexion.commit()

def action_affichage_regions():
    curseur=connexion.execute('SELECT Nom FROM Region ORDER BY Nom')
    for tuple in curseur:
        print(tuple[0])

def action_affichage_departements():
    curseur=connexion.execute('SELECT Nom FROM Departement')
    for tuple in curseur:
        print(tuple[0])

def action_affichage_villes_region():
    nom_region=input("Nom de la région : ")
    curseur=connexion.execute(f'SELECT Nom FROM Villes WHERE Dpt IN (SELECT Numero FROM Departement WHERE Region = "{nom_region}")')
    #curseur=connexion.execute('SELECT * From Villes WHERE Dpt IN(SELECT Numero From Departement WHERE Region="'+str(nom_region)+'")')
    for tuple in curseur:
        print(tuple[0])

def action_affichage_villes():
    curseur=connexion.execute('SELECT * FROM Villes ORDER BY Nom')
    for tuple in curseur:
        print(tuple[0])


def action_suppression_ville():
    v=input('Ville à supprimer : ')
    connexion.execute('DELETE FROM Villes WHERE Nom = "'+v+'"')
    connexion.commit()

def action_suppression_departement():
    d=input('Département à supprimer : ')
    connexion.execute('DELETE FROM Departement WHERE Nom = "?"',d)
    connexion.commit()

table_actions=[None,action_ajouter_region,action_ajouter_departement,action_ajouter_ville,action_affichage_regions,
               action_affichage_departements,action_affichage_villes_region,action_affichage_villes,
               action_suppression_ville,action_suppression_departement]

def appli():
    termine=False
    while not termine:
        action=lire_action()
        if action==0:
            termine=True
        else:
            table_actions[action]()

connexion=sqlite3.connect('collectivites.db')
connexion.execute('PRAGMA foreign_keys=ON')
appli()
connexion.close()
