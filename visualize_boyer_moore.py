import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def find_most_repeated_char(string):
    candidate = None
    count = 0
    max_count = 0
    max_char = None
    idx = 0

    # Find the candidate character using Boyer-Moore Majority Vote Algorithm
    for char in string:
        if count == 0:
            candidate = char
            count = 1
        elif char == candidate:
            count += 1
        else:
            count -= 1
        
        if count > max_count:
            max_count = count
            max_char = candidate
        
        idx += 1
        yield idx, candidate, count, max_char

    # Output the character with the maximum count
    yield idx, candidate, count, max_char

def animate(string):
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(string))
    ax.set_ylim(-len(string)//2, len(string)//2 + 1)
    ax.set_xticks(range(len(string)))
    ax.set_xticklabels(list(string))
    ax.set_xlabel("Characters")
    ax.set_ylabel("Count")
    ax.set_title("Boyer-Moore Majority Vote Algorithm")
    line, = ax.plot([], [], 'bo-')
    text = ax.text(0.05, 0.95, '', transform=ax.transAxes)
    text2 = ax.text(0.05, 0.90, '', transform=ax.transAxes)

    def update(data):
        idx, candidate, count, max_char = data
        line.set_data(range(idx), [0] * idx)
        text.set_text(f"Candidate: {candidate}")
        text2.set_text(f"Most repeated character: {max_char}")
        return line, text, text2

    ani = animation.FuncAnimation(fig, update, frames=find_most_repeated_char(string), interval=500)
    plt.show()

# Example usage
string = "abbbacaaabacab"
animate(string)
