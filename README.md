# DBDM_Project

4.1)
Nous avons principalement utiliser des structures de python, modifi�s l�g�rement si cela �tait n�cessaire.

Nous avons choisis de repr�senter les attributs par des chaines de caract�res. Il n'�tait pas n�cessaire d'avoir une structure plus pr�cise, nous pouvons appeler comme nous le d�sirons les attributs. 

Les ensembles d'attributs sont simplement un set, cette structure de donn�e ayant toute les m�thodes n�cessaires. Il n'y a pas de v�rification sur les �l�ments inclus dedans: impl�mentation dans l'esprit python. Nous avons modifi�s la fonction d'affichage afin d'avoir un affichage qui nous convenait plus. Enfin nous avons repr�ciser la copie afin que la copie soit �glament un set d'attributs. 

Les ensembles d'ensembles d'attributs sont directement des sets. Il n'y avait pas besoin de modification particuli�re.

Pour les d�pendances fonctionnelles (FD), nous avons d�fini une nouvelle classe qui contient simplement deux ensembles d'attributs: pr�requis et conclusion. Nous avons pr�cis� l'affichage mais �galement d�fini une fonction de hash, en utilisant celle de python, afin de pouvoir cr�er un dictionnaire de FD (le count). 

Les ensembles de FD sont simplement des sets.


4.2)
Pour le choose A nous avons simplement utilis� la m�thode de pop. Le choix de A n'est donc pas al�atoire mais ne suit aucune contrainte particuli�re.


4.3)
Dans le cas o� un pr�requis est vide, l'algorithme ne donne pas le r�sultat attendu (test left_blank). En effet la conclusion d'un pr�requis vide devrait �tre obtenue syst�matiquement hors ce n'est pas le cas. 


6.2)
Tout les tests ont �t� r�alis�s sur le m�me ordinateur (ordinateur personnel) � la suite.


6.3)
Les performances de l'algorithme 2 sont largement sup�rieures. De plus la complexit� semble lin�aire et non quadratique. 




