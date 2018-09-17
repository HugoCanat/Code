import time


class Person:

               def __init__(self, name='ezf', surname='hij', age=36, city='Paris'):
                              self.name = name
                              self.surname = surname
                              self.age = age
                              self._city = city
               def __str__(self):
                              return "{}, {}, {}, {}".format(self.name, \
                              self.surname, self.age, self.city)

               def __getattr__(self, name):
                              print("Warning ! The attribute '{}' doesn't exist".format(name))
               def __setattr__(self, nom_attr, val_attr):
                              object.__setattr__(self, nom_attr, val_attr)
               def __delattr__(self, name):
                              print("Warning! You can't delete '{}'".format(name))

               def _get_City(self):
                              return "access to city: {}".format(self._city)
               def _set_City(self, NewValue):
                              print("City is changing for: {}".format(NewValue))
                              self._city = NewValue
               city = property(_get_City, _set_City)

class Dict:
               def __init__(self):
                              self._dictionnaire = {}
               def __getitem__(self, index):
                              print("getting the item at the index number: " + str(index))
                              return self._dictionnaire[index]
               def __setitem__(self, index, value):
                              print("setting item '"+str(value)+"' at the index number: "+str(index))
                              self._dictionnaire[index] = value
               def __contains__(self, Object):
                              if Object in self._dictionnaire:
                                             return True
                              else:
                                             return False
               def __len__(self):
                              print("the len is: ")
                              return len(self._dictionnaire)

               def __getattr__(self, name):
                              print("The attibute '{}' doesn't exist".format(name))

class Duree:
               def __init__(self, min=1, sec=0):
                              self.min = min
                              self.sec = sec
               def __str__(self):
                              return "{0:02}:{1:02}".format(self.min, self.sec)

               def __add__(self, val):
                              print('add')
                              self.sec +=val
                              if self.sec >= 60:
                                             self.min += self.sec // 60
                                             self.sec = self.sec % 60
                              return self
               def __radd__(self, obj):
                              print("radd")
                              return self + obj
               def __iadd__(self, val):
                              print('iadd')
                              return self + val
               
               def __sub__(self, val):
                              print('sub')
                              
                              self.sec -= val
                              if self.sec < 0:
                                             self.min += self.sec //60
                                             self.sec = self.sec % 60
                              return self

               def __eq__(self, obj):
                              return self.min == obj.min and self.sec == obj.sec
               def __ne__(self, obj):
                              return self.min == obj.min and self.sec == obj.sec
               def __gt__(self, obj):
                              AS = (self.min * 60) + self.sec
                              OS = (obj.min * 60) + obj.sec
                              return AS > OS
               def __lt__(self, obj):
                              AS = (self.min * 60 ) + self.sec
                              OS = (obj.min * 60 ) + obj.sec
                              return AS < OS
               def __ge__(self, obj):
                              return self == obj or self > obj
               def __le__(self, obj):
                              return self == obj or self < obj
                              
class Temp:
               def __init__(self):
                              self.attr_1 = 2
                              self.attr_2 = 1
                              self.tempo = 5

               def __getstate__(self):
                              """renvoie le dictionnaire d'attributs a sérialiser"""
                              dict_attr = dict(self.__dict__)
                              dict_attr['tempo'] = 0
                              return dict_attr

#Création d'une classe similaire au fonctionnement de for mais dans\
#le sens inverse
class RevStr():
               def __init__(self, chaine_a_parcourir):
                              self.chaine_a_parcourir = chaine_a_parcourir
                              self.position = len(chaine_a_parcourir)
                                                  
               def __iter__(self):
                              return self

               def __next__(self):
                              if self.position == 0: # Fin du parcours
                                             raise StopIteration
                              self.position -= 1
                              return self.chaine_a_parcourir[self.position]
                              
                              

def generateur(min, max):
               """Premier générateur, il renvoit les nombres situer
entre min et max"""
               if min < max:
                              min += 1
                              while min < max:
                                             value = (yield min)
                                             if value is not None:
                                                            min = value          
                                             min += 1
               else:
                              min -= 1
                              while min > max:
                                             value = (yield min)
                                             if value is not None:
                                                            min = value
                                             min -= 1


###  Décorateur  ###
def mon_decorateur(fonction):
               """Notre décorateur : il va afficher un message avant l'appel
               de la fonction définie"""

               def fonctionModifiee():
                              """Fonction que l'on va renvoyer. Il s'agit en fait d'une
                              version un peu modifiée de notre fonction originellement définie.
                              On se contente d'afficher un avertissement avant d'exécuter notre
                              fonction originellement définie"""
                              
                              print("Attention ! On appelle {0}".format(fonction))
                              return fonction()

               return fonctionModifiee


@mon_decorateur
def salut():
               print("Salut!")

##Décorateur avec arguments ## pour controler le temps par exemple
            
def timeControler(sec):
      """Contrôle le temps mis par une fonction pour s'exécuter.
      Si le temps d'exécution est supérieur à nb_secs, on affiche une
      alerte"""
      
      def decorateur(fonct):
            """Notre décorateur. C'est lui qui est appelé directement
            LORS DE LA DEFINITION de notre fonction (fonction_a_executer)"""
            
            def fonctModi(*params, **Unommedparams):
                  """Fonction envoyée par notre décorateur elle se charage de calculer
                  le temps de son execution."""
                  TB = time.time()
                  vr = fonct(*params, **Unommedparams)
                  TA = time.time() - TB
                  if TA > sec:
                        print('Temps supérieur au maximum autorisé')
                  print("La fonction a mise {0} a s'executer".format(TA))
                  return vr
            return fonctModi
      return decorateur


#Decorateur pourn n'avoir qu'une seule instance de fonction/classe
def singleton(classe_definie):      
      instances = {} # Dictionnaire de nos instances singletons
      def get_instance():
            if classe_definie not in instances:
                  # On crée notre premier objet de classe_definie
                  instances[classe_definie] = classe_definie()
            return instances[classe_definie]
      return get_instance



#Controleur de types
"""Fonction chargée de controler le type des variables mises en paramètres d'une fonction."""
"""Peut être améliorée en permettant de controler un nombre indéfini de parametres et de types"""
def type_Control(type1, type2):
      def decorateur(fonct):
            def check(v1):
                  print(type(v1))
                  if type(v1) != type1 and type(v1) != type2:
                        raise TypeError
                  return fonct(v1)
            return check
      return decorateur


@timeControler(2)
@type_Control(int, str)
def TestFonct(string):
      c = input(string)

#Metaclasses


#Regular expression et module re
"""
Expression Régulière:

      Début ou fin de chaine:
            '^' + expression, pour chercher dans le debut d'une chaine
            ou
            expresion + '$', pour chercher dans la fin d'une chaine

            exemple:
                    ^chat   -> chaton
                    tte$    -> baguette

      Nombre d'occurence:
            caratères + '*', signifie que le caractères pour se trouver 0,1
            ou plusieurs fois dans la chaine

            | * | 0 ou plusieurs fois |
            | + | 1 ou plus           |
            | ? | 0 ou 1              |

            On peut également contrôler le nombre d'occurence avec:
            E{2}    signifie 2 fois la lettre E
            E{3,5}  signifie entre 3 et 5 fois la lettre E
            E{,8}   signifie entre 0 et 8 fois
            E{8,}   signifie 8 fois minimum
            et même avec des groupes de caractères
            (chat){5}

            exemple:
                 chat*    -> chatttt
                 c*       -> accueil
                 c{1}hat  -> chat

      Classe de caractères:
           [caractèreS]
           ou
           [caractère - caractère] pour choisir une gamme de caractère

           exemple:
               [abcd]
               [A-Z]
               [0-9]
               [a-z]{2}
               [A-Za-z0-9]
               
            
"""

import re
""" pour tester si l'utilisateur entre un numero de telephone correct"""
def TestNumTel():
      expression = r'^0[0-9]([ .-]?[0-9]{2}){4}$'
      num = ""
      while re.search(expression, num) is None:
            num = input('Saisissez vôtre numero de téléphone: ')

# CHAPITRE TEMPS #
import time
def TellTime():
      localtime = time.localtime()
      y = str(localtime[0])
      m = str(localtime[1])
      d = str(localtime[2])
      h = str(localtime[3])
      mi = str(localtime[4])
      s = str(localtime[5])
      print(d+'/'+m+'/'+y+'  '+h+':'+mi+"'"+s)

      ts_te = time.mktime(localtime)
      print(ts_te)

def telltime2():
      print(time.strftime('%A %d %B %Y %H:%M:%S'))

def Pause(temps=3.5):
      time.sleep(temps)
               
# PROGRAMMATION SYSTEME #
import sys
def syst():
      sys.stdin   # entrée standard
      sys.stdout  # sortie standard
      sys.stderr  # erreur standard

def Write(msg='Hello world'):
      std = sys.__stdout__
      
      fichier = open('fichier.txt', 'w')
      sys.stdout = fichier
      print(msg)
      fichier.close()
      sys.stdout = std


      

                              
#Reseau 
import socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creation serveur, va attendre des connexions clients
connexion_principale.bind(('', 1800))
#'' pour le nom de l'hôte, et 1800 pour le port utilisé
#Maintenant le socket 'connection_principale' est pres a écouter sur le port 1800

connexion_principale.listen(5)
#5 est le nombre maximum de connexions que le socket peut recevoir 
#sans les accepter
"""Si 5 client se connectent sur le serveur eet que celui n'accepte aucune 
connections, plus aucun client pourra se connecter"""

"""accepter une connection"""
connexion_avec_client, infos_connexion = connexion_principale.accept()
"""La methode accept() renvoit un socket avec la connection client et
les infos de connections (Ip, port), et stop le programme en attente
de connexions"""

"""Creation du socket client"""
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""connection au serveur"""
connexion_avec_serveur.connect(('localhost', 1800))
#1800 car les deux applis sont sur la meme machine, et localhost pour machine locale

"""faire communiquer les sockets"""
connexion_avec_client.send(b"Je viens d'accepter la connexion.")
msg_recu = connexion_avec_serveur.recv(1024)
#1024 pour la taille du message
print(msg_recu)

"""fermer la connexion"""
connexion_avec_client.close()
connexion_avec_serveur.close()

#Code serveur 
"""
import socket
import select
hote = ''
port = 12800


connexion_principale = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))


serveur_lance = True
clients_connectes = []

while serveur_lance:

   # On va vérifier que de nouveaux clients ne demandent pas à se connecter
   # Pour cela, on écoute la connexion_principale en lecture
   # On attend maximum 50ms
   connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
   
   for connexion in connexions_demandees:
      connexion_avec_client, infos_connexion = connexion.accept()
      # On ajoute le socket connecté à la liste des clients
      clients_connectes.append(connexion_avec_client)
   
   # Maintenant, on écoute la liste des clients connectés
   # Les clients renvoyés par select sont ceux devant être lus (recv)
   # On attend là encore 50ms maximum
   # On enferme l'appel à select.select dans un bloc try
   # En effet, si la liste de clients connectés est vide, uneexception
   # Peut être levée
   clients_a_lire = []
   try:
      clients_a_lire, wlist, xlist = select.select(clients_connectes,[], [], 0.05)
   except select.error:
      pass
   else:
   # On parcourt la liste des clients à lire
      for i, client in enumerate(clients_a_lire):
      # Client est de type socket
         msg_recu = client.recv(1024)
      # Peut planter si le message contient des caractères spéciaux
         msg_recu = msg_recu.decode()
         print("> {}".format(msg_recu))
         client.send(b"5 / 5")
         if msg_recu == "fin":
            del clients_a_lire[i]
            client.close()


print("Fermeture des connexions")
for client in clients_connectes:
   client.close()
connexion_principale.close()
"""