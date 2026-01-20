import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Visualisation géospatiale

    La section 4 était dédiée à l'utilisation de Altair pour la visualisation générale. Altair peut aussi être utilisée pour la visualisation géospatiale grâce au marqueur `mark_geoshape()`, bien intégré à GeoPandas. Nous ne l'utiliserons pas, car en géomatique, il existe de meilleures options.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Les graphiques avec *Matplotlib*

    *Matplotlib* a été créée en 2003 comme équivalent Python des modules graphiques de Matlab. *Matplotlib* a par la suite pris son propre chemin, mais reste un module difficile à utiliser, chargé de son histoire. C'est *Matplotlib* qui est appelé lorsque l'on utilise les méthodes `.plot()` de *Pandas* et *Geopandas*.
    """)
    return


@app.cell
def _(gpd):
    hvdq = gpd.read_file(
        "https://www.donneesquebec.ca/recherche/dataset/b4893e20-3a65-44fe-a428-68c79e303fb4/resource/fcdd3e3b-b6dc-45ae-9e88-542b842b1774/download/vdq-hydrobassinversant.geojson"
    )
    hvdq
    return (hvdq,)


@app.cell
def _(hvdq):
    hvdq.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La méthode `.explore()` des objets `GeoDataFrame` permet quant à elle un affichage interactif, qui passe par la librairie cartographique *[Folium](https://python-visualization.github.io/folium/latest/)*, elle-même basée sur la librairie Javascript Leaflet.
    """)
    return


@app.cell
def _(hvdq):
    hvdq.explore()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Il existe de nombreues options de modélisation en Python. *Matplotlib* est la base, et comme *GeoPandas*, plusieurs packages l'utilisent pour créer des graphiques spécialisés. *Contextily* permet d'ajouter des fonds de carte à *Matplotlib*. *Altair*, ou *Vega-Altair* vient avec *Marimo*, et permet de générer des visualisations de manière impérative. Le package `altair_tiles` permet d'ajouter des fonds de carte, mais so développement n'est pas abouti. La suite *Holoviews*, dont fait partie *Geoviews*, est aussi un puissant outil de visualisation, tout comme le package montréalais *Plotly* ou bien l'implémentation en Python du package JavaScript ObservablePlot, `pyobsplot`. *GeoPandas* utilise aussi *Folium* pour l'affichage interactif. Mais le package que nous allons préférer ici est *Lets-Plot*, qui offre une interface souple et intuitive, apte à générer rapidement des graphiques simples comme avancés pour l'exploration et la publication.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Altair n'est pas le package idéal pour les données géographiques. Il faudra confogurer marimo pour afficher toutes les  données `hdvq`, les propriétés de la carte restent peu intuitives à définir, et pour obtenir un fond de carte, il faudra installer le package supplémentaire `altair_tiles`.
    """)
    return


@app.cell
def _(alt, hvdq):
    carte = (
        alt.Chart(hvdq.sample(50))
        .mark_geoshape(fillOpacity=0.1, stroke="green", strokeWidth=2)
        .project(type="identity", reflectY=True)
        .properties(width=600, height=400)
    )
    carte
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lets-Plot

    Lets-Plot offre une interface déclarative pour la visualisation géospatiale en Python. Le package permet de créer des graphiques statiques et interactifs, avec un bon support pour les données géospatiales.
    """)
    return


@app.cell
def _(hvdq, lp):
    (
        lp.ggplot()
        + lp.geom_polygon(data=hvdq, mapping=lp.aes(fill="NIVEAU"))
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le principe de construction d'un graphique Lets-Plot est le suivant.

    ```
    graphique = (
        lp.ggplot(data=df, mapping=lp.aes(x='colonne_x', y='colonne_y'))
        + lp.geom_<type>()  # Ajout de géométries
        + lp.scale_<type>()  # Modification des échelles
        + lp.theme_<type>()  # Personnalisation du thème
        + lp.labs()          # Ajout de titres et labels
    )
    ```

    Le mapping esthétique associe les colonnes de données aux propriétés visuelles. Lorsque spécifié dans `lp.ggplot()`, le mapping est global et peut être alété localement dans les couche `lp.geom_<type>()`. Voici les attributs les plus courrants du mapping.

    ```
    lp.aes(
        x='longitude',        # Position horizontale
        y='latitude',         # Position verticale
        color='categorie',    # Couleur selon une variable
        size='population',    # Taille selon une variable
        fill='region',        # Remplissage
        alpha='densite',      # Transparence
        shape='type'          # Forme des points
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les géométries `geom_<type>()` placent des éléments graphiques sur le canevas dans l'ordre spécifié. Il en existe de nombreux types, décrits dans la documentation de *Lets-Plot*. En voici quelques uns.

    ```
    + lp.geom_point(size=3, alpha=0.7)
    + lp.geom_line(linetype='dashed', size=1.5)
    + lp.geom_bar(stat='identity', position='dodge')
    + lp.geom_histogram(bins=30, fill='blue', alpha=0.5)
    + lp.geom_boxplot(outlier_color='red')
    + lp.geom_density(fill='lightblue', alpha=0.3)
    + lp.geom_text(label='nom_ville', size=8, nudge_y=0.1)
    ```

    Et d'autres pour la cartographie.

    ```
    + lp.geom_polygon(aes(fill='population'), color='white', size=0.5)
    + lp.geom_map(aes(fill='valeur'), map=geodf)
    + lp.geom_density2d(aes(x='lon', y='lat'))
    + lp.geom_livemap(tiles='osm')  # OpenStreetMap
    ```

    Par exemple, avec le quartet d'Anscombe - un exemple classique de corrélations inadaptée.
    """)
    return


@app.cell
def _(pd):
    anscombes = pd.read_csv("data/anscombes.csv")
    anscombes.sample(10)
    return (anscombes,)


@app.cell
def _(anscombes, lp):

    (
        lp.ggplot(data=anscombes, mapping=lp.aes(x='x', y='y'))
        + lp.geom_smooth(method='lm', color='#666', size=0.5)
        #+ lp.geom_line(color='#A22CA8', size=1.0)
        + lp.geom_point()
        #+ lp.facet_wrap(facets='dataset')
        + lp.labs(title="Le quartet d'Anscombe")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Excercice: activez la ligne `lp.facet_wrap()` pour comprendre comment une information négligée peu mener à des conclusions trompeuses.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Facettage

    Le facettage permet de segmenter les graphiques en panneaux selon une colonne catégorielle. Il est intégré dans Lets-Plot grâce aux fonctions `lp.facet_wrap()`, qui découpe le graphique en différentes *facettes*, ou panneaux, et `lp.facet_grid()`, qui crée une grille 2D. Voici un exemple en cartographie avec `facet_wrap()`.
    """)
    return


@app.cell
def _(hvdq, lp):
    (
        lp.ggplot()
        + lp.geom_polygon(data=hvdq)
        + lp.facet_wrap(facets="NIVEAU", nrow=1)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fond de carte

    Avec Lets-Plot, la couche `lp.geom_livemap()` doit toujours être placée en premier lors de la construction d'un graphique, à défaut de quoi une erreur apparait. Pour bien voir le fond de carte, on peut ajouter une transparence statique, c'est-à-dire que le canal alpha (qui par convention est le terme utilisé pour la transparence) n'est pas relié à une colonne du tableau dans un argument `mapping=lp.aes(alpha=...)`. Le niveau de zoom est haituellement obtenu par tâtonnement.
    """)
    return


@app.cell
def _(hvdq, lp):
    (
        lp.ggplot()
        + lp.geom_livemap(zoom=9)
        + lp.geom_polygon(data=hvdq, alpha=0.4, size=0.3)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Des points

    Lets-Plot reconnaîtra le mapping des objets géométriques. Par exemple, `lp.geom_point()` trouvera tout seul la colonne de géométrie, et placera les points sur les bons axes avec le bon système de coordonnées.
    """)
    return


@app.cell
def _(gpd):
    stations = gpd.read_file("data/resultat.json")
    stations
    return (stations,)


@app.cell
def _(lp, stations):
    (
        lp.ggplot()
        + lp.geom_livemap(zoom=5)
        + lp.geom_point(data=stations)
        + lp.coord_map() # les axes sont de même dimensions
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lets-Plot générique

    Lets-Plot est un package générique. Sa grammaire graphique est intuitive et flexible. Elle permet d'afficher de nombreux types de graphiques, géospatiaux ou non. Pour plus d'exemples, https://lets-plot.org/index.html
    """)
    return


@app.cell
def _(pd):
    rivchaud = pd.read_csv("https://raw.githubusercontent.com/essicolo/ecologie-mathematique-R/refs/heads/master/data/023402_Q.csv", parse_dates=["Date"], dayfirst=False)
    rivchaud
    return (rivchaud,)


@app.cell
def _(lp, rivchaud):
    (
        lp.ggplot(
            data=rivchaud[
                (rivchaud["Date"] > "1990-01-01") &
                (rivchaud["Date"] < "1995-01-01")
            ],
            mapping=lp.aes(x="Date", y="Débit")
        )
        + lp.geom_line()
        + lp.geom_hline(yintercept=500, color="#ff13a0")
        + lp.theme_bw()
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import geopandas as gpd
    import altair as alt
    import lets_plot as lp
    lp.LetsPlot.setup_html()
    return alt, gpd, lp, mo, pd


if __name__ == "__main__":
    app.run()
