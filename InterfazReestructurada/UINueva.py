import os, sys, uuid
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)
sys.path.append(os.path.join(parent_dir, "Clases_Base"))
sys.path.append(os.path.join(parent_dir, "Estructuras"))

from Clases_Base.articulo import Articulo
from Clases_Base.Cliente import Cliente
from Estructuras.GestionClientes import GestionClientes
from Estructuras.GestionTarjetas import GestionTarjetas
from Estructuras.Carrodecompra import CarroDeCompra
from Estructuras.inventario import ListaInventario
from Procesar_Pago import ProcesarPago

# Las Clases nuevas xd
from InterfazReestructurada.forms import CreadorFormulario as FormBuilder
from InterfazReestructurada.componentes import crear_stat_card, crear_tarjeta_producto, render_tabla


class SistemaCompraModerno:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("🛒 Sistema de Compra Profesional")
        self.center_window(1200, 800)

        # Models
        self.inventario = ListaInventario()
        self.gestion_clientes = GestionClientes("clientes.csv")
        self.gestion_tarjetas = GestionTarjetas("tarjetas.csv", self.gestion_clientes)
        self.carrito = None
        self.usuario_actual = None

        self.content_frame = ctk.CTkFrame(self.root)
        self.content_frame.pack(fill="both", expand=True)


        self.sidebar = ctk.CTkFrame(self.content_frame, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.main_area = ctk.CTkFrame(self.content_frame)
        self.main_area.pack(side="right", fill="both", expand=True)

        self.create_main_interface()

    # ----------------- UTILS -----------------
    def center_window(self, w, h):
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def clear_content(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    # ----------------- DASHBOARD -----------------
    def show_welcome(self):
        self.clear_content()
        frame = ctk.CTkFrame(self.main_area)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(frame, text="¡Bienvenido al Sistema de Compra!",
                     font=ctk.CTkFont(size=32, weight="bold")).pack(pady=30)

        stats = ctk.CTkFrame(frame)
        stats.pack(pady=20, fill="x")
        stats.grid_columnconfigure((0, 1, 2), weight=1)
        crear_stat_card(stats, "👥", "Clientes", len(self.gestion_clientes.clientes), 0, 0)
        crear_stat_card(stats, "📦", "Productos",
                        len(self.inventario.pasar_a_lista_nodos(self.inventario)), 0, 1)
        crear_stat_card(stats, "💰", "Ventas Hoy", "$0", 0, 2)

    # ----------------- INVENTARIO -----------------
    def edit_product(self, articulo):
        form = FormBuilder(self.root, f"✏️ Editar {articulo.nombre}", size=(500, 600))
        form.add_title(f"Editar Producto: {articulo.nombre}")

        self.edit_nombre_var = ctk.StringVar(value=articulo.nombre)
        self.edit_tipo_var = ctk.StringVar(value=articulo.tipo)
        self.edit_precio_var = ctk.StringVar(value=str(articulo.precio))
        self.edit_cantidad_var = ctk.StringVar(value=str(len(articulo.pila.items)))

        form.add_entry("Nombre:", self.edit_nombre_var)
        form.add_entry("Categoría:", self.edit_tipo_var)
        form.add_entry("Precio (USD):", self.edit_precio_var)
        form.add_entry("Cantidad:", self.edit_cantidad_var)

        def save():
            try:
                articulo.nombre = self.edit_nombre_var.get().strip()
                articulo.tipo = self.edit_tipo_var.get().strip()
                articulo.precio = float(self.edit_precio_var.get())
 
                nueva_cant = int(self.edit_cantidad_var.get())
                diff = nueva_cant - len(articulo.pila.items)
                if diff > 0:
                    for _ in range(diff):
                        articulo.pila.push(articulo)
                elif diff < 0:
                    for _ in range(-diff):
                        articulo.pila.pop()
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
                self.show_inventory()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        form.add_buttons(save, form.window.destroy)

    # ----------------- CLIENTES -----------------
    def show_inventory(self):
        self.clear_content()
        ctk.CTkLabel(self.main_area, text="📦 Inventario",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        # TODO: Falta la logica

        # Search bar
        search_frame = ctk.CTkFrame(self.main_area)
        search_frame.pack(fill="x", padx=20, pady=5)
        self.search_var = ctk.StringVar()
        ctk.CTkEntry(search_frame, textvariable=self.search_var,
                     placeholder_text="Buscar cliente...").pack(side="left", fill="x", expand=True, padx=5)
        ctk.CTkButton(search_frame, text="🔍", width=40,
                      command=self.filter_clients).pack(side="left")

        # Listas de clientes
        self.client_list_frame = ctk.CTkScrollableFrame(self.main_area, label_text="Lista de Clientes")
        self.client_list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.update_client_list()

        ctk.CTkButton(self.content_frame, text="➕ Nuevo Cliente",
                      command=self.new_client).pack(pady=10)

    def filter_clients(self):
        term = self.search_var.get().lower()
        filtered = [c for c in self.gestion_clientes.clientes
                    if term in c.nombre.lower() or term in c.apellido.lower()]
        self.update_client_list(filtered)

    def update_client_list(self, clientes=None):
        for w in self.client_list_frame.winfo_children():
            w.destroy()

        headers = ["ID", "Nombre", "Apellido", "Correo", "Acciones"]
        rows = []
        clientes = clientes or self.gestion_clientes.clientes
        for c in clientes:
            rows.append((c.id_cliente, c.nombre, c.apellido, c.correo, "👁️ Ver"))
        render_tabla(self.client_list_frame, headers, rows)

        
        for i, cliente in enumerate(clientes):
            btn = ctk.CTkButton(self.client_list_frame.winfo_children()[i+1], 
                                text="👁️ Ver", width=60,
                                command=lambda c=cliente: self.view_client(c))
            btn.grid(row=0, column=4, padx=10)

    def view_client(self, cliente):
        form = FormBuilder(self.root, f"👁️ Cliente {cliente.nombre}", size=(500, 500))
        form.add_title("Detalles del Cliente")

        details = [
            ("ID:", cliente.id_cliente),
            ("Nombre:", cliente.nombre),
            ("Apellido:", cliente.apellido),
            ("Teléfono:", cliente.telefono),
            ("Correo:", cliente.correo),
            ("Dirección:", cliente.direccion_envio),
            ("Fecha Registro:", cliente.fecha_registro),
        ]
        for label, val in details:
            ctk.CTkLabel(form.main_frame, text=f"{label} {val}",
                         font=ctk.CTkFont(size=14)).pack(anchor="w", pady=3)

    # ----------------- COMPRAS -----------------
    def show_purchase(self):
        self.clear_content()
        ctk.CTkLabel(self.main_area, text="🛍️ Nueva Compra",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

        # cliente
        ctk.CTkButton(self.main_area, text="👥 Seleccionar Cliente",
                      command=self.select_client).pack(pady=10)

        # producto
        ctk.CTkButton(self.main_area, text="📦 Agregar Producto",
                      command=self.select_product).pack(pady=10)

        # carrito
        ctk.CTkButton(self.main_area, text="🛒 Ver Carrito",
                      command=self.show_cart).pack(pady=10)

    def select_client(self):
        form = FormBuilder(self.root, "👥 Seleccionar Cliente", size=(500, 600))
        form.add_title("Seleccionar Cliente")

        for cliente in self.gestion_clientes.clientes:
            btn = ctk.CTkButton(form.main_frame,
                                text=f"{cliente.nombre} {cliente.apellido}",
                                command=lambda c=cliente: self.set_client(c, form.window))
            btn.pack(fill="x", pady=5)

    def set_client(self, cliente, window):
        self.usuario_actual = cliente
        self.carrito = CarroDeCompra(cliente)
        messagebox.showinfo("Cliente seleccionado", f"{cliente.nombre} {cliente.apellido}")
        window.destroy()

    def select_product(self):
        if not self.carrito:
            messagebox.showerror("Error", "Seleccione un cliente primero")
            return
        form = FormBuilder(self.root, "📦 Seleccionar Producto", size=(600, 600))
        form.add_title("Seleccionar Producto")

        for nodo in self.inventario.pasar_a_lista_nodos(self.inventario):
            articulo = nodo.dato
            btn = ctk.CTkButton(form.main_frame,
                                text=f"{articulo.nombre} (${articulo.precio:.2f})",
                                command=lambda a=articulo: self.add_to_cart(a, form.window))
            btn.pack(fill="x", pady=5)

    def add_to_cart(self, articulo, window):
        self.carrito.agregar_producto(articulo)
        messagebox.showinfo("Carrito", f"{articulo.nombre} agregado al carrito")
        window.destroy()

    def show_cart(self):
        if not self.carrito or not self.carrito.productos:
            messagebox.showinfo("Carrito", "Carrito vacío")
            return

        form = FormBuilder(self.root, "🛒 Carrito", size=(500, 600))
        form.add_title("Productos en el carrito")

        for articulo in self.carrito.productos:
            ctk.CTkLabel(form.main_frame,
                         text=f"{articulo.nombre} - ${articulo.precio:.2f}").pack(anchor="w")

        total = sum(a.precio for a in self.carrito.productos)
        ctk.CTkLabel(form.main_frame, text=f"Total: ${total:.2f}",
                     font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)

        def pagar():
            ProcesarPago(self.carrito).ejecutar_pago()
            messagebox.showinfo("Pago", "Compra realizada con éxito")
            self.carrito = CarroDeCompra(self.usuario_actual)
            form.window.destroy()

        form.add_buttons(pagar, form.window.destroy)

    # ----------------- SIDEBAR -----------------
    def create_main_interface(self):
        ctk.CTkLabel(self.sidebar, text="Sistema Compra",
             font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(10, 20))

        
        for txt, cmd in [
            ("🏠 Inicio", self.show_welcome),
            ("👥 Gestión Clientes", self.show_inventory),
            ("📦 Inventario", self.show_inventory),
            ("🛒 Nueva Compra", self.show_purchase),
        ]:
            ctk.CTkButton(self.sidebar, text=txt, command=cmd, height=40).pack(fill="x", pady=5, padx=10)

       
        for txt in ["💳 Gestión Tarjetas", "📊 Reportes", "⚙️ Configuración"]:
            ctk.CTkButton(self.sidebar, text=txt, height=40).pack(fill="x", pady=5, padx=10)

       
        ctk.CTkButton(self.sidebar, text="🚪 Salir", height=40, fg_color="gray").pack(side="bottom", fill="x", pady=10, padx=10)

    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = SistemaCompraModerno()
    app.run()
