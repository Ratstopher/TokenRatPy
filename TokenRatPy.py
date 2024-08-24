from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os


def count_tokens(text):
    # Basic tokenization by splitting on whitespace
    tokens = text.split()
    return len(tokens)


def open_files(result_display):
    # Open file dialog to select multiple files
    filepaths = filedialog.askopenfilenames(
        title="Open Files",
        filetypes=(
            ("All files", "*.txt *.py *.js *.json"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("JavaScript files", "*.js"),
            ("JSON files", "*.json"),
        ),
    )

    if not filepaths:
        return

    total_tokens = 0
    file_details = []

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            tokens = count_tokens(content)
            total_tokens += tokens
            file_details.append(f"{os.path.basename(filepath)}: {tokens} tokens")

    # Display results in the Text widget
    result_message = "\n".join(file_details) + f"\n\nTotal Tokens: {total_tokens}"
    result_display.delete(1.0, END)  # Clear previous results
    result_display.insert(END, result_message)


def save_results(result_display):
    # Save the results to a file
    result_text = result_display.get(1.0, END).strip()
    if not result_text:
        messagebox.showwarning("Save Results", "No results to save.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )

    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(result_text)
        messagebox.showinfo("Save Results", f"Results saved to {save_path}")


def create_gui():
    root = Tk()
    root.title("Token Counter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # Create a Text widget to display results
    result_display = Text(mainframe, width=60, height=20, wrap="word")
    result_display.grid(column=1, row=2, columnspan=3, sticky=(W, E))

    open_button = ttk.Button(
        mainframe, text="Open Files", command=lambda: open_files(result_display)
    )
    open_button.grid(column=1, row=1, sticky=W)

    save_button = ttk.Button(
        mainframe, text="Save Results", command=lambda: save_results(result_display)
    )
    save_button.grid(column=2, row=1, sticky=E)

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()
