# 📊 Projet A/B Testing : Landing Page

Application : https://tests-statistiques-landing-page-gxdfuncfjkpxm9kfyzvafu.streamlit.app/

## 🎯 Objectif
Ce projet a pour but de **comparer deux versions d’une landing page** (une page "control" et une page "treatment") afin de déterminer laquelle convertit le mieux les utilisateurs.

## 📂 Contenu du projet
- **app.py** : Le script Streamlit qui permet d'explorer les données et d'effectuer les tests.
- **ab_data.csv** : Fichier de données brut (à placer dans le même répertoire que `app.py`).
- **README.md** : Ce fichier de documentation.

## 🛠️ Installation & Exécution
1. **Prérequis** : Assurez-vous d'avoir **Python 3.7+** et les dépendances suivantes :
   ```bash
   pip install streamlit pandas matplotlib seaborn scipy
   ```
2. **Lancer l'application** :
   ```bash
   streamlit run app.py
   ```

## 📌 Fonctionnalités de l'application Streamlit
- **Aperçu des données** : Affichage des premières lignes et statistiques descriptives du dataset.
- **Analyse Exploratoire (EDA)** : Distribution des groupes, histogramme des conversions, taux de conversion par groupe.
- **Évolution du taux de conversion** : Analyse de la conversion moyenne sur la période.
- **Variation quotidienne du taux de conversion par groupe** : Visualisation des taux de conversion journaliers pour la page de contrôle et la page de traitement.
- **Tests statistiques** :
  - **Test du Chi²** : pour comparer les proportions de conversions.
  - **Test de Student (T-Test)** : pour comparer les moyennes de conversions entre groupes.
  - **Test de Mann-Whitney** : test non paramétrique pour comparer les distributions.
  - **Interprétation** : Indique si la différence est significative ou non.
- **Conclusions et recommandations** : Synthèse finale du test A/B.

## 🎯 Objectifs et Méthodologie
1. **Importer et préparer les données** : Nettoyage des incohérences entre `group` et `landing_page`, conversion des dates.
2. **Analyse Exploratoire** : Découvrir la répartition des groupes, les taux de conversion globaux et par groupe.
3. **Visualisation temporelle** : Comprendre l'évolution de la conversion au fil du temps.
4. **Réaliser plusieurs tests statistiques** (Chi², T-Test, Mann-Whitney) pour évaluer la significativité des différences.
5. **Tirer des conclusions** sur la pertinence d’adopter la nouvelle page.

## 🔍 Résultats Clés
- **Taux de conversion global** : ~12%.
- **Pas de différence significative** entre la page de contrôle et la page de traitement (p-value > 0.05 dans tous les tests).
- **Conclusion** : La nouvelle page n’offre pas d’amélioration notable.

## 🚀 Recommandations
- **Ne pas implémenter la nouvelle page** en l’état, car elle n’améliore pas la conversion.
- **Tester de nouvelles variantes** avec un design ou un contenu différent.
- **Analyser des indicateurs complémentaires** (taux de rebond, temps moyen passé, etc.).


