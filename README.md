# DBDM_Project

4.1)
Nous avons principalement utiliser des structures de python, modifiés légérement si cel était nécessaire.

Nous avons choisis de représenter les attributs par des chaines de caractéres. Il n'était pas nécessaire d'avoir une structure plus précise, nous pouvons appeller comme nous le désirons les attributs. 

Les ensembles d'attributs sont simplement un set, cette structure de donnée ayant toute les méthode nécessaire. Il n'y pas de vérification sur les éléments inclus dedans: implémentation dans l'esprit python. Nous avons modifiés la fonction d'affichage afin d'avoir un affichage qui nous convenait plus. Enfin nous avons repréciser la copie afin que la copie soit églament un set d'attribut. 

Les ensembles d'ensemble d'attributs sont directement des sets. Il n'y avait pas besoin de modification particuliére.

Pour les dépendances fonctionnel (FD), nous avons définis une nouvelle classe qui contient simplement deux ensemble d'attributs: préréquis et conclusion. Nous avons préciser l'affichage mais également définit une fonction de hash, en utilisant celle de python, afin de pouvoir  créer un dictionnaire de FD (le count). 

Les ensembles de FD sont simplement des sets.


4.2)
Pour le choose A nous avons simplement utiliser la méthode de pop. Le choix de A n'est donc pas aléatoire mais ne suit aucune contrainte particuliére.


4.3)
Dans le cas ou un préréquis est vide, l'algorithme ne donne pas le résultat attendu (test ?). En effet la conclusion d'un préréquis vide devrait être obtenue systématiquement hors ce n'est pas le cas. 


6.2)
Tout les test ont était réalisés sur le même ordinateur (ordinateur personnel) à la suite.


6.3)
Les performances de l'algorithme 2 sont largement supérieur. De plus la complexité semble linéaire et non quadratique. 




