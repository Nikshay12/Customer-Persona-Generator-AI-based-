import matplotlib.pyplot as plt
import seaborn as sns

def plot_persona_distribution(df):
    plt.figure(figsize=(6,4))
    sns.countplot(x='persona', data=df, palette='Set2')
    plt.title("User Persona Distribution")
    plt.xlabel("Persona Cluster")
    plt.ylabel("Number of Users")
    plt.tight_layout()
    return plt
