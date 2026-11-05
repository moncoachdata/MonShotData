# MonShotData · le code des shots

Ce dépôt réunit le code Python des shots de la newsletter [MonShotData](https://www.monshotdata.com) : des astuces concrètes en data science, machine learning et IA, que tu peux appliquer tout de suite.

Les notebooks Jupyter qui accompagnent les shots sont ici, rangés par thème : **173 notebooks** répartis en 16 dossiers de sujets, plus un dossier de jeux de données.

## Comment retrouver le code d'un shot

1. Repère le thème du shot (Pandas, Plotting, Machine Learning…) et ouvre le dossier correspondant.
2. Ouvre le notebook : son nom reprend le sujet du shot.
3. Ou passe directement par l'[index](#index-par-thème) plus bas : les shots y sont reliés à leur notebook.

## Lancer un notebook

- **Sans rien installer** : ouvre le notebook dans Google Colab avec le lien « Colab » de l'index.
- **En local** : clone le dépôt, lance Jupyter, puis installe avec `pip install` les bibliothèques dont le notebook a besoin.
- Les jeux de données utilisés par certains notebooks sont dans le dossier [`_datasets`](https://github.com/moncoachdata/MonShotData/tree/main/_datasets).

```bash
git clone https://github.com/moncoachdata/MonShotData.git
cd MonShotData
jupyter notebook
```

## Les dossiers

| Dossier | Contenu | Notebooks |
|---|---|---:|
| [`Astuces Jupyter`](https://github.com/moncoachdata/MonShotData/tree/main/Astuces%20Jupyter) | Gagner du temps dans Jupyter : commandes magiques, sorties de cellules, interactivité. | 6 |
| [`Debugging`](https://github.com/moncoachdata/MonShotData/tree/main/Debugging) | Déboguer autrement qu'avec `print()` : IceCream, PySnooper. | 3 |
| [`Données Manquantes`](https://github.com/moncoachdata/MonShotData/tree/main/Donne%CC%81es%20Manquantes) | Visualiser et gérer les valeurs manquantes. | 2 |
| [`Machine Learning`](https://github.com/moncoachdata/MonShotData/tree/main/Machine%20Learning) | Clustering, régression, PCA, réseaux de neurones, évaluation et préparation des données. | 29 |
| [`NumPy`](https://github.com/moncoachdata/MonShotData/tree/main/NumPy) | Calcul matriciel, performances et petites astuces NumPy. | 8 |
| [`Optimisation Mémoire`](https://github.com/moncoachdata/MonShotData/tree/main/Optimisation%20Me%CC%81moire) | Consommer moins de mémoire : générateurs, types de données. | 4 |
| [`Optimisation du temps d'exécution`](https://github.com/moncoachdata/MonShotData/tree/main/Optimisation%20du%20temps%20d%27exe%CC%81cution) | Aller plus vite : Pandas, NumPy, Numba, Codon, formats de fichiers. | 13 |
| [`Outils cools`](https://github.com/moncoachdata/MonShotData/tree/main/Outils%20cools) | Des outils pratiques pour analyser ses données. | 1 |
| [`Pandas`](https://github.com/moncoachdata/MonShotData/tree/main/Pandas) | Manipuler les DataFrames plus vite et plus proprement. | 28 |
| [`Plotting`](https://github.com/moncoachdata/MonShotData/tree/main/Plotting) | Visualisation de données : Matplotlib, Seaborn, Plotly et graphiques alternatifs. | 30 |
| [`Python`](https://github.com/moncoachdata/MonShotData/tree/main/Python) | Python au-delà des bases : classes, dataclasses, mutabilité, décorateurs… | 35 |
| [`Sklearn`](https://github.com/moncoachdata/MonShotData/tree/main/Sklearn) | Scikit-learn : modèles de base, KMeans avec Faiss, Skorch, arbres de décision. | 6 |
| [`SQL`](https://github.com/moncoachdata/MonShotData/tree/main/SQL) | Les joins SQL avec DuckDB : semi join, anti join, natural join. | 1 |
| [`Statistiques`](https://github.com/moncoachdata/MonShotData/tree/main/Statistiques) | Corrélations et statistiques qui peuvent induire en erreur. | 3 |
| [`Terminal`](https://github.com/moncoachdata/MonShotData/tree/main/Terminal) | Recherche de code, traçage et refactorisation depuis le terminal. | 3 |
| [`Testing`](https://github.com/moncoachdata/MonShotData/tree/main/Testing) | Générer des données factices pour tester son code. | 1 |
| [`_datasets`](https://github.com/moncoachdata/MonShotData/tree/main/_datasets) | Les jeux de données utilisés par certains notebooks (Titanic, MNIST…). | · |

## Index par thème

Quand un shot s'appuie sur un notebook, les deux sont reliés dans le tableau. Les autres notebooks du dossier sont listés juste en dessous.

<details>
<summary><b>Astuces Jupyter</b> · 6 notebooks</summary>

_Gagner du temps dans Jupyter : commandes magiques, sorties de cellules, interactivité._

| Shot | Notebook | |
|---|---|---|
| [Transférer des variables entre les Notebooks Jupyter](https://www.monshotdata.com/p/transfert-variables-entre-notebooks) | [Commande magique store](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Commande-magique-store.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Commande-magique-store.ipynb) |
| [Récupérer la sortie calculée précédemment dans Jupyter Notebook](https://www.monshotdata.com/p/recuperer-sortie-cellule) | [Récupérer Output cellule](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Re%CC%81cupe%CC%81rer-Output-cellule.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Re%CC%81cupe%CC%81rer-Output-cellule.ipynb) |
| [Efface la sortie des cellules dans Jupyter Notebook pendant l'exécution](https://www.monshotdata.com/p/effacer-sortie-sur-jupyter-notebook) | [Clear cell Output](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Clear-cell-Output.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Clear-cell-Output.ipynb) |
| [Enrichis ton notebook avec des commandes interactives](https://www.monshotdata.com/p/notebook-avec-commandes-interactives) | [Commandes interactives](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Commandes-interactives.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Commandes-interactives.ipynb) |
| [Le hack Jupyter pour récupérer une sortie de cellule oubliée](https://www.monshotdata.com/p/3-facons-de-recuperer-la-sortie-dun-notebook-jupyter) | [Récupérer Output de 3 façons](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Re%CC%81cupe%CC%81rer-Output-de-3-fac%CC%A7ons.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Re%CC%81cupe%CC%81rer-Output-de-3-fac%CC%A7ons.ipynb) |

**Autres notebooks du dossier**

- [Chercher du code dans Jupyter](https://github.com/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Chercher-du-code-dans-Jupyter.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Astuces%20Jupyter/Chercher-du-code-dans-Jupyter.ipynb)

</details>

<details>
<summary><b>Debugging</b> · 3 notebooks</summary>

_Déboguer autrement qu'avec `print()` : IceCream, PySnooper._

| Shot | Notebook | |
|---|---|---|
| [N'utilise plus print() pour déboguer ton code](https://www.monshotdata.com/p/debogage-avec-icecream) | [icecream](https://github.com/moncoachdata/MonShotData/blob/main/Debugging/icecream.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Debugging/icecream.ipynb) |
| [Inspecter le flux du programme avec IceCream](https://www.monshotdata.com/p/inspection-flux-programme-avec-icecream) | [inspection flux](https://github.com/moncoachdata/MonShotData/blob/main/Debugging/inspection-flux.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Debugging/inspection-flux.ipynb) |
| [Le débogage facilité par PySnooper](https://www.monshotdata.com/p/debogage-facile-avec-pysnooper) | [pysnooper debugging](https://github.com/moncoachdata/MonShotData/blob/main/Debugging/pysnooper-debugging.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Debugging/pysnooper-debugging.ipynb) |

Fichiers annexes : [`pysnooper_expt.py`](https://github.com/moncoachdata/MonShotData/blob/main/Debugging/pysnooper_expt.py)

</details>

<details>
<summary><b>Données Manquantes</b> · 2 notebooks</summary>

_Visualiser et gérer les valeurs manquantes._

| Shot | Notebook | |
|---|---|---|
| [Gestion des Données Manquantes avec missingno](https://www.monshotdata.com/p/gestion-donnees-manquantes-avec-missingno) | [missingno](https://github.com/moncoachdata/MonShotData/blob/main/Donne%CC%81es%20Manquantes/missingno.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Donne%CC%81es%20Manquantes/missingno.ipynb) |
| [Datatype Sparse : gérer les valeurs manquantes avec Pandas](https://www.monshotdata.com/p/datatype-sparse) | [Datatype Sparse](https://github.com/moncoachdata/MonShotData/blob/main/Donne%CC%81es%20Manquantes/Datatype-Sparse.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Donne%CC%81es%20Manquantes/Datatype-Sparse.ipynb) |

</details>

<details>
<summary><b>Machine Learning</b> · 29 notebooks</summary>

_Clustering, régression, PCA, réseaux de neurones, évaluation et préparation des données._

| Shot | Notebook | |
|---|---|---|
| [KMeans vs DBSCAN : pourquoi KMeans n'est pas toujours adapté](https://www.monshotdata.com/p/kmeans-vs-dbscan-pour-clustering) | [DBSCAN vs KMeans](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/DBSCAN-vs-KMeans.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/DBSCAN-vs-KMeans.ipynb) |
| [Comment encoder des variables catégorielles avec plusieurs catégories ?](https://www.monshotdata.com/p/comment-encoder-des-variables-categorielles-avec-plusieurs-categories) | [Encodage catégoriel](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Encodage-cate%CC%81goriel.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Encodage-cate%CC%81goriel.ipynb) |
| [Augmentation des données : la technique sous-estimée du ML](https://www.monshotdata.com/p/une-technique-pour-ameliorer-la-performance-des-modeles) | [Augmentation Data](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Augmentation-Data.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Augmentation-Data.ipynb) |
| [KMeans++ : accélérer KMeans grâce à une meilleure initialisation](https://www.monshotdata.com/p/astuce-pour-ameliorer-la-duree-d-execution-de-kmeans) | [Améliorer durée exécution du KMeans](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Ame%CC%81liorer-dure%CC%81e-exe%CC%81cution-du-KMeans.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Ame%CC%81liorer-dure%CC%81e-exe%CC%81cution-du-KMeans.ipynb) |
| [Pourquoi définir des seeds pour les générateurs aléatoires ?](https://www.monshotdata.com/p/pourquoi-definir-des-seeds-pour-les-generateurs-aleatoires) | [Pourquoi fixer des Seeds](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Pourquoi-fixer-des-Seeds.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Pourquoi-fixer-des-Seeds.ipynb) |
| [Valide toujours ta variable de sortie avant d'utiliser la régression linéaire](https://www.monshotdata.com/p/valide-toujours-ta-variable-de-sortie-avant-d-utiliser-la-regression-lineaire) | [Régression Linéaire vérifier output](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Re%CC%81gression-Line%CC%81aire-ve%CC%81rifier-output.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Re%CC%81gression-Line%CC%81aire-ve%CC%81rifier-output.ipynb) |
| [Pourquoi est-il important de mélanger les données avant d'entraîner un modèle de ML ?](https://www.monshotdata.com/p/pourquoi-est-il-important-de-melanger-les-donnees-avant-d-entrainer-un-modele-de-ml) | [Pourquoi mélanger les données](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Pourquoi-me%CC%81langer-les-donne%CC%81es.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Pourquoi-me%CC%81langer-les-donne%CC%81es.ipynb) |
| [Le déséquilibre des classes : est-ce vraiment un problème incontournable en Machine Learning ?](https://www.monshotdata.com/p/le-desequilibre-des-classes-en-machine-learning) | [Déséquilibre des classes](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/De%CC%81se%CC%81quilibre-des-classes.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/De%CC%81se%CC%81quilibre-des-classes.ipynb) |
| [KMeans vs DBSCAN : comparaison visuelle des méthodes de clustering](https://www.monshotdata.com/p/comparaison-visuelle-entre-le-clustering-kmeans-vs-dbscan) | [Limites KMeans pour clustering](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Limites-KMeans-pour-clustering.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Limites-KMeans-pour-clustering.ipynb) |
| [Visualisation de l'impact des paramètres de régularisation](https://www.monshotdata.com/p/visualisation-de-l-impact-des-parametres-de-regularisation) | [Visualisation Régularisation](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Visualisation-Re%CC%81gularisation.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Visualisation-Re%CC%81gularisation.ipynb) |
| [Comment choisir le nombre parfait de dimensions avec l'Analyse en Composantes Principales ?](https://www.monshotdata.com/p/comment-choisir-le-nombre-parfait-de-dimensions-avec-le-pca) | [PCA hyperparamètre du nombre de dimensions](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/PCA-hyperparame%CC%80tre-du-nombre-de-dimensions.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/PCA-hyperparame%CC%80tre-du-nombre-de-dimensions.ipynb) |
| [Comment savoir si ta régression est performante ? La réponse en un graphique.](https://www.monshotdata.com/p/comment-savoir-si-ta-regression-est-performante) | [Diagramme résiduel de Régression Linéaire](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Diagramme-re%CC%81siduel-de-Re%CC%81gression-Line%CC%81aire.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Diagramme-re%CC%81siduel-de-Re%CC%81gression-Line%CC%81aire.ipynb) |
| [Un graphique simple pour visualiser la performance de tes régressions linéaires](https://www.monshotdata.com/p/un-graphique-simple-pour-visualiser-la-performance-de-tes-regressions-lineaires) | [Diagramme des résidus pour régression linéaire](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Diagramme-des-re%CC%81sidus-pour-re%CC%81gression-line%CC%81aire.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Diagramme-des-re%CC%81sidus-pour-re%CC%81gression-line%CC%81aire.ipynb) |
| [Quand la régression linéaire échoue : Découvre la méthode Theil-Sen](https://www.monshotdata.com/p/regression-theil-sen) | [Régression Theil Sen](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Re%CC%81gression-Theil-Sen.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Re%CC%81gression-Theil-Sen.ipynb) |
| [Régression linéaire sous-performante ? Traite l'asymétrie](https://www.monshotdata.com/p/asymetrie-regression-lineaire) | [Transformation des données pour la normalité](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Transformation-des-donne%CC%81es-pour-la-normalite%CC%81.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Transformation-des-donne%CC%81es-pour-la-normalite%CC%81.ipynb) |
| [Clustering non supervisé : les 3 métriques essentielles à connaître](https://www.monshotdata.com/p/performance-clustering-non-supervise) | [Évaluation Clustering Non Supervisé](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/E%CC%81valuation-Clustering-Non-Supervise%CC%81.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/E%CC%81valuation-Clustering-Non-Supervise%CC%81.ipynb) |
| [Arbres de décision : L'erreur que tout le monde fait (et comment l'éviter)](https://www.monshotdata.com/p/surapprentissage-arbres-decision) | [Surapprentissage arbres decision](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Surapprentissage-arbres-decision.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Surapprentissage-arbres-decision.ipynb) |
| [Comment les réseaux de neurones gèrent les données non séparables](https://www.monshotdata.com/p/reseaux-neurones-non-lineaires) | [Transformation Réseau de Neurones](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Transformation-Re%CC%81seau-de-Neurones.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Transformation-Re%CC%81seau-de-Neurones.ipynb) |

**Autres notebooks du dossier**

- [Confusion Scaling et Standardisation](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Confusion-Scaling-et-Standardisation.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Confusion-Scaling-et-Standardisation.ipynb)
- [Distance Mahalanobis](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Distance-Mahalanobis.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Distance-Mahalanobis.ipynb)
- [Graphique QQ](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Graphique-QQ.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Graphique-QQ.ipynb)
- [Guide PCA](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Guide-PCA.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Guide-PCA.ipynb)
- [Kernel PCA vs PCA](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Kernel-PCA-vs-PCA.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Kernel-PCA-vs-PCA.ipynb)
- [KMeans Faiss](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/KMeans-Faiss.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/KMeans-Faiss.ipynb)
- [KMeans Sklearn vs Faiss](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/KMeans-Sklearn-vs-Faiss.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/KMeans-Sklearn-vs-Faiss.ipynb)
- [Limites Régression Linéaire](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Limites-Re%CC%81gression-Line%CC%81aire.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Limites-Re%CC%81gression-Line%CC%81aire.ipynb)
- [Modèle de base Sklearn](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Mode%CC%80le-de-base-Sklearn.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Mode%CC%80le-de-base-Sklearn.ipynb)
- [Score de silhouette vs Méthode du coude](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Score-de-silhouette-vs-Me%CC%81thode-du-coude.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Score-de-silhouette-vs-Me%CC%81thode-du-coude.ipynb)
- [Skorch](https://github.com/moncoachdata/MonShotData/blob/main/Machine%20Learning/Skorch.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Machine%20Learning/Skorch.ipynb)

</details>

<details>
<summary><b>NumPy</b> · 8 notebooks</summary>

_Calcul matriciel, performances et petites astuces NumPy._

| Shot | Notebook | |
|---|---|---|
| [Régression linéaire polynomiale avec NumPy](https://www.monshotdata.com/p/regression-lineaire-avec-numpy) | [Régression Linéaire NumPy](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/R%C3%A9gression-Lin%C3%A9aire-NumPy.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/R%C3%A9gression-Lin%C3%A9aire-NumPy.ipynb) |
| [N'imprime plus les tableaux NumPy (Utilise plutôt Lovely-NumPy)](https://www.monshotdata.com/p/lonely-numpy) | [Lovely NumPy](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Lovely-NumPy.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Lovely-NumPy.ipynb) |
| [Différence entre Dot et Matmul avec NumPy](https://www.monshotdata.com/p/difference-dot-et-matmul) | [Dot et Matmul](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Dot-et-Matmul.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Dot-et-Matmul.ipynb) |
| [Une façon élégante d'effectuer la multiplication matricielle](https://www.monshotdata.com/p/une-facon-elegante-deffectuer-la-multiplication-matricielle) | [Opérateur multiplication matricielle](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Ope%CC%81rateur-multiplication-matricielle.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Ope%CC%81rateur-multiplication-matricielle.ipynb) |
| [Accélérer NumPy jusqu'à 20x avec Numexpr](https://www.monshotdata.com/p/acclrer-numpy-de-20x-avec-numexpr) | [Accélération de NumPy](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Acce%CC%81le%CC%81ration-de-NumPy.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Acce%CC%81le%CC%81ration-de-NumPy.ipynb) |

**Autres notebooks du dossier**

- [Accélérer NumPy avec Bottleneck](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Acce%CC%81le%CC%81rer-NumPy-avec-Bottleneck.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Acce%CC%81le%CC%81rer-NumPy-avec-Bottleneck.ipynb)
- [Différente Sortie pour Std Dev](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Diffe%CC%81rente-Sortie-pour-Std-Dev.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Diffe%CC%81rente-Sortie-pour-Std-Dev.ipynb)
- [Sorties NaN](https://github.com/moncoachdata/MonShotData/blob/main/NumPy/Sorties-NaN.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/NumPy/Sorties-NaN.ipynb)

</details>

<details>
<summary><b>Optimisation Mémoire</b> · 4 notebooks</summary>

_Consommer moins de mémoire : générateurs, types de données._

| Shot | Notebook | |
|---|---|---|
| [Économise de la mémoire avec les générateurs Python](https://www.monshotdata.com/p/generateurs-python) | [Générateurs](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/G%C3%A9n%C3%A9rateurs.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/G%C3%A9n%C3%A9rateurs.ipynb) |
| [Réduire de 90% l'utilisation de la mémoire d'un DataFrame Pandas](https://www.monshotdata.com/p/reduire-utilisation-memoire-dun-dataframe-pandas) | [Pandas Optimiser Datatype](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Pandas-Optimiser-Datatype.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Pandas-Optimiser-Datatype.ipynb) |

**Autres notebooks du dossier**

- [Modifier Datatype](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Modifier-Datatype.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Modifier-Datatype.ipynb)
- [Type de Données Catégorielles](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Type-de-Donne%CC%81es-Cate%CC%81gorielles.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20Me%CC%81moire/Type-de-Donne%CC%81es-Cate%CC%81gorielles.ipynb)

</details>

<details>
<summary><b>Optimisation du temps d'exécution</b> · 13 notebooks</summary>

_Aller plus vite : Pandas, NumPy, Numba, Codon, formats de fichiers._

| Shot | Notebook | |
|---|---|---|
| [La vectorisation ne garantit pas toujours de meilleures performances](https://www.monshotdata.com/p/mythe-vectorisation) | [Mythe de la Vectorisation](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Mythe-de-la-Vectorisation.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Mythe-de-la-Vectorisation.ipynb) |

**Autres notebooks du dossier**

- [Accélération de NumPy](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81ration-de-NumPy.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81ration-de-NumPy.ipynb)
- [Accélération Parquet](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81ration-Parquet.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81ration-Parquet.ipynb)
- [Accélérer NumPy avec Bottleneck](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81rer-NumPy-avec-Bottleneck.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81rer-NumPy-avec-Bottleneck.ipynb)
- [Accélérer Python avec Numba](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81rer-Python-avec-Numba.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Acce%CC%81le%CC%81rer-Python-avec-Numba.ipynb)
- [Apply Pandas avec NumPy](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Apply-Pandas-avec-NumPy.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Apply-Pandas-avec-NumPy.ipynb)
- [Apply plus rapide avec Swifter](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Apply-plus-rapide-avec-Swifter.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Apply-plus-rapide-avec-Swifter.ipynb)
- [Codon vs Python](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Codon-vs-Python.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Codon-vs-Python.ipynb)
- [Colonnes Conditionnelles](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Colonnes-Conditionnelles.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Colonnes-Conditionnelles.ipynb)
- [CSV Pickle Parquet Feather](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/CSV-Pickle-Parquet-Feather.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/CSV-Pickle-Parquet-Feather.ipynb)
- [KMeans Sklearn vs Faiss](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/KMeans-Sklearn-vs-Faiss.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/KMeans-Sklearn-vs-Faiss.ipynb)
- [Meilleur moyen d itérer un DataFrame](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Meilleur-moyen-d-ite%CC%81rer-un-DataFrame.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Meilleur-moyen-d-ite%CC%81rer-un-DataFrame.ipynb)
- [Ne jamais itérer sur un DataFrame](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Ne-jamais-ite%CC%81rer-sur-un-DataFrame.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/Ne-jamais-ite%CC%81rer-sur-un-DataFrame.ipynb)

Fichiers annexes : [`codon_expt.py`](https://github.com/moncoachdata/MonShotData/blob/main/Optimisation%20du%20temps%20d%27exe%CC%81cution/codon_expt.py)

</details>

<details>
<summary><b>Outils cools</b> · 1 notebooks</summary>

_Des outils pratiques pour analyser ses données._

| Shot | Notebook | |
|---|---|---|
| [Crée des tableaux croisés dynamiques sans code avec PivotTableJS](https://www.monshotdata.com/p/pivot-table-en-nocode) | [Nocode Pivot Groupby](https://github.com/moncoachdata/MonShotData/blob/main/Outils%20cools/Nocode-Pivot-Groupby.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Outils%20cools/Nocode-Pivot-Groupby.ipynb) |

Fichiers annexes : [`pivottablejs.html`](https://github.com/moncoachdata/MonShotData/blob/main/Outils%20cools/pivottablejs.html)

</details>

<details>
<summary><b>Pandas</b> · 28 notebooks</summary>

_Manipuler les DataFrames plus vite et plus proprement._

| Shot | Notebook | |
|---|---|---|
| [Définir le bon type de données pour les colonnes catégorielles](https://www.monshotdata.com/p/reduire-usage-memoire) | [Type de Données Catégorielles](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Type-de-Donn%C3%A9es-Cat%C3%A9gorielles.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Type-de-Donn%C3%A9es-Cat%C3%A9gorielles.ipynb) |
| [Modifier le type de données de plusieurs colonnes à la fois](https://www.monshotdata.com/p/modifier-datatypes) | [Modifier Datatype](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Modifier-Datatype.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Modifier-Datatype.ipynb) |
| [Ne crée pas de colonnes conditionnelles avec Apply de Pandas](https://www.monshotdata.com/p/colonness-conditionnelles) | [Colonnes Conditionnelles](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Colonnes-Conditionnelles.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Colonnes-Conditionnelles.ipynb) |
| [De jolis tracés interactifs avec Pandas](https://www.monshotdata.com/p/backend-plotly-avec-pandas) | [Backend Plotly avec Pandas](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Backend-Plotly-avec-Pandas.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Backend-Plotly-avec-Pandas.ipynb) |
| [Paralléliser Apply() de Pandas avec Swifter](https://www.monshotdata.com/p/apply-plus-rapide-avec-swifter) | [Apply plus rapide avec Swifter](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Apply-plus-rapide-avec-Swifter.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Apply-plus-rapide-avec-Swifter.ipynb) |
| [Une fonctionnalité cachée de la méthode describe de Pandas](https://www.monshotdata.com/p/caracteristique-cachee-methode-describe-de-pandas) | [Feature cachee de describe pandas](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Feature-cachee-de-describe-pandas.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Feature-cachee-de-describe-pandas.ipynb) |
| [Les styles Pandas : analyse tes DataFrames plus facilement](https://www.monshotdata.com/p/style-dataframes) | [Style DataFrames](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Style-DataFrames.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Style-DataFrames.ipynb) |
| [Supercharge la méthode value_counts() de Pandas avec Sidetable](https://www.monshotdata.com/p/superchage-value-counts-de-pandas) | [Meilleure méthode value counts](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Meilleure-me%CC%81thode-value_counts.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Meilleure-me%CC%81thode-value_counts.ipynb) |
| [Pandas-flavor : ajoute tes propres méthodes à un DataFrame](https://www.monshotdata.com/p/personnaliser-pandas) | [Personnalisation de Pandas](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Personnalisation-de-Pandas.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Personnalisation-de-Pandas.ipynb) |
| [Pandas merge() : trace l'origine des lignes avec indicator](https://www.monshotdata.com/p/argument-indicator-de-merge-pandas) | [Pandas Merge Indicator](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Pandas-Merge-Indicator.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Pandas-Merge-Indicator.ipynb) |
| [Le meilleur format de fichier pour stocker un DataFrame Pandas](https://www.monshotdata.com/p/meilleur-format-stockage-dataframe-pandas) | [CSV Pickle Parquet Feather](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/CSV-Pickle-Parquet-Feather.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/CSV-Pickle-Parquet-Feather.ipynb) |
| [3 astuces moins connues pour lire un fichier CSV avec Pandas](https://www.monshotdata.com/p/3-fonctionnalites-de-read-csv) | [3 Features de Read CSV](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/3-Features-de-Read-CSV.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/3-Features-de-Read-CSV.ipynb) |
| [Pandas apply : renvoyer plusieurs colonnes avec result_type](https://www.monshotdata.com/p/une-fonctionnalit-moins-connue-de-la-mthode-apply-de-pandas) | [Apply DataFrame Output](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Apply-DataFrame-Output.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Apply-DataFrame-Output.ipynb) |
| [Accélérer 5x la vitesse de Apply Pandas avec NumPy](https://www.monshotdata.com/p/accelerer-5x-apply-pandas-avec-numpy) | [Apply Pandas avec NumPy](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Apply-Pandas-avec-NumPy.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Apply-Pandas-avec-NumPy.ipynb) |
| [Arrête d'utiliser la méthode Describe de Pandas (épisode 2)](https://www.monshotdata.com/p/utilise-skimpy-plutot-que-describe) | [Skimpy](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Skimpy.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Skimpy.ipynb) |
| [Pandas : intégrer des graphiques dans les cellules d'un DataFrame](https://www.monshotdata.com/p/une-facon-moins-connue-de-creer-des-graphes-avec-pandas) | [DF avec graphiques inline](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/DF-avec-graphiques-inline.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/DF-avec-graphiques-inline.ipynb) |
| [Enrichis tes tableaux croisés dynamiques Pandas avec une heatmap](https://www.monshotdata.com/p/astuce-pour-enrichir-les-tableaux-croises-dynamiques) | [Enrichir les tableaux croisées dynamiques](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Enrichir-les-tableaux-croise%CC%81es-dynamiques.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Enrichir-les-tableaux-croise%CC%81es-dynamiques.ipynb) |
| [Itérer sur un DataFrame : passe par un tableau NumPy](https://www.monshotdata.com/p/meilleur-moyen-d-iterer-sur-un-dataframe) | [Meilleur moyen d itérer un DataFrame](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Meilleur-moyen-d-ite%CC%81rer-un-DataFrame.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Meilleur-moyen-d-ite%CC%81rer-un-DataFrame.ipynb) |
| [Pandas vs Polars : Comparaison des performances et de la mémoire](https://www.monshotdata.com/p/pandas-vs-polars) | [Polars vs Pandas](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Polars-vs-Pandas.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Polars-vs-Pandas.ipynb) |

**Autres notebooks du dossier**

- [Accélération Parquet](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Acce%CC%81le%CC%81ration-Parquet.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Acce%CC%81le%CC%81ration-Parquet.ipynb)
- [DataFrame depuis Dataclass](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/DataFrame-depuis-Dataclass.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/DataFrame-depuis-Dataclass.ipynb)
- [Différente Sortie pour Std Dev](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Diffe%CC%81rente-Sortie-pour-Std-Dev.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Diffe%CC%81rente-Sortie-pour-Std-Dev.ipynb)
- [Générer des conseils Pandas](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Ge%CC%81ne%CC%81rer-des-conseils-Pandas.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Ge%CC%81ne%CC%81rer-des-conseils-Pandas.ipynb)
- [Lecture CSV problématique](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Lecture-CSV-proble%CC%81matique.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Lecture-CSV-proble%CC%81matique.ipynb)
- [Ne jamais itérer sur un DataFrame](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Ne-jamais-ite%CC%81rer-sur-un-DataFrame.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Ne-jamais-ite%CC%81rer-sur-un-DataFrame.ipynb)
- [nsmallest et nlargest](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/nsmallest-et-nlargest.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/nsmallest-et-nlargest.ipynb)
- [Pandas Merge Validate](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/Pandas-Merge-Validate.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/Pandas-Merge-Validate.ipynb)
- [summarytools](https://github.com/moncoachdata/MonShotData/blob/main/Pandas/summarytools.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Pandas/summarytools.ipynb)

</details>

<details>
<summary><b>Plotting</b> · 30 notebooks</summary>

_Visualisation de données : Matplotlib, Seaborn, Plotly et graphiques alternatifs._

| Shot | Notebook | |
|---|---|---|
| [Simplifie ton tracé de régression avec Plotly](https://www.monshotdata.com/p/regression-avec-plotly) | [Tracé de Régression avec Plotly](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Trac%C3%A9-de-R%C3%A9gression-avec-Plotly.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Trac%C3%A9-de-R%C3%A9gression-avec-Plotly.ipynb) |
| [Tracer de façon élégante la frontière de décision d'un classificateur](https://www.monshotdata.com/p/frontieere-de-decision-classificateur) | [Frontière Décision Classifier](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Frontie%CC%80re-De%CC%81cision-Classifier.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Frontie%CC%80re-De%CC%81cision-Classifier.ipynb) |
| [Tracé de régression linéaire polynomiale facilité par Seaborn](https://www.monshotdata.com/p/regression-lineaire-polynomiale-avec-seaborn) | [Régression Linéaire polynomiale](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Re%CC%81gression-Line%CC%81aire-polynomiale.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Re%CC%81gression-Line%CC%81aire-polynomiale.ipynb) |
| [Analyser les données de flux avec les diagrammes de Sankey](https://www.monshotdata.com/p/analyse-flux-avec-diagrammes-sankey) | [Diagramme de Flux Sankey](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-de-Flux-Sankey.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-de-Flux-Sankey.ipynb) |
| [Diagrammes en cascade : Une meilleure alternative au tracé linéaire](https://www.monshotdata.com/p/diagrammes-en-cascade) | [Diagrammes Waterfall](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagrammes-Waterfall.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagrammes-Waterfall.ipynb) |
| [Les diagrammes à hexagones, une alternative plus riche aux diagrammes de dispersion](https://www.monshotdata.com/p/diagrammes-a-hexagones) | [Hexbins](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Hexbins.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Hexbins.ipynb) |
| [Diagramme à points : une alternative aux diagrammes à barres](https://www.monshotdata.com/p/diagramme-a-points) | [Diagramme à points](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-a%CC%80-points.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-a%CC%80-points.ipynb) |
| [Créer des tracés esquissés à la main en 1 ligne Python](https://www.monshotdata.com/p/creer-diagramme-esquisse-a-la-main) | [diagrammes style xkcd](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/diagrammes-style-xkcd.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/diagrammes-style-xkcd.ipynb) |
| [Diagramme de densité : lis enfin un nuage de milliers de points](https://www.monshotdata.com/p/diagramme-de-densite) | [Diagramme de densité](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-de-densite%CC%81.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-de-densite%CC%81.ipynb) |
| [Enrichir les nuages de mots en Python](https://www.monshotdata.com/p/enrichir-les-nuages-de-mots-en-python) | [Nuage de mots](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Nuage-de-mots.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Nuage-de-mots.ipynb) |
| [La carte calendaire, une alternative plus riche au tracé linéaire](https://www.monshotdata.com/p/la-carte-calendaire-une-alternative-plus-riche-au-trace-lineaire) | [Carte calendaire](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Carte-calendaire.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Carte-calendaire.ipynb) |
| [Perfplot : mesurer et comparer les durées d’exécution](https://www.monshotdata.com/p/mesurer-visualiser-et-comparer-les-durees-d-execution) | [Perfplot](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Perfplot.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Perfplot.ipynb) |
| [Rends tes tracés Matplotlib plus professionnels](https://www.monshotdata.com/p/rends-tes-traces-matplotlib-plus-professionnels) | [Matplotlib avec scienceplots](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Matplotlib-avec-scienceplots.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Matplotlib-avec-scienceplots.ipynb) |
| [Une technique sous-estimée pour créer de meilleurs graphiques de données](https://www.monshotdata.com/p/une-technique-sous-estimee-pour-creer-de-meilleurs-graphiques-de-donnees) | [Meilleur Storytelling](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Meilleur-Storytelling.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Meilleur-Storytelling.ipynb) |
| [Utiliser les diagrammes en boîte avec prudence ! Ils peuvent induire en erreur.](https://www.monshotdata.com/p/utiliser-les-diagrammes-en-boite-avec-prudence) | [Diagrammes en boîte trompeurs](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagrammes-en-boi%CC%82te-trompeurs.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagrammes-en-boi%CC%82te-trompeurs.ipynb) |
| [Ne crée pas de diagrammes à barres désordonnés. Essaye plutôt les diagrammes à bulles !](https://www.monshotdata.com/p/essaye-plutot-les-diagrammes-a-bulles)<br>[Tes diagrammes en barres sont illisibles ?](https://www.monshotdata.com/p/graphiques-bulles) | [Diagramme à bulles](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-a%CC%80-bulles.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Diagramme-a%CC%80-bulles.ipynb) |
| [Une technique sous-estimée pour améliorer tes visualisations de données](https://www.monshotdata.com/p/une-technique-sous-estimee-pour-ameliorer-te-visualisations-de-donnees) | [Annotations texte](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Annotations-texte.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Annotations-texte.ipynb) |
| [Heatmap avec taille : carrés ou cercles pour plus de lisibilité](https://www.monshotdata.com/p/une-astuce-simple-qui-rendra-tes-cartes-de-chaleur-plus-elegantes) | [Size encoded heatmaps](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Size-encoded-heatmaps.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Size-encoded-heatmaps.ipynb) |
| [Diagrammes de dispersion trop chargés ? Voici 3 façons simples de les épurer.](https://www.monshotdata.com/p/diagrammes-de-dispersion-trop-charges) | [3 astuces pour de meilleurs Scatter Plots](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/3-astuces-pour-de-meilleurs-Scatter-Plots.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/3-astuces-pour-de-meilleurs-Scatter-Plots.ipynb) |
| [Marque les esprits avec des graphiques Matplotlib spectaculaires !](https://www.monshotdata.com/p/marque-les-esprits-avec-des-graphiques-matplotlib-spectaculaires) | [Graphiques professionnels avec Matplotlib](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Graphiques-professionnels-avec-Matplotlib.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Graphiques-professionnels-avec-Matplotlib.ipynb) |
| [Le secret pour des graphiques Matplotlib de qualité stupéfiante](https://www.monshotdata.com/p/le-secret-pour-des-graphiques-matplotlib-de-qualite-stupefiante) | [Graphiques Matplotlib SVG](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Graphiques-Matplotlib-SVG.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Graphiques-Matplotlib-SVG.ipynb) |
| [Tes Heatmaps sont illisibles ? L'astuce qui change tout.](https://www.monshotdata.com/p/astuce-heatmaps-illisibles) | [Heatmap Scatter](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Heatmap-Scatter.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Heatmap-Scatter.ipynb) |
| [Visualiser l'évolution d'un classement ? Oublie les barres.](https://www.monshotdata.com/p/bump-chart-visualisation-classement-python) | [Bump chart](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Bump-chart.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Bump-chart.ipynb) |

**Autres notebooks du dossier**

- [bar chart race](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/bar-chart-race.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/bar-chart-race.ipynb)
- [Enrichir nos Heatmaps](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Enrichir-nos-Heatmaps.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Enrichir-nos-Heatmaps.ipynb)
- [Histogrammes trompeurs](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Histogrammes-trompeurs.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Histogrammes-trompeurs.ipynb)
- [Mosaic subplots](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Mosaic-subplots.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Mosaic-subplots.ipynb)
- [Ordre d'affichage Matplotlib](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Ordre-d%27affichage-Matplotlib.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Ordre-d%27affichage-Matplotlib.ipynb)
- [prévisualisation arbre de décision](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/pre%CC%81visualisation-arbre-de-de%CC%81cision.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/pre%CC%81visualisation-arbre-de-de%CC%81cision.ipynb)
- [Style Matplotlib](https://github.com/moncoachdata/MonShotData/blob/main/Plotting/Style-Matplotlib.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Plotting/Style-Matplotlib.ipynb)

</details>

<details>
<summary><b>Python</b> · 35 notebooks</summary>

_Python au-delà des bases : classes, dataclasses, mutabilité, décorateurs…_

| Shot | Notebook | |
|---|---|---|
| [Utilise la classe Slotted pour améliorer ton code Python](https://www.monshotdata.com/p/classe-slotted-pour-un-meilleur-code-python) | [Classes slotted](https://github.com/moncoachdata/MonShotData/blob/main/Python/Classes-slotted.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Classes-slotted.ipynb) |
| [Faire en sorte qu'un objet de classe se comporte comme une fonction](https://www.monshotdata.com/p/rendre-une-classe-appellable) | [Rendre une classe callable](https://github.com/moncoachdata/MonShotData/blob/main/Python/Rendre-une-classe-callable.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Rendre-une-classe-callable.ipynb) |
| [Pourquoi 256 est 256 mais 257 n'est pas 257 ?](https://www.monshotdata.com/p/comparaison-objets-entiers) | [Comparaison entiers](https://github.com/moncoachdata/MonShotData/blob/main/Python/Comparaison-entiers.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Comparaison-entiers.ipynb) |
| [Empêcher les importations sauvages en Python avec __all__](https://www.monshotdata.com/p/empecher-importations-sauvages) | [Importations sauvages](https://github.com/moncoachdata/MonShotData/blob/main/Python/Importations-sauvages.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Importations-sauvages.ipynb) |
| [Simplifie tes fonctions avec des fonctions partial](https://www.monshotdata.com/p/fonctions-partial) | [fonctions partial](https://github.com/moncoachdata/MonShotData/blob/main/Python/fonctions-partial.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/fonctions-partial.ipynb) |
| [__post_init__ : Ajouter des attributs à un objet Dataclass après l'initialisation](https://www.monshotdata.com/p/dataclass-post-init) | [dataclass post init](https://github.com/moncoachdata/MonShotData/blob/main/Python/dataclass-post-init.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/dataclass-post-init.ipynb) |
| [Frozenset : utiliser un set comme clé de dictionnaire](https://www.monshotdata.com/p/frozenset) | [Frozenset](https://github.com/moncoachdata/MonShotData/blob/main/Python/Frozenset.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Frozenset.ipynb) |
| [Rendre la notation par points plus puissante en Python](https://www.monshotdata.com/p/rendre-la-notation-par-points-plus-puissante-en-python) | [Notation par Points plus puissante](https://github.com/moncoachdata/MonShotData/blob/main/Python/Notation-par-Points-plus-puissante.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Notation-par-Points-plus-puissante.ipynb) |
| [Convertir Python en LaTeX n'a peut-être jamais été aussi simple](https://www.monshotdata.com/p/convertir-python-en-latex) | [Python en LaTeX](https://github.com/moncoachdata/MonShotData/blob/main/Python/Python-en-LaTeX.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Python-en-LaTeX.ipynb) |
| [Accélère ton code Python avec Numba en une seule ligne](https://www.monshotdata.com/p/accelerere-ton-code-python-avec-numba) | [Accélérer Python avec Numba](https://github.com/moncoachdata/MonShotData/blob/main/Python/Acce%CC%81le%CC%81rer-Python-avec-Numba.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Acce%CC%81le%CC%81rer-Python-avec-Numba.ipynb) |
| [10 façons de déclarer les annotations de type en Python](https://www.monshotdata.com/p/10-facons-de-declarer-les-annotations-de-type-en-python) | [Annotations de Type](https://github.com/moncoachdata/MonShotData/blob/main/Python/Annotations-de-Type.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Annotations-de-Type.ipynb) |
| [La manipulation d'objets mutables en Python peut parfois prêter à confusion](https://www.monshotdata.com/p/manipulation-d-objets-mutables-en-python) | [Modification objet mutable](https://github.com/moncoachdata/MonShotData/blob/main/Python/Modification-objet-mutable.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Modification-objet-mutable.ipynb) |
| [Python cache un secret que peu de programmeurs connaissent](https://www.monshotdata.com/p/python-cache-un-secret-que-peu-de-programmeurs-connaissent) | [Mutabilité Python](https://github.com/moncoachdata/MonShotData/blob/main/Python/Mutabilite%CC%81-Python.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Mutabilite%CC%81-Python.ipynb) |

**Autres notebooks du dossier**

- [Astuce de boucle moins connue](https://github.com/moncoachdata/MonShotData/blob/main/Python/Astuce-de-boucle-moins-connue.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Astuce-de-boucle-moins-connue.ipynb)
- [Astuce méthode startswith](https://github.com/moncoachdata/MonShotData/blob/main/Python/Astuce-me%CC%81thode-startswith.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Astuce-me%CC%81thode-startswith.ipynb)
- [Class Object contexte booléen](https://github.com/moncoachdata/MonShotData/blob/main/Python/Class-Object-contexte-boole%CC%81en.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Class-Object-contexte-boole%CC%81en.ipynb)
- [classmethod](https://github.com/moncoachdata/MonShotData/blob/main/Python/classmethod.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/classmethod.ipynb)
- [Codon vs Python](https://github.com/moncoachdata/MonShotData/blob/main/Python/Codon-vs-Python.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Codon-vs-Python.ipynb)
- [decorateur atexit register](https://github.com/moncoachdata/MonShotData/blob/main/Python/decorateur-atexit-register.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/decorateur-atexit-register.ipynb)
- [Dictionnaires contre intuitifs](https://github.com/moncoachdata/MonShotData/blob/main/Python/Dictionnaires-contre-intuitifs.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Dictionnaires-contre-intuitifs.ipynb)
- [Dictionnaires vs If Else](https://github.com/moncoachdata/MonShotData/blob/main/Python/Dictionnaires-vs-If-Else.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Dictionnaires-vs-If-Else.ipynb)
- [Différence Boucle For vs Liste de compréhension](https://github.com/moncoachdata/MonShotData/blob/main/Python/Diffe%CC%81rence-Boucle-For-vs-Liste-de-compre%CC%81hension.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Diffe%CC%81rence-Boucle-For-vs-Liste-de-compre%CC%81hension.ipynb)
- [DotMap meilleur dictionnaire](https://github.com/moncoachdata/MonShotData/blob/main/Python/DotMap-meilleur-dictionnaire.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/DotMap-meilleur-dictionnaire.ipynb)
- [f strings hack](https://github.com/moncoachdata/MonShotData/blob/main/Python/f-strings-hack.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/f-strings-hack.ipynb)
- [Les fonctions sont des objets](https://github.com/moncoachdata/MonShotData/blob/main/Python/Les-fonctions-sont-des-objets.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Les-fonctions-sont-des-objets.ipynb)
- [Liste Python comme clé dictionnaire](https://github.com/moncoachdata/MonShotData/blob/main/Python/Liste-Python-comme-cle%CC%81-dictionnaire.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Liste-Python-comme-cle%CC%81-dictionnaire.ipynb)
- [Masquer attributs dataclass](https://github.com/moncoachdata/MonShotData/blob/main/Python/Masquer-attributs-dataclass.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Masquer-attributs-dataclass.ipynb)
- [modificateurs accès Python](https://github.com/moncoachdata/MonShotData/blob/main/Python/modificateurs-acce%CC%80s-Python.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/modificateurs-acce%CC%80s-Python.ipynb)
- [Méthode join vs itération](https://github.com/moncoachdata/MonShotData/blob/main/Python/Me%CC%81thode-join-vs-ite%CC%81ration.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Me%CC%81thode-join-vs-ite%CC%81ration.ipynb)
- [Objet del Python](https://github.com/moncoachdata/MonShotData/blob/main/Python/Objet-del-Python.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Objet-del-Python.ipynb)
- [Stop Time.Time](https://github.com/moncoachdata/MonShotData/blob/main/Python/Stop-Time.Time.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Stop-Time.Time.ipynb)
- [Surcharge de fonctions](https://github.com/moncoachdata/MonShotData/blob/main/Python/Surcharge-de-fonctions.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Surcharge-de-fonctions.ipynb)
- [Tuple mutable](https://github.com/moncoachdata/MonShotData/blob/main/Python/Tuple-mutable.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Tuple-mutable.ipynb)
- [Underscores en Python](https://github.com/moncoachdata/MonShotData/blob/main/Python/Underscores-en-Python.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Underscores-en-Python.ipynb)
- [Warning deprecated](https://github.com/moncoachdata/MonShotData/blob/main/Python/Warning-deprecated.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Python/Warning-deprecated.ipynb)

Fichiers annexes : [`atexit-register.py`](https://github.com/moncoachdata/MonShotData/blob/main/Python/atexit-register.py), [`codon_expt.py`](https://github.com/moncoachdata/MonShotData/blob/main/Python/codon_expt.py)

</details>

<details>
<summary><b>Sklearn</b> · 6 notebooks</summary>

_Scikit-learn : modèles de base, KMeans avec Faiss, Skorch, arbres de décision._

| Shot | Notebook | |
|---|---|---|
| [Construis des modèles de base sans effort avec Sklearn](https://www.monshotdata.com/p/modeles-de-base-avec-sklearn) | [Modèle de base](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/Mode%CC%80le-de-base.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/Mode%CC%80le-de-base.ipynb) |
| [Rendre KMeans de Sklearn plus de 30 fois plus rapide](https://www.monshotdata.com/p/rendre-kmeans-de-sklearn-30x-plus-rapide) | [KMeans Sklearn vs Faiss](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/KMeans-Sklearn-vs-Faiss.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/KMeans-Sklearn-vs-Faiss.ipynb) |
| [Skorch : Utiliser l'API Scikit-learn sur les modèles PyTorch](https://www.monshotdata.com/p/skorch-utiliser-api-scikit-learn-sur-pytorch) | [Skorch](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/Skorch.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/Skorch.ipynb) |
| [Prévisualiser un arbre de décision avec Sklearn](https://www.monshotdata.com/p/previsualiser-un-arbre-de-decision-avec-sklearn) | [prévisualisation arbre de décision](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/pre%CC%81visualisation-arbre-de-de%CC%81cision.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/pre%CC%81visualisation-arbre-de-de%CC%81cision.ipynb) |

**Autres notebooks du dossier**

- [Données fictives avec Sklearn](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/Donne%CC%81es-fictives-avec-Sklearn.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/Donne%CC%81es-fictives-avec-Sklearn.ipynb)
- [Importation Metrics](https://github.com/moncoachdata/MonShotData/blob/main/Sklearn/Importation-Metrics.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Sklearn/Importation-Metrics.ipynb)

</details>

<details>
<summary><b>SQL</b> · 1 notebooks</summary>

_Les joins SQL avec DuckDB : semi join, anti join, natural join._

| Shot | Notebook | |
|---|---|---|
| [Semi, Anti et Natural Join : 3 joins SQL méconnus](https://www.monshotdata.com/p/semi-join-anti-join-natural-join-sql) | [Semi, Anti et Natural Join](https://github.com/moncoachdata/MonShotData/blob/main/SQL/Semi-Anti-Natural-Join.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/SQL/Semi-Anti-Natural-Join.ipynb) |

</details>

<details>
<summary><b>Statistiques</b> · 3 notebooks</summary>

_Corrélations et statistiques qui peuvent induire en erreur._

| Shot | Notebook | |
|---|---|---|
| [Pourquoi la corrélation (et d'autres statistiques) peut-elle être trompeuse ?](https://www.monshotdata.com/p/correlation-trompeuse) | [Statistiques trompeuses](https://github.com/moncoachdata/MonShotData/blob/main/Statistiques/Statistiques-trompeuses.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Statistiques/Statistiques-trompeuses.ipynb) |
| [La limite de la corrélation de Pearson que beaucoup ignorent souvent](https://www.monshotdata.com/p/limite-de-la-correlation-de-pearson-que-beaucoup-ignorent) | [Pearson vs Spearman](https://github.com/moncoachdata/MonShotData/blob/main/Statistiques/Pearson-vs-Spearman.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Statistiques/Pearson-vs-Spearman.ipynb) |
| [L'illusion des statistiques sommaires : un danger pour tes analyses de données](https://www.monshotdata.com/p/statistiques-sommaires-un-danger-pour-tes-analyses-de-donnees) | [Datasets avec zéro corrélation](https://github.com/moncoachdata/MonShotData/blob/main/Statistiques/Datasets-avec-ze%CC%81ro-corre%CC%81lation.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Statistiques/Datasets-avec-ze%CC%81ro-corre%CC%81lation.ipynb) |

</details>

<details>
<summary><b>Terminal</b> · 3 notebooks</summary>

_Recherche de code, traçage et refactorisation depuis le terminal._

| Shot | Notebook | |
|---|---|---|
| [Refactorisation automatisée du code avec Sourcery](https://www.monshotdata.com/p/refactorisation-automatisee-du-code-avec-sourcery) | [Sourcery](https://github.com/moncoachdata/MonShotData/blob/main/Terminal/Sourcery.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Terminal/Sourcery.ipynb) |

**Autres notebooks du dossier**

- [Chercher du code dans Jupyter](https://github.com/moncoachdata/MonShotData/blob/main/Terminal/Chercher-du-code-dans-Jupyter.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Terminal/Chercher-du-code-dans-Jupyter.ipynb)
- [Traçage Terminal](https://github.com/moncoachdata/MonShotData/blob/main/Terminal/Tra%C3%A7age-Terminal.ipynb) · [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Terminal/Tra%C3%A7age-Terminal.ipynb)

Fichiers annexes : [`my_code.py`](https://github.com/moncoachdata/MonShotData/blob/main/Terminal/my_code.py), [`my_code_refactored.py`](https://github.com/moncoachdata/MonShotData/blob/main/Terminal/my_code_refactored.py)

</details>

<details>
<summary><b>Testing</b> · 1 notebooks</summary>

_Générer des données factices pour tester son code._

| Shot | Notebook | |
|---|---|---|
| [Génère tes propres données fictives en quelques secondes](https://www.monshotdata.com/p/generer-donnees-factices) | [Générer Données Factices](https://github.com/moncoachdata/MonShotData/blob/main/Testing/G%C3%A9n%C3%A9rer-Donn%C3%A9es-Factices.ipynb) | [Colab](https://colab.research.google.com/github/moncoachdata/MonShotData/blob/main/Testing/G%C3%A9n%C3%A9rer-Donn%C3%A9es-Factices.ipynb) |

</details>

## Pour aller plus loin

- [Tous les shots](https://www.monshotdata.com/shots-data), classés par sujet
- [Les mini-cours du Cercle des Experts](https://www.monshotdata.com/mini-cours), pour aller au fond d'un sujet (aperçu gratuit de chacun)
- [DataXp](https://dataxp.fr), pour apprendre la data en codant, directement dans ton navigateur
- [La FAQ](https://www.monshotdata.com/faq)

## Une question, un bug, une idée ?

Ouvre une [issue](https://github.com/moncoachdata/MonShotData/issues) ou réponds directement à un mail de la newsletter.

---

Un notebook t'a servi ? Une étoile ⭐ sur le dépôt fait toujours plaisir, et tu peux [t'abonner à la newsletter](https://www.monshotdata.com/subscribe) pour recevoir les prochains shots.
