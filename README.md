# Détection de biais dans les données de santé au travail

**Projet portfolio — Master IA, Big Data & Développement (IPSSI Bordeaux)**

## Le problème

Les modèles d'IA en santé ne valent que ce que valent leurs données d'entraînement. Si les données de sinistralité AT/MP sous-représentent certaines populations (femmes dans le BTP, seniors dans l'intérim, jeunes dans le tertiaire), les algorithmes reproduiront ces biais sans que personne ne s'en rende compte.

Ce projet analyse la **représentativité** des bases de données publiques de santé au travail françaises et détecte les **biais démographiques** qui pourraient fausser des modèles prédictifs.

## Approche

Le projet croise trois sources de données ouvertes :

| Source | Contenu | Format |
|--------|---------|--------|
| **Assurance Maladie** | Sinistralité AT/MP par secteur CTN, sexe, âge | CSV/Excel |
| **DARES — SUMER 2017** | Expositions professionnelles par secteur (bruit, gestes répétitifs, RPS…) | XLS |
| **INSEE** | Population active de référence par secteur, sexe, âge | CSV |

L'analyse se déroule en 5 notebooks progressifs :

1. **Exploration** — Chargement, profilage, contrôles de cohérence
2. **Biais** — Ratios de représentation, test du Chi², indices de diversité
3. **Corrélations** — Croisement AT/MP × expositions SUMER, analyse de corrélation
4. **Prédiction ML** — Modèle Random Forest de prédiction du risque AT, SHAP
5. **Chatbot** — Assistant IA pour explorer les résultats (API Claude)

## Compétences démontrées

- **Data Analysis** : pandas, profiling, statistiques descriptives
- **Data Visualization** : matplotlib, seaborn, plotly
- **Statistiques** : Chi², Pearson, Shannon, représentativité
- **Machine Learning** : scikit-learn, Random Forest, SHAP, évaluation
- **IA responsable** : détection de biais, équité algorithmique
- **Expertise métier** : 20 ans en santé au travail (IPRP/IST)

## Installation

```bash
git clone https://github.com/laurebonnefond/biais-sante-travail.git
cd biais-sante-travail
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```

## Structure du projet

```
biais-sante-travail/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_exploration.ipynb     # Profilage des données
│   ├── 02_biais.ipynb           # Détection de biais
│   ├── 03_correlations.ipynb    # Corrélations AT × DARES
│   ├── 04_prediction_ml.ipynb   # Modèle prédictif
│   └── 05_chatbot.ipynb         # Chatbot IA
├── data/
│   ├── raw/                     # Données brutes
│   └── processed/               # Données nettoyées
├── src/
│   └── utils.py                 # Fonctions réutilisables
└── assets/                      # Figures générées
```

## Sources et références

- [Assurance Maladie — Open Data Risques Professionnels](https://www.assurance-maladie.ameli.fr/etudes-et-donnees/donnees/liste-donnees-open-data)
- [DARES — Enquête SUMER 2017](https://dares.travail-emploi.gouv.fr/enquete-source/surveillance-medicale-des-expositions-des-salaries-aux-risques-professionnels)
- [DARES — Synthèse Stat n°35 : Expositions par secteur](https://dares.travail-emploi.gouv.fr/publications/les-expositions-aux-risques-professionnels-par-secteur-d-activite)
- [INSEE — Population active](https://www.insee.fr/fr/statistiques)
- [INRS — Statistiques AT/MP](https://www.inrs.fr/demarche/atmp/statistiques-nationales.html)

## Auteure

**Laure Bonnefond** — Infirmière santé au travail & IPRP  
Master IA, Big Data & Développement — IPSSI Bordeaux (2026-2028)

## Licence

MIT
