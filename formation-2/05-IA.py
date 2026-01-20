import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Les IA

    L'IA est aujourd'hui enchâssée dans la plupart des écosystèmes numériques. En programmation, l'IA agit de 5 grandes manières:

    - la **complétion**, où l'assistant devine les caractères qui devraient suivre une commande à venir, selon le contexte,
    - la **conversation**, où l'assistant répond textuellement à des requêtes,
    - en mode **édition**, l'assistant vous suggérera des changements localisés à même votre code, vous évitant ainsi d'effectuer des enfilades de copier-coller,
    - en mode **agent**, où l'assistant évalue tout le contexte d'un dossier de travail - et non seulement le fichier en cours - avant de suggérer des modifications, et
    - en mode **développement** pour développer en entier un projet.

    Nous couvrirons tous ces rôles, à l'exception du dernier, qui est en ce moemnt très exploratoire. Dans tous les cas, il faut toujours garder à l'esprit le professionnalisme, qui implique que la responsabilité des solutions programmées incombe à un humain et non à son assistant IA.

    Marimo offre une plateforme d'analyse automatique sur marimo.app/ai, mais voyons comment organiser un environnement de travail gratuitement. L'interface de congiguration de Marimo se trouve sous `⚙ > User settings` un espace pour configurer l'IA. Le Ministère de la cybersécurité et du numérique (MCN) a déclaré à la hâte un moratoire interdisant l'utilisation d'IA génératives payantes, ce qui redirige les employé.es vers des options gratuites plus laxistes en terme de sécurité - le MCN est au courrant des limitations de son approche et proposera bientôt des guides plus pratiques et sensés. Il existe plusieurs options conformes, mais Ollama offre une intéressante flexibilité.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## L'option polyvalente avec Ollama

    Olla am est un distributeur générique de modèles open source ouvrant un serveur local qui permet d'héberger un modèle à même votre ordinateur, ou d'installer un proxy vers un modèle infonuagique. Pour installer Ollama, suivez les instructions sur [ollama.com](https://ollama.com/). En l'exécutant, vous démarrez un petit serveur d'IA local qui vous permettra d'installer et d'exécuter des modèles. Ceux-ci sont listés sur [ollama.com/library](https://ollama.com/library). Vous aurez sous vos yeux deux types de modèles.

    - Tous sont installables sur votre ordinateur, et peuvent fonctionner de manière totalement découplée du web.
    - Certains, avec l'étiquette [`#cloud`](https://ollama.com/search?c=cloud), peuvent être utilisés gratuitement sur une infrasctructure distante.

    ### Modèles locaux

    Notez néanmoins que toute information qui transige sur un serveur peut être utilisée par le serveur. Il existe des droits et de longues conditions générales d'utilisations, que l'on accepte d'emblée, mais rien ne garanti qu'ils seront appliqués. Chaque information, ne serait-ce que pour l'autocomplétion (qui demande une veille continue sur le contenu), peut se retrouver exposée. Si vous travaillez avec des données sensibles, vous êtes imputable. Avec un modèle local d'Ollama, aucune information ne quitte votre ordinateur, qui doit en revanche bénéficier de ressources suffisantes pour héberger un modèle d'IA, gourmand même dans ses variations les plus légères. En local, choisissez un modèle adapté aux capacités de votre ordinateur (truc: demandez à une IA de vous en suggérer un selon le CPU/GPU et la mémoire vive dont vous disposez). Pour installer un modèle, ouvrez un terminal (Windows PowerShell cmd ou Miniforge prompt), et tapez, par exemple,

    ```bash
    ollama pull ministral-3:8b-instruct-2512-q4_K_M
    ```

    ### Modèles hébergés

    Si vous préférez l'option infonuagique, vous téléchargerez un *proxy*, pas le modèle lui-même.

    ```bash
    ollama pull mistral-large-3:675b-cloud
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Configurer marimo pour Ollama

    Les étapes pour configurer Ollama dans marimo ne sont pas toujours évidentes.

    1. **Installez** le package `openai`.
    1. **Connexion**. Dans `⚙ > User settings > AI > AI Providers`, sous Ollama, entrez l'adresse du serveur local, par défaut `http://localhost:11434/v1`.
    1. **Activation**. Dans `⚙ > User settings > AI > AI Models`, cochez Ollama. Ajoutez un nouveau modèle avec son nom (provider: Ollama, name: `mistral-large-3:675b-cloud`).
    1. **Sélection**. Dans `⚙ > User settings > AI > AI Features`, sélectionnez *custom* sous Provider, et sélectionnez le modèle que vous avez téléchargé sous Autocomplete Model (choisissez un modèle plus léger), Chat Model et Edit Model.

    Pour les détails, voyez la [capsule de marimo dédiée à Ollama](https://www.youtube.com/watch?v=IoveQCa6feg).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## L'option étendue avec Google AI Studio

    Plusieurs modèles de la classe Gemini sont disponibles via Ollama cloud. Mais vous viendrez probablement à bout des quotas d'utilisation de Ollama. Google AI Studio, bien qu'étant un service moins confidentiel que Ollama, a une offre de quota bien plus étendue. Pour configurer Marimo avec Google AI Studio, vous devez avoir un compte Google.

    1. Sur [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys), vous pourrez générer une clé API.
    1. **Connexion**. Dans `⚙ > User settings > AI > AI Providers`, sous Google, collez la clé API.
    1. **Activation**. Dans `⚙ > User settings > AI > AI Models`, cochez Google.
    1. **Sélection**. Dans `⚙ > User settings > AI > AI Features`, sélectionnez *custom* sous Provider, et sélectionnez le modèle que vous voulez utilier pour Autocomplete Model (choisissez un modèle plus léger), Chat Model et Edit Model.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## L'IA dans VSCode

    L'extension Github Copilot offre un assistant performant et gratuit avec un compte GitHub (gratuit seulement dans sa version intrégrée dans VSCode), mais n'est pas privé: comme Gemini envoie le code à Google, GitHub Copilot envoie votre code à Github (Microsoft). Il existe d'autres options plus privées, comme les extensions [Cline](https://cline.bot/) et [Continue](https://www.continue.dev/), et si cela vous intéresse, vous trouverez votre chemin dans les dédales d'installations, et vous trouverez probablement comment utiliser un modèle Ollama gratuit. Dans le *chat* de Github Copilot, Continue ou Cline, cliquez sur le modèle actuel, et vous aurez le choix entre plusieurs - même ceux d'Ollama si vous l'avez installé.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## L'IA dans Zed

    [Zed](https://zed.dev/) est un IDE concurrent à VSCode, moins pratique pour les notebooks, mais très rapide et légère. Il vient avec un système d'agents IA que l'on peut connecter à de nombreux fournisseurs, dont Ollama. Fait intéressant, on y trouve une extension pour utiliser l'agent Mistral Vibe, qui se conforme à des règles de confidentialité européennes, plus strictes, et qui a une offre gratuite intéressante.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
