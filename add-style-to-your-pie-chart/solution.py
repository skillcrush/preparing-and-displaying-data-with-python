import matplotlib.pyplot as plt

snack_scores = [80,45,34]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

colors = ["#5F9EA0","#7FFFD4","#FF69B4"]

plt.pie(snack_scores, labels=slice_labels, colors=colors, )

plt.title("Snack Scores",  fontsize=16)

plt.savefig("snack_scores.png")