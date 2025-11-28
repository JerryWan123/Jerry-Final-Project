# Binary Search Visualizer
# Jerry Wan's Final Project
# Student ID: 20526613
import gradio as gr

# 1. Binary Search Logic

# Performs binary search on a sorted list.
# Records each step (left, mid, right, mid_value) for visualization.
def binary_search(arr, target):
    steps = []                               # List to store recorded steps
    left, right = 0, len(arr) - 1            # Initialize pointers

    while left <= right:                      # Continue while search window is valid
        mid = (left + right) // 2             # Middle index (integer division)

        # Record current search state for visualization
        steps.append({
            "left": left,
            "mid": mid,
            "right": right,
            "list_state": arr.copy(),         # Save list snapshot
            "mid_value": arr[mid],
        })

        if arr[mid] == target:                # Target found
            return steps, True
        elif arr[mid] < target:               # Search the right half
            left = mid + 1
        else:                                 # Search the left half
            right = mid - 1

    return steps, False                        # Target not found

# 2. Format Each Step for Markdown Display

# Formats one step into Markdown, using **(value)** to highlight the mid index.
def format_step(step, step_number):
    arr = step["list_state"]
    mid = step["mid"]

    visual_list = ""                           # Build visual representation of the list
    for i, val in enumerate(arr):
        if i == mid:
            visual_list += f"**({val})** "     # Highlight mid index
        else:
            visual_list += f"{val} "

    # Markdown representation of the step
    md = f"""
### 🔎 Step {step_number}
Left: `{step['left']}` | Mid: `{step['mid']}` | Right: `{step['right']}`
Mid value: `{step['mid_value']}`

### 📊 List Visualization
{visual_list}
"""
    return md

# 3. Main App Function

# Handles user input, input validation, sorting, running binary search,
# and formatting the Markdown output for display.
def run_app(list_input, target_input):

    # Check for empty input
    if not list_input.strip() or not target_input.strip():
        return "⚠️ Please enter BOTH a list and a target number."

    try:
        arr = list(map(int, list_input.split(",")))    # Convert "1,3,5" → [1, 3, 5]
        original = arr.copy()                          # Save original list
        arr.sort()                                     # Required for binary search
        target = int(target_input)
    except:
        return "❌ ERROR: Only numbers are allowed. Example: 1, 3, 5, 7"

    # Perform binary search
    steps, found = binary_search(arr, target)

    # Build Markdown output
    md_output = "## 🔢 Sorted Input List\n"
    md_output += f"Original: `{original}`\n\n"
    md_output += f"Sorted: `{arr}`\n\n"

    # Add search steps
    md_output += "## 🔍 Search Steps\n"
    for i, s in enumerate(steps):
        md_output += format_step(s, i + 1)            # Step numbering

    # Final result display
    if found:
        md_output += f"""
## 🎉 Result: Target <span style="font-size:22px; font-weight:bold;">{target}</span> FOUND!
"""
    else:
        md_output += f"""
## ❌ Result: Target <span style="font-size:22px; font-weight:bold;">{target}</span> NOT Found.
"""

    return md_output

# 4. Gradio Interface (UI)

# Defines the UI components, labels, and output type for the web app.
interface = gr.Interface(
    fn=run_app,                                        # Function to run
    inputs=[
        gr.Textbox(label="Enter numbers (e.g., 7,1,9,3)", placeholder="Numbers separated by commas"),
        gr.Textbox(label="Enter target number", placeholder="e.g., 7")
    ],
    outputs=gr.Markdown(),                             # Output as Markdown
    title="🔍 Binary Search Visualizer",
    description="Visualizes each step of Binary Search with clean styling, step numbering, and highlighted mid values.",
)

# 5. Launch the App

# Starts the Gradio application locally.
if __name__ == "__main__":
    interface.launch()
