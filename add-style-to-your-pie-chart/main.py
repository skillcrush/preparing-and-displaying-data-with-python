import matplotlib.pyplot as plt

snack_scores = [80,45,34]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

plt.pie(snack_scores, labels=slice_labels)

plt.title("Snack Scores")

plt.savefig("snack_scores.png")