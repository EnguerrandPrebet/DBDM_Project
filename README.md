# DBDM_Project

4.1)
Nous avons principalement utiliser des structures de python, modifiés légèrement si cela était nécessaire.

Nous avons choisis de représenter les attributs par des chaines de caractères. Il n'était pas nécessaire d'avoir une structure plus précise, nous pouvons appeler comme nous le désirons les attributs. 

Les ensembles d'attributs sont simplement un set, cette structure de donnée ayant toute les méthodes nécessaires. Il n'y a pas de vérification sur les éléments inclus dedans: implémentation dans l'esprit python. Nous avons modifiés la fonction d'affichage afin d'avoir un affichage qui nous convenait plus. Enfin nous avons repréciser la copie afin que la copie soit églament un set d'attributs. 

Les ensembles d'ensembles d'attributs sont directement des sets. Il n'y avait pas besoin de modification particulière.

Pour les dépendances fonctionnelles (FD), nous avons défini une nouvelle classe qui contient simplement deux ensembles d'attributs: prérequis et conclusion. Nous avons précisé l'affichage mais également défini une fonction de hash, en utilisant celle de python, afin de pouvoir créer un dictionnaire de FD (le count). 

Les ensembles de FD sont simplement des sets.


4.2)
Pour le choose A nous avons simplement utilisé la méthode de pop. Le choix de A n'est donc pas aléatoire mais ne suit aucune contrainte particulière.


4.3)
Dans le cas où un prérequis est vide, l'algorithme ne donne pas le résultat attendu (test left_blank). En effet la conclusion d'un prérequis vide devrait être obtenue systématiquement hors ce n'est pas le cas. 


6.2)
Tout les tests ont été réalisés sur le même ordinateur (ordinateur personnel) à la suite.


6.3)
Les performances de l'algorithme 2 sont largement supérieures. De plus la complexité semble linéaire et non quadratique. 




