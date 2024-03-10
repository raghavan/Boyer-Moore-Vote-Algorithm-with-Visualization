# Boyer-Moore Majority Vote Algorithm

This project implements the **Boyer-Moore Majority Vote Algorithm** to find the most repeated character in a string. The algorithm is efficient, with a time complexity of O(n), where `n` is the length of the string.

## Algorithm Implementation

The implementation of the Boyer-Moore Majority Vote Algorithm is located in the `boyer_moore_majority_vote.py` file. The algorithm operates as follows:

1. Initialize a candidate character and a count variable to `None` and `0`, respectively.
2. Iterate through each character in the string:
   - If the count becomes `0`, update the candidate to the current character and set the count to `1`.
   - If the current character is the same as the candidate, increment the count by `1`.
   - If the current character is different from the candidate, decrement the count by `1`.
3. After the iteration, the candidate character will be the most repeated character in the string.

```
python3 boyer_moore_majority_vote.py
```
It will return the most repeated character in the string.

## Algorithm Visualization

The project also includes a visualization of the Boyer-Moore Majority Vote Algorithm using Python's Matplotlib library. The visualization is available in the `visualize_boyer_moore.py` file.

To run the visualization, execute the `visualize_boyer_moore.py` script. It will display an animation that shows the algorithm's execution step by step, including:

- A line plot that updates at each iteration, showing the current index and the count.
- Text annotations that display the current candidate character, its count, and the most repeated character found so far.

```
python3 visualize_boyer_moore.py
```
The visualization offers a visual understanding of how the algorithm operates and determines the most repeated character in the string.

## Usage

Clone the repository:

```bash
git clone https://github.com/your-username/boyer-moore-majority-vote.git
```

Ensure you have Python installed, along with the Matplotlib library 
**pip install matplotlib**
