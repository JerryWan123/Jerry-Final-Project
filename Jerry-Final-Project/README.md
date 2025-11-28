<h1 align="center" style="font-size:42px; font-weight:bold;">🔍 Binary Search Visualizer</h1> <h3 align="center">Jerry Wan - CISC-121 - Final Project

20526613</h3>

<h2 style="font-size:30px;">🖼 Demo Screenshot</h2>

Correct Example:

![alt text](<Screenshot 2025-11-27 195956.png>)

Error Example:

![alt text](<Screenshot 2025-11-27 201527.png>)

<h2 style="font-size:32px;">📌 1. Understanding the Requirements</h2>

This project implements an interactive Python application.

Its functionalities include:

1. Taking a list of integers and a target integer, and sorting the list.

2. Performing a binary search algorithm.

3. Displaying each search step using an interactive user interface.

4. Highlighting intermediate values ​​at each iteration.

5. Clearly displaying the search results ("Found" or "Not Found").

<h3 style="font-size:26px;">🔹 Problem</h3>

This app presents the algorithm in a visual way, showing how to efficiently find a target integer in a list of numbers using binary search.

<h3 style="font-size:26px;">🔹 Inputs</h3>

1. A comma-separated list of integers

2. A single target integer

Example:

1,5,10,123,8,21,2

Target: 2

(Same to the demo)

<h3 style="font-size:26px;">🔹 Outputs</h3>

1. Sorted list

2. Recorded search steps (left, mid, right pointers)

3. Mid value at each step (use brackets and bold text to present.)

4. Final result statement

<h3 style="font-size:26px;">🔹 Constraints</h3>

Only integers are allowed and input cannot be empty

List auto removes spaces

Binary Search requires sorting

No floats or special characters

<h2 style="font-size:32px;">🧪 2. Draft Code</h2>

Before building the final application and UI, I created a basic draft code to validate the algorithm:

# Simple draft code before UI

    def binary_search_basic(arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


This code is an important part of the program's basic algorithm; it demonstrates that the pointers behave correctly and the algorithm flow follows expectations.

<h2 style="font-size:32px;">🧠 3. Computational Thinking</h2>
<h3 style="font-size:26px;">1️⃣ Decomposition</h3>

The problem is broken down into the following parts:

Input list/target value

Sorting

Binary search logic

Step recording

Markdown output formatting

Gradio UI design

Deployment settings

<h3 style="font-size:26px;">2️⃣ Pattern Recognition</h3>

Binary Search displays strong patterns:

Midpoint recalculation

Halving the search space (leading to O(log n) time complexity)

Pointer updates

Predictable repetition

These patterns shaped the visualization.

<h3 style="font-size:26px;">3️⃣ Abstraction</h3>

The UI hides unnecessary complexity:

Only relevant values shown: left, mid, right, mid_value and highlighting mid with **(value)**

Internal list states simplified

Clear error handling messages

Minimalist interface

<h3 style="font-size:26px;">4️⃣ Algorithm Design</h3>

Binary search works by repeatedly selecting the middle element of a sorted list and comparing it with the target value. Depending on whether the target value is less than or greater than the middle element, the algorithm adjusts the left or right pointer, discarding half of the remaining search space. This process continues until the target value is found or the search range is exhausted.

<h2 style="font-size:32px;">🎨 4. UI Design (Gradio)</h2>

1. Two textboxes

For list input and target input.

2. Markdown output

For proper use of headings, bold text, and formatted output

3. Step number support

Every iteration labeled as “Step 1”, “Step 2”, etc.

4. Mid highlight

Displayed as **(value)** inside the list.

5. Theme

The interface uses original Gradio theme.

<h2 style="font-size:32px;">📁 5. Project Structure</h2>

Folder: Jerry-Final-Project
1. app.py # Main Python application
2. requirements.txt # Dependencies (Gradio)
3. README.md # Documentation
4. screenshots # UI screenshots


<h2 style="font-size:32px;">🛠 6. How to Run Locally</h2>
 
Requirements:

Python 3.13 and above

Install Gradio in terminal: pip install gradio

Run the app in terminal: python app.py

The terminal will provide a URL based on your computer device; clicking it will automatically open the program in your browser window.

<h2 style="font-size:32px;">🚀 7. Deployment — HuggingFace Spaces</h2>

[(Hugging Face link)](https://huggingface.co/spaces/JerryWan0618/Jerry-BinarySearch-Visualizer)

<h2 style="font-size:32px;">🌐 8. GitHub Repository</h2>

[(GitHub link)](https://github.com/JerryWan123/Jerry-Final-Project/tree/main/Jerry-Final-Project)

<h2 style="font-size:32px;">🏁 9. Author/Acknowledgements</h2>

Name: Jerry Wan

Student ID: 20526613 

Section: CISC-121 F25 001

This project uses:

    Python 3.13.7 with Visual Studio Code
    
    Gradio for UI design

    ChatGPT for basic program structure building and logical organization

    Hugging Face for the deployed version app