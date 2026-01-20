import marimo

# uv run --with marimo marimo edit

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Python

    Le python est une famille de reptile avec pas de pattes comprenant 10 espèces. Mais [Python](https://www.python.org/about/) est un langage de programmation lancé en 1991 par Guido van Rossum, un fan du groupe d'humoristes britanniques Mounty Python.

    Python est un langage dynamique, c'est-à-dire que le code peut être exécuté ligne par ligne ou bloc par bloc: un avantage majeur pour des activités qui nécessitent des interactions fréquentes. Python s'impose non seulement pour créer des applications, mais aussi comme outil de calcul scientifique.

    > La liberté, c’est la liberté de dire que deux et deux font quatre. Si cela est accordé, tout le reste suit. - George Orwell, 1984
    """
    )
    return


@app.cell
def _():
    2 + 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""`[x]` Test d'Orwell, check!""")
    return


@app.cell
def _():
    67.1 + 43.2
    return


@app.cell
def _():
    2 * 4
    return


@app.cell
def _():
    2**6  # deux exposant six
    return


@app.cell
def _():
    1 / 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Tout va bien pour l'instant. Remarquez que la dernière opération comporte des espaces entre les nombres et l'opérateur `/`. Dans ce cas (ce n'est pas toujours le cas), les espaces ne signifient rien - il est même suggéré de les placer pour éclaircir le code, ce qui est utile lorsque les équations sont complexes. Puis, après l'opération `2**6`, j'ai placé le symbole `#` suivi d'une note. Le symbole `#` est interprété par Python comme un ordre de ne pas considérer ce qui le suit. Cela est très utile pour insérer à même le code des commentaires pertinents pour mieux comprendre les opérations. Mais en programmation littéraire, il vaut mieux commenter dans des cellules de texte.

    Assigner des objets à des variables est fondamental en programmation. Par exemple.
    """
    )
    return


@app.cell
def _():
    a = 3
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Techniquement, `a` pointe vers le nombre entier `3`. Conséquemment, on peut effectuer des opérations sur `a`.""")
    return


@app.cell
def _(a):
    a * 6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Dans le cas particulier de l'interface Marimo, on ne peut réassigner une variable. J'ai mis le code en commentaire pour éviter d'affecter tout le carnet, mais voyez ce qui arrive si l'on enlève le `#`.""")
    return


@app.cell
def _():
    # a = 4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    À l'image d'Excel, les carnets de calcul Marimo sont réactifs, c'est-à-dire que changer une valeur dans une cellule met à jour le carnet entier. Ainsi, si on assigne une valeur à `a` à deux endroits, impossible de savoir laquelle doit supplanter l'autre. L'utilisation de barres de soulignement avant un nom de variable, par exemple `_a` ou `_b` permet de définir les variables locales, n'étant valide que dans la cellule où elles sont définies. Il est donc possible d'utiliser `_a` ou `_b` plusieurs fois, ce qui ne serait pas possible avec `a` ou `b`. L'utilisation de la barre de soulignement n'est pas nécessaire lorsqu'un code est exécuté de bas en haut, mais c'est une bonne pratique pour indiquer qu'il s'agit d'une variable temporaire.

    Le nom d'une variable doit toujours commencer par une lettre ou le symbole `_`, et ne doit pas contenir de caractères réservés (espaces, `+`, `*`, `.`). Par convention, les objets qui commencent par une lettre majuscules sont utilisés pour définir des classes (modules), utiles pour le développement de fonctionnalités avancées, mais rarement utilisés dans le cadre d'une feuille de calcul scientifique.
    """
    )
    return


@app.cell
def _():
    rendement_arbre = 50
    nombre_arbre = 300
    nombre_pomme = rendement_arbre * nombre_arbre
    nombre_pomme
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Types de données

    Jusqu'à maintenant, nous n'avons utilisé que des **nombres entiers** (*integer* ou `int`) et des **nombres réels** (*float* ou `float64`). Python inclut d'autres types. La **chaîne de caractère** (*string*) est un ou plusieurs symboles. Elle est définie entre des doubles guillemets `" "` ou des apostrophes `' '`. Il n'existe pas de standard sur l'utilisation de l'un ou de l'autre, mais en règle générale, on utilise les apostrophes pour les expressions courtes, contenant un simple mot ou séquence de lettres, et les guillemets pour les phrases. La raison est que les guillemets sont utiles pour insérer des apostrophes dans une chaîne de caractère, par exemple `"l'ours"` est valide, mais pas `'l'ours'`.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""L'opérateur `+` sur des caractères retourne une concaténation. La fonction `len()` peut calculer le nombre de caractères de la chaîne. Puisque Marimo n'affiche que le dernier élément d'une cellule, utilisons la fonction `print()` pour afficher plusieurs éléments.""")
    return


@app.cell
def _():
    _a = "L'ours"
    _b = "polaire"
    print(_a + " " + _b + " ressemble à un faux zèbre.")

    _c = _a + " " + _b
    print(len(_c))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Quatorze, c'est bien cela (comptez "L'ours polaire", en incluant l'espace). `len`, pour *lenght* (longueur), est une fonction incluse par défaut dans l'environnement de travail de Python. La fonction est appelée en écrivant `len()`. Mais une fonction de quoi? Des arguments qui se trouvent entre les parenthèses. Dans ce cas, il y a un seul argument: `_c`.

    En calcul scientifique, il est courant de lancer des requêtes testant si un résultat est vrai ou faux.
    """
    )
    return


@app.cell
def _():
    _a = 17
    print(_a < 10)
    print(_a > 10)
    print(_a == 10)
    print(_a != 10)
    print(_a == 17)
    print(~_a == 17)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Je viens d'introduire un nouveau type de donnée: les données booléennes (*boolean*, ou `bool`), qui ne peuvent prendre que deux états - `True` ou `False`. En même temps, j'ai utilisé la fonction `print` parce que dans mon carnet, seule la dernière opération permet d'afficher le résultat. Si l'on veut forcer une sortie, on utilise `print`. Puis, on a vu plus haut que le symbole `=` est réservé pour assigner des objets: pour les tests d'égalité, on utilise le double égal, `==`, ou `!=` pour la non-égalité. Enfin, pour inverser une donnée de type booléenne, on utilise le symbole `~`.

    Pour les tests sur les chaînes de caractères, on utilisera `in` et son inverse `not in`.
    """
    )
    return


@app.cell
def _():
    print("o" in "Ours")
    print("O" in "Ours")
    print("O" not in "Ours")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Les collections de données

    Les exercices précédents ont permis de présenter les types de données offerts par défaut sur Python qui sont les plus importants pour le calcul scientifique : `int` (*integer*, ou nombre entier), `float` (nombre réel), `str` (*string*, ou chaîne de caractère) et `bool` (booléen). D'autres s'ajouteront, comme les unités de temps (date-heure), les catégories et les géométries (points, linges, polygones) géoréférencées.

    Lorsque l'on procède à des opérations de calcul en science, nous utilisons rarement des valeurs uniques. Nous préférons les organiser et les traiter en collections. Par défaut, Python offre trois types importants : les **listes**, les **tuples** et les **dictionnaires**.

    D'abord, les **listes**, ou `list`, sont une série de variables sans restriction sur leur type. Elles peuvent même contenir d'autres listes. Une liste est délimitée par des crochets `[ ]`, et les éléments de la liste sont séparés par des virgules.
    """
    )
    return


@app.cell
def _():
    magie = ["Impero", "Protego", "Expecto Patronum", "Wingardium Leviosa"]
    magie
    return (magie,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Pour accéder aux éléments d'une liste, appelle la liste suivie de la position de l'objet désiré entre crochets. Fait important : en Python, l'indice du premier élément est zéro. Autre particularité de Marimo: le résultat s'affiche en haut de votre code. La raison: plutôt que l'inverse, on aime souvent mieux jeter un oeil aux résultats, puis investiguer la méthode. Mais les sorties en Python pur s'afficheront en-dessous, comme les résultats de `print()`. Ceci dit, si vous préférez que les résultats s'affichent sous la cellule, cliquez sur l'icône ⚙️ > User settings > Display et sélectionnez *below*.""")
    return


@app.cell
def _(magie):
    print(magie[0])
    print(magie[2])
    print(magie[:2])
    print(magie[2:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Pour les deux dernières commandes, la position `:2` signifie jusqu'à 2 non inclusivement et `2:` signifie de 2 à la fin.

    Pour ajouter un élément à notre liste, on peut utiliser la méthode `append`. À la différence d'une fonction, la méthode est une propriété d'un objet.
    """
    )
    return


@app.cell
def _(magie):
    magie.append("Endoloris")
    magie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Notez que la méthode `append` est appelée après la variable et précédée un point. Cette manière de procéder est courante en programmation orientée objet. La fonction `append` est un attribut d'un objet `list` et prend un seul argument : l'objet qui est ajouté à la liste. C'est une manière de dire `grenouille.saute(longueur=0.8, hauteur=0.3)`. En lançant `magie[2] = "Petrificus Totalus"`, on note qu'il est possible de changer un élément de la liste.""")
    return


@app.cell
def _(magie):
    print(magie)
    magie[2] = "Petrificus Totalus"
    print(magie)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Si les données contenues dans une liste sont de même type, cette liste peut être considérée comme un vecteur. En créant une liste de vecteurs de dimensions cohérentes, on crée une matrice. Nous verrons plus tard que pour les vecteurs et les matrices, on utilisera un format offert par un module complémentaire. Pour l'instant, on pourrait définir une matrice comme suit.""")
    return


@app.cell
def _():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    mat
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Les **tuples**, définis `tuple` par Python, différent des listes du fait que ses éléments ne peuvent pas être modifiés. Un tuple est délimité par des parenthèses `( )`, et comme chez la liste,  ses éléments sont séparés par des virgules. Les tuples sont moins polyvalents que les listes. Vous les utiliserez probablement rarement, et surtout comme arguments dans certaines fonctions en calcul scientifique, arguments qui souvent peuvent être définis en termes de listes.""")
    return


@app.cell
def _():
    magie_tuple = ("Impero", "Protego", "Expecto Patronum", "Wingardium Leviosa")
    magie_tuple[2] = "Expelliarmus"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Les **dictionnaires**, ou `dict`, sont des listes dont chaque élément est identifié par une clé. Un dictionnaire est délimité par des accolades sous forme `mon_dict = {'clé1': x, 'clé2': y, 'clé3': z }`. On appelle un élément par sa clé entre des crochets, par exemple `mon_dict['clé1']`.

    Le `dict` se rapproche d'un tableau: nous verrons plus tard que le format de tableau (offert dans un module complémentaire) est bâti à partir du format `dict`. Contrairement à un tableau dans lequel les colonnes contiennent toutes le même nombre de lignes, chaque élément du dictionnaire est indépendant des autres.
    """
    )
    return


@app.cell
def _():
    tableau = {
        "espece": [
            "Petromyzon marinus",
            "Lepisosteus osseus",
            "Amia calva",
            "Hiodon tergisus",
        ],
        "poids": [10, 13, 21, 4],
        "longueur": [35, 44, 50, 8],
    }
    print("Mon tableau: ", tableau)
    print("Mes espèces:", tableau["espece"])
    print("Noms des clés (ou colonnes):", tableau.keys())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Les fonctions

    Plus haut, j'ai présenté la fonction `len` et  la méthode `append`. Une myriade de fonctions est livrée par défaut avec Python. Mais il en manque aussi cruellement.
    """
    )
    return


@app.cell
def _(sqrt):
    sqrt(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Message d'erreur: la commande `sqrt` n'est pas définie. De nombreuses extensions (les *modules*) permettent de combler ces manques. Nous aborderons ça un peu plus loin dans ce chapitre. Pour l'instant, exerçons-nous à créer notre propre fonction de racine carrée.""")
    return


@app.function
def racine(x, n=2):
    r = x ** (1 / n)
    return r


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""En Python, `def` est le mot-clé pour définir une fonction. Suit ensuite, après un espace, le nom que vous désirez donner à la fonction: `racine`. Les arguments de la fonction suivent entre les parenthèses. Dans ce cas, `x` est la valeur de laquelle on veut extraire la racine et `n` est l'ordre de la racine. L'argument `x` n'a pas de valeur par défaut: elle doit être spécifiée pour que la fonction fonctionne. La mention `n=2` signifie que si la valeur de `n` n'est pas spécifiée, elle prendra la valeur de 2 (la racine carrée). Pour marquer la fin de la définition et le début de la suite d'instructions, on utilise les deux points `:`, puis un retour de ligne. Une indentation (ou retrait) de quatre barres d'espacement signifie que l'on se trouve à l'intérieur de la suite d'instructions, où l'on calcule une valeur de `r` comme l'exposant de l'inverse de l'ordre de la racine. La dernière ligne indique ce que la fonction doit retourner.""")
    return


@app.cell
def _():
    print(racine(9))
    print(racine(x=9))
    print(racine(8, 3))
    print(racine(x=8, n=3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    S'ils ne sont pas spécifiés, Python comprend que les arguments sont entrés dans l'ordre défini dans la fonction. En entrant `racine(9)`, Python comprend que le `9` est attribué à `x` et donne à `n` sa valeur par défaut, `2`. Ce qui est équivalent à entrer `racine(x=9)`. Les autres entrées sont aussi équivalentes, et extraient la racine cubique. S'il se peut qu'il y ait confusion entre les arguments nommés et ceux qui ne le sont pas, Python vous retournera un message d'erreur. Règle générale, il est préférable pour la lisibilité du code de nommer les arguments plutôt que de les spécifier dans l'ordre.

    Supposons maintenant que vous avez une liste de données dont vous voulez extraire la racine.
    """
    )
    return


@app.cell
def _():
    data = [3.5, 8.1, 10.2, 0.5, 5.6]
    return (data,)


@app.cell
def _(data):
    racine(x=data, n=2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Oups. Python vous dit qu'il y a une erreur, et, dans le *Traceback*, il vous indique à quelle ligne de notre fonction l'erreur est encourue. Les exposants `**` ne sont pas applicables aux listes. Une solution est d'appliquer la fonction à chaque élément de la liste avec une **itération**. On verra plus tard des manières plus efficaces de procéder. Je me sers de ce cas d'étude pour introduire les boucles itératives.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Les boucles

    Les boucles permettent d'effectuer une même suite d'opérations sur plusieurs objets. Pour faire suite à notre exemple:
    """
    )
    return


@app.cell
def _(data):
    racine_data = []
    for i in [0, 1, 2, 3, 4]:
        r = racine(x=data[i], n=2)
        racine_data.append(r)

    racine_data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Nous avons d'abord créé une liste vide, `racine_data`. Ensuite, pour (**`for`**) chaque indice de la liste (`i in [0, 1, 2, 3, 4]`), nous demandons à Python d'effectuer la suite d'opération qui suit le `:` et qui est indentée de quatre espaces. Dans la suite d'opération, calculer la racine carrée de `data` à l'indice `i`, puis l'ajouter à la liste `racine_data`. Au lieu d'entrer une liste `[0, 1, 2, 3, 4]`, on aurait pu utiliser la fonction `range` et lui assigner automatiquement la longueur de la liste. 

    On peut aussi lancer des boucles en une seule ligne.
    """
    )
    return


@app.cell
def _(data):
    racine_data_inline = [racine(x=d, n=2) for d in data]
    racine_data_inline
    return


@app.cell
def _(mo):
    mo.md(r"""La fonction `range` retourne une séquence calculée au besoin. Elle est calculée si elle est évoquée dans une boucle ou en lançant `list`.""")
    return


@app.cell
def _(data):
    print(range(len(data)))
    print(list(range(len(data))))
    print(range(2, len(data)))
    print(list(range(2, len(data))))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Première observation, si un seul argument est inclus, `range` retourne une séquence partant de zéro. Seconde observation, la séquence se termine en excluant l'argument. Ainsi, `range(2,5)` retourne la séquence [2, 3, 4]. En spécifiant la longueur de data comme argument, la séquence `range(5)` retourne la liste `[0, 1, 2, 3, 4]`, soit les indices dont nous avons besoin pour itérer dans la liste.

    Les boucles `for` vous permettront par exemple de générer en peu de temps 10, 100, 1000 graphiques (autant que vous voulez), chacun issu de simulations obtenues à partir de conditions initiales différentes, et de les enregistrer dans un répertoire sur votre ordinateur. Un travail qui pourrait prendre des semaines sur Excel peut être effectué en Python en quelques secondes. L'inconvénient de `for` est que vous n'utilisez qu'une seule file d'attente, l'itération suivante ne pouvant pas commencer avec que la précédente soit terminée. Des stratégies existent pour effectuer des calculs en *parallèle*, mais cela sort du contexte de cette formation.

    Un second outil est disponible pour les itérations : les boucles **`while`**. Elles effectuent une opération tant qu'un critère n'est pas atteint. Elles sont utiles pour les opérations dont on cherche une convergence. Je les couvre rapidement puisqu'elles sont rarement utilisées dans les flux de travail courants. En voici un petit exemple.
    """
    )
    return


@app.cell
def _():
    x = 100
    while x > 1.1:
        x = racine(x)
        print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Nous avons inité x à une valeur de 100. Puis, tant que (`while`) le test `x > 1.1` est vrai, attribuer à `x` la nouvelle valeur calculée en extrayant la racine de la valeur précédente de `x`. Enfin, indiquer la valeur avec `print`.

    Explorons maintenant comment Python réagit si on lui demande de calculer $\sqrt{-1}$.
    """
    )
    return


@app.cell
def _():
    racine(x=-1, n=2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    D'abord, Python ne retourne pas de message d'erreur, mais un nouveau type de donnée: le nombre imaginaire. Puis, `6.123233995736766e-17` n'est pas zéro, mais très proche. La résolution des calculs étant numérique, on obeserve parfois de légères déviations par rapport aux solutions mathématiques.

    Si pour un cas particulier, on veut éviter que notre fonction retourne un nombre imaginaire, comment s'y prendre? Avec une **condition**.

    ## Conditions: `if`, `elif`, `else`

    > Si la condition 1 est remplie, effectuer une suite d'instruction 1. Si la condition 1 n'est pas remplie, et si la condition 2 est remplie, effectuer la suite d'instruction 2. Sinon, effectuer la suite d'instruction 3.

    Voilà comment on exprime une suite de conditions. Pour notre racine d'un nombre négatif, on pourrait procéder comme suit.
    """
    )
    return


@app.function
def racine_positive_nn(x, n=2):
    if x < 0:
        raise ValueError("x est négatif")
    elif x == 0:
        raise ValueError("x est nul")
    else:
        r = x ** (1 / n)
        return r


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""La racine positive et non-nulle (`racine_positive_nn`) comprend les mots-clés `if` (si), `elif` (une contraction de *else if*) et `else` (sinon). `ValueError` est une fonction pour retourner un message d'erreur lorsqu'elle est précédée de `raise`. Comme c'est le cas pour `def` et `for`, les instructions des conditions sont indentées. Notez la double indentation (8 espaces) pour les instructions des conditions. Alors que la plupart des langages de programmation demandent d'emboîter les instructions dans des parenthèses, accolades et crochets, Python préfère nous forcer à bien indenter le code (ce que l'on devrait faire de toute manière pour améliorer la lisibilité) et s'y fier pour effectuer ses opérations.""")
    return


@app.cell
def _():
    racine_positive_nn(x=-1, n=2)
    return


@app.cell
def _():
    racine_positive_nn(x=0, n=2)
    return


@app.cell
def _():
    racine_positive_nn(x=4, n=2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Charger un module

    Le module *Numpy* est une boîte d'outil de calcul numérique incluant par de nombreuses fonctions mathématiques. Un message d'erreur apparaîtra s'il n'est pas installé. Nous verrons plus tard comment gérer Python en local, mais dans un environnement web, pour l'installer, vous pouvez passer par le symbole de cube (*Manage packages*) dans la barre verticale de *Marimo*.

    <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 256 256"><path fill="currentColor" d="m223.68 66.15l-88-48.15a15.88 15.88 0 0 0-15.36 0l-88 48.17a16 16 0 0 0-8.32 14v95.64a16 16 0 0 0 8.32 14l88 48.17a15.88 15.88 0 0 0 15.36 0l88-48.17a16 16 0 0 0 8.32-14V80.18a16 16 0 0 0-8.32-14.03M128 32l80.34 44L128 120L47.66 76ZM40 90l80 43.78v85.79l-80-43.75Zm96 129.57v-85.75L216 90v85.78Z"/></svg>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Un module installé n'est pas nécessairement chargé dans une session de travail. Il existe deux manières de charger un module, la première, en chargeant le module directement ou avec un alias (raccourci), la deuxième, en important directement un sous-module ou une fonction.

    Méthode `import`:

    ```
    import module
    module.fontion()

    import module as mod
    mod.fonction()
    ```

    Méthode `from`:

    ```
    from module import fonction
    fonction()
    ```

    En général, l'importation est effectuée en haut de code. Mais étant donné que *Marimo* se charge de l'ordre d'exécution des cellules, on pourra les placer à la fin si l'on juge par exemple qu'ils encombrent la lecture des calculs. Par exemple, dans un carnet *Marimo*, il est d'usage d'importer `marimo` avec l'alias `mo`.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""La plupart des fonctions que vous aurez à construire seront vouées à des instructions spécialisées à votre cas d'étude. Pour la plupart des opérations d'ordre général (comme les racines carrées, les tests statistiques, la gestion de matrices et de tableau, les graphiques, les modèles d'apprentissage, etc.), des équipes ont déjà développé des fonctions nécessaires à leur utilisation, et les ont laissées disponibles au grand public, en mode ouvert. Comme une langue, on n'apprend à s'exprimer en un langage informatique qu'en se mettant à l'épreuve, ce que vous ferez tout au long de cette formation.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## La programmation orientée objet

    Même si Python est un langage de programmation orienté objet, en calcul scientifique, nous utilisons les objets sans avoir nécessairement besoin d'en programmer de nouveaux. Un objet est un outil informatique que l'on *instancie* pour effectuer des tâches. Nous l'avons fait dans ce carnet en instanciant `numpy` avec l'alias `np`, qui devient l'objet `numpy` avec la nomination `np` dans notre session.

    L'image suivante décrit une classe comme le plan d'un robot, l'instanciation comme sa construction selon des spécifications, les méthodes comme des commandes à actionner et les attributs comme les particularités de l'instance.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("images/poo.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Concrètement, par exemple en utilisant le package StatsModels pour l'analyse statistique, on retrouvera cette même structure.

    ```python
    import numpy as np
    import statsmodels.api as sm

    # Création des données
    X = np.random.rand(100, 3)
    X = sm.add_constant(X)
    y = 2 + 3*X[:, 1] - 2*X[:, 2] + 1*X[:, 3] + np.random.normal(0, 1, 100)

    # Instanciation d'un objet de la classe OLS
    model = sm.OLS(y, X)  # Création d'un objet modèle

    # Appel de la méthode fit() qui encapsule un nouvel objet (ResultsWrapper) dans results
    results = model.fit()  

    # Utilisation des méthodes et attributs de l'objet results
    print(results.params)  # Attribut contenant les coefficients
    print(results.rsquared)  # Attribut R²
    print(results.pvalues)  # Attribut des p-values

    # Appel de la méthode predict() sur l'objet results
    predictions = results.predict(X)  

    # Appel d'une méthode qui génère un rapport texte complexe
    print(results.summary())
    ```

    Si votre besoin est de créer une procédure à appliquer à plusieurs cas, il vaut probablement mieux créer une fonction. Si toutefois vous programmez un package qui a besoin de définir plusieurs robots, les classes, qui peuvent être instanciées en plusieurs objets, seront utiles. Je n'ai commencé à utiliser les classes que lorsque j'ai commencé à créer des packages en Python. Et même dans ce cas, les classes ne sont souvent pas d'absolue nécessitée. Ma recommandation est de laisser les classes pour l'utilisation avancée.
    """
    )
    return


if __name__ == "__main__":
    app.run()
