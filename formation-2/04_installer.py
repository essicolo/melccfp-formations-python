import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Installer Python

    Marimo en ligne exécute du code Python grâce à Pyodide, un compilateur de code Python basé su des technologies web. Le code n'est pas exécuté dans l'infonuagique, mais dans votre navigateur. Cette approche a l'inconvéneient de n'utiliser qu'un seul processeur, mais elle a l'avantage de ne pas nécessiter d'installation de logiciel. Il existe de nombreuses approches pour installer Python, qui se déclinent en deux philosophies: le Python natif (vanille) et tout-en-un.

    ```
    Vanille
    ----- * ------------------------- virtualenv
           \         /--------------- pipx
            \ ----- * --------------- pip, venv
                     \ ----- * ------ poetry
                              \ ----- uv

    Tout-en-un
    ----- * --------------- conda
           \ ----- * ------ mamba
                    \ ----- pixi
    ```


    | Outil          | Emplacement des environnements                               | Cas d’usage typique                                                                 |
    | -------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
    | conda      | Centralisé (`~/miniconda3/envs/` ou `~/anaconda3/envs/`)     | Dépendances système lourdes (géospatial, data science)                              |
    | **mamba**      | Centralisé (`~/mamba/envs/`)                                 | Idem conda, mais bien plus rapide                                                   |
    | **pixi**       | Local au projet (`.pixi/envs/`) + cache global pour binaires | Idem mamba, mais local au projet et plus reproductible                              |
    | virtualenv | Local au projet (`.venv/`)                                   | Environnements légers et classiques                                                 |
    | pipx       | Centralisé (`~/.local/pipx/venvs/`)                          | Installation isolée d’outils CLI Python                                             |
    | poetry     | Local (`.venv/` ou global selon config)                      | Développement, packaging et publication d’applications                              |
    | **uv**         | Local (`.venv/` dans le projet)                              | Projets modernes et rapides, gestion unifiée d’environnements et dépendances Python |

    La plus facile est probablement `uv`. Mais `uv` gère surtout le Python pur. Pour des tâches complexes de reprojection avec `pyproj` ou `GDAL`, codés en C++. S'ils ne sont pas installés sur votre système (la seule manière fiable de les installés sur le système sans droit d'admin est de passer pas WSL), il faudra passer par `pixi` (un successeur de conda et `mamba`), qui est toutefois un peu plus complexe que `uv`.

    `uv` est simple et solide, mais offre surtout la possibilité de créer des environnements temporaires (prochaine section). Si vous ne comptez pas les utiliser, je vous suggère d'utiliser `pixi`. Néanmoins, pour installer `uv`, ouvrez un terminal Windows PowerShell, puis collez la commande ci-dessous (clic droit), suivi de `Enter`.

    ```
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

    Et une commande similaire pour `pixi`.

    ```
    powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Les carrés de sables

    Les carrés de sables (`sandbox`)  avec `uv` sont des environnements de calcul temporaires. Le temps d'installation étant souvent très court, mais puisque l'environnment est isolé, il aura du mal à se connecter à vos comptes IA. Toujours dans PowerShell, naviguez dans vos dossiers avec la commande `cd` (*change directory*), puis pour démarrer un nouveau projet avec la commande suivante.

    ```bash
    cd C:\Users\abcde01\Documents\mon_projet
    uv run --with marimo --with polars --with altair marimo edit
    ```

    `uv run` créera un environnement, les `--with <package>` installera les packages et `marimo edit` lancera marimo. Vous pourrez par la suite installer d'autres packages dans marimo. Pour plus de reproductibilité, je vous suggère de prendre en note la commande utilisée pour lancer le carré de sable (dans un fichier `README.md`, par exemple). La commande `uvx` créera un véritable carré de sable isolé, mais à ce jour elle n'est pas compatible avec Marimo et dans ce cadre d'utilisation, `uv` et `uvx` se comporteront de la même manière.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Les environnements persistants

    `uv` permet d'installer différentes versions de Python dans vos dossiers personnels. Toujours dans PowerShell, naviguez dans vos dossiers avec la commande `cd` (*change directory*), puis pour démarrer un nouveau project, lancez `uv init`. Pour créer votre projet, lancez `uv venv`. Ces opérations créerons un fichier `pyproject.toml`, qui contient les informations pour reproduire votre environnement, et un dossier `.venv`,  Pour entrer dans votre environnement, lancez `.venv\Scripts\Activate`. Pour ajouter des packages, `uv add <package>` ajoutera automatiquement le package au fichier `pyproject.toml`, tandis que `uv pip install <package>` installera le package sans l'ajouter. Pour mettre à jour, `uv sync`. Pour sortir de l'environnement, tapez `deactivate`.

    Par exemple,


    ```bash
    cd C:\Users\abcde01\Documents\mon_projet
    uv init
    uv venv
    .venv\Scripts\Activate
    uv add marimo
    marimo edit
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Quant à `pixi`, restez aussi dans PowerShell. Dans votre dossier, lancez `pixi init`. Pour activer l'environnement, `pixi shell`. Pour installer des packages, `pixi add <package>`, pour mettre à jour `pixi install` et pour quitter l'environnement, tapez `exit`.

    ```bash
    cd C:\Users\abcde01\Documents\mon_projet
    pixi init
    pixi shell
    pixi add marimo
    marimo edit
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Installation cloud

    Plusieurs entreprises offrent des environnements de calcul Python avec Marimo ([Molab](https://molab.marimo.io/)) ou des interfaces Jupyter, similaires à celle de Marimo, comme [Deepnote](deepnote.com), [Hex](https://hex.tech/), [Google](https://colab.research.google.com/) ou [Microsoft](https://ml.azure.com). Bien que ces services offrent des options gratuites, leur utilisation professionnelle peut entraîner des coûts. De plus, il est important de prendre conscience que les centres de données où les données et les codes sont hébergés sont soumis aux réglementations de juridictions où ils se trouvent, ce qui peut conférer aux autorités un libre accès aux données que l'on croit confidentielles. À mon avis, préférez des solutions locales.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interfaces

    ### Visual Studio Code - recommandée en mode avancé

    La méthode de travail classique en Python est d'écrire un script avec n'importe quel éditeur texte, et le lancer dans un terminal, par exemple `python mon_script.py`. Mais il existe plusieurs manières d'écrire en Python en passant par Visual Studio Code (VScode). Je ne couvrirai que l'approche en mode *pourcentage* et celle en mode *Jupyter* (bien que le module [Quarto](https://quarto.org/) soit aussi très intéressant). Dans tous les cas, installez l'extension **Python** dans VScode (ouvrir le gestionnaire d'extensions dans le menu vertical, cherchez Python). Pour les deux modes, assurez-vous d'ajouter `ipykernel` dans votre environnement :

    ```bash
    pixi add ipykernel
    ```

    #### Mode Jupitext

    Ce mode n'a pas de nom formel, mais on l'appelle parfois ainsi, ou "mode pourcentage". Lorsqu'un fichier est enregistré avec l'extension `.py`, un bouton Run Cell apparaît lorsque vous tapez `# %%`. Il s'agit d'un diviseur de cellules. Pour inclure des cellules de texte *Markdown*,

    ```python
    # %% [markdown]
    "\"\"
    # Titre 1

    Votre texte...
    "\"\"
    ```

    On vous demandera de sélectionner un *kernel* (noyau). L'utilisation des noyaux est une couche supplémentaire de gestion utilisée pour lier un environnement de calcul et une interface de calcul. Heureusement, VScode nous permet de nous en passer. Sélectionnez *Python Environment*, puis sélectionnez l'environnement que vous avez créer avec `mamba`, ou votre gestionnaire de modules préféré. S'il n'apparaît pas, le bouton ↻ en haut à droite du menu de sélection d'environnement devrait le faire apparaître. S'il n'y est toujours pas, redémarrer VScode devrait aider.

    #### Mode Jupyter

    Les fichiers Jupyter se terminent par l'extension `.ipynb`, un héritage de l'ancien nom *IPython notebook*. Si vous créez un fichier avec cette extension, un environnement Jupyter sera généré de facto par VScode. Vous pourrez y intercaler des cellules de calcul en Python (sélectionner la cellule, puis appuyez sur `y`) et des cellules en *Markdown* (idem, appuyez sur `m`). Pour ajouter des cellules au-dessus, `a`, et en dessous, `b`. Pour exécuter une cellule, c'est comme avec *Marimo*, `Ctrl + ↵` ou `Maj + ↵` pour exécuter sans passer à la suivante. Si vous désirez utiliser *Jupyter lab*, qui à l'instar de *Marimo* a son interface web, vous devrez néanmoins apprendre à gérer les *kernels*. Notez cependant que le format `.ipynb` est en fait un fichier `json` qui contient beaucoup d'information. L'exécution d'une cellule étant considéré en suivi de version comme une modification de toute l'information, le suivi sur Git est difficile à suivre. De plus, sur VSCode ou Jupyter lab, les cellules ne s'exécutent pas de manière réactive, comme le fait *Marimo*.

    #### Mode Marimo

    En plus d'une interface web, Marimo offre une extension pour VSCode. Cette extension fonctionne bien, mais elle est dans ses débuts et doit être configurée manuellemet. D'abord, créez votre ewnvironnement avec pixi, puis ajoutez le pâckage `pixi add marimo`. Puis installez l'extension Marimo dans VSCode. Une fois installée par le gestionnaire de package de VSCode, affichez la page de l'extension, cliquez sur l'icone ⚙️ > Settings, puis modifiez l'option Marimo : Python path (`marimo.pythonPath`) pour qu'elle pointe vers l'environnement virtuel que vous avez créé, par exemple `.pixi/envs/default/python.exe`. Vous devrez ajuster ce paramètre si vous utilisez un autre environnement virtuel.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo - recommandée pour l'exploration rapide

    Après avoir installé Marimo, vous pouvez lancer l'interface en tapant

    ```
    marimo edit
    ```

    L'interface Marimo devrait apapparaître comme onglet dans votre navigateur. Si la commande n'est pas reconnue, c'est peut-être parce que l'environnement Python n'est pas activé. Contrairement à *Jupyter lab* et à son intégration dans Visual Studio Code (description ci-dessous), Marimo ne conserve pas par défaut le rendu du code comme les tableaux, graphiques, etc: les fichiers de calcul sont purement du code Python - ce qui est un avantage pour le suivi des modifications. Marimo est néanmoins apte à conserver les objets créés lors d'une session de travail grâce à un cache optimisé pour Marimo.

    ```
    with mo.persistent_cache(name="mon_cache"):
        x = fonction(arguments)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Autres outils

    VSCode, développé par Microsoft, est probablement le logiciel le plus utilisé dans le monde de la programmation, et peut être adapté pour le calcul scientifique en Python en installant des extensions. Puisqu'il s'agit d'un logiciel libre, plusieurs entreprises l'ont transformé pour en faire une plateforme plus clé en main, par exemple Position, Cursor et Windsurf. Avec un compte GitHub, vous aurez un accès limité mais gratuit à l'assistant de programmation Github Copilot. VSCode vient avec une télémétrie embarquée, ce qui signifie que ce vous y écrivez est envoyé à Microsoft. Que ce soit par souci de confidentialité ou simplement parce que vous n'aimez pas qu'un robot lise constamment ce que vous écrivez, la version [VSCodium](https://vscodium.com/) retire la télémétrie. Notez néanmoins qu'utiliser une assistance IA couplée au web signifie que vous envoyez vos données dans les nuages. Nous aborderons les assistants au chapitre 5. Pour l'instant avec VSCode ou VSCodium, veillez à installer les extensions Python et Jupyter. L'IDE [Zed](https://zed.dev/) est également un environnement de travail apprécié.

    Développé par l'entreprise Jetbrains, [Pycharm](https://www.jetbrains.com/pycharm/) est un éditeur de texte brut enchâssé dans une interface clé en main pour la programmation en Python. La version gratuite (appelée *community version*) vient avec de nombreuses fonctionnalités, mais aussi la restriction importante qui consiste à bloquer l'édition de fichiers Jupyter. Plusieurs à la DPEH l'utilisent.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
