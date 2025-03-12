import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind, mannwhitneyu
import os

# Trouver le chemin absolu du fichier en fonction du répertoire actuel
chemin_data = os.path.join(os.path.dirname(__file__), '../data/ab_data.csv')

# Charger les données
@st.cache_data
def load_data():
    file_path = chemin_data  # Assurez-vous de mettre le bon chemin
    df = pd.read_csv(file_path)
    df = df[~((df['group'] == 'control') & (df['landing_page'] == 'new_page'))]
    df = df[~((df['group'] == 'treatment') & (df['landing_page'] == 'old_page'))]
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    return df

df = load_data()

# Titre de l'application
st.title("📊 Analyse A/B Testing : Landing Page")

# Sélection d'une analyse
option = st.sidebar.selectbox("Choisissez une analyse", [
    "Aperçu des données",
    "Analyse Exploratoire (EDA)",
    "Évolution du taux de conversion",
    "Tests statistiques",
    "Conclusions et recommandations"
])

if option == "Aperçu des données":
    st.subheader("🔍 Aperçu des données")
    st.write(df.head())
    st.write(df.describe())

elif option == "Analyse Exploratoire (EDA)":
    st.subheader("📊 Analyse Exploratoire des Données")
    
    # Répartition des groupes
    fig, ax = plt.subplots()
    sns.countplot(x=df['group'], palette="coolwarm", ax=ax)
    ax.set_title("Répartition des groupes A/B")
    st.pyplot(fig)
    
    # Distribution des conversions
    fig, ax = plt.subplots()
    sns.histplot(df['converted'], bins=2, kde=False, discrete=True, ax=ax)
    ax.set_title("Distribution des conversions (0 = non converti, 1 = converti)")
    st.pyplot(fig)
    
    # Taux de conversion par groupe
    conversion_by_group = df.groupby("group")['converted'].mean()
    fig, ax = plt.subplots()
    sns.barplot(x=conversion_by_group.index, y=conversion_by_group.values, palette="coolwarm", ax=ax)
    ax.set_title("Taux de conversion par groupe")
    st.pyplot(fig)
    
elif option == "Évolution du taux de conversion":
    st.subheader("📈 Évolution du taux de conversion dans le temps")
    
    daily_conversion = df.groupby("date")['converted'].mean()
    fig, ax = plt.subplots()
    ax.plot(daily_conversion, marker="o", linestyle="-", color="b")
    ax.set_title("Évolution du taux de conversion au fil du temps")
    ax.set_xlabel("Date")
    ax.set_ylabel("Taux de conversion")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
elif option == "Tests statistiques":
    st.subheader("📊 Résultats des tests statistiques")
    
    # Test du Chi²
    contingency_table = pd.crosstab(df["group"], df["converted"])
    chi2, p_value_chi2, _, _ = chi2_contingency(contingency_table)
    st.write(f"🔹 **Test du Chi²** : Statistique = {chi2:.2f}, p-value = {p_value_chi2:.4f}")
    
    # Test de Student (T-Test)
    group_A = df[df["group"] == "control"]["converted"]
    group_B = df[df["group"] == "treatment"]["converted"]
    t_stat, p_value_ttest = ttest_ind(group_A, group_B)
    st.write(f"🔹 **Test de Student** : Statistique = {t_stat:.2f}, p-value = {p_value_ttest:.4f}")
    
    # Test de Mann-Whitney
    u_stat, p_value_mw = mannwhitneyu(group_A, group_B, alternative="two-sided")
    st.write(f"🔹 **Test de Mann-Whitney** : Statistique = {u_stat:.2f}, p-value = {p_value_mw:.4f}")
    
    # Interprétation des résultats
    if p_value_chi2 > 0.05 and p_value_ttest > 0.05 and p_value_mw > 0.05:
        st.write("❌ **Aucune différence significative entre les groupes.** La nouvelle page n'améliore pas la conversion.")
    else:
        st.write("✅ **Différence significative détectée.** La nouvelle page a un impact sur la conversion.")
    
elif option == "Conclusions et recommandations":
    st.subheader("📌 Conclusions et recommandations")
    st.write("- **Les deux pages ont des taux de conversion très proches.**")
    st.write("- **Les tests statistiques indiquent qu'il n'y a pas de différence significative entre les groupes.**")
    st.write("- **Recommandation** : Ne pas implémenter la nouvelle page sauf si d'autres métriques montrent un avantage.")
    st.write("- **Améliorations possibles** : Tester d'autres variantes de la page, analyser le comportement des utilisateurs.")

st.sidebar.write("📌 Sélectionnez une analyse pour explorer les résultats du test A/B.")