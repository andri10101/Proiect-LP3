"""
Script Python pentru analiza unui set de date despre boli de inimă.

Setul de date a fost preluat de la: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

AUTORI: CHERCIU I. E. ANDRA-MARIA, CIOBĂNICĂ I. D. ALEXANDRU CONSTANTIN
ECHIPA: 12-E3

Funcționalități implementate:
1. Citirea datelor cu pandas
2. Afișarea primelor 5 rânduri
3. Afișarea de statistici descriptive
4. Generarea a două histograme (vârstă și tensiune)
5. Crearea unei matrici de corelație (heatmap)

SURSE:
- https://pandas.pydata.org
- https://matplotlib.org
- https://seaborn.pydata.org
- https://www.geeksforgeeks.org/plotting-correlation-matrix-using-python/
"""

# Importăm bibliotecile necesare pentru manipularea și vizualizarea datelor
import pandas as pd               # pentru manipularea datelor tabelare (DataFrame)
import matplotlib.pyplot as plt   # pentru a crea grafice simple (ex. histograme)
import seaborn as sns             # pentru grafice avansate, cum ar fi heatmap-ul

# 1. Citirea datelor din fișier CSV

# Se citește fișierul 'heart.csv' aflat în același folder cu acest script.
# Acesta conține date despre pacienți (vârstă, sex, tensiune, colesterol)
df = pd.read_csv('heart.csv')

# 2. Afișarea primelor 5 rânduri

# Se afișează primele 5 rânduri pentru a înțelege structura și conținutul datelor
print("=== Primele 5 rânduri din setul de date ===\n")
print(df.head())

# 3. Statistici descriptive

# Se afișează statistici de bază: medie, deviație standard, min, max, quartile
print("\n=== Statistici descriptive pentru fiecare coloană ===\n")
print(df.describe())

# 4. Histogramă: Distribuția vârstei

# Cream o figură de 8x6 inch
plt.figure(figsize=(8, 6))

# Cream histograma pentru coloana 'vârsta' pacienților
# bins=15 înseamnă că vom împărți valorile în 15 intervale
plt.hist(df['varsta'], bins=15, color='skyblue', edgecolor='black')

# Adăugăm titlu și etichete pe axe
plt.title('Distribuția vârstei pacienților')
plt.xlabel('Vârstă')
plt.ylabel('Număr de pacienți')
plt.grid(True)  # adaugă o grilă pentru lizibilitate

# Afișăm graficul
plt.show()

# 5. Histogramă: Tensiunea la repaus


plt.figure(figsize=(8, 6))  # dimensiune grafic
plt.hist(df['tensiune'], bins=15, color='salmon', edgecolor='black')  # histograma tensiunii arteriale

# Titlu și etichete
plt.title('Distribuția tensiunii arteriale la repaus')
plt.xlabel('Tensiune arterială (mm Hg)')
plt.ylabel('Număr de pacienți')
plt.grid(True)

# Afișăm graficul
plt.show()

# 6. Matrice de corelație (heatmap)

# Calculăm corelația între toate coloanele numerice
# Corelația este un număr între -1 și 1 care arată cât de legate sunt două variabile
correlation_matrix = df.corr()

# Cream o figură mai mare pentru o mai bună vizibilitate
plt.figure(figsize=(12, 10))

# Desenăm un heatmap folosind Seaborn
# annot=True → afișează valorile în fiecare celulă
# cmap='coolwarm' → paleta de culori de la albastru (corelație negativă) la roșu (pozitivă)
# fmt='.2f' → afișează valorile rotunjite la 2 zecimale
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Adăugăm titlu
plt.title('Matrice de corelație între atributele din setul de date')

# Afișăm heatmap-ul
plt.show()