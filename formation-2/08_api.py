import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 8. API de données publiques

    Les dépôts de données classiques offrent à des adresses non systématiques des ensembles de données hétérogènes, par exemple des fichiers GeoJSON, ou des shape files. Les API (*Application Programming Interface*) permettent, grâce à du code, d'accéder de manière systématique à des données hébergées sur des serveurs distants. Certaines organisations privées, gouvernementales et institutions de recherche offrent un accès gratuit à leurs données via des API, ce qui offre de nombreux avantages.

    - L'accès est direct, sans télécharger manuellement des fichiers volumineux.
    - Les données sont à jour, les requêtes accèdant aux données les plus récentes.
    - On ne récupère que les données ciblées (temporelles, spatiales, variables).
    - Les scripts peuvent être exécutés de manière reproductible, répétée et planifiée.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Planetary Computer

    [Planetary Computer](https://planetarycomputer.microsoft.com/) est une plateforme de Microsoft offrant un accès gratuit à des données environnementales spatialisées. On y retrouve des images satellites, des données climatiques et météorologiques, des modèles numériques de terrain, des données d'occupation du sol, des données océanographiques, etc. L'accès se fait via l'API STAC (*SpatioTemporal Asset Catalog*), un standard pour organiser et découvrir des données géospatiales.
    """)
    return


@app.cell
def _():
    import marimo as mo # marimo
    import numpy as np # calcul matriciel
    import pandas as pd # tableaux
    import geopandas as gpd # tableaux géoréférencés
    import lets_plot as lp # graphiques déclaratifs
    import matplotlib.pyplot as plt # graphiques impératifs
    import xarray as xr # grilles multidimensionnelles
    import rioxarray as rxr # ... geéoréférencées
    from rioxarray.merge import merge_arrays # une méthode cachée à charger explicitement
    from rasterstats import zonal_stats # statistiques sur des grilles

    import planetary_computer as pc # accès aux données de PC
    import pystac_client # accès à l'API de PC

    lp.LetsPlot.setup_html() # les graphiques s'affichent comme dans un page web
    return (
        gpd,
        lp,
        merge_arrays,
        mo,
        np,
        pc,
        pd,
        plt,
        pystac_client,
        rxr,
        zonal_stats,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Connexion au catalogue STAC

    Le catalogue STAC de Planetary Computer s'ouvre avec la bibliothèque `pystac_client`. Le modificateur `pc.sign_inplace` ajoute automatiquement les jetons d'authentification nécessaires pour accéder aux données.
    """)
    return


@app.cell
def _(pc, pystac_client):
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1", modifier=pc.sign_inplace
    )
    print(f"Titre du catalogue: {catalog.title}")
    print(f"Description: {catalog.description}")
    return (catalog,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Explorer les collections disponibles

    Le catalogue contient de nombreuses collections de données. Utilisons Python pour rechercher une liste de termes décrivant typiquement des données hydrologiques.
    """)
    return


@app.cell
def _(catalog, pd):
    collections = list(catalog.get_collections())

    collections_df = pd.DataFrame(
        [
            {
                "ID": col.id,
                "Titre": col.title,
                "Description": col.description[:100] + "..."
                if len(col.description) > 100
                else col.description,
            }
            for col in collections
        ]
    )

    # Filter for hydrology-related collections
    hydro_keywords = [
        "terrain", "water", "land", "precip", "climat", "temperature", "snow"
    ]
    collections_hydro = collections_df[
        collections_df["Titre"].str.lower().str.contains("|".join(hydro_keywords), na=False)
        | collections_df["Description"].str.lower().str.contains("|".join(hydro_keywords), na=False)
    ]
    collections_hydro
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exemple 1 : Modèle numérique de terrain (MNT)

    Nous cherchons à récupérer le modèle numérique de terrain Copernicus DEM à 30m de résolution pour une zone d'intérêt au Québec: les bassins versants de la ville de Québec. Récupérons d'abord les géométries du bassin versant.
    """)
    return


@app.cell
def _(gpd):
    # Charger les bassins versants de la ville de Québec
    url_geojson = "https://www.donneesquebec.ca/recherche/dataset/b4893e20-3a65-44fe-a428-68c79e303fb4/resource/fcdd3e3b-b6dc-45ae-9e88-542b842b1774/download/vdq-hydrobassinversant.geojson"
    bassins_vdq = gpd.read_file(url_geojson)
    bassins_vdq.plot()
    return (bassins_vdq,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous pouvons extraire les limites des éléments géométriques par la propiéré `.total_bounds`.
    """)
    return


@app.cell
def _(bassins_vdq):
    bounds = bassins_vdq.total_bounds
    bounds
    return (bounds,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rechercher et télécharger le MNT

    Utilisons l'API STAC pour rechercher les données de terrain couvrant notre zone d'intérêt. L'ensemble de données recherché est [`cop-dem-glo-30`](https://planetarycomputer.microsoft.com/dataset/cop-dem-glo-30).

    **Conseil de pro**. Le téléchargement de données lourde risque d'être relancé constamment dans l'arbre d'exécution de Marimo. Mieux vaut désactiver l'exécution automatique.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("images/reactive-execution.png")
    return


@app.cell(disabled=True)
def _(bounds, catalog, merge_arrays, pc, rxr):
    # Rechercher dans la collection Copernicus DEM
    search_mnt = catalog.search(collections=["cop-dem-glo-30"], bbox=bounds)

    # Charger toutes les tuiles et les fusionner automatiquement
    items_mnt = list(search_mnt.items())

    # une boucle sur une seule ligne donne un code compact. merge_arrays fusionne les truiles
    mnts = [rxr.open_rasterio(pc.sign(item.assets["data"].href)) for item in items_mnt]
    mnt = merge_arrays(mnts)
    return (mnt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La méthod `.plot()` fonctionne en affichant la première bande par défaut (il n'y a en qu'une seule).
    """)
    return


@app.cell
def _(mnt):
    mnt.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    L'API téléchargeant les tuiles qui couvre la zone désirée, il est attentdu que la zone soit plus large que nos polygones. Corrigeons ça!
    """)
    return


@app.cell
def _(bassins_vdq, mnt):
    mnt_clipped = mnt.rio.clip(bassins_vdq.geometry.values, bassins_vdq.crs).squeeze() # squeeze retire les dimensions d'une taille de 1 (ici, une seule bande)
    mnt_clipped.plot()
    return (mnt_clipped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Calculer des statistiques zonales

    Calculons l'élévation moyenne et l'étendue d'élévation pour chaque bassin versant.
    """)
    return


@app.cell
def _(bassins_vdq, mnt_clipped, plt):
    _fig, _ax = plt.subplots(1, 1, figsize=(7, 7))
    mnt_clipped.plot(ax=_ax, cmap='terrain')
    bassins_vdq.plot(ax=_ax, facecolor='none', edgecolor='black', linewidth=1)
    return


@app.cell
def _(mo):
    mo.md(r"""
    La fonction `zonal_stats` calcule les statistiques raster par zone vectorielle.
    """)
    return


@app.cell
def _(mnt_clipped):
    mnt_clipped
    return


@app.cell
def _(bassins_vdq, mnt_clipped, zonal_stats):
    # Calculer les statistiques zonales
    stats = zonal_stats(
        bassins_vdq, # le geodataframe qui contient les polygones
        mnt_clipped.values, # mnt_clipped est un data array, dont on extrait les valeurs
        affine=mnt_clipped.rio.transform(), # pour transformer les angles en distances
        stats=["mean", "min", "max", "std"], # les statistiques recherchées
        nodata=None, # comment sont nommées les valeurs manquantes. certaines sources vont donner 1E20, d'autres -9999, NaN, ., -, etc.
    )
    stats # stats est un dictionnaire
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Il est plus pratique d'afficher les statistiques dans un data frame, et encore plus de les afficher aux côtés des données source.
    """)
    return


@app.cell
def _(bassins_vdq, stats):
    # Ajouter au GeoDataFrame
    bassins_stats = bassins_vdq.copy()
    bassins_stats["elev_mean"] = [s["mean"] for s in stats]
    bassins_stats["elev_min"] = [s["min"] for s in stats]
    bassins_stats["elev_max"] = [s["max"] for s in stats]
    bassins_stats["elev_range"] = bassins_stats["elev_max"] - bassins_stats["elev_min"]

    bassins_stats[["NOM", "elev_mean", "elev_min", "elev_max", "elev_range"]]
    bassins_stats
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exemple 2 : Données d'occupation du sol

    Planetary Computer héberge également des données d'occupation du sol. Récupérons les données ESA WorldCover à 10m de résolution pour analyser la composition de nos bassins.
    """)
    return


@app.cell
def _(bounds, catalog):
    # Rechercher les données d'occupation du sol
    search_landcover = catalog.search(collections=["esa-worldcover"], bbox=bounds)
    items_lc = list(search_landcover.items())
    items_lc
    return (items_lc,)


@app.cell
def _(mo):
    mo.md(r"""
    Le catalogue contient des données de 2021 (premier item de la liste) et de 2020 (deuxième item). Prenons 2021.
    """)
    return


@app.cell
def _(items_lc):
    item_lc = items_lc[0]
    return (item_lc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Récupérons les données.
    """)
    return


@app.cell
def _(bounds, item_lc, pc, rxr):
    lc_url = pc.sign(item_lc.assets["map"].href)
    landcover = rxr.open_rasterio(lc_url).squeeze()
    landcover_clipped = landcover.rio.clip_box(*bounds)
    return (landcover_clipped,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Visualiser l'occupation du sol

    Créons une carte avec une palette de couleurs appropriée pour l'occupation du sol.
    """)
    return


@app.cell
def _(norm):
    norm
    return


@app.cell
def _(bassins_vdq, landcover_clipped, np, plt):
    # Codes de classification ESA WorldCover - décrits dans landcover_clipped.attrs["legend"]
    lc_classes = {
        10: {"label": "Arbres", "color": '#006400'},
        20: {"label": "Arbustes", "color": '#ffbb22'},
        30: {"label": "Prairie", "color": '#ffff4c'},
        40: {"label": "Culture", "color": '#f096ff'},
        50: {"label": "Bâti", "color": '#fa0000'},
        60: {"label": "Végétation éparse", "color": '#b4b4b4'},
        70: {"label": "Neige/Glace", "color": '#f0f0f0'},
        80: {"label": "Eau permanente", "color": '#0064c8'},
        90: {"label": "Milieux humides herbacés", "color": '#0096a0'},
        95: {"label": "Mangrove", "color": '#00cf75'},
        100: {"label": "Mousse et lichen", "color": '#fae6a0'},
    }

    # Identifier les catégories réellement présentes dans les données
    unique_codes = np.unique(landcover_clipped.values)

    # Filtrer pour ne garder que les catégories présentes
    codes_present = sorted([code for code in lc_classes.keys() if code in unique_codes])
    labels = [lc_classes[code]["label"] for code in codes_present]
    colors = [lc_classes[code]["color"] for code in codes_present]

    # Visualisation
    # Ce code utilise des fonctions matplotlib avancées, proposée par IA, pour gérer les catégories.
    # Pour afficher des catégories discrètes (non continues), matplotlib nécessite :
    # - ListedColormap : une palette de couleurs discrètes (une couleur par catégorie)
    # - BoundaryNorm : définit les limites entre chaque catégorie
    # - mpatches : crée des éléments de légende (patches = rectangles colorés)
    from matplotlib.colors import ListedColormap, BoundaryNorm
    import matplotlib.patches as mpatches
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(codes_present + [105], len(codes_present))
    _fig, _ax = plt.subplots(figsize=(10, 8))
    landcover_clipped.plot(ax=_ax, cmap=cmap, norm=norm, add_colorbar=False)
    bassins_vdq.plot(ax=_ax, facecolor='none', edgecolor='white', linewidth=1)
    patches = [mpatches.Patch(color=color, label=label, edgecolor='black') for label, color in zip(labels, colors)]
    _ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left', title='Occupation du sol')
    return (norm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Autres API de données géospatiales

    Au-delà de Planetary Computer, plusieurs autres API offrent un accès gratuit à des données géospatiales :

    ### API globales

    - **[Google Earth Engine](https://earthengine.google.com/)** : Vaste catalogue de données satellites et climatiques
    - **[Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)** : Données climatiques européennes
    - **[NASA EarthData](https://www.earthdata.nasa.gov/)** : Données satellites et climatiques de la NASA
    - **[USGS Earth Explorer](https://earthexplorer.usgs.gov/)** : Landsat, ASTER, données de terrain
    - **[Open-Meteo](https://open-meteo.com/)** : API météo gratuite sans clé API

    ### Exemple avec Open-Meteo

    Open-Meteo offre une API simple d'accès pour des données météorologiques historiques et prévisionnelles. Elle n'a besoin que d'un package générique, `requests` : nous n'avons besoin que de formater l'url. Open-Meteo est utile pour les données légères et ponctuelles, pas pour les grilles lourdes.
    """)
    return


@app.cell
def _(bassins_vdq, pd):
    import requests

    # Obtenir le centroïde d'un bassin
    bassin_example = bassins_vdq[bassins_vdq["NOM"] == "Rivière Saint-Charles"].iloc[0]
    centroid = bassin_example.geometry.centroid

    # Requête à l'API Open-Meteo - Archive historique
    url_meteo = "https://archive-api.open-meteo.com/v1/archive"  # API archive, pas forecast
    params = {
        "latitude": centroid.y,
        "longitude": centroid.x,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31",
        "daily": "temperature_2m_mean,precipitation_sum",
        "timezone": "America/Toronto",
    }

    response = requests.get(url_meteo, params=params)
    data_meteo = response.json()

    # Convertir en DataFrame
    df_meteo = pd.DataFrame(
        {
            "date": pd.to_datetime(data_meteo["daily"]["time"]),
            "temp_mean": data_meteo["daily"]["temperature_2m_mean"],
            "precipitation": data_meteo["daily"]["precipitation_sum"],
        }
    )

    df_meteo = df_meteo.melt(id_vars=["date"])
    return (df_meteo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Visualiser les données météorologiques
    """)
    return


@app.cell
def _(df_meteo, lp):
    (
        lp.ggplot(data=df_meteo, mapping=lp.aes(x="date", y="value"))
        + lp.facet_wrap(facets="variable", ncol=2, scales="free_y")
        + lp.geom_line()
        + lp.theme_minimal()
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bonnes pratiques

    - **Vérifier les licences**. Pour des projets publics, certains API demandent des licences pro, d'autres pas Assurez-vous du droit d'utilisation des données.
    - **Citer les sources**. Toujours mentionner la provenance des données. Cela rend votre méthodologie plus crédible et plus reproductible.
    - **Valider les données**. Vérifiez la cohérence et la qualité des données téléchargées. Certaines données, même d'excellente qualité, peuvent être peu fiable dans votre contexte. Comme toute information, assurez-vous qu'elle est contextuellement transférable.
    - **Gérer les versions**. Notez la date de téléchargement et les versions d'API utilisées.
    - **Optimiser les requêtes**. Même si les API sont gratuites pour vous, elles restent un coût pour les organisations qui distribuent les données. Limitez la bande passante en ciblant précisément vos besoins
    """)
    return


if __name__ == "__main__":
    app.run()
