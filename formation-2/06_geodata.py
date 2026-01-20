import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 6. Données géospatiales

    Les données spatialisées sont associées à un ou plusieurs géométries localisés selon un système géodésique. Avec les librairies appropriées, Python devient un système d'information géographique complet... à l'exception de l'interface visuel classique manipulable avec un pointeur (souris). Les modules dont nous aurons besoin sont

    - *GeoPandas*, pou manipuler des données vectorielles,
    - *Rioxarray*, pour la manipulation de données raster,
    - *Matplotlib*, *Altair* et *Lets-Plot* pour créer des graphiques
    - *Planetary computer*, *Open meteo* et *CDS API*, par exemple, pour télécharger des données géospatiale,
    - *Scikit-learn* pour la prédiction et la modélisation.

    La section 6 vous permettra de comprendre la structure et la manipulation des données tabulaires et spatiales en Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## *GeoPandas*

    La formation 1, destinée aux personnes débutantes en Python, prenait le package *Polars* comme outil d'exploration de données. *Polars* offre une interface rapide, moderne et intuitive, mais ne supporte toujours pas les données géospatiales ([le projet GeoPolars a été suspendu](https://github.com/geopolars/geopolars)). L'outil de tableaux *Pandas*, qui précède *Polars* et s'avère moins efficace et moins intuitif, est néanmoins équipé pour la géomatique avec *GeoPandas*, une extension qui permet l'ajout des colonnes contenant des items géométrique. Dès qu'un élément géographique est indéré, l'objet `pandas.DataFrame` devient un objet `geopandas.GeoDataFrame`, qui inclut un attribut `.crs` (*coordinate reference system*) - le système géodésique associé à l'élément géographique. La librairie `geopandas` est conventionnellement chargée avec l'alias `gpd`. La fonction `gpd.read_*()` peut charger dans la session de calcul des shapefiles, geojson et des tables PostGIS. Chargeons, par exemple, un geojson gracieuseté d'Hydro-Québec.
    """)
    return


@app.cell
def _():
    import geopandas as gpd

    url_geojson = "https://www.donneesquebec.ca/recherche/dataset/b4893e20-3a65-44fe-a428-68c79e303fb4/resource/fcdd3e3b-b6dc-45ae-9e88-542b842b1774/download/vdq-hydrobassinversant.geojson"
    hydro_vdq = gpd.read_file(url_geojson)
    hydro_vdq.head()
    return gpd, hydro_vdq


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Je n'ai affiché que la première ligne, puisque l'objet `POLYGON` comprend un trop grand nombre de points pour être consulté aisément. L'objet `hydro_vdq_` est de type `GeoDataFrame`.
    """)
    return


@app.cell
def _(hydro_vdq):
    type(hydro_vdq)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### De *Polars* à *Pandas*

    Ce tableau présente les différences entre *Polars* et *Pandas*.

    | **Opération**                      | **Polars**                                                    | **pandas**                                        | **Notes / remarques**                                                                                |
    | ---------------------------------- | ------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
    | **Filtrer**                        | `df.filter(pl.col("val") > 10)`                               | `df[df["val"] > 10]`                              | Même logique : Polars privilégie les expressions fonctionnelles, Pandas l’accès direct par crochets. |
    | **Sélection**                      | `df.select(["x", "y"])`                                       | `df[["x", "y"]]`                                  | Syntaxe semblable, plus explicite en Polars, implicite en Pandas             |
    | **Ajouter / modifier une colonne** | `df.with_columns((pl.col("x") + pl.col("y")).alias("somme"))` | `df["somme"] = df["x"] + df["y"]`                 | `with_columns` crée un nouveau DataFrame (pur), Pandas ajoute la colonne au DataFrame.                                |
    | **Groupement / agrégation**        | `df.groupby("region").agg(pl.col("temp").mean())`             | `df.groupby("region")["temp"].mean()`             | Polars fonctionne en chaîne d'opérations; Pandas directement sur le DataFrame.                                 |
    | **Jointure**                       | `df.join(df2, on="id", how="left")`                           | `df.merge(df2, on="id", how="left")`              | Idem, Polars utilisant une grammaire plus proche de SQL.                                     |
    | **Renommer des colonnes**          | `df.rename({"x": "lon", "y": "lat"})`                         | `df.rename(columns={"x": "lon", "y": "lat"})`     | Pandas nomme les lignes et les colonnes; Polars seulement les colonnes.                                        |
    | **Chaînage d’opérations**          | `df.filter(...).with_columns(...).groupby(...).agg(...)`      | `df[df.val > 10].assign(...).groupby(...).mean()` | Polars favorise le pipeline lisible ; Pandas empile les opérations.                                  |

    Vous pouvez passer de l'un à l'autre en ajoutant `dfpl.to_pandas()` à un tableau *Polars* et `pl.DataFrame(dfpd)` sur un tableau *Pandas*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Opérations

    Les opérations de sélection, de filtre et de jointure restent les mêmes qu'avec *Pandas*. *Geopandas* permet par surcroît des opérations spatiales comme la gestion de systèmes géodésique, le calcul d'aires et de distances ou des combinaisons de polygones. Mais si le système géodésique n'est pas bien identifié dans les données source, le CRS imposé par défaut dans l'attribut `.crs` peut être modifié avec la méthode `.set_crs()`.
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Représentons nos données dans le système 32198 (NAD83 / Quebec Lambert) pour calculer des distances et des aires.
    """)
    return


@app.cell
def _(hydro_vdq):
    hydro_vdq_32198 = hydro_vdq.to_crs(32198)
    hydro_vdq_32198["area"] = hydro_vdq_32198.area
    hydro_vdq_32198["centroid"] = hydro_vdq_32198.centroid
    return (hydro_vdq_32198,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Une fois représentés comme des distances, il est possible de calculer des aires (`.area`) et des centroides (`.centroid`).
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    hydro_vdq_32198
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous pouvons procéder à une reconversion.
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    hydro_vdq_4326 = hydro_vdq_32198.to_crs(4326)
    return (hydro_vdq_4326,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La méthode `.plot()` automatise la représentation graphique des objets. J'ai ajusté les couleurs pour rendre les contours plus évidents.
    """)
    return


@app.cell
def _(hydro_vdq_4326):
    hydro_vdq_4326.plot(color="#D0EBE7", edgecolor="black")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Opérations spatiales avancées

    GeoPandas offre une panoplie d'opérations spatiales pour analyser et transformer les géométries. Explorons quelques opérations courantes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Buffers (zones tampons)

    La méthode `.buffer()` crée une zone tampon autour des géométries. C'est utile pour définir des zones d'influence ou de protection.
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    # Créer un buffer de 500 mètres autour des bassins
    hydro_vdq_buffer = hydro_vdq_32198.copy()
    hydro_vdq_buffer["geometry"] = hydro_vdq_buffer.geometry.buffer(500)
    hydro_vdq_buffer
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Intersections et unions

    Les opérations booléennes spatiales permettent de combiner ou d'extraire des parties de géométries. Par exemple, calculer l'union de tous les bassins (zone totale couverte).
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    union_bassins = hydro_vdq_32198.geometry.union_all()
    union_bassins
    return


@app.cell
def _(mo):
    mo.md(r"""
    Ou bien, calculer l'enveloppe convexe (le plus petit polygone convexe contenant tous les bassins)
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    convex_hull = hydro_vdq_32198.geometry.union_all().convex_hull
    convex_hull
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Jointures spatiales

    Les jointures spatiales permettent de combiner des GeoDataFrames basées sur leurs relations spatiales plutôt que sur des clés communes.  Créeons des points d'échantillonnage aléatoires (disons des écahntillons de sols).
    """)
    return


@app.cell
def _(gpd, hydro_vdq_32198, np):
    np.random.seed(726548)
    n_points = 20

    # Obtenir les limites de la zone
    minx, miny, maxx, maxy = hydro_vdq_32198.total_bounds

    # Générer des points aléatoires
    random_points = gpd.GeoDataFrame(
        {
            "id": range(n_points),
            "value": np.random.randint(1, 100, n_points)
        },
        geometry=gpd.points_from_xy(
            np.random.uniform(minx, maxx, n_points),
            np.random.uniform(miny, maxy, n_points)
        ),
        crs=32198
    )

    random_points
    return (random_points,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Effectuons une jointure spatiale en associant chaque point au bassin qui le contient.
    """)
    return


@app.cell
def _(gpd, hydro_vdq_32198, random_points):
    points_with_basin = gpd.sjoin(
        random_points,
        hydro_vdq_32198[["NOM", "geometry"]],
        how="left",
        predicate="within"
    )
    points_with_basin
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Calculs de distances et de relations spatiales

    GeoPandas offre plusieurs méthodes pour analyser les relations spatiales entre géométries.
    """)
    return


@app.cell
def _(hydro_vdq_32198, plt):
    hydro_vdq_distances = hydro_vdq_32198.copy()
    bassin_ref = hydro_vdq_32198.geometry[hydro_vdq_32198["NOM"] == "Lac Beauport"].iloc[0]
    hydro_vdq_distances["distance"] = hydro_vdq_distances.geometry.distance(bassin_ref)
    hydro_vdq_distances["adjacent"] = hydro_vdq_distances.geometry.boundary.intersects(bassin_ref.boundary)

    fig, ax = plt.subplots(figsize=(10, 10))

    hydro_vdq_distances.plot(
        column="adjacent",
        ax=ax,
        categorical=True,
        legend=True,
        edgecolor="black"
    )
    hydro_vdq_32198[hydro_vdq_32198["NOM"] == "Lac Beauport"].plot(
        ax=ax,
        color="red",
        edgecolor="darkred",
        linewidth=2,
        label="Lac Beauport"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Dissolve (fusion par attribut)

    La méthode `.dissolve()` permet de fusionner des géométries selon un attribut commun, similaire à un `GROUP BY` en SQL.
    """)
    return


@app.cell
def _(hydro_vdq_32198):
    # Ajouter une catégorie basée sur la taille des bassins
    hydro_vdq_categorized = hydro_vdq_32198.copy()
    hydro_vdq_categorized["categorie"] = hydro_vdq_categorized["area"].apply(
        lambda x: "Grand" if x > 10e6 else "Moyen" if x >5e6 else "Petit"
    )

    # Fusionner les bassins par catégorie
    bassins_par_categorie = hydro_vdq_categorized.dissolve(by="categorie")
    bassins_par_categorie.reset_index().plot(
        column="categorie",
        cmap="Set1",
        legend=True,
        edgecolor="black"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Données raster avec *rioxarray*

    Les données raster représentent des informations spatialisées sous forme de grille régulière, comme les modèles numériques de terrain (MNT), les images satellite, ou les données climatiques. Le package *rioxarray* combine la puissance de *xarray* pour les données multidimensionnelles avec les capacités géospatiales de *rasterio*.
    """)
    return


@app.cell
def _():
    import rioxarray as rxr
    import xarray as xr
    return (rxr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Récupérer la topographie

    *Planetary computer* offre un accès libre à de nombreuses données géospatiales, dont des modèles numériques de terrain (MNT) globaux à haute résolution. Nous verrons plus loin comment l'utiliser, mais pour l'instant, nous n'avons besoin que d'extraire le MNT.
    """)
    return


@app.cell
def _(hydro_vdq_4326, rxr):
    import planetary_computer as pc
    import pystac_client
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=pc.sign_inplace
    )
    bounds_vdq = hydro_vdq_4326.total_bounds
    item = next(catalog.search(collections=["cop-dem-glo-30"], bbox=bounds_vdq).items())
    topo_vdq_url = pc.sign(item.assets["data"].href)
    topo_vdq = rxr.open_rasterio(topo_vdq_url).squeeze()
    topo_vdq = topo_vdq.rio.clip_box(*bounds_vdq)
    topo_vdq = topo_vdq.to_dataset(name='elevation')
    #topo_vdq.rio.to_raster("data/topo_vdq.tif") # pour l'enregistrer
    topo_vdq
    return (topo_vdq,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les fichiers raster peuvent prendre plusieurs formes en Python. La plus pratique est la `xarray`, qui combine la puissance de `numpy` pour les tableaux multidimensionnels avec des fonctionnalités spécifiques aux données géospatiales. Le package `rioxarray` ajoute des capacités géospatiales à `xarray`, permettant de manipuler facilement des rasters avec des informations de géoréférencement. Un `xarray.DataSet` comprend des indices, des coordonnées, des dimensions et des attributs.

    - **index**. Les index identifient chaque dimension du raster (par exemple, les coordonnées x et y).
    - **coordonnées**. Les coordonnées fournissent des valeurs spécifiques pour chaque index (par exemple, les valeurs réelles de longitude et latitude).
    - **variables**. Les variables contiennent les données raster elles-mêmes (par exemple, l'élévation).
    - **référence spatiale**, ou `spatial_ref`. Il s'agit des méta-données décrivant le système de coordonnées utilisé pour géoréférencer le raster (par exemple, EPSG:4326 pour WGS84).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Visualisation simple du raster

    Xarray offre des méthodes de visualisation intégrées simples. La méthode `.plot()` s'applique toutefois au type `DataArray`, qui est l'équivalent d'une colonne dans un `DataSet`.
    """)
    return


@app.cell
def _(topo_vdq):
    topo_vdq["elevation"].plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Découpage (clip) avec des géométries vectorielles

    Une opération courante consiste à découper un raster selon une géométrie vectorielle.
    """)
    return


@app.cell
def _(hydro_vdq_4326, topo_vdq):
    topo_vdq_clipped = topo_vdq.rio.clip(
        hydro_vdq_4326.geometry.values,
        hydro_vdq_4326.crs
    )

    topo_vdq_clipped["elevation"].plot()
    return (topo_vdq_clipped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Reprojection de rasters

    Comme avec les données vectorielles, il est possible de reprojeter des rasters dans un autre système de coordonnées.
    """)
    return


@app.cell
def _(topo_vdq_clipped):
    # Reprojeter le raster en NAD83 / Quebec Lambert (EPSG:32198)
    topo_vdq_dist = topo_vdq_clipped.rio.reproject("EPSG:32198")
    topo_vdq_dist
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Opérations raster avancées

    Rioxarray permet de nombreuses opérations sur les rasters :
    - Calcul de pentes et d'aspects (orientation)
    - Rééchantillonnage (résolution)
    - Mosaïque de plusieurs rasters
    - Extraction de valeurs à des points spécifiques
    - Opérations algébriques entre rasters
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous sommes loin d'avoir couvert tous les types d'opérations spatiales possibles. Pour aller plus loin avec GeoPandas, je vous suggère de consulter la [documentation officielle](https://geopandas.org/en/stable/getting_started/introduction.html). Pour rioxarray, la [documentation](https://corteva.github.io/rioxarray/stable/) offre de nombreux exemples d'utilisation.
    """)
    return


if __name__ == "__main__":
    app.run()
