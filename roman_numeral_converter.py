# A simple GUI application using the Tkinter library to convert Roman numerals to their corresponding numeric values
# Created by Curtis Kin Kokuloku, student at the University of Minnesota; majoring in Computer Science

import tkinter as tk
from tkinter import messagebox


def romanToInt(s):
    # Method that converts the string 's' to an integer value

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }  # dictionary to store the values of each Roman numeral
    result = 0
    prev_value = 0

    # Traverse the Roman numeral from right to left
    n = len(s)
    for i in range(n - 1, -1, -1):
        current_char = s[i]
        current_value = roman_dict[current_char]

        # Check if the previous character has a smaller value, then subtract its value
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value

    return result


class RomanConverterApp:
    def __init__(self):
        # Constructor; executed when an object of this class is created.
        # It sets up the GUI window and widgets.
        self.window = tk.Tk()  # Creates the main GUI window
        self.window.title("Roman Numeral Converter")  # Sets the title of the GUI window

        self.label = tk.Label(
            self.window, text="Enter Roman Numeral:"
        )  # Creates a label widget with the given text
        self.label.pack()  # Packs the label widget, ensuring it is displayed in the window

        self.entry = tk.Entry(
            self.window
        )  # Creates an entry widget (text box) that allows the user to input the Roman numeral
        self.entry.pack()  # Packs the entry widget to display it in the window
        self.entry.bind(
            "<Return>", self.on_enter
        )  # Bind the Enter key to the on_enter method

        # Creates a button widget with the label "Convert" and associates it with the convert method, which will be called when the button is clicked.
        self.convert_button = tk.Button(
            self.window, text="Convert", command=self.convert
        )
        self.convert_button.pack()  # Packs the button widget to display it in the window

    def convert(self):
        # Method that parses the text entered by the user and called the romanToInt method to convert the text into an integer value

        roman_numeral = (
            self.entry.get().upper()
        )  # Retrieves the input from the entry widget, converts it to uppercase

        if not roman_numeral:
            messagebox.showerror(
                "Error", "Please enter a Roman numeral."
            )  # Display error message for empty input
            return

        try:  # Handle exceptions
            numeric_value = romanToInt(roman_numeral)
            messagebox.showinfo(
                "Result", f"{roman_numeral} is equal to {numeric_value}"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_enter(self, event):
        # Method called when the Enter key is pressed
        self.convert()


if __name__ == "__main__":
    app = RomanConverterApp()
    app.window.mainloop()
