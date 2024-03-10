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
        yield idx, char, count, max_char

    # Output the character with the maximum count
    yield idx, char, count, max_char

def animate(string):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, len(string))
    ax.set_ylim(-len(string)//2, len(string)//2 + 1)
    ax.set_xticks(range(len(string)))
    ax.set_xticklabels(list(string), fontsize=14)
    ax.set_xlabel("Characters", fontsize=16)
    ax.set_ylabel("Count", fontsize=16)
    ax.set_title("Finding the Most Frequent Character", fontsize=20, fontweight='bold', color='darkblue')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    line, = ax.plot([], [], 'bo-', linewidth=3, markersize=12)
    
    text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=16, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    text2 = ax.text(0.05, 0.85, '', transform=ax.transAxes, fontsize=16, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.8))
    
    # Add a title above the plot
    title = ax.text(0.5, 1.05, "Character Frequency Visualization", transform=ax.transAxes, 
                    fontsize=24, fontweight='bold', color='darkgreen', horizontalalignment='center')

    def update(data):
        idx, current_char, count, max_char = data
        line.set_data(range(idx), [0] * idx)
        text.set_text(f"Current Character: {current_char}\nFrequency: {count}")
        text2.set_text(f"Most Frequent Character: {max_char}")
        return line, text, text2, title

    ani = animation.FuncAnimation(fig, update, frames=find_most_repeated_char(string), interval=800)
    
    # Add a colorful background gradient
    ax.set_facecolor('lightblue')
    fig.patch.set_facecolor('white')
    
    # Add a legend with colorful markers
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Characters',
                                  markerfacecolor='blue', markersize=12)]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=14)
    
    plt.tight_layout()
    plt.show()

# Example usage
string = "abbbacaabacab"
animate(string)
