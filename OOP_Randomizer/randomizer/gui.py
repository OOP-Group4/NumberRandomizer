import tkinter as tk

from .backend import Randomizer
from .history import HistoryManager

class NumberRandomizerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Number Randomizer")
        
        # Set window size to a percentage of screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set the desired size as 80% of screen width and height
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.root.geometry(f"{window_width}x{window_height}+{int(screen_width * 0.1)}+{int(screen_height * 0.1)}")
        
        self.root.configure(bg="mint cream")

        self.history_manager = HistoryManager()
        self.create_header()
        self.create_main_sections()

        self.current_category = "ByRange"

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="PaleGreen4", height=80)
        header_frame.pack(fill="x", side="top")

        title_label = tk.Label(
            header_frame,
            text="Number Randomizer",
            font=("Times", 36, "bold"),
            fg="gray100",
            bg="PaleGreen4"
        )
        title_label.place(relx=0.5, rely=0.5, anchor="center")

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)

    def create_main_sections(self):
        margin_left = 0.05
        margin_right = 0.05
        margin_bottom = 0.05

        self.section1_frame = tk.Frame(self.root, bg="gray100", relief="solid", bd=1)
        self.section1_frame.place(
            relx=margin_left,
            rely=0.2,
            relwidth=0.6 - margin_left - margin_right,
            relheight=0.8 - margin_bottom
        )

        self.section2_frame = tk.Frame(self.root, bg="gray100", relief="solid", bd=1)
        self.section2_frame.place(
            relx=0.6 + margin_left,
            rely=0.2,
            relwidth=0.4 - margin_left - margin_right,
            relheight=0.8 - margin_bottom
        )

        self.page1_frame = ByRangePage(self.section1_frame, self)
        self.page2_frame = ByListPage(self.section1_frame, self)

        self.create_navigation_buttons()
        self.create_output_section()
        self.create_history_section()

        self.show_page(self.page1_frame) 

    def create_navigation_buttons(self):
        button_frame = tk.Frame(self.section1_frame, bg="gray100")
        button_frame.pack(side="top", fill="x", pady=5)

        button1 = tk.Button(
            button_frame,
            text="By Range",
            command=lambda: self.show_page(self.page1_frame),
            font=("Helvetica", 12, "bold"),
            width=15,
            height=2,
            fg="brown3",
            bg="gray100"
        )
        button1.pack(side="left", fill="x", expand=True, padx=5)

        button2 = tk.Button(
            button_frame,
            text="By List",
            command=lambda: self.show_page(self.page2_frame),
            font=("Helvetica", 12, "bold"),
            width=15,
            height=2,
            fg="goldenrod3",
            bg="gray100"
        )
        button2.pack(side="left", fill="x", expand=True, padx=5)

    def create_output_section(self):
        self.output_frame = tk.Frame(self.section2_frame, bg="gray100")
        self.output_frame.place(relx=0.5, rely=0.1, anchor="center", width=500, height=100)

        self.output_label = tk.Label(
            self.output_frame,
            text="0",
            font=("Helvetica", 18, "bold"),
            bg="white",
            fg="black",
            relief="raised",
            width=20,
            height=2,
            bd=5,
        )
        self.output_label.place(relx=0.5, rely=0.5, anchor="center")

    def create_history_section(self):
        history_frame = tk.Frame(self.section2_frame, bg="gray100")
        history_frame.place(relx=0.5, rely=0.35, anchor="n", width=450, height=350)

        history_label = tk.Label(
            history_frame,
            text="HISTORY LOG",
            font=("Helvetica", 18, "bold"),
            fg="black",
            bg="gray100"
        )
        history_label.pack(pady=10)

        button_frame = tk.Frame(history_frame, bg="gray100")
        button_frame.pack(side="top", pady=5)

        clear_button = tk.Button(
            button_frame,
            text="Reset/ Clear History",
            font=("Helvetica", 14, "bold"),
            bg="palegreen4",
            fg="gray100",
            width=18,
            command=lambda: self.clear_history(self.current_category)
        )
        clear_button.pack(side="left", padx=5)

        copy_button = tk.Button(
            button_frame,
            text="📋Copy",
            font=("Helvetica", 14, "bold"),
            bg="palegreen4",
            fg="gray100",
            width=8,
            command=lambda: self.copy_history_to_clipboard(self.current_category)
        )
        copy_button.pack(side="left", padx=5)

        self.history_listbox = tk.Listbox(
            history_frame,
            font=("Helvetica", 14),
            bd=2, 
            highlightbackground="palegreen4", 
            highlightthickness=2,
            bg="white",
            fg="black",
            height=15,
            width=30,
            justify="left"
        )
        self.history_listbox.pack(side="top", fill="both", expand=True, padx=50, pady=10)
        history_frame.pack_propagate(False)


    def show_page(self, page):
        for p in [self.page1_frame, self.page2_frame]:
            p.hide()
        page.show()

        if page == self.page1_frame:
            self.current_category = "ByRange"
        elif page == self.page2_frame:
            self.current_category = "ByList"

        self.update_history_display(self.current_category)


    def update_output(self, result, category):
        self.output_label.config(text=str(result))
        self.history_manager.update_history(category, result)
        self.update_history_display(category)

    def copy_history_to_clipboard(self, category):
        history_text = "\n".join(map(str, self.history_manager.get_history(category)))
        self.root.clipboard_clear()
        self.root.clipboard_append(history_text)
        self.root.update()
    
    def clear_history(self, category):
        self.history_manager.clear_history(category)
        self.update_history_display(category)
    
    def update_history_display(self, category):
        self.history_listbox.delete(0, tk.END)
        for item in self.history_manager.get_history(category):
            self.history_listbox.insert(tk.END, item)

class Page:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.frame = tk.Frame(self.parent, bg="gray100")
        self.create_widgets()

    def create_widgets(self):
        pass

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()


class ByRangePage(Page):
    def create_widgets(self):
        entry_frame = tk.Frame(self.frame, bg="gray100")
        entry_frame.pack(side="top", pady=50)

        background_color = self.frame.cget("bg")
        tk.Label(entry_frame, text="Enter Range:", font=("Helvetica", 18, "bold"), bg=background_color).grid(row=0, column=0, pady=10, sticky="w")

        tk.Label(entry_frame, text="Min:", font=("Helvetica", 16), bg=background_color).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.min_entry = tk.Entry(entry_frame, font=("Helvetica", 16), bd=2, highlightbackground="brown3", highlightthickness=2)
        self.min_entry.grid(row=3, column=0, padx=10, pady=5)

        tk.Label(entry_frame, text="→", font=("Helvetica", 30, "bold"), bg=background_color).grid(row=3, column=1, padx=5)

        self.max_entry = tk.Entry(entry_frame, font=("Helvetica", 16), bd=2, highlightbackground="brown3", highlightthickness=2)
        self.max_entry.grid(row=3, column=3, padx=10, pady=5)
        tk.Label(entry_frame, text="Max:", font=("Helvetica", 16), bg=background_color).grid(row=2, column=3, padx=10, pady=5, sticky="w")

        generate_button = tk.Button(
            self.frame,
            text="Generate Number",
            font=("Helvetica", 18, "bold"),
            bg="brown3",
            fg="white",
            width=20,
            command=self.generate_number_ui
        )
        generate_button.place(relx=0.5, rely=0.9, anchor="center")

    def generate_number_ui(self):
        try:
            min_value = int(self.min_entry.get())
            max_value = int(self.max_entry.get())
            if min_value >= max_value:
                self.display_error("Invalid range! Min must be less than Max.")
            else:
                result = Randomizer.generate_random_number(min_value, max_value)
                self.app.update_output(result, "ByRange")
        except ValueError:
            self.display_error("Invalid input!")

    def display_error(self, message: str):
        self.app.update_output(message, "ByRange")

class ByListPage(Page):
    def create_widgets(self):
        entry_frame = tk.Frame(self.frame, bg="gray100")
        entry_frame.pack(side="top", pady=50)

        background_color = self.frame.cget("bg")
        tk.Label(entry_frame, text="Enter a list of numbers (comma-separated):", font=("Helvetica", 18, "bold"), bg=background_color).grid(row=0, column=0, pady=10, sticky="w")
        
        total_width = (3 * 10) + (2 * 5)
        self.list_entry = tk.Entry(entry_frame, font=("Helvetica", 16), width=total_width,  bd=2, highlightbackground="goldenrod3", highlightthickness=2)
        self.list_entry.grid(row=3, column=0, padx=10, pady=10)

        shuffle_button = tk.Button(
            self.frame,
            text="Shuffle List",
            font=("Helvetica", 18, "bold"),
            bg="goldenrod3",
            fg="white",
            width=20,
            command=self.shuffle_list_ui
        )
        shuffle_button.place(relx=0.5, rely=0.9, anchor="center")

    def shuffle_list_ui(self):
        try:
            input_list = [int(x.strip()) for x in self.list_entry.get().split(",")]
            shuffled_list = Randomizer.shuffle_list(input_list)
            self.app.update_output(shuffled_list, "ByList")
        except ValueError:
            self.app.update_output("Invalid list!", "ByList")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberRandomizerApp(root)
    root.mainloop()
