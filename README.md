-	Formation en deux groupes : débutants et avancés
-	Jour 1, AM : débutant 1
   - Introduction à Python, pertinence, avantages
   - Familiarisation avec l’interface de carnet de calcul
   - Programmation et calculs de base
   - Exemples et travail en équipe
-	Jour 1, PM : avancé 1
   - Configurer un poste de calcul
   - Utilisation des agents de programmation IA
   - Exploration de données géographiques
   - Exemples et travail en équipe
-	Jour 2, AM : débutant 2
   - Exploration des données, notion de tableaux
   - Visualisation des données
   - Configurer Python sur un poste de travail
   - Exemples et travail en équipe
-	Jour 2, PM : avancé 2
   - Visualisation interactive
   - Récupération de données publiques
   - Machine learning
   - Exemples et travail en équipe


## To do, formation 2

### 06 - geodata

[x] Rappel Polars → équivalents pandas (select, filter, groupby, etc.) 
[ ] Introduction à GeoPandas : géométries, projections, jointures spatiales avec un cas d'Hydro-Québec
[ ] Lecture et fusion de rasters avec rioxarray.
[ ] Représentation rapide : .plot() et base de Altair (ou Lets-Plot plus tard).
[ ] Mini-cas : extraire la température moyenne d’un raster ERA5 pour des points d’échantillonnage.

### Visualiser les données géospatiales

[ ] Introduction à la logique “grammaire graphique” (aes, geom_*).
[ ] Cartes de points, polygones et rasters (geom_tile, geom_sf).
[ ] Combinaison de couches vectorielles + raster.
[ ] Personnalisation (échelles, projections, palettes, facettes).
[ ] Mini-cas : carte de NDVI sur une région + données de stations météo.

### APIs

[ ] Utiliser les catalogues STAC (Planetary Computer).
[ ] Téléchargement et mosaïquage d’images Sentinel.
[ ] Requêtes climatologiques (ERA5-Land ou Open-Meteo).
[ ] Préparation des données pour analyse (rééchantillonnage, alignement).
[ ] Mini-cas : produire un cube spatio-temporel température–NDVI.

## sklearn

[ ] Préparation des jeux de données (features géographiques, raster → dataframe).
[ ] Régression linéaire et aléatoire (RandomForestRegressor) pour prédire un indicateur (ex. NDVI à partir du climat).
[ ] Évaluation et visualisation des résultats (scatter, carte des prédictions).
[ ] Introduction rapide aux modèles spatiaux et validation croisée spatiale.
[ ] Mini-cas : modèle prédictif simple de rendement ou d’humidité du sol.