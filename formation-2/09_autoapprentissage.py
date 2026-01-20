import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    import altair as alt
    import altair_tiles as til
    import lets_plot as lp
    from lets_plot import tilesets # tilesets n'est pas directement disponible sous lp
    lp.LetsPlot.setup_html()

    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression

    import warnings

    warnings.filterwarnings("ignore", category=FutureWarning)
    return (
        LinearRegression,
        PolynomialFeatures,
        alt,
        gpd,
        lp,
        mo,
        np,
        pd,
        tilesets,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 9. Auto-apprentissage

    On parle beaucoup d'intelligence artificielle. Il s'agit néanmoins d'un mot-valise englobant plusieurs approches, avec une jolie couche de marketing. L'intelligence étant une capacité sentiente (capacité à posséder une attention objective, réservée jusqu'ici aux animaux — dont les humains) et l'artificialité n'ayant pas de définition scientifique formelle. Nous utilisons le terme auto-apprentissage dans le sens que l'humain donne à un algorithme la disposition de générer des réponses par l'expérience empirique.

    Par exemple, avant les réseaux de neurones, les algorithmes pour jouer aux échecs étaient gouvernés par des règles logiques. La question posée à l'algorithme est *dans la situation donnée, quel est le prochain bon coup?*. Aux échecs, l'encodage des situations possibles étant pratiquement incalculable (environ $10^{43}$), un bon algorithme pourrait plutôt passer par l'expérience. On pose alors une autre question à l'algorithme : *étant donnée toutes ces parties que tu as observées, quel est le prochain coup qui a la plus grande probabilité de mener vers une victoire*? En fait, la manière dont un cerveau humain aborde la plupart des problèmes est non pas par la logique, mais par l'expérience : d'où la métaphore "intelligence artificielle".

    La plupart des problèmes d'auto-apprentissage est abordée en liant une situation représentée par une matrice *X*, regroupant les *features* corrélée à un vecteur *y*, regroupant les *targets*. $\epsilon$ est l'erreur d'estimation.

    $$
    y = f(X) + \epsilon
    $$

    où

    $$X = \begin{bmatrix} x_{11} & x_{12} & \cdots & x_{1p} \\ x_{21} & x_{22} & \cdots & x_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ x_{n1} & x_{n2} & \cdots & x_{np} \end{bmatrix}, \quad y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}, \quad \epsilon = \begin{bmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{bmatrix}$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Entrées $X$ et sorties $Y$

    La matrice $X$, qui indique les entrées ou les *features*, peut être en plusieurs dimensions. Pour estimer l'envergure d'un oiseau (distance du bout d'une aile à l'autre, la variable $y$), une matrice $X$ peut être un tableau 2D, où chaque colonne est une variable, par exemple la masse, l'espèce, le sexe, etc. Aussi en 2D, pensons à une photo satellite, la première dimension étant la position en longitude, la deuxième en latitude. On remplit la matrice avec des chiffres désignant l'intensité de la bande, par exemple le rouge. Ajoutons le vert et bleu. Nous avons maintenant trois dimensions : latitude, longitude, bande. Nous pouvons ajouter le temps pour obtenir une série temporelle d'images pour chaque bande, ajoutant un quatrième dimension, comme dans un vidéo.

    De même, le *target* n'est pas nécessairement un vecteur comme l'envergure d'un oiseau, et peut se déplier en un nombre de dimensions voulu. Dans ce cas, plusieurs stratégies peuvent être adoptées : on pourra générer une collection de modèles indépendants, chacun produisant un vecteur que l'on peut ensuite concaténer aux autres pour créer une matrice. Si toutefois on suppose que les sorties du modèle doivent être cohérentes, on pourra aussi créer un modèle plus complexe, en multi-sortie (*multioutput*).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fonction objective

    L'erreur $\epsilon$ a la même dimension que la sortie $y$. Dans notre équation d'auto-apprentissage, il s'agit d'une erreur absolue. La fonction objective permet de donner une instruction à notre algorithme, qui se résume souvent par *trouve les paramètres de mon équation qui permettent de minimiser l'erreur des estimations*. La fonction objective n'est jamais la somme des erreurs. Ce serait en effet un très mauvais guide puisque de grandes erreurs positives s'annuleraient avec de grandes erreurs négatives. La somme des valeurs absolues des erreurs peut très bien être utilisée. Mais en optimisation, on passe souvent par la dérivée de la fonction objective pour rechercher son minimum, et la dérivée de la valeur absolue de x est indéfinie. Alors, on préfère minimiser la somme ou la moyenne du carré des erreurs, le MSE (*mean square error*) et sa racine carrée, le RMSE (*root mean square error*). Il existe plusieurs types de fonction objective, mais restons-en à l'erreur moyenne des carrés.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Validation et test

    Pour les modèles paramétriques comme la régression linéaire, utiliser insuffisamment de paramètres rend un modèle peu flexible, de sorte que de véritables tendances soient considérées comme du bruit de fond. En revanche, en utiliser trop de paramètres mène à considérer du bruit comme une véritable tendance. Le graphique ci-dessous montre des ajustements sur une fonction sinusoïdale bruitée par un modèle linéaire, un polynôme de degré 3 et un autre de degré 15. On observe l'effet d'un sous-apprentissage et d'un sur-apprentissage.

    Minimiser l'erreur n'est pas la meilleure manière de représenter un phénomène. Comment s'y prendre? En utilisant la validation, le test, ou, mieux, les deux. Les deux approches consistent à retirer des données, minimiser l'erreur sur les données conservées, et évaluer l'erreur sur les données retirées. Leur objectif est d'évaluer la performance d'un modèle non pas sur des données sur lesquelles il a été entraîné, mais sur de nouvelles données. En l'occurrence, la prédiction avec le polynome de degré 15 pour une valeur en $x=9,8$ s'écarterait beaucoup de la véritable tendance. Mais quelle et la différence entre la validation et le test?
    """)
    return


@app.cell(hide_code=True)
def _(LinearRegression, PolynomialFeatures, alt, np, pd):
    np.random.seed(42)
    _ndata = 20
    _predfactor = 10
    _x = np.linspace(0, 10, _ndata)
    _xpred = np.linspace(0, 10, _ndata * _predfactor)
    _y = 3 * np.sin(_x / 2) + np.random.normal(0, 2, _ndata)
    _ypred = 3 * np.sin(_xpred / 2) + np.random.normal(0, 2, _ndata * _predfactor)
    _df = pd.DataFrame({"x": _x, "y": _y})
    _dfpred = pd.DataFrame({"x": _xpred, "y": _ypred})

    _model_under = LinearRegression()
    _model_under.fit(_x.reshape(-1, 1), _y)
    _dfpred["y_under"] = _model_under.predict(_xpred.reshape(-1, 1))

    _poly_good = PolynomialFeatures(degree=3)
    _X_good = _poly_good.fit_transform(_x.reshape(-1, 1))
    _Xpred_good = _poly_good.fit_transform(_xpred.reshape(-1, 1))
    _model_good = LinearRegression()
    _model_good.fit(_X_good, _y)
    _dfpred["y_good"] = _model_good.predict(_Xpred_good)

    _poly_over = PolynomialFeatures(degree=15)
    _X_over = _poly_over.fit_transform(_x.reshape(-1, 1))
    _Xpred_over = _poly_over.fit_transform(_xpred.reshape(-1, 1))
    _model_over = LinearRegression()
    _model_over.fit(_X_over, _y)
    _dfpred["y_over"] = _model_over.predict(_Xpred_over)

    _df_melted = pd.melt(
        _dfpred, id_vars=["x"], value_vars=["y", "y_under", "y_good", "y_over"]
    )
    _df_melted["description"] = _df_melted["variable"].map(
        {
            "y": "Données",
            "y_under": f"Sous-apprentissage (ECM: {np.mean((_dfpred.y - _dfpred.y_under) ** 2):.3f})",
            "y_good": f"Apprentissage correct (ECM: {np.mean((_dfpred.y - _dfpred.y_good) ** 2):.3f})",
            "y_over": f"Sur-apprentissage (ECM: {np.mean((_dfpred.y - _dfpred.y_over) ** 2):.3f})",
        }
    )

    _points = (
        alt.Chart(_df[["x", "y"]])
        .mark_circle(size=50)
        .encode(x="x", y="y", color=alt.value("black"))
    )

    _lines = (
        alt.Chart(_df_melted[_df_melted.variable != "y"])
        .mark_line()
        .encode(
            x="x",
            y="value",
            color=alt.Color(
                "description", scale=alt.Scale(range=["blue", "green", "red"])
            ),
        )
        .properties(width=400, height=400, title="Régression polynomiale")
    )

    _chart = alt.layer(_lines, _points)

    _chart.interactive()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### La validation croisée

    Elle consiste à séquentiellement, et de manière systématique, retirer des données, ajuster et évaluer. La méthode la plus courante est de séparer les données au hasard en un nombre $k$ de parties égales, fréquemment (pas toujours) au hasard — on parle alors de *k-fold cross-validation*. Séquentiellement, on garde un bloc pour l'évaluation et le reste pour l'ajustement. Une validation croisée à 10 plis donnera 10 indices d'erreur du modèle, donnant ainsi une distribution des erreurs selon les paramètres du modèle. Le nombre de plis est une décision de l'analyste. Le modèle correctement paramétré sera ensuite lissé sur l'ensemble des données... à moins qu'on ait le luxe d'avoir mis de côté des données test.

    ### L'entraînement et le test

    Le test suit le même principe que la validation croisée. On segmente les données en deux parties : l'un pour entraîner le modèle, l'autre pour le tester. On n'entraîne le modèle que sur les données d'entraînement, et on l'évalue sur les données de test. De cette manière, on évalue le modèle de manière réellement indépendante. La proportion de données à conserver pour l'entraînement est une décision d'analyste. Si on a suffisamment de données, on garde habituellement entre 50 et 70% des données pour l'entraînement.

    Que ce soit en validation ou en test, il faut porter une attention particulière au domaine des données modélisées. Si l'un des plis d'un *k-fold* contient beaucoup de données spéciales, les erreurs de validation croisée seront hétérogènes. De même, si toutes les données d'une catégorie se trouvent par hasard dans l'entraînement, le modèle ne sera pas testé sur cette catégorie, et si l'entière catégorie se trouve dans le test, le modèle ne sera pas entraîné pour elle. C'est ainsi qu'on parle souvent de biais raciaux ou genrés dans les modèles entraînés sur des hommes blancs.

    La collecte de données représentatives peut être insuffisante pour atténuer les biais. Dans ces cas, on pourra utiliser des algorithmes de stratification pour que les proportions de classes et les étalements des domaines (distribution des variables continues comme l'âge, le revenu, etc.) soient conservés lors de la séparation des données.  La stratification devient néanmoins complexe avec plusieurs variables ou des données très déséquilibrées.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transformation de données

    Certaines données sont utiles, pour un modèle, d'autres moins. Si certaines peuvent être utilisées telles qu'elles sont représentées, on gagnerait à en transformer d'autres. La sélection et la transformation des données préalablement à un modèle prend le nom d'*ingénierie des données*.

    ### Encodage catégoriel

    Dans le cas d'un modèle sur la taille des manchots, nous avions comme prédicteurs l'âge, la masse, le sexe et l'espèce. L'âge et la masse sont des variables numériques. Le sexe d'un manchot est une variable booléenne, représentée par un 0 ou un 1 (peu importe à quel sexe on attribue le 0 ou le 1, tant que l'encodage booléen est systématique).

    L'espèce est une variable catégorielle, qui peut être encodée en plusieurs colonnes booléennes (une par espèce, avec 1 indiquant l'appartenance). On retire généralement une colonne de référence, son appartenance pouvant être étant déduite là où l'on ne retrouve que des 0 (pour $D$ catégories, on a $D-1$ degrés de liberté).

    ### Log

    Le log permet de donner plus de poids aux faibles valeurs, et respecte plus strictement les cas de distributions asymétriques positives. L'âge et la masse des manchots ne peuvent être négatives. Dans le cas de ce modèle, il pourrait valoir la peine d'en extraire le log avant de standardiser les données.

    ### Standardisation

    Parfois appelée *normalisation*, la transformation consiste à soustraire la moyenne de chaque observation, puis de diviser le résultat par l'écart-type.


    $$Z = \frac{X - \mu}{\sigma}$$

    Si on l'applique à toutes les variables numériques de la matrice $X$, on obtient un tableau dans lequel le poids des variables est égal. C'est particulièrement important pour les modèles dans lesquels l'ampleur des variables est important.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Modèles

    Un modèle est une maquette qui représente ce qu'il décrit de manière simplifiée. En mathématiques et en science des données, les modèles sont souvent utilisés pour la prédiction. Parmi eux figurent les réseaux de neurones, mais il existe bien d'autres types de modèles prédictifs.

    ### Les *k*-proches voisins

    Le modèle des *k*-proches voisins (KNN) suppose que les observations voisines sont similaires. Par exemple, pour prédire l'altitude d'un point donné, on identifie les *k* points les plus proches et on calcule la moyenne de leurs altitudes. Le choix du nombre de voisins ($k$) et de la mesure de distance utilisée est crucial: un petit $k$ rend le modèle sensible aux variations dans l'environnement immédiat d'un point, et inversement si $k$ est trop élevé. Ce modèle est particulièrement efficace en géomatique, où la distance euclidienne a une signification claire. La standardisation des données est toutefois cruciale pour bien calculer les distances.

    ### Les arbres de décision

    Un arbre de décision est une séquence hiérarchique de choix booléens qui mènent à une décision finale. La décision est la variable cible, $y$, et l'arbre étant conçu pour que chaque décision corresponde le plus possible à celle des données. La cible peut être une catégorie ou un nombre, mais dans le cas du nombre les prédictions d'un arbre donnent une moyenne pour le cas passant à travers l'arbre. Les arbres de décisions sont simples à calculer, mais leur plus grand avantage est leur interprétabilité: un modèle simple peut être imprimé et facilement audité, contrairement aux boîtes noires.

    ### Les forêts aléatoires

    Les forêts aléatoires combinent plusieurs arbres de décision, chacun formé à partir d'un sous-ensemble des données tiré aléatoirement, avec remplacement (un procédé que l'on nomme le *bootstrapping*). Afin de rendre le processus encore plus exploratoire, les *features* sont resélectionnées au hasard à chaque embranchement de chaque arbre. La prédiction finale est obtenue par vote majoritaire (classification) ou moyenne (régression) des différents arbres. Ce modèle est robuste et bien adapté aux données spatiales corrélées.

    ### Le *gradient boosting*

    Le *gradient boosting* est un algorithme d'ensemble comme les forêts aléatoires, mais au lieu de moyenner des arbres indépendants, il les construit séquentiellement. Chaque nouvel arbre apprend à corriger les erreurs résiduelles de l'ensemble précédent. Cette approche additive est mathématiquement élégante et produit souvent de meilleures performances que les forêts aléatoires, particulièrement avec des données limitées. Alors que les forêts aléatoires sont parallélisables (chaque arbre peut être calculé indépendamment de l'autre), le *gradient boosting* doit attendre le résultat de l'arbre précédent pour calculer le suivant.

    Si l'objectif est une régression plutôt qu'une classification, sachez que les arbres de décision et les KNN sont des algorithmes générant des sorties discontinues, en palier. Les processus gaussiens et les réseaux de neurones retournent plutôt des sorties lisses.

    ### Les processus gaussiens

    Les processus gaussiens sont une extension du concept de loi normale à un nombre infini de dimensions, modélisant ainsi la corrélation dans l'espace des variables. Ils généralisent le krigeage (une méthode d'interpolation) et utilisent le théorème de Bayes pour offrir un avantage significatif : prédire non seulement une valeur, mais aussi son incertitude sous forme de distribution.

    ### Les réseaux de neurones

    Un réseau de neurones classique (séquentiel) se compose d'un empilement de couches neuronales. Chaque couche effectue un produit matriciel par multiplication avec des poids et l'addition d'un intercept (un *biais*), suivi d'une transformation via une fonction d'activation. Pour des tâches plus complexes, il est possible d'intégrer des couches spécialisées. L'*architecture* du réseau de neurones peut être adaptée aux exigences spécifiques de la modélisation, en combinant par exemple des séries temporelles, des données statiques ou des analyses d'image. Aujourd'hui, ils sont largement utilisés pour analyser des images satellites, classer l'occupation du sol et prédire des phénomènes non-linéaires. Bien que nécessitant de grandes quantités de données et une expertise avancée, les réseaux de neurones sont capables de modéliser des relations spatiales complexes en géomatique.

    | Modèle | Utilisation |
    |--------|-------------|
    | *k*-proches voisins | Modèle *baseline*, démonstrations académiques |
    | Arbres de décision | Règles de décision explicites |
    | Forêts aléatoires | Robuste et parallélisables |
    | Gradient boosting | Polyvalent |
    | Processus gaussiens | Quantification de l'incertitude et krigeage |
    | Réseaux de neurones | Données volumineuses et calculs complexes |

    Assez de théorie. Passons à un tutoriel sur *Scikit-learn*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Flux de travail

    Voici en général en quoi consiste un flux de travail en auto-apprentissage.
    """)
    return


@app.cell
def _(mo):
    mo.image("images/ml_.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tutoriel

    > inspiré d'[un tutoriel plus avancé que j'ai publié sur Nextjournal](https://nextjournal.com/essicolo/spatial-prediction-of-soil-pollutants-with-multi-output-gaussian-processes)

    ![](https://upload.wikimedia.org/wikipedia/commons/3/32/Meuse_Montherme.jpg)

    <small>[Fleuve Meuse, crédit Pierre Lavaurs](https://fr.wikipedia.org/wiki/Meuse_%28fleuve%29)</small>

    Le [fleuve Meuse](https://www.openstreetmap.org/#map=12/50.9619/5.7327) coule à travers l'Allemagne, les Pays-Bas, la Belgique et la France. Plusieurs industries se sont installées sur ses rives, ce qui a entraîné une pollution de son lit ainsi que des sols riverains par des métaux. Une zone située au nord de Maastricht, aux Pays-Bas, est souvent utilisée comme cas d'étude en géostatistique. Ce tutoriel passe par une série d'étapes :

    1. afficher des données géographiques sur un fond cartographique,
    2. effectuer des requêtes spatiales,
    3. modéliser des attributs spatiaux avec des processus gaussiens,
    4. projeter des attributs spatiaux sur une carte de fond.
    """)
    return


@app.cell
def _(pd):
    meuse_df = pd.read_csv("data/meuse.csv")
    meuse_df.head()
    return (meuse_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le site Web distribuant l'ensemble de données de la Meuse indique que les coordonnées `x` et `y` sont projetées dans le système `proj4: +init=epsg:28992`. Si nous nous intéressons uniquement à la modélisation, nous n'aurions pas besoin de nous soucier beaucoup du système de coordonnées. Mais comme nous nous intéressons au traçage des données sur une carte et à l'exécution ultérieure de requêtes spatiales, spécifions à *GeoPandas* que `x` et `y` sont des géométries de points exprimées dans le CRS 28992, puis transformons-les en coordonnées angulaires de longitude-latitude avec la référence WGS84.
    """)
    return


@app.cell
def _(gpd, meuse_df):
    meuse_gdf = (
        gpd.GeoDataFrame(
            meuse_df, geometry=gpd.points_from_xy(meuse_df["x"], meuse_df["y"])
        )
        .set_crs(crs=28992)
        .to_crs(crs=4326)
    )
    meuse_gdf.head()
    return (meuse_gdf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les points d'échantillonnage se trouvent sur la rive d'un méandre.
    """)
    return


@app.cell
def _(meuse_gdf):
    # Extraire les points de la géométrie, pour qu'ils soient lisibles dans vega-altair
    meuse_gdf["lon"] = meuse_gdf.geometry.x
    meuse_gdf["lat"] = meuse_gdf.geometry.y
    meuse_gdf
    return


@app.cell
def _(lp, meuse_gdf, tilesets):
    (
        lp.ggplot()
        + lp.geom_livemap(zoom=13, tiles=tilesets.OSM)
        + lp.geom_point(data=meuse_gdf, mapping=lp.aes(x="lon", y="lat"), alpha=0.8)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Effectuer des requêtes spatiales

    La colonne `dist` du tableau `meuse_gdf` contient l'information de la distance entre la rivière et l'échantillon. Cependant, si nous souhaitons évaluer la distance en tout point du domaine d'application de notre modèle, afin de faire ensuite nos projections dans l'espace, nous devrons être capables de calculer la distance à la rivière.

    Nous travaillons ici avec des coordonnées géographiques (longitude, latitude), que nous approximons sous forme de données géométriques. À cette échelle et pour notre usage, c'est approprié. Mais à plus petite échelle, proche des pôles, ces distances pourraient être déformées.

    Nous aurons besoin de la forme de la rivière pour calculer la distance à celle-ci en tout point. J'ai tracé une ligne à la souris et au clic dans QGIS le long du centre de la rivière. Comme une ligne est difficile à manipuler avec un csv, je l'ai exportée au format geojson, qui peut être importé sans peine avec GeoPandas.
    """)
    return


@app.cell
def _(gpd):
    river = gpd.read_file("data/river.geojson")
    river.plot()
    return (river,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Utilisons la fonction `distance` de *GeoPandas* dans une boucle sur chaque observation. J'ai attribué une nouvelle colonne nommée `distance_river`.
    """)
    return


@app.cell
def _(lp, meuse_gdf, river):
    meuse_gdf_dr = meuse_gdf.assign(
        distance_river=[
            meuse_gdf["geometry"][i].distance(river["geometry"][0])
            for i in range(meuse_gdf.shape[0])
        ]
    )

    lp.ggplot(meuse_gdf_dr) + lp.geom_point(lp.aes(x="dist", y="distance_river"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le graphique montre que les distances sont comparables.

    ### Modéliser les attributs spatiaux

    Cette partie est probablement la plus difficile. Notre flux de travail est le suivant.

    1. Affecter les observations à l'entraînement et aux tests
    1. Prétraiter les données (normaliser à 0 moyenne et 1 variance)
    1. Créer et ajuster le modèle avec les **processus gaussiens**
    1. Prédire et critiquer le modèle
    1. Utiliser le modèle

    #### 1. Affecter les données à l'entraînement et au test

    Il s'agit d'une étape nécessaire pour vérifier si le modèle est bon pour prédire à des endroits inconnus du modèle. La séparation doit être effectuée de manière aléatoire, mais il est parfois avisé de s'assurer d'une séparation stratifiée par classe. Dans notre cas, nous devrions être en mesure de prédire les concentrations peu importe la distance par rapport au lit de la rivière. Conservons 70 % des données en formation, le reste en test.
    """)
    return


@app.cell
def _(meuse_gdf, pd):
    from sklearn.model_selection import train_test_split

    meuse_gdf["dist_class"] = pd.qcut(meuse_gdf["dist"], q=4).astype(str)
    train_df, test_df = train_test_split(
        meuse_gdf,
        train_size=0.7,
        stratify=meuse_gdf[
            "dist_class"
        ],  # pour s'assurer d'un équilibre entre les distances de la rivière
        random_state=695185,  # random.org
    )

    # ajouter l'indice comme nouvelle colonne
    meuse_gdf["ensemble"] = "test"  # par défaut tout est test
    meuse_gdf.loc[train_df.index, "ensemble"] = "train"
    return test_df, train_df


@app.cell
def _(lp, pd, test_df, train_df):
    train_df["set"] = "train"
    test_df["set"] = "test"
    _combined_df = pd.concat([train_df, test_df])
    _combined_df_long = _combined_df[[
        "lon", "lat", "dist", "cadmium", "copper", "lead", "zinc", "set"
    ]].melt(id_vars=["set", "lon", "lat", "dist"])

    _combined_df_long

    (
        lp.ggplot(_combined_df_long, lp.aes(x="variable", y="value", fill="set"))
        + lp.facet_wrap(facets="variable", scales="free", nrow=2)
        + lp.geom_violin(alpha=0.5)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2. Prétraiter les données

    Afin de rendre tout le flux de travail indépendant de l'ensemble *test*, il est préférable de séparer les ensembles avant le prétraitement. De cette manière, on effectuera par exemple une standardisation basée sur les statistiques de l'ensemble d'entraînement seulement.

    Identifions, à cette étape, les variables qui serviront à prédire, les  caractéristiques (*features*), et les variables qui seront prédites, les cibles (*targets*).
    """)
    return


@app.cell
def _():
    targets = ["cadmium", "copper", "lead", "zinc"]
    features = ["lon", "lat", "dist"]
    return features, targets


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    L'ensemble de données contient d'autres informations utiles pour prédire les polluants du sol. Nous aurions pu utiliser l'altitude, la fréquence des inondations, le type de sol, etc. Mais n'oublions pas que si nous souhaitons prédire les polluants à n'importe quel endroit de notre carte, nous devons également fournir les valeurs de chaque *feature* à n'importe quel endroit. Que feriez-vous pour les obtenir ? Pensez-y 30 secondes...

    ⏲️

    Pour les variables catégorielles (par exemple le sol), vous pourriez dessiner des polygones dans votre SIG pour délimiter des zones et effectuer des requêtes spatiales pour attribuer la catégorie à l'enceinte d'un polygone. Mais cela serait impossible pour les variables numériques. Dans tous les cas (catégories et numériques), vous pourriez créer un modèle spatial simple, par exemple un modèle *k*-nearest neighbors avec la variable d'intérêt (par exemple `elev`) comme *target* et la position (`lon` et `lat`), puis utiliser ce modèle pour prédire à n'importe quel endroit ce qui deviendrait une entité pour le modèle de polluant du sol. Ce faisant, vous devez adapter le modèle de polluant du sol aux résultats de votre premier modèle spatial, et non aux points d'origine.

    Nous ne le ferons pas ici, car cela ne ferait que compliquer l'approche - nous nous en tiendrons à la position et à la distance par rapport à la rivière comme *features*. Nous gardons la colonne `ensemble` puisqu'elle nous sera utile pour filtrer les données.
    """)
    return


@app.cell
def _(features, meuse_gdf, targets):
    XY = meuse_gdf[targets + features + ["ensemble"]]
    XY
    return (XY,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La standardisation peut très bien être effectuée en calculant la moyenne et l'écart-type, avec *Numpy* ou *Pandas*, mais *Scikit-learn* offre des outils propices au prétraitement, comme `StandardScaler`.
    """)
    return


@app.cell
def _(XY, features, meuse_gdf, pd, targets):
    from sklearn.preprocessing import StandardScaler

    scalerX = StandardScaler().set_output(transform="pandas")  # on veut générer un tableau et non une matrice
    scalerX.fit(XY.query("ensemble == 'train'")[features])
    X_sc = scalerX.transform(XY[features])

    scalerY = StandardScaler().set_output(transform="pandas")
    scalerY.fit(XY.query("ensemble == 'train'")[targets])
    Y_sc = scalerY.transform(XY[targets])

    XY_sc = pd.concat([X_sc, Y_sc], axis=1)

    XY_sc["ensemble"] = meuse_gdf["ensemble"]
    return XY_sc, scalerX, scalerY


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Isolons nos tableaux d'entraînement et de test, ainsi que nos tableaux de *features* et de *targets*.
    """)
    return


@app.cell
def _(XY_sc, features, targets):
    # features, train
    Xsc_tr = XY_sc.query("ensemble == 'train'").drop(columns="ensemble")[features]

    # features, test
    Xsc_te = XY_sc.query("ensemble == 'test'").drop(columns="ensemble")[features]

    # targets, train
    Ysc_tr = XY_sc.query("ensemble == 'train'").drop(columns="ensemble")[targets]

    # targets, test
    Ysc_te = XY_sc.query("ensemble == 'test'").drop(columns="ensemble")[targets]
    return Xsc_te, Xsc_tr, Ysc_te, Ysc_tr


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Les valeurs de concentration sont des données compositionnelles. Habituellement, je les aurais transformées en ratios logarithmiques avant la mise à l'échelle, mais cela aurait compliqué ce flux de travail. Pour plus d'informations, lisez [Why, and How, Should Geologists Use Compositional Data](https://en.wikibooks.org/wiki/Why,_and_How,_Should_Geologists_Use_Compositional_Data_Analysis), par Ricardo A. Valls (2008).

    #### 3. Créer les modèles

    Les processus gaussiens sont particulièrement adaptés aux géostatistiques. À la différence des semi-variogrammes, qui demandent des postulats rigides sur les modèles, les processus gaussiens, basés sur les fonctions de covariance ou *kernels*, restent flexibles. Des APIs avancés pour les processus gaussiens permettent de modéliser plusieurs sorties corrélées par *corégionalisation*. Bien que *scikit-learn* propose des processus gaussiens multi-sortie, il s'agit en fait de sorties indépendantes. Afin de montrer la flexibilité de l'API de *scikit-learn*, nous allons également utiliser des réseaux de neurones.

    Définissons d'abord la validation croisée.
    """)
    return


@app.cell
def _():
    from sklearn.model_selection import cross_validate
    from sklearn.model_selection import KFold

    cv = KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_validate, cv


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lançons la validation croisée. Elle peut servir à modifier les paramètres du modèle. De bons paramètres réduisent l'écart entre les scores d'entraînement et de test.
    """)
    return


@app.cell
def _(mo):
    length_scale = mo.ui.slider(0.1, 3.0, 0.1, value=2.0, label="length scale")
    log_alpha = mo.ui.slider(-2, 1, 0.1, value=-0.5, label="log alpha")
    return length_scale, log_alpha


@app.cell
def _(length_scale):
    length_scale
    return


@app.cell
def _(log_alpha):
    log_alpha
    return


@app.cell
def _(Xsc_tr, Ysc_tr, cross_validate, cv, length_scale, log_alpha, np):
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import Matern, WhiteKernel

    kernel = Matern(length_scale=length_scale.value, length_scale_bounds=[0.01, 10.0])
    gpr = GaussianProcessRegressor(kernel=kernel, alpha=np.exp(log_alpha.value), random_state=0)

    _cv_results = cross_validate(
        gpr, Xsc_tr, Ysc_tr, cv=cv, scoring="r2", return_train_score=True
    )
    _cv_results
    return (gpr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Une fois que le modèle est satisfaisant, nous pouvons lancer le véritable ajustement.
    """)
    return


@app.cell
def _(Xsc_te, Xsc_tr, Ysc_te, Ysc_tr, gpr):
    gpr.fit(Xsc_tr, Ysc_tr)
    gpr.score(Xsc_te, Ysc_te)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les réseaux de neurones ne sont pas plus compliqués à utiliser. La classe `MPLPRegressor` (MLP, *Multi-Layer Perceptron*) prend comme argument central un tuple dont la longueur est le nombre de couches et dont chaque chiffre est le nombre de neurones dans la couche.
    """)
    return


@app.cell
def _(Xsc_tr, Ysc_tr, cross_validate, cv):
    from sklearn.neural_network import MLPRegressor

    mlp = MLPRegressor(
        hidden_layer_sizes=(30, 30),
        activation="relu",
        max_iter=1000,
        random_state=0,
    )

    _cv_results = cross_validate(
        mlp, Xsc_tr, Ysc_tr, cv=cv, scoring="r2", return_train_score=True
    )
    _cv_results
    return (mlp,)


@app.cell
def _(Xsc_te, Xsc_tr, Ysc_te, Ysc_tr, mlp):
    mlp.fit(Xsc_tr, Ysc_tr)
    mlp.score(Xsc_te, Ysc_te)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visualiser les valeurs prédites en fonction des valeurs observées permet d'évaluer s'il y a des écarts importants sur certaines parties du domaine de prédiction.
    """)
    return


@app.cell
def _(Xsc_te, Ysc_te, alt, gpr, mlp, pd):
    Ysc_te_gprpred = pd.DataFrame(
        gpr.predict(Xsc_te), columns=Ysc_te.columns
    ).melt()
    Ysc_te_gprpred["observed"] = Ysc_te.melt()["value"]
    Ysc_te_gprpred["model"] = "gpr"

    Ysc_te_mlppred = pd.DataFrame(
        mlp.predict(Xsc_te), columns=Ysc_te.columns
    ).melt()
    Ysc_te_mlppred["observed"] = Ysc_te.melt()["value"]
    Ysc_te_mlppred["model"] = "mlp"

    Ysc_te_pred = pd.concat([Ysc_te_gprpred, Ysc_te_mlppred])

    _base = alt.Chart(Ysc_te_pred).encode(x="observed", y="value")

    alt.layer(
        _base.mark_point(),  # points
        _base.mark_line(color="red").encode(y="observed"),  # ligne diagonale
    ).facet(column="variable", row="model").configure_view(
        continuousWidth=150, continuousHeight=150
    )

    Ysc_te_pred
    return (Ysc_te_pred,)


@app.cell
def _(Ysc_te_pred, lp):
    (
        lp.ggplot(Ysc_te_pred)
        + lp.facet_wrap(facets="variable")
        + lp.geom_point(lp.aes(x="observed", y="value", color="model"), alpha=0.5)
        + lp.geom_abline(intercept=0, slope=1)
        + lp.ggsize(height=400, width=500)
        + lp.theme_minimal()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les deux modèles performent plutôt bien. Nous ne retiendrons que le modèle par processus gaussien pour la suite.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 4. Utiliser le modèle

    Créer une grille...
    """)
    return


@app.cell
def _(gpd, np, pd):
    import itertools

    def expand_grid(data_dict):
        rows = itertools.product(*data_dict.values())
        return pd.DataFrame.from_records(rows, columns=data_dict.keys())


    gridres = 0.001  # grid resolution : could be finer
    lon_grid = np.arange(5.71, 5.77, gridres)
    lat_grid = np.arange(50.95, 51.0, gridres)

    squaregrid = expand_grid({"lon": lon_grid, "lat": lat_grid})

    squaregrid = gpd.GeoDataFrame(
        squaregrid,
        geometry=gpd.points_from_xy(squaregrid.lon, squaregrid.lat),
        crs="EPSG:4326",
    )
    squaregrid
    return (squaregrid,)


@app.cell
def _(lp, squaregrid, tilesets):
    (
        lp.ggplot()
        + lp.geom_livemap(zoom=13, tiles=tilesets.OSM)
        + lp.geom_point(data=squaregrid, mapping=lp.aes(x="lon", y="lat"), alpha=0.8, size=1)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cette grille s'étend au-delà de notre modèle. Prédire les concentrations sur la rive Ouest de la rivière est risqué, puisque nous ne disposons de données qu'entre la rive Est et le canal. J'ai dessiné un polygone avec QGIS, je l'ai exporté au format geojson. Nous pouvons filtrer les points de grille en écartant les points hors du polygone.
    """)
    return


@app.cell
def _(gpd, lp, squaregrid, tilesets):
    geo_polygon = gpd.read_file("data/polygon.geojson")

    grid_gdf = gpd.sjoin(squaregrid, geo_polygon, predicate="within")

    (
        lp.ggplot()
        + lp.geom_livemap(zoom=13, tiles=tilesets.OSM)
        + lp.geom_point(data=grid_gdf, mapping=lp.aes(x="lon", y="lat"), alpha=0.8, size=1)
    )
    return (grid_gdf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Calculons la distance de la rivière pour chaque point de grille.
    """)
    return


@app.cell
def _(grid_gdf, lp, river, tilesets):
    grid_dist = grid_gdf.assign(
        dist=[
            grid_gdf["geometry"][i].distance(river["geometry"][0])
            for i in grid_gdf.index
        ]
    )

    (
        lp.ggplot(grid_dist)
        + lp.geom_livemap(zoom=13, tiles=tilesets.OSM)
        + lp.geom_tile(mapping=lp.aes(x="lon", y="lat", fill="dist"), alpha=0.8)
        + lp.scale_fill_brewer(type = 'seq', palette = 'Reds')
    )
    return (grid_dist,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour obtenir des résultats conformes, on doit formater les *features* de la grille de la même manière qu'on l'a fait pour les données sur lesquelles le modèle s'est entraîné.
    """)
    return


@app.cell
def _(features, grid_dist, scalerX):
    grid_distsc = scalerX.transform(grid_dist[features])
    return (grid_distsc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Effectuons la prédiction pour la matrice `grid_distsc`.
    """)
    return


@app.cell
def _(gpr, grid_dist, grid_distsc, pd, scalerY, targets):
    Ypred_sc = gpr.predict(grid_distsc)
    if Ypred_sc.ndim == 1:
        Ypred_sc = Ypred_sc.reshape(-1, 1)
    Ypred = scalerY.inverse_transform(Ypred_sc)
    Ypred = pd.DataFrame(Ypred, columns = targets)
    meuse_pred = (
        pd.concat([grid_dist.reset_index(drop=True), Ypred.reset_index(drop=True)], axis=1)
        .drop(columns=["geometry", "index_right", "id", "dist"])
        .melt(id_vars=["lon", "lat"])
    )
    meuse_pred
    return (meuse_pred,)


@app.cell
def _(length_scale):
    length_scale
    return


@app.cell
def _(log_alpha):
    log_alpha
    return


@app.cell
def _(lp, meuse_gdf, meuse_pred):
    meuse_gdf_melt = meuse_gdf.melt(id_vars=["lon", "lat"])

    def plot_predictions(metal):
        p = (
            lp.ggplot() 
            + lp.geom_livemap(tiles=lp.tilesets.OSM) 
            + lp.scale_fill_brewer(type='seq', palette='Reds') 
            + lp.geom_tile(
                data=meuse_pred.loc[meuse_pred["variable"] == metal, :], 
                mapping=lp.aes('lon', 'lat', fill='value')
            )
            + lp.geom_point(
                data=meuse_gdf_melt.loc[meuse_gdf_melt["variable"] == metal, :], 
                mapping=lp.aes('lon', 'lat', fill='value'),
                size=2,
                shape=21
            )
            + lp.ggtitle(metal)
        )
        return p

    plots = [plot_predictions(metal) for metal in ['cadmium', 'copper', 'lead', 'zinc']]
    lp.gggrid(plots, ncol=2) + lp.ggsize(800, 800)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercice

    Chargez les données `data/penguis.csv` et tentez de prédire l'espèce de manchot selon les propriétés mesurées.
    """)
    return


@app.cell
def _(pd):
    pd.read_csv("data/penguins.csv")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
