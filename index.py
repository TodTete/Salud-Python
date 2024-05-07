import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#Creado por Ricardo Vallejo Sánchez
def contiene_numero(s):
    return any(c.isdigit() for c in s)

def calcular_imc(peso, altura):
    def switch_estado_peso(imc):
        switch = {
            (18.5, 25): "Peso Normal",
            (25, 30): "Sobrepeso",
            (30, 35): "Obesidad (Clase 1)",
            (35, 40): "Obesidad (Clase 2)",
            (40, float('inf')): "Obesidad (Clase 3)",
        }
        for key, value in switch.items():
            if key[0] <= imc < key[1]:
                return value
        return "Bajo Peso"

    def calcular_imc_recursivo(peso, altura):
        if altura == 0:
            return "La altura no puede ser cero. Introduce un valor válido."

        imc = peso / (altura ** 2)
        estado_peso = switch_estado_peso(imc)

        return f"Tu IMC es: {imc:.2f}. Estado de Peso: {estado_peso}"

    return calcular_imc_recursivo(peso, altura)

def calcular_tmb(peso, altura, edad, genero):
    if genero == "Masculino":
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura * 100) - (5.677 * edad)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura * 100) - (4.330 * edad)

    return f"Tu TMB es: {tmb:.2f} kcal/día"

def verificar_oxigenacion(saturacion_oxigeno):
    if 95 <= saturacion_oxigeno <= 100:
        return "Saturación de oxígeno en sangre: Normal"
    elif 90 <= saturacion_oxigeno < 95:
        return "Saturación de oxígeno en sangre: Moderadamente baja. Consulta a un médico."
    elif saturacion_oxigeno < 90:
        return "Saturación de oxígeno en sangre: Baja. Busca atención médica de inmediato."
    else:
        return "Ingresa un valor válido para la saturación de oxígeno."

def verificar_presion_arterial(presion_sistolica, presion_diastolica):
    condiciones = [
        (lambda s, d: s < 90 or d < 60, "Presión arterial: Muy baja. Consulta a un médico."),
        (lambda s, d: 90 <= s <= 120 and 60 <= d <= 80, "Presión arterial: Normal"),
        (lambda s, d: 120 < s <= 130 and 80 < d <= 89, "Presión arterial: Elevada. Controla tu estilo de vida y hábitos alimenticios."),
        (lambda s, d: 130 < s <= 140 or 89 < d <= 90, "Presión arterial: Hipertensión (Etapa 1). Consulta a un médico."),
        (lambda s, d: 140 < s <= 180 or 90 < d <= 120, "Presión arterial: Hipertensión (Etapa 2). Busca atención médica de inmediato."),
        (lambda s, d: s > 180 or d > 120, "Presión arterial: Crisis hipertensiva. Llama a emergencias médicas."),
    ]

    for condicion, resultado in condiciones:
        if condicion(presion_sistolica, presion_diastolica):
            return resultado

    return "Ingresa valores válidos para la presión arterial."

def verificar_frecuencia_cardiaca(frecuencia_cardiaca):
    if 60 <= frecuencia_cardiaca <= 100:
        return f"Frecuencia cardíaca: Normal ({frecuencia_cardiaca} lpm)"
    elif frecuencia_cardiaca < 60:
        return f"Frecuencia cardíaca: Baja. Consulta a un médico ({frecuencia_cardiaca} lpm)"
    elif frecuencia_cardiaca > 100:
        return f"Frecuencia cardíaca: Alta. Consulta a un médico ({frecuencia_cardiaca} lpm)"

    return "Ingresa un valor válido para la frecuencia cardíaca."

def mostrar_ayuda_oxigeno(event):
    messagebox.showinfo("Saturación de Oxígeno en Sangre", "La saturación de oxígeno en sangre mide el porcentaje de oxígeno que se transporta por la sangre. Valores normales: 95-100%.")

def mostrar_ayuda_presion(event):
    messagebox.showinfo("Presión Arterial", "La presión arterial mide la fuerza del flujo de sangre contra las paredes de las arterias. Se expresa en dos números: sistólica/diastólica (mmHg).")

def mostrar_ayuda_frecuencia(event):
    messagebox.showinfo("Frecuencia Cardíaca", "La frecuencia cardíaca es el número de latidos del corazón por minuto (lpm). El rango normal es entre 60 y 100 lpm.")

def mostrar_resultado():
    global nombre
    nombre = entry_nombre.get().strip()
    peso = entry_peso.get().strip()
    altura = entry_altura.get().strip()
    edad = entry_edad.get().strip()
    genero = combo_genero.get()
    saturacion_oxigeno = entry_oxigeno.get().strip()
    presion_sistolica = entry_presion_sistolica.get().strip()
    presion_diastolica = entry_presion_diastolica.get().strip()
    frecuencia_cardiaca = entry_frecuencia_cardiaca.get().strip()

    if not nombre or not peso or not altura or not edad or not saturacion_oxigeno or not presion_sistolica or not presion_diastolica or not frecuencia_cardiaca:
        label_resultado.config(text="Por favor, completa todos los campos.")
        label_resultado_tmb.config(text="")
    elif contiene_numero(nombre):
        label_resultado.config(text="El nombre no puede contener números.")
        label_resultado_tmb.config(text="")
    else:
        try:
            peso = float(peso)
            altura = float(altura)
            edad = int(edad)
            saturacion_oxigeno = float(saturacion_oxigeno)
            presion_sistolica = int(presion_sistolica)
            presion_diastolica = int(presion_diastolica)
            frecuencia_cardiaca = int(frecuencia_cardiaca)

            resultado_imc = calcular_imc(peso, altura)
            resultado_tmb = calcular_tmb(peso, altura, edad, genero)
            resultado_oxigeno = verificar_oxigenacion(saturacion_oxigeno)
            resultado_presion = verificar_presion_arterial(presion_sistolica, presion_diastolica)
            resultado_frecuencia = verificar_frecuencia_cardiaca(frecuencia_cardiaca)

            label_resultado.config(text=resultado_imc)
            label_resultado_tmb.config(text=resultado_tmb)
            label_resultado_oxigeno.config(text=resultado_oxigeno)
            label_resultado_presion.config(text=resultado_presion)
            label_resultado_frecuencia.config(text=resultado_frecuencia)

        except ValueError:
            label_resultado.config(text="Por favor, introduce valores numéricos válidos.")
            label_resultado_tmb.config(text="")
            label_resultado_oxigeno.config(text="")
            label_resultado_presion.config(text="")
            label_resultado_frecuencia.config(text="")
            
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_oxigeno.delete(0, tk.END)
    entry_presion_sistolica.delete(0, tk.END)
    entry_presion_diastolica.delete(0, tk.END)
    entry_frecuencia_cardiaca.delete(0, tk.END)
    label_resultado.config(text="")
    label_resultado_tmb.config(text="")
    label_resultado_oxigeno.config(text="")
    label_resultado_presion.config(text="")
    label_resultado_frecuencia.config(text="")

root = tk.Tk()
root.title("Calculadora de Salud")
root.geometry("1200x500")  

style = ttk.Style()
style.configure("TFrame", background="#d3e0e9")  
style.configure("TButton", background="#4caf50", font=("Arial", 10, "bold"), foreground="black")  
style.configure("TLabel", background="#d3e0e9", font=("Arial", 12, "bold"))  
style.configure("TEntry", background="white", font=("Arial", 10)) 

frame = ttk.Frame(root, style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")

label_nombre = ttk.Label(frame, text="Sistema de Salud:", font=("Arial", 14, "bold"), foreground="#4caf50")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

label_nombre = ttk.Label(frame, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=10, pady=10)
entry_nombre = ttk.Entry(frame, font=("Arial", 10))
entry_nombre.grid(row=1, column=1, padx=10, pady=10)

label_peso = ttk.Label(frame, text="Peso (kg):")
label_peso.grid(row=2, column=0, padx=10, pady=10)
entry_peso = ttk.Entry(frame, font=("Arial", 10))
entry_peso.grid(row=2, column=1, padx=10, pady=10)

label_altura = ttk.Label(frame, text="Altura (m):")
label_altura.grid(row=3, column=0, padx=10, pady=10)
entry_altura = ttk.Entry(frame, font=("Arial", 10))
entry_altura.grid(row=3, column=1, padx=10, pady=10)

label_edad = ttk.Label(frame, text="Edad:")
label_edad.grid(row=4, column=0, padx=10, pady=10)
entry_edad = ttk.Entry(frame, font=("Arial", 10))
entry_edad.grid(row=4, column=1, padx=10, pady=10)

label_genero = ttk.Label(frame, text="Género:")
label_genero.grid(row=5, column=0, padx=10, pady=10)
generos = ["Masculino", "Femenino"]
combo_genero = ttk.Combobox(frame, values=generos, font=("Arial", 10))
combo_genero.grid(row=5, column=1, padx=10, pady=10)
combo_genero.set(generos[0]) 

label_oxigeno = ttk.Label(frame, text="Saturación de Oxígeno (%):")
label_oxigeno.grid(row=1, column=2, padx=10, pady=10)
entry_oxigeno = ttk.Entry(frame, font=("Arial", 10))
entry_oxigeno.grid(row=1, column=6, padx=10, pady=10)

label_presion_sistolica = ttk.Label(frame, text="Presión Arterial Sistólica (mmHg):")
label_presion_sistolica.grid(row=2, column=2, padx=10, pady=10)
entry_presion_sistolica = ttk.Entry(frame, font=("Arial", 10))
entry_presion_sistolica.grid(row=2, column=6, padx=10, pady=10)

label_presion_diastolica = ttk.Label(frame, text="Presión Arterial Diastólica (mmHg):")
label_presion_diastolica.grid(row=3, column=2, padx=10, pady=10)
entry_presion_diastolica = ttk.Entry(frame, font=("Arial", 10))
entry_presion_diastolica.grid(row=3, column=6, padx=10, pady=10)

label_frecuencia_cardiaca = ttk.Label(frame, text="Frecuencia Cardíaca (lpm):")
label_frecuencia_cardiaca.grid(row=4, column=2, padx=10, pady=10)
entry_frecuencia_cardiaca = ttk.Entry(frame, font=("Arial", 10))
entry_frecuencia_cardiaca.grid(row=4, column=6, padx=10, pady=10)

btn_calcular = ttk.Button(frame, text="Calcular Salud", command=mostrar_resultado)
btn_calcular.grid(row=6, column=2, columnspan=2, pady=10)

btn_limpiar = ttk.Button(frame, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.grid(row=6, column=4, columnspan=2, pady=10)

label_resultado = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#4caf50")
label_resultado.grid(row=10, column=0, columnspan=2, pady=10)

label_resultado_tmb = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#4caf50")
label_resultado_tmb.grid(row=11, column=0, columnspan=2, pady=10)

label_resultado_oxigeno = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#4caf50")
label_resultado_oxigeno.grid(row=12, column=0, columnspan=2, pady=10)

label_resultado_presion = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#4caf50")
label_resultado_presion.grid(row=13, column=0, columnspan=2, pady=10)

label_ayuda_oxigeno = ttk.Label(frame, text="¿Qué es esto?", foreground="blue", cursor="question_arrow", font=("Arial", 10))
label_ayuda_oxigeno.grid(row=1, column=9, padx=10)
label_ayuda_oxigeno.bind("<Button-1>", mostrar_ayuda_oxigeno)

label_ayuda_presion = ttk.Label(frame, text="¿Qué es esto?", foreground="blue", cursor="question_arrow", font=("Arial", 10))
label_ayuda_presion.grid(row=2, column=9, padx=10)
label_ayuda_presion.bind("<Button-1>", mostrar_ayuda_presion)

label_ayuda_frecuencia = ttk.Label(frame, text="¿Qué es esto?", foreground="blue", cursor="question_arrow", font=("Arial", 10))
label_ayuda_frecuencia.grid(row=4, column=9, padx=10)
label_ayuda_frecuencia.bind("<Button-1>", mostrar_ayuda_frecuencia)

label_ayuda_frecuencia = ttk.Label(frame, text="¿Qué es esto?", foreground="blue", cursor="question_arrow", font=("Arial", 10))
label_ayuda_frecuencia.grid(row=3, column=9, padx=10)
label_ayuda_frecuencia.bind("<Button-1>", mostrar_ayuda_presion)

label_resultado_frecuencia = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#4caf50")
label_resultado_frecuencia.grid(row=14, column=0, columnspan=2, pady=10)

root.mainloop()