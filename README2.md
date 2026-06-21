# Détection de biais dans les données de santé au travail

**Projet portfolio — Master IA, Big Data & Développement (IPSSI Bordeaux)**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Le problème

Les modèles d'IA en santé ne valent que ce que valent leurs données d'entraînement. Si les données de sinistralité AT/MP sous-représentent certaines populations (femmes dans le BTP, seniors dans l'intérim, jeunes dans le tertiaire), les algorithmes reproduiront ces biais sans que personne ne s'en rende compte.

Ce projet analyse la **représentativité** des bases de données publiques de santé au travail françaises, détecte les **biais démographiques** qui pourraient fausser des modèles prédictifs, construit un **modèle ML équitable** de prédiction du risque AT, et fournit un **chatbot interactif** pour explorer les résultats.

## Résultats clés

| Indicateur | Valeur |
|---|---|
| Biais critiques détectés (écart > 10%) | **16** |
| Tests Chi² significatifs (genre) | **9/9 secteurs** |
| Corrélations significatives (AT × DARES) | **9** (p < 0.05) |
| Modèle ML — Accuracy test | **61%** |
| Modèle ML — F1-macro | **0.64** |
| Audit fairness (équité H/F) | **1.7%** (✅ < 5%) |
| Top prédicteur (SHAP) | **Contraintes posturales** |

## Sources de données

Le projet croise trois sources de données ouvertes :

| Source | Contenu | Format |
|--------|---------|--------|
| **Assurance Maladie** | Sinistralité AT/MP par secteur CTN, sexe, âge | CSV/Excel |
| **DARES — SUMER 2017** | Expositions professionnelles par secteur | XLS |
| **INSEE** | Population active de référence | CSV |

## Structure du projet

L'analyse se déroule en **5 notebooks progressifs** :

| # | Notebook | Compétence |
|---|---|---|
| 01 | **Exploration** — Chargement, profilage, contrôles de cohérence | Data Analysis |
| 02 | **Biais** — Ratios de représentation, test Chi², indices Shannon | Statistiques |
| 03 | **Corrélations** — AT/MP × expositions SUMER (Pearson, Spearman) | Analyse croisée |
| 04 | **Prédiction ML** — Random Forest, SHAP, audit fairness | Machine Learning |
| 05 | **Chatbot** — Assistant IA (API Claude) + widget HTML | Intégration IA |

```
biais-sante-travail/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_biais.ipynb
│   ├── 03_correlations.ipynb
│   ├── 04_prediction_ml.ipynb
│   └── 05_chatbot.ipynb
├── data/
│   ├── raw/             # Données brutes
│   └── processed/       # Résultats intermédiaires + modèle ML sérialisé
├── src/
│   └── utils.py         # Fonctions réutilisables
└── assets/
    ├── chatbot.html     # Widget interactif déployable
    └── *.png            # Figures générées (16 visualisations)
```

## Compétences démontrées

- **Data Analysis** : pandas, profiling, statistiques descriptives
- **Data Visualization** : matplotlib, seaborn, heatmaps, scatter plots
- **Statistiques** : Chi², Pearson, Spearman, Shannon, représentativité
- **Machine Learning** : scikit-learn, Random Forest, validation croisée stratifiée
- **Explicabilité** : SHAP values, permutation importance
- **IA responsable** : détection de biais, audit fairness, équité algorithmique
- **Intégration API** : Anthropic Claude, prompt engineering, conception conversationnelle
- **Expertise métier** : 20 ans en santé au travail (IPRP/IST)

## Installation et utilisation

```bash
git clone https://github.com/laurebonnefond/biais-sante-travail.git
cd biais-sante-travail
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```

Pour le chatbot (Notebook 05), définir la clé API :
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

## Démonstration

Le widget HTML interactif (`assets/chatbot.html`) peut être ouvert directement dans un navigateur ou déployé sur GitHub Pages pour une démonstration aux recruteurs.

## Sources et références

- [Assurance Maladie — Open Data Risques Professionnels](https://www.assurance-maladie.ameli.fr/etudes-et-donnees/donnees/liste-donnees-open-data)
- [DARES — Enquête SUMER 2017](https://dares.travail-emploi.gouv.fr/enquete-source/surveillance-medicale-des-expositions-des-salaries-aux-risques-professionnels)
- [DARES — Synthèse Stat n°35 : Expositions par secteur](https://dares.travail-emploi.gouv.fr/publications/les-expositions-aux-risques-professionnels-par-secteur-d-activite)
- [INSEE — Population active](https://www.insee.fr/fr/statistiques)
- [INRS — Statistiques AT/MP](https://www.inrs.fr/demarche/atmp/statistiques-nationales.html)

## Limites et perspectives

- **Dataset agrégé** : analyse au niveau secteur (CTN/NAF), pas au niveau établissement
- **Biais déclaratif non corrigé** : la sous-déclaration apparaît dans le modèle comme "risque faible"
- **Périmètre régime général** : pas de MSA, DOM, ou indépendants
- **Évolutions** : RAG sur les notebooks, intégration au site portfolio PréventIA-LaB, modèle régionalisé

## Auteure

**Laure Bonnefond** — Infirmière santé au travail & IPRP
Master IA, Big Data & Développement — IPSSI Bordeaux (2026-2028)

## Licence

MIT
