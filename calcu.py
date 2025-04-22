import tkinter as tk
from tkinter import messagebox


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.configure(bg="#2b2b2b")
        self.root.geometry("375x550")
        self.root.resizable(False, False)

        # Ajustamos el Entry con un tamaño y espaciado adecuados
        self.entrada = tk.Entry(
            root,
            width=17,
            font=("Helvetica", 26),
            borderwidth=0,
            relief="solid",
            bg="#2b2b2b",
            fg="white",
            justify="right",
        )
        self.entrada.grid(
            row=0, column=0, columnspan=1, ipadx=0, ipady=1, padx=(1, 2), pady=(1, 10)
        )

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ("C", 2),
            ("<-", 1),
            ("/", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("*", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("-", 1),
            ("1", 1),
            ("2", 1),
            ("3", 1),
            ("+", 1),
            ("0", 2),
            (".", 1),
            ("=", 1),
        ]
        # Colores específicos para diferentes tipos de botones
        
        colores_botones = {
            "numero": "#4d4d4d",
            "operador": "#fe9505",
            "igual": "#fe9505",
            "fondo": "#2b2b2b",
            "texto": "#ffffff",
            "reset": "#d32f2f",
            "borrar": "#fe9505",
        }

        # Marco para contener los botones
        frame_botones = tk.Frame(self.root, bg="#2b2b2b")
        frame_botones.grid(row=1, column=0, columnspan=4, pady=(0, 10))

        fila = 0
        columna = 0
        
        
        # Crear cada botón dinámicamente
        for boton, span in botones:
            color_fondo = (
                colores_botones["operador"]
                if boton in ["/", "*", "-", "+", "=", "<-"]
                else colores_botones["numero"]
            )
            if boton == "C":
                color_fondo = colores_botones["reset"]
            elif boton == "<-":
                color_fondo = colores_botones["borrar"]
            elif boton == "=":
                color_fondo = colores_botones["igual"]

            tk.Button(
                frame_botones,
                text=boton,
                width=5 * span,
                height=2,
                font=("Arial", 20),
                bg=color_fondo,
                fg=colores_botones["texto"],
                borderwidth=0,
                command=lambda b=boton: self.click_boton(b),
            ).grid(
                row=fila, column=columna, columnspan=span, padx=1, pady=1, sticky="nsew"
            )

            columna += span
            if columna >= 4:
                fila += 1
                columna = 0

    def validar_entrada(self, expresion):
        """Valida que la expresión no tenga operadores consecutivos."""
        operadores = set("+-*/")
        for i in range(1, len(expresion)):
            if expresion[i] in operadores and expresion[i - 1] in operadores:
                return False
        return True

    def click_boton(self, valor):
        if valor == "=":
            expresion = self.entrada.get()
            if self.validar_entrada(expresion):
                try:
                    resultado = str(eval(expresion))
                    self.entrada.delete(0, tk.END)
                    self.entrada.insert(tk.END, resultado)
                except Exception:
                    messagebox.showerror("ERROR", "Entrada no válida")
                    self.entrada.delete(0, tk.END)
            else:
                messagebox.showerror("ERROR", "Operadores consecutivos no permitidos")
        elif valor == "C":
            self.entrada.delete(0, tk.END)
        elif valor == "<-":
            if len(self.entrada.get()) > 0:
                self.entrada.delete(len(self.entrada.get()) - 1, tk.END)
        else:
            self.entrada.insert(tk.END, valor)


if __name__== "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()