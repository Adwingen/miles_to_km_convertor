from tkinter import *
from tkinter import messagebox

# Constante de conversão de milhas para quilômetros
MILES_TO_KM_CONVERSION_FACTOR = 1.609

# Função para converter milhas em quilômetros
def miles_to_km():
    try:
        # Tentativa de conversão de entrada para float
        miles = float(my_input.get())
        km = miles * MILES_TO_KM_CONVERSION_FACTOR
        result_label.config(text=f"{km:.2f}")  # Exibindo o resultado com duas casas decimais
    except ValueError:
        # Se a entrada não for válida, exibe uma mensagem de erro
        messagebox.showerror("Entrada inválida", "Por favor, insira um número válido.")
        result_label.config(text="0.00")  # Reseta o resultado para um valor padrão

# Configuração da janela principal
window = Tk()
window.title("Conversor de Milhas para Km")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Campo de entrada (Entry)
my_input = Entry(width=10)
my_input.grid(column=1, row=1)

# Rótulo "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

# Rótulo "is equal to"
miles_is_equal_to = Label(text="is equal to")
miles_is_equal_to.grid(column=0, row=2)

# Rótulo para exibir o resultado
result_label = Label(text="0.00")
result_label.grid(column=1, row=2)

# Rótulo "KM"
km_label = Label(text="KM")
km_label.grid(column=2, row=2)

# Botão para calcular
button_calculate = Button(text="Calcular", command=miles_to_km)
button_calculate.grid(column=1, row=3)

# Iniciando o loop principal da janela
window.mainloop()
