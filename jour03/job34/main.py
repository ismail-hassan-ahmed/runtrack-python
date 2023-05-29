import matplotlib.pyplot as plt

with open("data.txt", "r") as f:
    sentences = f.readlines()

word_counts = [len(sentence.split()) for sentence in sentences]
plt.hist(word_counts, bins=range(0, 30, 2), color='blue')
plt.title('Distribution du nombre de mots par phrase')
plt.xlabel('Nombre de mots')
plt.ylabel('Fréquence')
plt.show()