"""
Example of tkinter app where a button on the MainApp allows the user to open a second
window where they can control a number of independent sliders.

Slider values are returned to the MainApp.
"""

import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # hold the outputs from the sliders
        self.slider_values = []
        self.slider_frames = []
        self.max_sliders = 6

        self.slider_window = self.slider_window = SliderWindow(self)
        self.slider_window.add_slider_frame()

        self.slider_button = tk.Button(self,
                                       text="Open Sliders",
                                       command=self.open_slider_window)
        self.slider_button.pack(padx=20, pady=20)

    def open_slider_window(self):
        self.slider_window.deiconify()


class SliderWindow(tk.Toplevel):
    def __init__(self, main_app):
        super().__init__(master=main_app)

        self.app = main_app
        self.title('Slider Window')

        self.new_slider_button = tk.Button(self,
                                           text="Add Slider",
                                           command=self.add_slider_frame)

        self.remove_slider_button = tk.Button(self,
                                              text="Remove Slider",
                                              command=self.delete_slider_frame)

        self.exit_button = tk.Button(self, text="Exit", command=self.withdraw)

        self.exit_button.pack(padx=20, pady=(5, 15), side=tk.BOTTOM)
        self.new_slider_button.pack(padx=20, pady=(5, 5), side=tk.BOTTOM)
        self.remove_slider_button.pack(padx=20, pady=(5, 5), side=tk.BOTTOM)

        # handle the windows close button
        self.protocol('WM_DELETE_WINDOW', self.withdraw)

        # Window is initialised in withdrawn state (can't be seen) use the deiconify method to show it
        self.withdraw()

    def add_slider_frame(self):
        if len(self.app.slider_frames) < self.app.max_sliders:
            new_slider_frame = SliderFrame(self, self.app)

            self.app.slider_frames.append(new_slider_frame)
            self.app.slider_values.append({'freq': None, 'amp': None})

            new_slider_frame.pack(side=tk.TOP, padx=20, pady=5)

    def delete_slider_frame(self):
        if len(self.app.slider_frames) > 1:
            slider_to_remove = self.app.slider_frames.pop()
            self.app.slider_values.pop()
            slider_to_remove.pack_forget()
            slider_to_remove.destroy()


class SliderFrame(tk.Frame):
    def __init__(self, root, main_app):
        super().__init__(master=root)
        self.app = main_app

        self.freq_value = tk.IntVar()
        self.amp_value = tk.IntVar()

        self.freq_slide = tk.Scale(
            self,
            from_=0,
            to=20000,
            orient='horizontal',
            command=self.slider_change,
            variable=self.freq_value,
        )

        self.amp_slide = tk.Scale(
            self,
            from_=-10,
            to=10,
            orient='horizontal',
            command=self.slider_change,
            variable=self.amp_value,
        )

        self.freq_slide.pack(side=tk.LEFT, padx=5)
        self.amp_slide.pack(side=tk.LEFT, padx=5)

    def slider_change(self, event):
        slider_index = self.app.slider_frames.index(self)
        app.slider_values[slider_index]['freq'] = self.freq_value.get()
        app.slider_values[slider_index]['amp'] = self.amp_value.get()
        print(app.slider_values)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
