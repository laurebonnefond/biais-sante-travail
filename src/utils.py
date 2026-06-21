"""
Fonctions utilitaires pour le projet Biais Santé au Travail.
Auteure : Laure Bonnefond — IPRP / IST
"""

import pandas as pd
import numpy as np
from scipy import stats


def ratio_representation(pct_data: float, pct_reference: float) -> float:
    """
    Calcule le ratio de représentation.
    
    ratio = 1.0 → représentation parfaite
    ratio < 1.0 → sous-représentation
    ratio > 1.0 → surreprésentation
    
    Args:
        pct_data: pourcentage dans le dataset
        pct_reference: pourcentage dans la population de référence
    
    Returns:
        Ratio de représentation (float)
    """
    if pct_reference == 0:
        return np.nan
    return pct_data / pct_reference


def test_chi2_representation(observed: list, expected: list) -> dict:
    """
    Test du Chi² pour évaluer si la distribution observée
    diffère significativement de la distribution attendue.
    
    Args:
        observed: effectifs observés par catégorie
        expected: effectifs attendus par catégorie
    
    Returns:
        dict avec chi2, p_value, significatif (seuil 5%)
    """
    chi2, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    return {
        'chi2': round(chi2, 2),
        'p_value': round(p_value, 6),
        'significatif': p_value < 0.05,
        'interpretation': (
            "Biais significatif détecté" if p_value < 0.05
            else "Pas de biais significatif"
        )
    }


def indice_shannon(proportions: list) -> float:
    """
    Calcule l'indice de diversité de Shannon.
    Plus l'indice est élevé, plus la distribution est diversifiée.
    
    Args:
        proportions: liste de proportions (doivent sommer à 1)
    
    Returns:
        Indice de Shannon (float)
    """
    proportions = np.array(proportions)
    proportions = proportions[proportions > 0]  # éviter log(0)
    return -np.sum(proportions * np.log2(proportions))


def indice_equitabilite(proportions: list) -> float:
    """
    Calcule l'indice d'équitabilité de Pielou (Shannon normalisé).
    
    E = 1.0 → distribution parfaitement uniforme
    E = 0.0 → une seule catégorie représentée
    
    Args:
        proportions: liste de proportions
    
    Returns:
        Indice d'équitabilité (float entre 0 et 1)
    """
    n = len([p for p in proportions if p > 0])
    if n <= 1:
        return 0.0
    h = indice_shannon(proportions)
    h_max = np.log2(n)
    return h / h_max if h_max > 0 else 0.0


def matrice_biais(df_data: pd.DataFrame, df_ref: pd.DataFrame,
                  cols_data: list, cols_ref: list,
                  index_col: str = 'secteur') -> pd.DataFrame:
    """
    Construit une matrice de ratios de représentation
    entre un dataset et une population de référence.
    
    Args:
        df_data: DataFrame des données à analyser
        df_ref: DataFrame de la population de référence
        cols_data: colonnes de pourcentage dans df_data
        cols_ref: colonnes correspondantes dans df_ref
        index_col: colonne d'index (ex: 'secteur')
    
    Returns:
        DataFrame avec les ratios (1.0 = parfait)
    """
    ratios = pd.DataFrame(index=df_data[index_col])
    for col_d, col_r in zip(cols_data, cols_ref):
        label = col_d.replace('pct_', '').replace('_', ' ').title()
        ratios[label] = (df_data[col_d].values / df_ref[col_r].values).round(2)
    return ratios


PALETTE = ['#0F6E56', '#185FA5', '#D85A30', '#534AB7', '#993556',
           '#BA7517', '#639922', '#E24B4A', '#5F5E5A']

CTN_LABELS = {
    'A': 'Métallurgie',
    'B': 'BTP',
    'C': 'Transports',
    'D': 'Commerce alim.',
    'E': 'Chimie',
    'F': 'Bois/Textile',
    'G': 'Commerce non alim.',
    'H': 'Services I',
    'I': 'Services II',
}
