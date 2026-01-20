import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    # 2. Données

    > **Dicton**. Proportions de temps voué aux calcul scientifique: 80% de nettoyage de données mal organisées, 20% de calcul.

    Une donnée est une valeur associée à une variable. Une variable peut être une dimension, une date, une couleur, le résultat d'un test statistique, à laquelle on attribue la valeur quantitative ou qualitative d'un chiffre, d'une chaîne de caractère, d'un symbole conventionné, etc.

    Ce chapitre traite de l'importation, l'utilisation et l'exportation de données structurées, en Python, sous forme de vecteurs, matrices, tableaux et ensemble de tableaux (bases de données).

    Bien qu'il soit toujours préférable d'organiser les structures qui accueilleront les données d'une expérience avant-même de procéder à la collecte de données, l'analyste doit s'attendre à réorganiser ses données en cours de route. Or, des données bien organisées au départ faciliteront aussi leur réorganisation.

    Ce chapitre débute avec quelques définitions : les données et leurs types, les vecteurs, les matrices, les tableaux et les bases de données, ainsi que leur signification en Python. Puis, nous verrons comment organiser un tableau selon quelques règles simples, mais importantes pour éviter les erreurs et les opérations fastidieuses pour reconstruire un tableau mal conçu. Ensuite, nous traiterons des formats de tableau courant, pour enfin passer à l'utilisation de polars, une bibliothèque Python utile pour effectuer des opérations sur les tableaux.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Types de données

    Dans la section précédente, nous avons survolé différents types d'objets : réels, entiers, chaînes de caractères et booléens. Les données peuvent appartenir à d'autres types : dates, catégories ordinales (ordonnées : faible, moyen, élevé) et nominales (non-ordonnées : espèces, cultivars, couleurs, etc.).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Vecteurs

    Dans la section d'introduction à Python, nous avons vu comment Python permet d'organiser des collections d'objets. Bien qu'il soit important de connaître leur existence pour apprendre à maîtriser Python, les listes et les dictionnaires sont peu pratiques pour le calcul. Pour les listes, il faudrait passer par des boucles... ce qui est loin d'être pratique. On préférera généralement utiliser des vecteurs, qui, grâce à la *vectorisation*, peuvent être soumis à des opérations avec des scalaires. Les vecteurs sont accessibles via le module Numpy. Par convention, les fonctions de Numpy sont importés avec l'alias `np`.
    """
    )
    return


@app.cell
def _():
    # Non
    # mon_vecteur = [1, 2, 3, 4]
    # mon_vecteur + 1

    # Bof
    # mon_vecteur = [1, 2, 3, 4]
    # [x + 1 for x in mon_vecteur]

    # Oui
    import numpy as np

    mon_vecteur = np.array([1, 2, 3, 4])
    mon_vecteur + 1
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Contrairement à une liste, un vecteur contient obligatoirement des valeurs même type. À défaut de définir un même type, Numpy transformera chaque valeur en chaîne de caractère.""")
    return


@app.cell
def _():
    [1, 2, 3, "grenouille"]  # liste
    return


@app.cell
def _(np):
    np.array([1, 2, 3, "grenouille"])  # vecteur
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Matrices

    La matrice est une généralisation du vecteur. Alors que le vecteur a une seule dimension, la matrice accepte un nombre le dimension N (naturel positif) nécessaire pour l'application.
    """
    )
    return


@app.cell
def _(np):
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return


@app.cell
def _(np):
    np.array(
        [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    Une matrice 2D peut indiquer l'élévation d'un point dans l'espace x, y. En 3D, vous pouvez inclure non seulement l'élévation, mais aussi l'épaisseur de sol et d'autres variables. Ajouter une évolution dans le temps et vous obtenez une matrice 4D.

    Vous ne pourrez toutefois pas ajouter une couche d'une variable catégorielle dans une matrice numérique: comme les vecteurs, les matrices ne contiennent qu'un seul type de données.

    Les matrices à plusieurs dimensions sont utilisées surtout en modélisation, et une organisation multidimensionnelle des données passe souvent par le module `xarray`, que nous couvrirons à la section 6. En analyse de données, on préférera les tableaux.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Tableaux
    De manière générale, un tableau de données est une organisation de données en deux dimensions, comportant des *lignes* et des *colonnes*. Il est préférable de respecter la convention selon laquelle les lignes sont des observations et les colonnes sont des variables. Ainsi, un tableau est une collection de vecteurs de même longueur, chaque vecteur représentant une variable. Chaque variable est libre de prendre le type de données approprié. La position d'une donnée dans le vecteur correspond à une observation.

    ## Base de données
    Imaginez que vous consignez des données de différents sites (A, B et C), et que chaque site possède ses propres caractéristiques. Il est redondant de décrire le site pour chaque observation. Vous préférerez créer deux tableaux: un pour décrire vos observations, et un autre pour décrire les sites. De cette manière, vous créez une collection de tableaux intereliés: une *base de données*. Nous ne couvrons pas les bases de données ici, mais Python fonctionne très bien comme intermédiaire pour les requêtes sur des bases de données SQL, par exemple avec le package `SQLAlchemy`.

    En Python, les données structurées en tableaux, ainsi que les opérations sur les tableaux, peuvent être gérés grâce aux packages *polars* ou, plus récemment, *Polars*. Mais avant de se lancer dans l'utilisation de ces outils, voyons quelques règles à suivre pour bien structurer ses données.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Organiser un tableau de données

    Afin de repérer chaque cellule d'un tableau, on attribue à chaque ligne et à chaque colonne colonnes un identifiant *unique*, que l'on nomme *indice* pour les lignes et *entête* pour les colonnes.

    ***Règle no 1.** Une variable par colonne, une observation par ligne.* 

    Les unités expérimentales sont décrites par une ou plusieurs variables par des chiffres ou des lettres. Chaque variable devrait être présente en une seule colonne, et chaque ligne devrait correspondre à une unité expérimentale où ces variables ont été mesurées. La règle parait simple, mais elle est rarement respectée. Prenez par exemple le tableau suivant.

    | Site | Traitement A | Traitement B | Traitement C |
    | --- | --- | --- | --- |
    | Sainte-Patente | 4.1 | 8.2 | 6.8 |
    | Sainte-Affaire | 5.8 | 5.9 | NA |
    | Saint-Gréement | 2.9 | 3.4 | 4.6 |

    *Tableau 1. Rendements obtenus sur les sites expérimentaux selon les traitements.*

    Qu'est-ce qui cloche avec ce tableau ? Chaque ligne est une observation, mais contient plusieurs observations d'une même variable, le rendement, qui devient étalé sur plusieurs colonnes. *À bien y penser*, le type de traitement est une variable et le rendement en est une autre :

    | Site | Traitement | Rendement |
    | --- | --- | --- |
    | Sainte-Patente | A | 4.1 |
    | Sainte-Patente | B | 8.2 |
    | Sainte-Patente | C | 6.8 |
    | Sainte-Affaire | A | 5.8 |
    | Sainte-Affaire | B | 5.9 |
    | Sainte-Affaire | C | NA |
    | Saint-Gréement | A | 2.9 |
    | Saint-Gréement | B | 3.4 |
    | Saint-Gréement | C | 4.6 |

    *Tableau 2. Rendements obtenus sur les sites expérimentaux selon les traitements.*

    Plus précisément, l'expression *à bien y penser* suggère une réflexion sur la signification des données. Certaines variables peuvent parfois être intégrées dans une même colonne, parfois pas. Par exemple, les concentrations en cuivre, zinc et plomb dans un sol contaminé peuvent être placés dans la même colonne "Concentration" ou déclinées en plusieurs colonnes Cu, Zn et Pb. La première version trouvera son utilité pour des créer des graphiques (chapitre 5), alors que la deuxième favorise le traitement statistique.

    ***Règle no 2.** Ne pas répéter les informations.*

    Rerpenons la même expérience. Supposons que vous mesurez la précipitation à l'échelle du site.

    | Site | Traitement | Rendement | Précipitations |
    | --- | --- | --- | --- |
    | Sainte-Patente | A | 4.1 | 813 |
    | Sainte-Patente | B | 8.2 | 813 |
    | Sainte-Patente | C | 6.8 | 813 |
    | Sainte-Affaire | A | 5.8 | 642 |
    | Sainte-Affaire | B | 5.9 | 642 |
    | Sainte-Affaire | C | NA | 642 |
    | Saint-Gréement | A | 2.9 | 1028 |
    | Saint-Gréement | B | 3.4 | 1028 |
    | Saint-Gréement | C | 4.6 | 1028 |

    *Tableau 3. Rendements obtenus sur les sites expérimentaux selon les traitements.*

    Segmenter l'information en deux tableaux serait préférable.

    | Site | Précipitations |
    | --- | --- |
    | Sainte-Patente | 813 |
    | Sainte-Affaire | 642 |
    | Saint-Gréement | 1028 |

    *Tableau 4. Précipitations sur les sites expérimentaux.*

    Les tableaux 2 et 4, ensemble, forment une base de données (collection organisée de tableaux).

    ***Règle no 3.** Ne pas bousiller les données.*

    Par exemple.

    - *Ajouter des commentaires dans des cellules*. Si une cellule mérite d'être commentée, il est préférable de placer les commentaires soit dans un fichier décrivant le tableau de données, soit dans une colonne de commentaire juxtaposée à la colonne de la variable à commenter. Par exemple, si vous n'avez pas mesuré le pH pour une observation, n'écrivez pas "échantillon contaminé" dans la cellule, mais annoter dans un fichier d'explication que l'échantillon no X a été sont systématiquessystématique, il peut être pratique de les inscrire dans une colonne `commentaire_pH`.
    - *Inscriptions non systématiques*. Il arrive souvent que des catégories d'une variable ou que des valeurs manquantes soient annotées différemment. Il arrive même que le séparateur décimal soit non systématique, parfois noté par un point, parfois par une virgule. Par exemple, une fois importés dans votre session, les catégories `St-Ours` et `Saint-Ours` seront traitées comme deux catégories distinctes. De même, les cellules correspondant à des valeurs manquantes ne devraient pas être inscrites parfois avec une cellule vide, parfois avec un point, parfois avec un tiret ou avec la mention `NA`. Le plus simple est de laisser systématiquement ces cellules vides.
    - *Inclure des notes dans un tableau*. La règle "une colonne, une variable" n'est pas respectée si on ajoute des notes un peu n'importe où sous ou à côté du tableau.
    - *Ajouter des sommaires*. Si vous ajoutez une ligne sous un tableau comprenant la moyenne de chaque colonne, qu'est-ce qui arrivera lorsque vous importerez votre tableau dans votre session de travail ? La ligne sera considérée comme une observation supplémentaire.
    - *Inclure une hiérarchie dans les entêtes*. Afin de consigner des données de texture du sol, comprenant la proportion de sable, de limon et d'argile, vous organisez votre entête en plusieurs lignes. Une ligne pour la catégorie de donnée, *Texture*, fusionnée sur trois colonnes, puis trois colonnes intitulées *Sable*, *Limon* et *Argile*. Votre tableau est joli, mais il ne pourra pas être importé conformément dans un votre session de calcul : on recherche *un entête unique par colonne*. Votre tableau de données devrait plutôt porter les entêtes *Texture sable*, *Texture limon* et *Texture argile*. Un conseil : réserver le travail esthétique à la toute fin d'un flux de travail.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Formats de tableau

    Plusieurs outils sont à votre disposition pour créer des tableaux. Je vous présente ici les plus communs.

    ### *.xls* ou *.xlsx*
    Microsoft Excel est un logiciel de type *tableur*, ou chiffrier électronique. L'ancien format *xls* a été remplacé par le format *xlsx* avec l'arrivée de Microsoft Office 2010. Il s'agit d'un format propriétaire, dont l'alternative libre la plus connue est le format *ods*, popularisé par la suite bureautique LibreOffice. Les formats *xls*, *xlsx* ou *ods* sont davantage utilisés comme outils de calcul que d'entreposage de données. Ils contiennent des formules, des graphiques, du formatage de cellule, etc. **Je ne les recommande pas pour stocker des données**.

    ### *.csv* et *.json*
    Le format *csv*, pour *comma separated values*, est un fichier texte, que vous pouvez ouvrir avec n'importe quel éditeur de texte brut (Bloc note, [Visual studio code](https://code.visualstudio.com/), etc.). Chaque colonne doit être délimitée par un caractère cohérent (conventionnellement une virgule, mais en français un point-virgule ou une tabulation pour éviter la confusion avec le séparateur décimal) et chaque ligne du tableau est un retour de ligne. Il est possible d'ouvrir et d'éditer les fichiers csv dans un éditeur texte, mais il est parfois plus pratique de les ouvrir avec des tableurs (LibreOffice Calc, Microsoft Excel, Google Sheets, etc.).

    Comme le format *csv*, le format *json* indique un fichier en texte clair. Il est utilisé davantage pour le partage de données des applications web. En analyse et modélisation, ce format est surtout utilisé pour les données géoréférencées ou lorsque l'on a besoin de consigner de l'information de manière plus souple qu'un tableau.

    **Encodage**. Puisque les formats *csv* et *json* sont des fichiers texte, un souci particulier doit être porté sur la manière dont le texte est encodé. Les caractères accentués pourraient être importés incorrectement si vous importez votre tableau en spécifiant le mauvais encodage. Pour les fichiers en langues occidentales, l'encodage UTF-8 devrait être utilisé. Toutefois, par défaut, Excel utilise un encodage de Microsoft. Si le *csv* a été généré par Excel, il est préférable de l'ouvrir avec votre éditeur texte, de l'enregistrer dans l'encodage UTF-8, puis de s'assurer que le délimiteur décimal est un point et que le délimiteur de colonne est une virgule.

    ### Autres formats
    D'autres formats existent comme [Parquet](parquet.apache.org) pour le stockage efficace de données massives, ou [NetCDF](https://en.wikipedia.org/wiki/NetCDF) pour les tableaux multidimensionnels. L'extension .db est utilisée pour [DuckDB](duckdb.org), un format pour les bases de données stockées en format de colonnes, qui inclut également un [module SIG](https://duckdb.org/docs/extensions/spatial/overview.html).

    ### Entreposer ses données
    La manière la plus sécure pour entreposer ses données est de les confiner dans une base de données sécurisée sur un serveur sécurisé dans un environnement sécurisé. C'est aussi la manière la moins accessible. Des espaces de stockage nuagiques, comme Onedrive ou [autre](https://alternativeto.net/software/microsoft-onedrive/), peuvent être pratiques pour les backups et le partage des données avec une équipe de travail (qui risque en retour de bousiller vos données). Le suivi de version est possible chez certains fournisseurs d'espace de stockage. Mais pour un suivi de version plus rigoureux, les espaces de développement (comme GitHub) sont plus appropriés. Dans tous les cas, il est important de garder (1) des copies anciennes pour y revenir en cas d'erreurs et (2) un petit fichier décrivant les changements effectués sur les données.

    ### Suggestion
    En *csv* pour les petits tableaux, en *db* avec [DuckDB](https://duckdb.org/) pour les bases de données plus complexes, puis migrer vers [PostgreSQL](postgresql.org) et l'extension [PostGIS](https://postgis.net/) si vous devez gérer des droits d'utilisation. Cette formation se concentre toutefois sur les données de type *csv*.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Explorer les données

    Pour démarrer, j'ai créé un dossier `data`, et j'y ai déposé le jeu de données *Palmer penguins*, [arrangé par Allison Horst](https://allisonhorst.github.io/palmerpenguins/) à partir de recherches sur le dimorphisme sexuel chez les manchots ([Gorman et al., 2014](https://doi.org/10.1371/journal.pone.0090081)).

    <center>
        <img src="https://github.com/allisonhorst/palmerpenguins/raw/main/man/figures/lter_penguins.png" width=20%>
        <img src="https://github.com/allisonhorst/palmerpenguins/raw/main/man/figures/culmen_depth.png" width=20%>
        <p><a href="https://github.com/allisonhorst/palmerpenguins">Images par Allison Horst</a></p>
    </center>
    """
    )
    return


@app.cell
def _():
    import polars as pl

    penguins = pl.read_csv(
        "data/penguins.csv",
        null_values="NA",
    )
    penguins
    return penguins, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    Conformément aux règles de construction d'un tableau, *polars* demande à ce que chaque colonne possède un entête unique, et qu'une colonne ne contienne qu'un type de données.

    ### Sélectionner et filtrer des données

    On utilise le terme *sélectionner* lorsque l'on désire choisir une ou plusieurs lignes et colonnes d'un tableau (la plupart du temps des colonnes). L'action de *filtrer* signifie de sélectionner des axes (la plupart du temps des lignes) selon certains critères.

    #### Sélectionner

    Il y a plusieurs manières de sélectionner une colonne. La plus rapide consiste à fournir une liste entre crochets directement après avoir appelé le tableau.
    """
    )
    return


@app.cell
def _(penguins):
    penguins.select("bill_depth_mm", "bill_length_mm")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Une sélection négative, par exclusion, peut également être effectuée.""")
    return


@app.cell
def _(penguins, pl):
    penguins.select(
        pl.exclude(["bill_depth_mm", "bill_length_mm", "body_mass_g", "year", "rowid"])
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Filtrer

    La méthode `.filter()` permet d'utiliser des opérations de filtres booléen (vrai/faux). La colonne est sélectionnée avec `pl.col()`, l'inverse de `pl.exclude()`. `filter` est l'équivalent de `WHERE` en SQL.
    """
    )
    return


@app.cell
def _(penguins, pl):
    penguins.filter(
        (pl.col("species") == "Adelie") & (pl.col("island") == "Torgersen")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Les opérations de *polars* peuvent également être effectués en chaîne, en les englobant entre parenthèses.""")
    return


@app.cell
def _(penguins, pl):
    (
        penguins
        .filter(pl.col("sex") == 'female')
        .select("year", "bill_length_mm")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Effectuer un sommaire avec `group_by`

    La méthode `.group_by()` permet d'effectuer des calculs par groupe et sous-groupes. À la suite d'un regroupement, on calcule habituellement une agrégation.
    """
    )
    return


@app.cell
def _(penguins, pl):
    (
        penguins
        .filter(
            (pl.col("island") == "Dream") & ((pl.col("sex").is_in(["male", "female"]) ))
        )
        .group_by(["species", "sex"])
        .agg(
            body_mass_g_mean=pl.col("body_mass_g").mean(),
            body_mass_g_std=pl.col("body_mass_g").std()
        )
        .sort("species")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Dès que vous installez le module `duckdb`, Marimo vous donne accès aux commandes SQL sur des tableaux. Par exemple,""")
    return


@app.cell
def _(mo, penguins):
    _df = mo.sql(
        f"""
        SELECT species, sex,
            AVG(body_mass_g) AS mean_body_mass,
            STDDEV(body_mass_g) AS std_body_mass
        FROM penguins
        WHERE island = 'Dream' AND sex IN ('female', 'male')
        GROUP BY species, sex
        ORDER BY species
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Effectuer des calculs avec `with_columns`

    `with_columns` est super pratique pour effectuer des opérations sur des colonnes.
    """
    )
    return


@app.cell
def _(penguins, pl):
    (
        penguins
        .with_columns(
            (pl.col("body_mass_g") / 1000).alias("body_mass_kg")
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Tableau large - tableau long

    Le tableau `penguins` est formaté correctement selon les règles établies précédemment. Ce n'est pas toujours le cas. Par exemple celui-ci.
    """
    )
    return


@app.cell
def _(np, pl):
    experience = pl.DataFrame(
        {
            "Site": ["Sainte-Patente", "Sainte-Affaire", "Saint-Gréement"],
            "Traitement A": [4.1, 5.8, 2.9],
            "Traitement B": [8.2, 5.9, 3.4],
            "Traitement C": [6.8, np.nan, 4.6],
        }
    )
    experience
    return (experience,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Pour transformer ce tableau en mode *tidy* (organisé), utilisons la méthode `.unpivot()` - méthode _seekwellpolars_ pour renommer la méthode équivalente, `.melt()`. Cette méthode prend, comme argument `id_var`, les colonnes qui ne doivent *pas* être fusionnées. Dans ce cas-ci, les sites.""")
    return


@app.cell
def _(experience):
    experience_long = experience.unpivot(index="Site")
    experience_long
    return (experience_long,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""L'opération inverse est `.pivot()`. Il faudra néanmoins spécifier la variable à étaler dans l'argument `on`.""")
    return


@app.cell
def _(experience_long):
    experience_long.pivot(index="Site", on="variable")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Combiner des tableaux

    Nous avons introduit plus haut la notion de base de données. Nous voudrions peut-être utiliser le nom de l'espèce de manchot pour lui attribuer certaines caractéristiques.
    """
    )
    return


@app.cell
def _(pl):
    penguins_meta = pl.read_csv("data/penguins_meta.csv")
    penguins_meta
    return (penguins_meta,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Notre information est organisée en deux tableaux, liés par la colonne `species`. Comment fusionner l'information pour que l'info soit être utilisée dans son ensemble ? Par des opérations de jointure. La plus commune est la jointure à gauche, où le tableau de droit vient se coller au tableau de gauche.""")
    return


@app.cell
def _(penguins, penguins_meta):
    penguins.join(penguins_meta, on="species", how="left")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Ainsi, les informations sont combinées. Plusieurs [types de jointure](https://en.wikipedia.org/wiki/Join_(SQL)) peuvent être effectuées.""")
    return


if __name__ == "__main__":
    app.run()
