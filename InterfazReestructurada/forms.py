import customtkinter as ctk

class CreadorFormulario:
    def __init__(self, parent, title, size=(500, 600)):
        """Con esto se pueden crear ventanas, asi no hace falta tener que repetir tanto codigo"""
        self.window = ctk.CTkToplevel(parent)
        self.window.title(title)
        w, h = size
        x = (self.window.winfo_screenwidth() // 2) - (w // 2)
        y = (self.window.winfo_screenheight() // 2) - (h // 2)
        self.window.geometry(f"{w}x{h}+{x}+{y}")
        self.window.transient(parent)
        self.window.grab_set()

        self.main_frame = ctk.CTkFrame(self.window)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        pass

    def add_titulo(self, text, size=20):
        lbl = ctk.CTkLabel(
            self.main_frame,
            text=text,
            font=ctk.CTkFont(size=size, weight="bold")
        )
        lbl.pack(pady=(10, 20))
        return lbl

    def add_entry(self, label_text, var, placeholder="", hidden=False):
        ctk.CTkLabel(
            self.main_frame,
            text=label_text,
            font=ctk.CTkFont(size=14)
        ).pack(anchor="w", padx=20, pady=(10, 5))

        entry = ctk.CTkEntry(
            self.main_frame,
            textvariable=var,
            height=35,
            font=ctk.CTkFont(size=12),
            placeholder_text=placeholder,
            show="*" if hidden else None
        )
        entry.pack(fill="x", padx=20, pady=(0, 10))
        return entry

    def add_botones(self, on_save, on_cancel=None,
                    save_text="💾 Guardar", cancel_text="❌ Cancelar"):
        frame = ctk.CTkFrame(self.main_frame)
        frame.pack(fill="x", padx=20, pady=20)

        if on_cancel:
            ctk.CTkButton(
                frame,
                text=cancel_text,
                command=on_cancel,
                fg_color=("gray70", "gray30"),
                hover_color=("gray60", "gray40"),
                height=40
            ).pack(side="right", padx=10, pady=10)

        ctk.CTkButton(
            frame,
            text=save_text,
            command=on_save,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40
        ).pack(side="right", padx=10, pady=10)
