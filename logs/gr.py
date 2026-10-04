import matplotlib.pyplot as plt

steps, train, val = [], [], []

with open("somelogs.txt") as f:
    for line in f:
        if line[:4] == "step":
            parts = line.split()
            steps.append(int(parts[1][:-1]))
            train.append(float(parts[4][:-1]))
            val.append(float(parts[7]))

plt.plot(steps, train, label="Train loss")
plt.plot(steps, val, label="Val loss")
plt.xlabel("Step")
plt.ylabel("Loss")
plt.legend()
plt.grid()
plt.savefig("loss.png")