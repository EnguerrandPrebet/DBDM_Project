# DBDM_Project

4.1)
Nous avons principalement utiliser des structures de python, modifi�s l�g�rement si cel �tait n�cessaire.

Nous avons choisis de repr�senter les attributs par des chaines de caract�res. Il n'�tait pas n�cessaire d'avoir une structure plus pr�cise, nous pouvons appeller comme nous le d�sirons les attributs. 

Les ensembles d'attributs sont simplement un set, cette structure de donn�e ayant toute les m�thode n�cessaire. Il n'y pas de v�rification sur les �l�ments inclus dedans: impl�mentation dans l'esprit python. Nous avons modifi�s la fonction d'affichage afin d'avoir un affichage qui nous convenait plus. Enfin nous avons repr�ciser la copie afin que la copie soit �glament un set d'attribut. 

Les ensembles d'ensemble d'attributs sont directement des sets. Il n'y avait pas besoin de modification particuli�re.

Pour les d�pendances fonctionnel (FD), nous avons d�finis une nouvelle classe qui contient simplement deux ensemble d'attributs: pr�r�quis et conclusion. Nous avons pr�ciser l'affichage mais �galement d�finit une fonction de hash, en utilisant celle de python, afin de pouvoir  cr�er un dictionnaire de FD (le count). 

Les ensembles de FD sont simplement des sets.


4.2)
Pour le choose A nous avons simplement utiliser la m�thode de pop. Le choix de A n'est donc pas al�atoire mais ne suit aucune contrainte particuli�re.


4.3)
Dans le cas ou un pr�r�quis est vide, l'algorithme ne donne pas le r�sultat attendu (test ?). En effet la conclusion d'un pr�r�quis vide devrait �tre obtenue syst�matiquement hors ce n'est pas le cas. 


6.2)
Tout les test ont �tait r�alis�s sur le m�me ordinateur (ordinateur personnel) � la suite.


6.3)
Les performances de l'algorithme 2 sont largement sup�rieur. De plus la complexit� semble lin�aire et non quadratique. 




