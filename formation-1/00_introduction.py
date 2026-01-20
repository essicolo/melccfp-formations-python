import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    # Introduction

    Excel est utile pour consigner de petits ensembles de données, effectuer des analyses de base et générer des graphiques simples. Mais avec Excel, la probabilité de commettre des erreurs grandit rapidement avec la complexité des calculs. Les procédures de vérification demandent souvent que les calculs soient audités par des tiers pour s'assurer de leur exactitude. Or, Excel a aussi le défaut d'être difficile à auditer.

    Tout cela peut être heureusement corrigé par des langages de programmation, dont l'utilisation s'est démocratisée avec les outils de calcul en ligne, qui ont néanmoins le désavantage d'une offre gratuite restreinte, et nécessite le déplacement de données parfois conventionnées vers des serveurs privés, ne serait-ce que dans la mémoire vive. Nous favoriserons ici le langage Python et les outils de calcul locaux.

    Ce document est un carnet de calcul (notebook) qui comprend des cellules de texte et des cellules de code. Les cellules de texte sont écrites en format Markdown, une manière [très simple](https://www.markdownguide.org/cheat-sheet/) d'écrire avec une mise en forme de base. Pour la partie code, c'est un peu comme dans Excel, sauf que des noms de variable remplacent les noms des cellules.
    """
    )
    return


@app.cell
def _():
    _a = 2
    _b = 4
    _a + _b
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""En Python, on peut créer des listes de nombres, de caractères, de n'importe quoi, en utilisant des crochets.""")
    return


@app.cell
def _():
    _a = [1, 2, 3]
    _a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Les noms des variables doivent commencer par une lettre ou la barre de soulignement, ne pas contenir de caractères spéciaux et... évitons autant que possible d'utiliser des termes réservés, comme `True` ou `for`. Le nom de mes variables débute jusqu'ici par une barre de soulignement: une manière de faire en sorte que la variable n'est valide que dans sa cellule. Comme Excel, ce carnet de calcul est réactif: si je défini une variable `a` deux fois, le calculateur ne saura plus laquelle est la bonne. Si vous commettez cette bévue, n'ayez crainte, Python vous demandera de corriger la situation avec un courtois message d'erreur.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Les messages d'erreur

    Les messages d'erreur sont inévitables, même pour les pros. Ce qui fait la différence entre novices et experts, c'est que les experts savent rapidement comment régler un problème, et ça inclut la capacité à comprendre les messages d'erreur et à corriger la situation. Disons que vous voulez ajouter 1 à chaque élément de la liste.
    """
    )
    return


@app.cell
def _():
    a = [1, 2, 3]
    a + 1
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    > Truc de pro, ayez toujours tout proche un onglet avec un moteur de recherche ou un assistant IA pour en savoir plsu sur vos messages d'erreur.

    La variable `a` étant une liste, Python s'attend à ce qu'on ajoute une liste à une liste.
    """
    )
    return


@app.cell
def _(a):
    a + [1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    Le bogue le plus insidieux est celui effectue la mauvaise opération sans générer d'erreur. Rappelez-vous que Python est un langage de programmation générique: il ne sait pas que vous voulez effectuer une opération mathématique.

    ## L'écosystème Python

    On pourrait effectuer une boucle et ajouter 1 à chaque élément de la liste (les boucles sont expliquées dans le carnet `01_python.py`), mais lorsque vient le temps d'effectuer des opérations mathématiques, nous pouvons jeter un oeil à l'écosystème de Python. Pour ajouter de nouvelles capacités à Python, nous devons importer des modules (aussi appelés librairies ou bibliothèques, et packages en anglais). C'est de ses modules que Python gagne ses super-pouvoirs. Pour les calculs sur des matrices et les opérations de mathématiques, nous avons besoin du module *Numpy*, que nous importons avec l'alias de notre choix: par convention, nous prenons `np`, puis nous spécifions que `a` est un vecteur, sur lequel nous effectuerons notre opération sans problème.
    """
    )
    return


@app.cell
def _(a):
    import numpy as np

    np.array(a) + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## À propos de cette formation

    Cette formation vise à introduire Python et son écosystème aux professionnels œuvrant dans les domaines de l'hydrologie et de la géomatique. Elle couvre quelques aspects généraux, et vous guidera vers des utilisations plus spécialisées.

    1. Bases en programmation Python
    2. Manipulation des matrices et des tableaux
    3. Visualisations
    4. Installer Python localement
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
