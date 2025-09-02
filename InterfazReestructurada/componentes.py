import customtkinter as ctk

def crear_stat_card(parent, icono, titulo, valor, row, col):
    """Small stat box for dashboard"""
    card = ctk.CTkFrame(parent)
    card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

    ctk.CTkLabel(card, text=icono, font=ctk.CTkFont(size=30)).pack(pady=(15, 5))
    ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=24, weight="bold")).pack(pady=5)
    ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=12)).pack(pady=(0, 15))
    return card


def crear_tarjeta_producto(parent, nodo, on_edit, on_delete):
    """Display one product in inventory list"""
    articulo = nodo.dato
    cantidad_disponible = len(nodo.pila.items)

    card_frame = ctk.CTkFrame(parent)
    card_frame.pack(fill="x", padx=10, pady=5)

    card_frame.grid_columnconfigure(1, weight=1)

    # Icon by category
    iconos = {"Electrónica": "💻", "Muebles": "🪑", "Educación": "📚", "Fotografía": "📷"}
    icon = iconos.get(articulo.tipo, "📦")
    ctk.CTkLabel(card_frame, text=icon, font=ctk.CTkFont(size=30)).grid(
        row=0, column=0, rowspan=2, padx=15, pady=15
    )

    info = ctk.CTkFrame(card_frame)
    info.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    info.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(info, text=articulo.nombre,
                 font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, columnspan=2, sticky="w")

    ctk.CTkLabel(info, text=f"Categoría: {articulo.tipo}", font=ctk.CTkFont(size=12)).grid(row=1, column=0, sticky="w")
    ctk.CTkLabel(info, text=f"Precio: ${articulo.precio:.2f}",
                 font=ctk.CTkFont(size=14, weight="bold"),
                 text_color=("green", "lightgreen")).grid(row=1, column=1, sticky="e")

    stock_color = ("red", "lightcoral") if cantidad_disponible < 5 else ("blue", "lightblue")
    ctk.CTkLabel(info, text=f"Stock: {cantidad_disponible} unidades",
                 font=ctk.CTkFont(size=12), text_color=stock_color).grid(row=2, column=0, sticky="w")

    btns = ctk.CTkFrame(card_frame)
    btns.grid(row=0, column=2, padx=10, pady=10)
    ctk.CTkButton(btns, text="✏️", width=30, command=lambda: on_edit(articulo)).pack(pady=2)
    ctk.CTkButton(btns, text="🗑️", width=30, fg_color=("red", "darkred"),
                  hover_color=("darkred", "red"),
                  command=lambda: on_delete(articulo.nombre)).pack(pady=2)

    return card_frame


def render_tabla(parent, headers, filas):
    """Esto hace tablas genericas (headers + lista de filas)"""
    header_frame = ctk.CTkFrame(parent)
    header_frame.pack(fill="x", padx=10, pady=(5, 10))
    for i, header in enumerate(headers):
        ctk.CTkLabel(header_frame, text=header,
                     font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=i, padx=10, sticky="w")

    for fila in filas:
        fila_frame = ctk.CTkFrame(parent)
        fila_frame.pack(fill="x", padx=10, pady=2)
        for i, cell in enumerate(fila):
            ctk.CTkLabel(fila_frame, text=str(cell), font=ctk.CTkFont(size=11)).grid(
                row=0, column=i, padx=10, sticky="w"
            )
