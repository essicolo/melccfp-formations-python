import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Visualisation

    De nombreux packages ont été développés en Python pour la visualisation, avec chacun leurs avantages et inconvénients, selon votre objectif et votre expérience.

    Ces packages peuvent être catégorisés selon leur approche, impérative ou déclarative. L'approche impérative, la plus classique, demande des instructions précises sur la manière d'afficher les objets. L'approche déclarative, plus moderne, demande plutôt ce que l'on désire afficher, et s'occupe de construire un graphique adapté. Le package de visualisation impérative le plus connu en Python est Matplotlib, qui a l'avantage de vous donner le plein contrôle sur vos graphiques, mais le désavantage de demander beaucoup d'information pour un graphique simple.

    Nous allons plutôt travailler en mode déclaratif avec Holoviews, qui permet de créer rapidement des visualisations interactives, exploratoires ou destinées à être publiées. Le mode déclaratif le plus utilisé, et utilisé aussi par Holoviews, est une *grammaire graphique*, où chaque variable d'un tableau peut être associée à un ou plusieurs attributs graphiques. Dans un chapitre subséquent, nous explorerons les capacités cartographiques de la suite Holoviz, dont fait partie Holoviews, mais aussi Geoviews.

    Dans cette section, nous allons explorer différents types de graphiques avec Holoviews, notamment

    - les nuages de points simples et colorés,
    - la segmentation d'un graphique en plusieurs panneaux (le *facetting*)
    - la superposition de couches,
    - la juxtaposition de graphiques,
    - etc.

    Pour notre premier exercice, demandons nous...

    ## Pourquoi explorer graphiquement ?

    Deux jeux de données aux statistiques identiques peuvent avoir des structures radicalement différentes : la visualisation graphique est indispensable pour déceler la structure réelle.
    """
    )
    return


@app.cell
def _(pl):
    datasaurus = pl.read_csv("data/datasaurus.csv")
    datasaurus.group_by("dataset").agg(
        x_mean=pl.col("x").mean(),
        x_std=pl.col("x").std(),
        y_mean=pl.col("y").mean(),
        y_std=pl.col("y").std(),
    )
    return (datasaurus,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Les moyennes et écarts-type sont semblables pour tous les jeux de données. Si l'on effectuait des tests statistiques, ils ne seraient pas significativement différents. On pourrait alors conclure que ces données proviennent de distributions statistiques identiques à un niveau de confiance très sévère. Pour démontrer que ces statistiques ne vous apprendront pas grand-chose sur la structure des données, [Matejka et Fitzmaurice (2017)](https://www.autodeskresearch.com/publications/samestats) ont généré les données que nous avons chargées. Des statistiques semblables cachent parfois des structures bien différentes.

    <img src=https://www.research.autodesk.com/app/uploads/2023/03/DinoSequential-1.gif width=600>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Choisir le type de graphique le plus approprié

    De nombreuses manières de présenter les données sont couramment utilisées, comme les nuages de point, les lignes, les histogrammes, les diagrammes en barre et en pointe de tarte. Il existe de même de nombreux guides pour sélectionner le type de graphique approprié selon la situation. Je vous conseille le guide [*From data to viz*](https://www.data-to-viz.com/). En ce qui a trait aux couleurs, le choix n'est pas anodin, ne serait-ce que de sélectionner des couleurs robustes aux handicaps visuels : préférez donc les couleurs de [*Color brewer 2*](colorbrewer2.org).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Les graphiques avec Altair

    Le package [Altair](https://altair-viz.github.io/), aussi connu sous le nom Vega-Altair, fonctionne en mode déclaratif basé sur la grammaire graphique Vega-Lite. Altair couvre les besoins autant en visualisation exploratoire qu'en production de graphiques statiques ou interactifs. Notez bien qu'il est toutefois plutôt pauvre pour la cartographie.

    Altair fonctionne en mode déclaratif, sous la forme générale suivante.

    ```
    (
        alt.Chart(data=<TABLEAU>)
        .mark_<TYPE>()
        .encode(
            x='<VARIABLE_X>',
            y='<VARIABLE_Y>',
            color='<VARIABLE_COULEUR>',
            ...
        )
        .properties(width=600, height=400)
    )
    ```

    L'alias `alt` initie le graphique avec `Chart()` qui prend en argument le tableau de données (typiquement un tableau pandas). La méthode `.mark_*()` définit le type de graphique (`mark_point()`, `mark_line()`, `mark_bar()`, etc.). La méthode `.encode()` lie les variables du tableau aux attributs visuels (axes x et y, couleur, taille, etc.). Enfin, `.properties()` permet de définir les dimensions et autres propriétés du graphique.

    Voici un exemple tout simple avec les données `datasaurus`.
    """
    )
    return


@app.cell
def _(alt, datasaurus):
    (
        alt.Chart(datasaurus)
        .mark_point()
        .encode(x="x", y="y")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Le graphique ci-dessus montre un nuage de points qui permet difficilement d'explorer les données `datasaurus`. Ce tableau contient toutefois une autre colonne, nommée `dataset`.  Encodons la couleur des points, faisant ainsi varier la couleur selon la colonne catégorielle `dataset`.""")
    return


@app.cell
def _(alt, datasaurus):
    (
        alt.Chart(datasaurus)
        .mark_point()
        .encode(x="x", y="y", color="dataset:N") # :N pour les données nominales, optionnellement spécifié
        .properties(width=500, height=400)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    On y voit déjà un peu mieux. Mes yeux étant sensibles à la couleur, j'aperçois bien le `X` violet. Mais ce graphique n'est pas propice à une bonne exploration, en plus de poser problème aux yeux moins sensibles aux couleurs.

    Ainsi, de même que la couleur, nous pouvons lier une variable numérique à la dimension des points (`size`), etc. Pour y voir plus clairement, nous pouvons utiliser les facettes pour diviser un graphique en plusieurs panneaux. On peut y accéder avec la méthode `.facet()`.
    """
    )
    return


@app.cell
def _(alt, datasaurus):
    (
        alt.Chart(datasaurus)
        .mark_point(shape="circle", filled=True, size=10, opacity=0.7, color="green")
        .encode(x="x:Q", y="y:Q")
        .properties(width=100, height=100)
        .facet(facet="dataset:N", columns=5)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Exercices**. Jouez avec les données datasaurus, notamment en vous servant de ce que vous avez appris jusqu'ici.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## La superposition des couches

    Il existe d'autres géométries que les nuages de points. Explorons maintenant les lignes avec les données économiques.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(pl):
    economics = pl.read_csv("data/economics.csv")
    economics = economics.with_columns(
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date")
    )
    return (economics,)


@app.cell
def _(alt, economics):
    (
        alt.Chart(economics)
        .mark_line()
        .encode(
            x=alt.X("date:T", axis=alt.Axis(labelAngle=-60)),
            y="unemploy:Q",
        )
        .properties(width=500, height=350)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    | **Type Altair**   | **Méthode mark** | **Encodages typiques**               | **Usage**                            |
    | ----------------- | ---------------- | ------------------------------------ | ------------------------------------ |
    | Nuage de points   | `.mark_point()`  | `x`, `y`, `color`, `size`, `shape`   | Visualiser des relations bivariées   |
    | Ligne             | `.mark_line()`   | `x`, `y`, `color`                    | Visualiser des tendances temporelles |
    | Barres            | `.mark_bar()`    | `x` (catégorie), `y` (valeur)        | Comparer des catégories              |
    | Boîtes à moustaches | `.mark_boxplot()` | `x` (groupe), `y` (valeur)        | Visualiser des distributions         |
    | Carte de chaleur  | `.mark_rect()`   | `x`, `y`, `color` (valeur)           | Visualiser des matrices              |
    | Histogramme       | `.mark_bar()`    | `x` (bins), `y` (count)              | Visualiser une distribution          |
    | Aire              | `.mark_area()`   | `x`, `y`, `y2`                       | Visualiser des plages                |
    | Texte             | `.mark_text()`   | `x`, `y`, `text`                     | Ajouter des annotations              |
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    | Encodage     | Points            | Lignes       | Barres/Boîtes |
    | ------------ | ----------------- | ------------ | ------------- |
    | color        | oui               | oui          | oui           |
    | size         | oui               | oui (trait)  | non           |
    | shape        | oui               | non          | non           |
    | opacity      | oui               | oui          | oui           |
    | strokeWidth  | oui               | oui          | oui (bordure) |
    | strokeDash   | oui               | oui          | non           |
    | tooltip      | oui               | oui          | oui           |
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Exemples

    Recommandé

    ```python
    mo.ui.altair_chart(
        alt.Chart(datasaurus)
        .mark_point(shape='square')
        .encode(x="x", y="y", color="dataset")
    )
    ```

    Parfois utilisé

    ```python
    alt.Chart(datasaurus)\
        .mark_point(shape='square')\
        .encode(x="x", y="y", color="dataset")
    ```

    Ou bien...

    ```python
    alt.Chart(
        datasaurus
    ).mark_point(
        shape='square'
    ).encode(
        x="x", y="y", color="dataset"
    )
    ```

    ### `alt.Chart(data)`

    C'est l'initiation du graphique avec les données (un tableau pandas, à toute fin pratique).

    Exemple

    ```python
    alt.Chart(df)
    ```

    ### `.transform_*()`

    Bien qu'il soit, la plupart du temps, préférable d'effectuer les calculs directement sur les tableaux, *Altair* permet de modifier les données à même la commande graphique. À moins de vouloir créer des graphiques avec une interactivité construite directement dans *Altair*, je recommande de n'utiliser que `.transform_density(...)` pour le calcul de densité, également utile pour visualiser des distributions.

    Exemple

    ```python
    (
        alt.Chart(df)
        .transform_density('x', as_=['x', 'density'])
        .mark_area()
        .encode(x='x:Q', y='density:Q')
    )
    ```

    ### `.mark_*()`

    Cette méthode sert à spécifier la géométrie. Parmi celles disponibles, on retrouve

    - `.mark_point()`
    - `.mark_line()`
    - `.mark_bar()`
    - `.mark_area()`
    - `.mark_text()`
    - `.mark_rect()` (de type *heatmap*)
    - `.mark_rule()` (ligne horizontale ou verticale)
    - `.mark_circle()`
    - `.mark_square()`
    - `.mark_geoshape()`

    À l'intérieur des parenthèses, on peut spécifier des paramètres **globaux** du graphique, par exemple la couleur des points, les épaisseurs des traits, etc.

    Exemple

    ```python
    .mark_line(color='red', size=2, interpolate='monotone')
    ```

    ### `.encode()`

    C'est la méthode qui lie les variables du tableau aux éléments nécessaires pour construire le graphique.

    - `x`, `y` : axes
    - `color` : couleur
    - `size` : taille des points, lignes, etc.
    - `shape` : forme des symboles
    - `text` : contenu d’une `mark_text()`
    - `opacity`, `stroke`, `fill`, `tooltip`, ...

    Exemple

    ```python
    .encode(x='longueur', y='hauteur', color='groupe:N')
    ```

    Il arrive souvent que les encodages doivent être modifiés, par exemple définir les limites des axes. Dans ce cas, il faut appeler leur objet `altair`. De plus, il est possible mais optionnel de spécifier à *Altair* le type de données, par exemple `longueur:Q` pour les données quantitatives, ou `groupe:N` pour les catégories nominales.


    ```python
    .encode(
        x=alt.X('longueur:Q', scale=alt.Scale(type='log'), axis=alt.Axis(title='Log X')),
        y=alt.Y('largeur:Q', scale=alt.Scale(zero=False)),
        color=alt.Color('groupe:N', legend=alt.Legend(title='Catégorie'))
    )
    ```

    ### `.properties(...)`

    Ce sont les propriétés générales du graphique, comme la taille, les titres, etc.


    ```python
    .properties(width=300, height=200, title='Un joli graphique')
    ```

    **Note**. Pour les facettes, il faut appliquermles `properties` `width` et `height` **avant `.facet()`**.

    ### `.facet(...)`

    Crée une **grille de sous-graphiques** en séparant les données selon des variables.

    - `row='groupe'` : une ligne par valeur unique
    - `column='groupe'` : une colonne par valeur unique
    - `facet=alt.Facet('groupe', ...)` : version complète avec contrôle du tri, titre, etc.

    **Note**. On retrouve ici et là des exemples où les facettes sont appelées sous forme `.encode(..., row='group1', column='groupe2')`. Cette approche fonctionne, mais causera des soucis lorsque l'on désire ajouter des couches au graphique (nous y arriverons bientôt). Je recommande de toujours ajouter `.facet(...)` plutôt que de l'enchâsser dans `.encode()`.

    ### `.configure_*()`

    C'est le centre de contrôle avant d'afficher le graphique, qui permet de modifier l’apparence globale.

    - `.configure_axis()` : taille, couleur, ticks
    - `.configure_legend()` : position, forme, police
    - `.configure_view()` : marges, bordure du cadre
    - `.configure_title()` : style du titre global
    - `.configure_point()`, `.configure_line()` : géométries globales

    Exemples

    ```python
    .configure_axis(grid=False)
    .configure_title(fontSize=18, anchor='start')
    ```

    ### `.save(...)`

    Le graphique peut être enregistré en format image-pixel (.png), en format d'image vectorielle (.svg), dans une page web avec Javascript (html) ou en une description destinée à *Vega-Lite* (.json). Pour les formats d'images, assurez-vous que le package `vl-convert-python` est installé. Notez que les formats svg, html et json exportent les données de chaque point: un graphique avec de nombreux points deviendra rapidement lourd.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Composition avancée dans Altair : superposition, juxtaposition et facettage

    ### Superposition de couches (*Layering*) dans Altair

    La superposition de couches permet de combiner plusieurs représentations `mark_*()` sur les mêmes axes. Altair offre deux approches équivalentes, soit l’opérateur `+` ou la fonction `alt.layer()`. Par exemple, nous désirons tracer des points de données et une régression linéaire sur le même graphique.
    """
    )
    return


@app.cell
def _(pl):
    ascombe_quartet = pl.read_csv(
        "https://gist.githubusercontent.com/ericbusboom/b2ac1d366c005cd2ed8c/raw/c92c66e43d144fa9c29dbd602d5af6988e8db533/anscombes.csv"
    )
    ascombe_quartet
    return (ascombe_quartet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Le package *statsmodels* permet d'effectuer des statistiques avancées. La formulation testée, `"y ~ x*dataset"`, signifie que `y` est modélisé en fonction de `x`, avec un terme d'interaction pour chaque niveau de la variable catégorielle `dataset`. Cela permet d'évaluer l'influence de `x` sur `y`, du `dataset` sur `y`, et des différences entre les effets de `x` sur `y` des `datasets` (A, B, C, D). Le modèle estime ainsi une pente et une intercept distinctes pour chaque groupe, permettant de comparer les effets.""")
    return


@app.cell
def _(ascombe_quartet, smf):
    model = smf.ols("y ~ x*dataset", data=ascombe_quartet.to_pandas()).fit()
    print(model.summary())
    return (model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""La *p-value* indique la probabilité que les données aient été collectées d'un ensemble dont l'effet réel est nul. Conventionnellement, une *p-value* sous 0.05 est considéré comme un effet signigifactif - cette approche est néanmoins contestée, avec raison. Mais dans notre cas, les p-values sur les variables autres que `x` sont tellement élevées que l'on pourrait conclure que ces effets ne sont pas statistiquement significatifs. Tous les groupes de la variable `dataset` sont-ils issus d'une même distribution?""")
    return


@app.cell
def _(ascombe_quartet, model, pl):
    ascombe_pred = ascombe_quartet.with_columns(
        pl.Series(model.predict(ascombe_quartet.to_pandas())).alias("y_pred")
    )
    ascombe_pred
    return (ascombe_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Nous utilisons le package `statsmodels` pour effectuer la régression, mais une approche plus rapide, sans passer par `statsmodels`, passerait simplement par `.transform_regression('x', 'y')`.""")
    return


@app.cell
def _(alt, ascombe_pred):
    base = alt.Chart(ascombe_pred).encode(x="x:Q", y="y:Q")
    points = base.mark_point(color="blue", opacity=0.5)
    #ligne_altair = base.transform_regression("x", "y").mark_line(color="red")
    ligne = base.mark_line(color="red").encode(y="y_pred:Q")
    overlay = points + ligne
    overlay
    return ligne, overlay, points


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    L’ordre dans lequel les calques sont définis détermine lequel est dessiné au-dessus de l’autre. Le premier graphique fourni sera en arrière-plan, et le second par-dessus.

    ### Juxtaposition horizontale et verticale

    En plus de superposer des calques, Altair permet de juxtaposer des graphiques côte à côte (colonnes) ou en pile (lignes). Les opérateurs `|` et `&` offrent une syntaxe concise pour cela :

    - L’opérateur **`|`** réalise une concaténation horizontale (graphiques alignés côte à côte). Par exemple, `graphique_gauche | graphique_droite`. On peut ainsi comparer deux visualisations différentes côte à côte.
    - L’opérateur **`&`** réalise une concaténation verticale (graphiques l’un au-dessus de l’autre). Par exemple, `graphique_haut & graphique_bas` empile verticalement deux graphiques.

    Ces opérateurs sont des alias des fonctions `alt.hconcat()` et `alt.vconcat()`. Vous pouvez enchaîner plusieurs `|` pour aligner plus de deux graphiques horizontalement, et de même avec `&` verticalement. Par exemple : `chart1 | chart2 | chart3` placera trois graphiques en ligne. De même, on peut créer une grille en combinant `|` et `&` (d’abord concaténer des lignes, puis juxtaposer ces lignes verticalement, etc.).

    Chaque sous-graphique conserve ses propres axes et échelles par défaut. Vous pouvez ajuster les propriétés de chaque panneau individuellement via `.properties(width, height)` sur chaque chart avant la concaténation, afin de contrôler la taille relative de chaque vue. Altair permet aussi d’ajuster l’espacement entre graphiques juxtaposés via l’argument `spacing` des fonctions `hconcat/vconcat` (par exemple `alt.hconcat(chart1, chart2, spacing=10)`).
    """
    )
    return


@app.cell
def _(alt, ascombe_quartet, overlay):
    histogramme = (
        alt.Chart(ascombe_quartet)
        .mark_bar()
        .encode(x=alt.X("x:Q", bin=True, scale=alt.Scale(zero=True)), y="count()")
        .properties(height=100)
    )
    histogramme & overlay.properties(height=200)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Facettage et composition de graphiques

    Altair impose certaines contraintes lorsqu’on combine facettage avec d’autres compositions :

    - **Ne pas superposer des graphiques déjà facettés :** Il est impossible de combiner avec `+` des charts qui sont eux-mêmes facettés (ou définis avec `column`/`row`). Cela produirait une erreur du type *“Faceted charts cannot be layered”*. En d’autres termes, on ne peut pas empiler deux facettes différentes l’une sur l’autre. **La solution** : effectuez d’abord la superposition des calques, puis appliquez le facettage sur le résultat combiné. Par exemple, pour afficher des barres avec leurs labels numériques par catégorie, créez `bars + labels` puis facettez-le par catégorie (`(bars + labels).facet('categorie:N')`) plutôt que de tenter de superposer deux charts déjà facettés séparément, ce qui mènera à une erreur `TypeError: Faceted charts cannot be layered. Instead, layer the charts before faceting.`.
    - **Définir la taille de chaque facette sur le graphique de base** : Pour que chaque facette ait les bonnes dimensions, il est recommandé de définir la largeur (`width`) et la hauteur (`height`) sur le chart de base **avant** d’appliquer `.facet()`. En effet, ces dimensions s’appliquent à chaque sous-graphe facetté, et cascadera sur l'ensemble. Par exemple, nous appliquons les propriétés à `points`, mais elles cascadent automatiquement vers les lignes. Placer `.properties()` après le facettage n'aura aucun effet sur le graphique final.
    - **Pas de facettage direct sur un ensemble juxtaposé** : Altair ne supporte pas le facettage d’un chart déjà concaténé (juxtaposé). Autrement dit, on ne peut pas prendre un graphique composite créé avec `|` ou `&` et ensuite appeler `.facet(...)` dessus. Si vous avez besoin d’un arrangement plus complexe, il faudra recourir à des solutions manuelles ou utiliser d’autres fonctionnalités avancées (en consultant un assistant IA, par exemple).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Le facettage permet ici de comprendre que notre test statistique était bidon! Il ne fallait pas tester les tendances linaries, mais la structure globale des données, par exemple en utilisant des modèles différents.""")
    return


@app.cell
def _(alt, ligne, points):
    (
        alt.layer(points.properties(width=120, height=120), ligne)
        .facet(alt.Facet("dataset:N"), columns=2)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Cartographie avec Altair et Folium

    La visualisation cartographique est essentielle pour explorer des données géospatiales. Nous allons explorer trois approches : Altair standard, Altair avec des tuiles de fond, et Folium pour des cartes interactives plus avancées.

    ### Exemple 1 : Carte simple avec Altair

    Altair peut afficher des données géographiques de base en utilisant `mark_geoshape()`. Commençons par charger des données géographiques du Canada.
    """
    )
    return


@app.cell
def _(alt, pl):
    # Données des capitales provinciales canadiennes
    capitales = pl.DataFrame({
        "ville": ["Victoria", "Edmonton", "Regina", "Winnipeg", "Toronto", 
                  "Québec", "Fredericton", "Halifax", "Charlottetown", "St. John's",
                  "Yellowknife", "Whitehorse", "Iqaluit"],
        "province": ["BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "NT", "YT", "NU"],
        "latitude": [48.4284, 53.5461, 50.4452, 49.8951, 43.6532, 
                     46.8139, 45.9636, 44.6488, 46.2382, 47.5615,
                     62.4540, 60.7212, 63.7467],
        "longitude": [-123.3656, -113.4938, -104.6189, -97.1384, -79.3832,
                      -71.2080, -66.6431, -63.5752, -63.1311, -52.7126,
                      -114.3718, -135.0568, -68.5170],
        "population": [91867, 1010899, 226404, 749534, 2794356,
                       542298, 58220, 439819, 36990, 108860,
                       20340, 28225, 7740]
    })

    carte_simple = (
        alt.Chart(capitales)
        .mark_circle(size=100)
        .encode(
            longitude="longitude:Q",
            latitude="latitude:Q",
            size=alt.Size("population:Q", scale=alt.Scale(range=[50, 500]), legend=alt.Legend(title="Population")),
            color=alt.Color("province:N", legend=None),
            tooltip=["ville:N", "province:N", "population:Q"]
        )
        .properties(width=600, height=400, title="Capitales provinciales du Canada")
    )

    carte_simple
    return (capitales,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exemple 2 : Carte avec fond de tuiles (Altair + XYZ tiles)

    Pour ajouter un fond de carte style OpenStreetMap, nous pouvons utiliser le package `altair_tiles` qui permet d'ajouter des tuiles XYZ comme fond de carte. Cette approche nécessite d'installer `altair_tiles`.

    **Note** : Si `altair_tiles` n'est pas installé, vous pouvez l'installer avec `pip install altair-tiles` ou `uv pip install altair-tiles`.
    
    Altair-tiles utilise une approche où l'on crée d'abord une couche de tuiles, puis on superpose nos données par-dessus.
    """
    )
    return


@app.cell
def _(alt, altair_tiles, capitales):
    # Vérifier si altair_tiles est disponible
    if altair_tiles is not None:
        # Créer une carte avec des tuiles OpenStreetMap
        base_tiles = altair_tiles.create_tiles("OpenStreetMap")
        
        # Ajouter les points par-dessus
        points_capitales = (
            alt.Chart(capitales)
            .mark_circle(size=150, opacity=0.8)
            .encode(
                longitude="longitude:Q",
                latitude="latitude:Q",
                size=alt.Size("population:Q", scale=alt.Scale(range=[100, 800])),
                color=alt.value("red"),
                tooltip=["ville:N", "province:N", "population:Q"]
            )
        )
        
        # Combiner les tuiles et les points
        carte_avec_tuiles = base_tiles + points_capitales
        carte_avec_tuiles.properties(
            width=700, 
            height=500,
            title="Capitales canadiennes sur fond OpenStreetMap"
        )
    else:
        # Alternative sans altair_tiles : projection simple
        (
            alt.Chart(capitales)
            .mark_circle(size=150, opacity=0.8)
            .encode(
                longitude="longitude:Q",
                latitude="latitude:Q",
                size=alt.Size("population:Q", scale=alt.Scale(range=[100, 800])),
                color=alt.Color("province:N"),
                tooltip=["ville:N", "province:N", "population:Q"]
            )
            .project(type="mercator")
            .properties(
                width=700, 
                height=500,
                title="Capitales canadiennes (projection Mercator - altair_tiles non disponible)"
            )
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exemple 3 : Carte interactive avec Folium

    [Folium](https://python-visualization.github.io/folium/) est une bibliothèque Python qui permet de créer des cartes interactives basées sur Leaflet.js. Elle est particulièrement utile pour créer des cartes web interactives avec des marqueurs, des popups, et différents styles de tuiles.

    Folium s'intègre très bien avec Marimo et offre une grande flexibilité pour la cartographie interactive.
    """
    )
    return


@app.cell
def _(capitales, folium, mo):
    # Créer une carte centrée sur le Canada
    carte_folium = folium.Map(
        location=[56.1304, -106.3468],  # Centre approximatif du Canada
        zoom_start=4,
        tiles="OpenStreetMap"
    )
    
    # Ajouter des marqueurs pour chaque capitale
    for row in capitales.iter_rows(named=True):
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["population"] / 50000,  # Taille proportionnelle à la population
            popup=f"<b>{row['ville']}</b><br>{row['province']}<br>Pop: {row['population']:,}",
            tooltip=row["ville"],
            color="red",
            fill=True,
            fillColor="red",
            fillOpacity=0.6
        ).add_to(carte_folium)
    
    # Ajouter un contrôle de couches
    folium.LayerControl().add_to(carte_folium)
    
    # Afficher la carte dans Marimo
    mo.Html(carte_folium._repr_html_())
    return (carte_folium,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exemple 4 : Carte choroplèthe avec Folium

    Une carte choroplèthe colore des régions en fonction d'une variable. Voici un exemple avec des données synthétiques pour les provinces canadiennes.
    """
    )
    return


@app.cell
def _(mo, pl):
    # Données synthétiques sur les provinces
    donnees_provinces = pl.DataFrame({
        "province": ["BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL"],
        "nom_complet": ["British Columbia", "Alberta", "Saskatchewan", "Manitoba", 
                       "Ontario", "Quebec", "New Brunswick", "Nova Scotia", 
                       "Prince Edward Island", "Newfoundland and Labrador"],
        "valeur": [4.8, 5.2, 3.1, 2.9, 14.7, 8.5, 1.2, 1.8, 0.6, 1.0]  # Données fictives
    })
    
    # Note : Pour une vraie carte choroplèthe, il faudrait des données GeoJSON
    # des frontières provinciales. Voici un exemple conceptuel :
    
    mo.md(f"""
    **Données des provinces préparées :**
    
    {donnees_provinces}
    
    Pour créer une carte choroplèthe complète avec Folium, vous auriez besoin de :
    
    1. Un fichier GeoJSON avec les géométries des provinces canadiennes
    2. La méthode `folium.Choropleth()` pour lier les données aux géométries
    
    Exemple de code (nécessite un fichier GeoJSON) :
    
    ```python
    carte = folium.Map(location=[56, -106], zoom_start=4)
    
    folium.Choropleth(
        geo_data='canada_provinces.geojson',
        name='choropleth',
        data=donnees_provinces.to_pandas(),
        columns=['province', 'valeur'],
        key_on='feature.properties.code',
        fill_color='YlOrRd',
        legend_name='Valeur par province'
    ).add_to(carte)
    ```
    
    **Ressources pour obtenir des données GeoJSON :**
    - [Natural Earth Data](https://www.naturalearthdata.com/)
    - [Statistics Canada Boundary Files](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index-eng.cfm)
    - [GeoJSON.xyz](http://geojson.xyz/)
    """)
    return (donnees_provinces,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Comparaison des approches

    | Approche | Avantages | Inconvénients | Cas d'usage |
    |----------|-----------|---------------|-------------|
    | **Altair simple** | - Syntaxe déclarative cohérente<br>- Intégration parfaite avec le workflow Altair | - Pas de fond de carte<br>- Limité aux projections simples | Visualisations géographiques simples, diagrammes de points |
    | **Altair + Tiles** | - Ajoute un contexte cartographique<br>- Garde la syntaxe Altair | - Nécessite package additionnel<br>- Moins flexible que Folium | Cartes avec contexte géographique, analyse spatiale légère |
    | **Folium** | - Très interactif<br>- Nombreuses options de tuiles<br>- Support des GeoJSON | - API différente d'Altair<br>- Plus verbeux | Cartes web interactives, tableaux de bord, applications géospatiales |

    Pour des analyses cartographiques plus avancées en Python, considérez également :
    - **GeoPandas** : manipulation de données géospatiales
    - **Plotly Express** : cartes interactives avec `px.scatter_geo()`, `px.choropleth()`
    - **Holoviews/Geoviews** : approche déclarative pour la cartographie
    - **Leafmap** : interface simplifiée pour créer des cartes interactives
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Exercices

    Le tableau *diamonds* a été utilisé par Hadley Wickham, un pionier du langage R (surtout utilisé pour les statistiques) dans son livre [*ggplot2: Elegant Graphics for Data Analysis*](https://ggplot2-book.org/). Il est très utile pour développer ses habiletés en visualisation déclarative.
    """
    )
    return


@app.cell
def _(pl):
    diamonds = pl.read_csv(
        "https://raw.githubusercontent.com/tidyverse/ggplot2/refs/heads/main/data-raw/diamonds.csv"
    )
    diamonds_500 = diamonds.sample(500)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    À partir des [exemples sur le site de Altair](https://altair-viz.github.io/gallery/index.html),

    - tracez la distribution des prix pour chaque carat
    - utilisez des facettes pour représenter les distributions selon les carats et les couleurs (pour discrétiser une variable continue, utilisez par exemple `pd.qcut(df['A'], n=5, equidistant=True)`)
    - amusez-vous!

    **Exercice cartographique** : Créez une carte Folium qui montre les capitales canadiennes avec des marqueurs personnalisés selon la taille de la population, et ajoutez des cercles de rayon proportionnel autour de chaque ville.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## D'autres librairies graphiques

    Vega-Altair est communément utilisée, et très bien intégrée à Marimo. De nombreuses librairies graphiques ont néanmoins été développées en Python. Lets-plot est remarquablement flexible et intuitive, en plus de posséder un bon support pour la cartographie - elle n'est toutefois pas installable dans un environnement Marimo en ligne. Vous noterez également l'utilisation étendue de [Matplotlib](https://matplotlib.org/), de [Seaborn](https://seaborn.pydata.org/), de [Plotly](https://plotly.com/python/), de [Bokeh](https://bokeh.org/) et de [Holoviews](https://holoviews.org/).
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    import folium
    from folium import plugins
    import statsmodels.formula.api as smf
    
    # Tentative d'import d'altair_tiles (optionnel)
    try:
        import altair_tiles
    except ImportError:
        altair_tiles = None
    
    return alt, altair_tiles, folium, mo, pl, plugins, smf


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
