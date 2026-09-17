# geocoding



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

* [Create](https://docs.gitlab.com/user/project/repository/web_editor/#create-a-file) or [upload](https://docs.gitlab.com/user/project/repository/web_editor/#upload-a-file) files
* [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.esiee.fr/bakalayc/geocoding.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

* [Set up project integrations](https://git.esiee.fr/bakalayc/geocoding/-/settings/integrations)

## Collaborate with your team

* [Invite team members and collaborators](https://docs.gitlab.com/user/project/members/)
* [Create a new merge request](https://docs.gitlab.com/user/project/merge_requests/creating_merge_requests/)
* [Automatically close issues from merge requests](https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically)
* [Enable merge request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/)
* [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

* [Get started with GitLab CI/CD](https://docs.gitlab.com/ci/quick_start/)
* [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/user/application_security/sast/)
* [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/topics/autodevops/requirements/)
* [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/user/clusters/agent/)
* [Set up protected environments](https://docs.gitlab.com/ci/environments/protected_environments/)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Comparaison entre ma première implémentation et la correction assistée par IA

J’ai d’abord réalisé les différentes étapes du projet à partir des exemples du cours : géocodage d’une adresse, création d’une carte Folium, affichage des températures, extraction des communes d’Île-de-France et création d’une carte choroplèthe.

L’intelligence artificielle a ensuite été utilisée comme outil de correction et d’explication lorsque certaines erreurs apparaissaient.

### 1. Gestion de l’environnement Python

Dans ma première tentative, j’exécutais le programme avec :

```bash
python3 ex01_geocoding.py
```

Cette commande provoquait une erreur, car les bibliothèques installées avec `uv` n’étaient pas disponibles dans le Python global du Mac.

La correction a consisté à utiliser l’environnement reproductible du projet :

```bash
uv run python ex01_geocoding.py
```

J’ai compris qu’un projet contenant un fichier `pyproject.toml` devait être exécuté avec `uv run` afin d’utiliser les bonnes versions de Python et des dépendances.

### 2. Création de la carte météorologique

Dans ma première version, j’avais créé plusieurs objets `Map` et utilisé différentes variables comme `map`, `map1` et `carte`. J’avais notamment écrit :

```python
map.add_child(cm)
```

Cela provoquait une erreur, car `map` faisait référence à la fonction intégrée de Python et non à ma carte Folium.

La version corrigée utilise un seul objet :

```python
carte = folium.Map(
    location=coords,
    tiles="OpenStreetMap",
    zoom_start=6
)

carte.add_child(cm)
```

Cette correction m’a permis de comprendre qu’il fallait créer une seule carte, lui ajouter les différents éléments, puis l’enregistrer à la fin.

### 3. Exportation des données géographiques

J’avais initialement utilisé :

```python
geojson.dump(idf, fichier)
```

Cette instruction produisait une erreur, car une `GeoDataFrame` contient des objets NumPy qui ne sont pas directement sérialisables par le module `geojson`.

La correction proposée a été :

```python
idf.to_file(
    "idf.geojson",
    driver="GeoJSON",
    index=False
)
```

La méthode `to_file()` de GeoPandas est mieux adaptée à l’exportation d’une `GeoDataFrame`, car elle traite correctement les géométries et les types de données associés.

### 4. Préparation des données de population

Dans une première version, j’avais utilisé la variable `pop_data` avant de l’avoir créée, ce qui provoquait une erreur `NameError`.

L’ordre correct est :

```python
pop_data = pd.read_csv(
    "insee-pop-communes.csv",
    sep=";",
    dtype={"DEPCOM": str}
)

dpt_code = pop_data["DEPCOM"]
```

Le paramètre `dtype={"DEPCOM": str}` permet de conserver les codes INSEE sous forme de chaînes de caractères et d’éviter la suppression des zéros placés au début.

### 5. Filtrage des communes d’Île-de-France

Le masque booléen permet de déterminer si chaque commune appartient à l’un des départements franciliens :

```python
mask = (
    dpt_code.str.startswith("75")
    | dpt_code.str.startswith("77")
    | dpt_code.str.startswith("78")
    | dpt_code.str.startswith("91")
    | dpt_code.str.startswith("92")
    | dpt_code.str.startswith("93")
    | dpt_code.str.startswith("94")
    | dpt_code.str.startswith("95")
)
```

Il doit ensuite être réellement appliqué :

```python
pop_data = pop_data[mask]
```

Ma première version construisait le masque, mais ne l’appliquait pas systématiquement aux données.

### 6. Problème de correspondance pour Paris

Paris apparaissait en noir sur la carte choroplèthe. Le problème ne venait pas de Folium, mais d’une différence entre les deux jeux de données :

* le fichier GeoJSON représente Paris avec le code `75056` ;
* le fichier INSEE représente séparément les 20 arrondissements avec les codes `75101` à `75120`.

La correction consiste à additionner les populations des arrondissements et à créer une ligne unique pour le code `75056`.

Cette étape m’a permis de comprendre qu’une jointure peut échouer même lorsque les deux fichiers parlent du même territoire, si leurs identifiants ou leur niveau de découpage géographique sont différents.

### Conclusion

L’IA n’a pas seulement fourni une version corrigée du code. Elle m’a principalement aidée à interpréter les messages d’erreur, à identifier les incohérences entre les jeux de données et à comprendre le rôle de chaque outil.

Les principaux apprentissages sont :

* utiliser `uv` pour isoler et reproduire l’environnement Python ;
* différencier les données numériques, géographiques et cartographiques ;
* conserver les codes INSEE sous forme de chaînes de caractères ;
* appliquer correctement un masque Pandas ;
* utiliser GeoPandas pour exporter des données géographiques ;
* faire correspondre les jeux de données grâce à un identifiant commun ;
* vérifier la compatibilité du découpage géographique avant de construire une carte choroplèthe.
