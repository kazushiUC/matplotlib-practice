import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 14

#===== practice 1 =====
fig, ax = plt.subplots(
    facecolor="white"
)

ax.bar(
    ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sut"],
    [19, 22, 24, 21, 20, 22, 20],
    label="highest temp",
)
ax.plot(
    ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sut"],
    [10, 13, 12, 12, 10, 11, 12],
    label="lowest temp",
    marker="^",
    color="m"
)

ax.set_xlabel(
    "day"
)
ax.set_ylabel(
    "temp",
    rotation="horizontal"
)
ax.set_title(
    "Temperature in Tokyo in October"
)
ax.set_yticks(
    [0, 5, 10, 15, 20, 25]
)
ax.grid()
ax.legend()


#===== practice 2 =====
fig, ax = plt.subplots(
    facecolor="white"
)

ax.scatter(
    [120, 122, 122, 123, 125, 125, 126, 127, 128, 129, 129, 130],
    [21, 23, 22, 26, 21, 25, 28, 27, 28, 25, 31, 32]
)

ax.set_xlabel("height")
ax.set_ylabel(
    "weight",
    rotation="horizontal"
)
ax.set_title("2-A")
ax.grid()


#===== practice 3 =====
fig, ax = plt.subplots(
    facecolor="white"
)

ax.hist(
    [30, 41, 43, 45, 50, 51, 55, 56, 59, 60, 61, 63, 64, 66, 69, 69, 72, 75, 77, 80, 87, 90, 95]
)

ax.set_xlabel("score")
ax.set_ylabel(
    "count",
    rotation="horizontal"
)
ax.set_title("2-A")
ax.grid()


#===== practice 4 =====
fig, ax = plt.subplots(
    2,
    2,
    facecolor="white",
    figsize=(15, 10)
)

ax[0, 0].plot(
    ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sut"],
    [19, 22, 24, 21, 20, 22, 20]
)

ax[0, 1].bar(
    ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sut"],
    [10, 13, 12, 12, 10, 11, 12],
)

ax[1, 0].scatter(
    [120, 122, 122, 123, 125, 125, 126, 127, 128, 129, 129, 130],
    [21, 23, 22, 26, 21, 25, 28, 27, 28, 25, 31, 32]
)

ax[1, 1].hist(
    [30, 41, 43, 45, 50, 51, 55, 56, 59, 60, 61, 63, 64, 66, 69, 69, 72, 75, 77, 80, 87, 90, 95]
)

ax[0, 0].grid()
ax[1, 0].grid()
ax[0, 1].grid()
ax[1, 1].grid()


plt.show()