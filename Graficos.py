import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
clases_base_path = os.path.join(current_dir, "Clases_Base")
sys.path.append(clases_base_path)
estructuras_path = os.path.join(current_dir, "Estructuras")
sys.path.append(estructuras_path)
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from Clases_Base.Cliente import Cliente
from Estructuras.GestionClientes import GestionClientes
from Estructuras.Carrodecompra import CarroDeCompra
from Estructuras.inventario import PilaArticulos, ListaInventario, Nodo
from Clases_Base.articulo import Articulo
from Procesar_Pago import ProcesarPago
from Estructuras.GestionTarjetas import GestionTarjetas
from Estructuras.GestionClientes import GestionClientes
class SistemaCompraModerno:
    def __init__(self):
        
        ctk.set_appearance_mode("light")  
        ctk.set_default_color_theme("blue")  
        self.root = ctk.CTk()
        self.root.title("🛒 Sistema de Compra Profesional")
        self.root.geometry("1200x800")
        self.centrar_ventana()
        self.usuario_actual = None
        self.carrito = None
        self.inventario = PilaArticulos() 
        self.gestion_clientes = GestionClientes("clientes.csv")
        self.gestion_tarjetas = GestionTarjetas("tarjetas.csv",self.gestion_clientes)
        
        self.crear_interfaz_principal()
        
    def centrar_ventana(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        ancho = 1200
        alto = 800
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def crear_interfaz_principal(self):
        """Crear la interfaz principal del sistema"""
        
        
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)
        
        self.crear_sidebar()
       
        self.crear_area_contenido()
        
        self.mostrar_bienvenida()
    
    def crear_sidebar(self):
        """Crear el menú lateral"""
        self.sidebar = ctk.CTkFrame(self.main_container, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="🛒 Sistema Compra", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))
        botones_menu = [
            ("🏠 Inicio", self.mostrar_bienvenida),
            ("👤 Gestión Clientes", self.mostrar_gestion_clientes),
            ("📦 Inventario", self.mostrar_inventario),
            ("🛍️ Nueva Compra", self.mostrar_nueva_compra),
            ("💳 Gestión Tarjetas", self.mostrar_gestion_tarjetas),
            ("📊 Reportes", self.mostrar_reportes),
            ("⚙️ Configuración", self.mostrar_configuracion)
        ]
        
        self.botones_menu = []
        for i, (texto, comando) in enumerate(botones_menu, 1):
            btn = ctk.CTkButton(
                self.sidebar,
                text=texto,
                command=comando,
                height=40,
                font=ctk.CTkFont(size=14),
                anchor="w"
            )
            btn.grid(row=i, column=0, padx=20, pady=5, sticky="ew")
            self.botones_menu.append(btn)
        
        self.btn_salir = ctk.CTkButton(
            self.sidebar,
            text="🚪 Salir",
            command=self.salir_aplicacion,
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color=("gray75", "gray25"),
            hover_color=("gray65", "gray35")
        )
        self.btn_salir.grid(row=10, column=0, padx=20, pady=(20, 20), sticky="ew")
    
    def crear_area_contenido(self):
        """Crear el área principal de contenido"""
        self.content_frame = ctk.CTkFrame(self.main_container)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
    
    def limpiar_contenido(self):
        """Limpiar el área de contenido"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_bienvenida(self):
        """Mostrar pantalla de bienvenida"""
        self.limpiar_contenido()
        welcome_frame = ctk.CTkFrame(self.content_frame)
        welcome_frame.pack(fill="both", expand=True, padx=20, pady=20)
        title_label = ctk.CTkLabel(
            welcome_frame,
            text="¡Bienvenido al Sistema de Compra!",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title_label.pack(pady=50)
        subtitle_label = ctk.CTkLabel(
            welcome_frame,
            text="Gestiona clientes, inventario y procesa pagos de manera eficiente",
            font=ctk.CTkFont(size=16)
        )
        subtitle_label.pack(pady=10)
        
       
        stats_frame = ctk.CTkFrame(welcome_frame)
        stats_frame.pack(pady=40, padx=40, fill="x")
        stats_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.crear_stat_card(stats_frame, "👥", "Clientes", "0", 0, 0)
        self.crear_stat_card(stats_frame, "📦", "Productos", "0", 0, 1)
        self.crear_stat_card(stats_frame, "💰", "Ventas Hoy", "$0", 0, 2)
        quick_access_frame = ctk.CTkFrame(welcome_frame)
        quick_access_frame.pack(pady=20, padx=40, fill="x")
        
        quick_label = ctk.CTkLabel(
            quick_access_frame,
            text="Accesos Rápidos",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        quick_label.pack(pady=10)
        quick_buttons_frame = ctk.CTkFrame(quick_access_frame)
        quick_buttons_frame.pack(pady=10, padx=20, fill="x")
        quick_buttons_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        btns_rapidos = [
            ("🛍️ Nueva Venta", self.mostrar_nueva_compra),
            ("👤 Nuevo Cliente", self.mostrar_gestion_clientes),
            ("📦 Ver Inventario", self.mostrar_inventario)
        ]
        
        for i, (texto, comando) in enumerate(btns_rapidos):
            btn = ctk.CTkButton(
                quick_buttons_frame,
                text=texto,
                command=comando,
                height=50,
                font=ctk.CTkFont(size=14, weight="bold")
            )
            btn.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
    
    def crear_stat_card(self, parent, icono, titulo, valor, row, col):
        """Crear una tarjeta de estadística"""
        card = ctk.CTkFrame(parent)
        card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
        
        icon_label = ctk.CTkLabel(card, text=icono, font=ctk.CTkFont(size=30))
        icon_label.pack(pady=(15, 5))
        
        value_label = ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=24, weight="bold"))
        value_label.pack(pady=5)
        
        title_label = ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=12))
        title_label.pack(pady=(0, 15))
    
    def mostrar_gestion_clientes(self):
        """Mostrar la interfaz de gestión de clientes"""
        self.limpiar_contenido()
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="👤 Gestión de Clientes",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        clientes_frame = ctk.CTkFrame(self.content_frame)
        clientes_frame.pack(fill="both", expand=True, padx=20, pady=10)
        buttons_frame = ctk.CTkFrame(clientes_frame)
        buttons_frame.pack(fill="x", padx=20, pady=10)
        btn_nuevo = ctk.CTkButton(
            buttons_frame,
            text="➕ Nuevo Cliente",
            command=self.nuevo_cliente,
            height=35
        )
        btn_nuevo.pack(side="left", padx=5)
        
        btn_buscar = ctk.CTkButton(
            buttons_frame,
            text="🔍 Buscar Cliente",
            command=self.buscar_cliente,
            height=35
        )
        btn_buscar.pack(side="left", padx=5)
        lista_frame = ctk.CTkScrollableFrame(clientes_frame, label_text="Lista de Clientes")
        lista_frame.pack(fill="both", expand=True, padx=20, pady=10)
        placeholder = ctk.CTkLabel(
            lista_frame,
            text="No hay clientes registrados. Haz clic en 'Nuevo Cliente' para comenzar.",
            font=ctk.CTkFont(size=14)
        )
        placeholder.pack(pady=50)
    
    def mostrar_inventario(self):
        """Mostrar la interfaz del inventario"""
        self.limpiar_contenido()
        
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="📦 Gestión de Inventario",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        inv_frame = ctk.CTkFrame(self.content_frame)
        inv_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        placeholder = ctk.CTkLabel(
            inv_frame,
            text="Módulo de inventario en construcción...",
            font=ctk.CTkFont(size=16)
        )
        placeholder.pack(pady=100)
    
    def mostrar_nueva_compra(self):
        """Mostrar la interfaz para nueva compra"""
        self.limpiar_contenido()
        
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="🛍️ Nueva Compra",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        compra_frame = ctk.CTkFrame(self.content_frame)
        compra_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        placeholder = ctk.CTkLabel(
            compra_frame,
            text="Módulo de compra en construcción...",
            font=ctk.CTkFont(size=16)
        )
        placeholder.pack(pady=100)
    
    def mostrar_gestion_tarjetas(self):
        """Mostrar gestión de tarjetas"""
        self.limpiar_contenido()
        
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="💳 Gestión de Tarjetas",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        
        tarjetas_frame = ctk.CTkFrame(self.content_frame)
        tarjetas_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        placeholder = ctk.CTkLabel(
            tarjetas_frame,
            text="Módulo de tarjetas en construcción...",
            font=ctk.CTkFont(size=16)
        )
        placeholder.pack(pady=100)
    
    def mostrar_reportes(self):
        """Mostrar reportes del sistema"""
        self.limpiar_contenido()
        
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="📊 Reportes del Sistema",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        
        reportes_frame = ctk.CTkFrame(self.content_frame)
        reportes_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        placeholder = ctk.CTkLabel(
            reportes_frame,
            text="Módulo de reportes en construcción...",
            font=ctk.CTkFont(size=16)
        )
        placeholder.pack(pady=100)
    
    def mostrar_configuracion(self):
        """Mostrar configuración del sistema"""
        self.limpiar_contenido()
        
        title_label = ctk.CTkLabel(
            self.content_frame,
            text="⚙️ Configuración del Sistema",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=20)
        
        config_frame = ctk.CTkFrame(self.content_frame)
        config_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        
        theme_label = ctk.CTkLabel(config_frame, text="Tema de la aplicación:", font=ctk.CTkFont(size=14))
        theme_label.pack(pady=10)
        
        theme_var = ctk.StringVar(value="light")
        theme_menu = ctk.CTkOptionMenu(
            config_frame,
            values=["light", "dark"],
            variable=theme_var,
            command=self.cambiar_tema
        )
        theme_menu.pack(pady=5)
    
    def cambiar_tema(self, nuevo_tema):
        """Cambiar el tema de la aplicación"""
        ctk.set_appearance_mode(nuevo_tema)
    
    def nuevo_cliente(self):
        """Abrir diálogo para nuevo cliente"""
        messagebox.showinfo("Nuevo Cliente", "Funcionalidad de nuevo cliente en desarrollo...")
    
    def buscar_cliente(self):
        """Abrir diálogo para buscar cliente"""
        messagebox.showinfo("Buscar Cliente", "Funcionalidad de búsqueda en desarrollo...")
    
    def salir_aplicacion(self):
        """Confirmar y salir de la aplicación"""
        if messagebox.askyesno("Confirmar Salida", "¿Estás seguro de que deseas salir?"):
            self.root.quit()
            self.root.destroy()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

def main():
    """Función principal"""
    try:
        app = SistemaCompraModerno()
        app.ejecutar()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error", f"Error al iniciar: {e}")

if __name__ == "__main__":
    main()