import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Installer Python

    La version web de Marimo exécute du code Python grâce à Pyodide, un compilateur de code Python basé sur des technologies web (Web Assembly). Le code n'est pas exécuté dans l'infonuagique, mais dans votre navigateur. Bien qu'en ligne, il ne transige pas avec le web: l'application est téléchargée comme un site internet normal et les calculs se font sur votre ordinateur. Cette approche est pratique et favorise la confidentialité, mais a l'inconvéneient de n'utiliser qu'un seul processeur, ce qui rend les opérations intensives plus lents que si elles étaient exécutées avec tous vos processeurs. Vous pouvez louer des services de calcul infonuagique (avec Marimo, Deepnote, Google colab ou Hex), mais installer Python localement reste une solution plutôt accessible, en particulier avec `uv`, un gestionnaire d'environnements virtuels. Pour installer `uv`, ouvrez un terminal Windows PowerShell, puis collez la commande ci-dessous (clic droit), suivi de `Enter`.

    ```
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Les carrés de sables

    Les carrés de sables (`sandbox`) sont des environnements de calcul temporaires. Le temps d'installation étant souvent très court, c'est probablement ce que vous utiliserez 90% du temps. Toujours dans PowerShell, naviguez dans vos dossiers avec la commande `cd` (*change directory*), puis pour démarrer un nouveau projet avec la commande suivante.

    ```bash
    cd C:\Users\abcde01\Documents\mon_projet
    uv run --with marimo --with polars --with altair marimo edit
    ```

    `uv run` créera un environnement, les `--with <package>` installera les packages et `marimo edit` lancera marimo. Vous pourrez par la suite installer d'autres packages dans marimo. Pour plus de reproductibilité, je vous suggère de prendre en note la commande utilisée pour lancer le carré de sable (dans un fichier `README.md`, par exemple). La commande `uvx` créera un véritable carré de sable isolé, mais à ce jour elle n'est pas compatible avec Marimo et dans ce cadre d'utilisation, `uv` et `uvx` se comporteront de la même manière.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Les environnements persistants

    `uv` permet d'installer différentes versions de Python dans vos dossiers personnels. Toujours dans PowerShell, naviguez dans vos dossiers avec la commande `cd` (*change directory*), puis pour démarrer un nouveau project, lancez `uv init`. Pour créer votre projet, lancez `uv venv`. Ces opérations créerons un fichier `pyproject.toml`, qui contient les informations pour reproduire votre environnement, et un dossier `.venv`,  Pour entrer dans votre environnement, lancez `.venv\Scripts\Activate`. Pour ajouter des packages, `uv add <package>` ajoutera automatiquement le package au fichier `pyproject.toml`, tandis que `uv pip install <package>` installera le package sans l'ajouter. Pour sortir de l'environnement, tapez `deactivate`.

    Par exemple,


    ```bash
    cd C:\Users\abcde01\Documents\mon_projet
    uv init
    uv venv
    .venv\Scripts\Activate
    uv add marimo
    marimo edit
    ```

    `uv` installera une version de Python à même vos dossier, dans un répertoire `.venv`. Cette approche a du sens pour une travail plus approfondi, mais elle est plus lourde à gérer. Si vos calculs sont relativement simples, je vous suggère d'utiliser les carrés de sable avec `uv run...`.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
