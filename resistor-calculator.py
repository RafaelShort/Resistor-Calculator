import tkinter as tk
from tkinter import ttk, messagebox

def value_to_colors(resistance):
    digit_colors = {
        0: "black", 1: "brown", 2: "red", 3: "orange",
        4: "yellow", 5: "green", 6: "blue", 7: "violet",
        8: "gray", 9: "white"
    }
    
    multiplier_colors = {
        1: "black", 10: "brown", 100: "red", 1000: "orange",
        10000: "yellow", 100000: "green", 1000000: "blue"
    }

    if resistance < 10 or resistance >= 10000000:
        return "Valor fora do intervalo suportado."

    resistance_str = str(resistance)
    first_digit = int(resistance_str[0])
    second_digit = int(resistance_str[1])
    
    if len(resistance_str) > 2:
        power = len(resistance_str) - 2
        multiplier = 10 ** power
    else:
        multiplier = 1

    colors = [
        digit_colors[first_digit],
        digit_colors[second_digit],
        multiplier_colors[multiplier],
    ]

    return colors

def calculate_colors():
    try:
        resistance = int(entry_resistance.get())
        colors = value_to_colors(resistance)
        if isinstance(colors, str):
            messagebox.showerror("Erro", colors)
        else:
            result.set("As cores do resistor são: " + ", ".join(colors))
            draw_resistor(colors)  # Desenha as 3 cores
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def colors_to_value():
    color1 = combo_color1.get()
    color2 = combo_color2.get()
    color3 = combo_color3.get()
    
    digit_colors = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "gray": 8, "white": 9
    }
    
    multiplier_colors = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000,
        "yellow": 10000, "green": 100000, "blue": 1000000
    }
    
    if color1 in digit_colors and color2 in digit_colors and color3 in multiplier_colors:
        value = (digit_colors[color1] * 10 + digit_colors[color2]) * multiplier_colors[color3]
        result.set(f"O valor da resistência é: {value} Ohms")
        draw_resistor([color1, color2, color3])  # Desenha as cores selecionadas
    else:
        messagebox.showerror("Erro", "Selecione cores válidas.")

def draw_resistor(colors):
    # Limpa a tela antes de desenhar o novo resistor
    canvas.delete("all")
    
    width = 60
    height = 20
    space = 5
    num_bands = len(colors)

    # Calcular a posição x inicial para centralizar
    x_initial = (canvas.winfo_width() - (width * num_bands + space * (num_bands - 1))) / 2

    # Desenhar cada faixa de cor
    for i, color in enumerate(colors):
        x0 = x_initial + i * (width + space)
        x1 = x0 + width
        canvas.create_rectangle(x0, 10, x1, 10 + height, fill=color)

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Resistores")

# Variável para o resultado
result = tk.StringVar()

# Opção para calcular a resistência a partir do valor
frame_value = ttk.Frame(root, padding="10")
frame_value.grid(row=0, column=0, sticky=(tk.W, tk.E))

label_resistance = ttk.Label(frame_value, text="Digite o valor da resistência (Ohms):")
label_resistance.grid(row=0, column=0, sticky=tk.W)

entry_resistance = ttk.Entry(frame_value)
entry_resistance.grid(row=0, column=1)

button_calculate = ttk.Button(frame_value, text="Calcular Cores", command=calculate_colors)
button_calculate.grid(row=0, column=2)

# Opção para calcular o valor a partir das cores
frame_colors = ttk.Frame(root, padding="10")
frame_colors.grid(row=1, column=0, sticky=(tk.W, tk.E))

label_colors = ttk.Label(frame_colors, text="Selecione as cores do resistor:")
label_colors.grid(row=0, column=0, columnspan=3)

# Criar listas de cores
digit_colors = ["black", "brown", "red", "orange", "yellow",
                "green", "blue", "violet", "gray", "white"]
multiplier_colors = ["black", "brown", "red", "orange", "yellow", 
                     "green", "blue"]

combo_color1 = ttk.Combobox(frame_colors, values=digit_colors, state="readonly")
combo_color1.grid(row=1, column=0)

combo_color2 = ttk.Combobox(frame_colors, values=digit_colors, state="readonly")
combo_color2.grid(row=1, column=1)

combo_color3 = ttk.Combobox(frame_colors, values=multiplier_colors, state="readonly")
combo_color3.grid(row=1, column=2)

button_calculate_value = ttk.Button(frame_colors, text="Calcular Valor", command=colors_to_value)
button_calculate_value.grid(row=1, column=3)

# Label para mostrar o resultado
label_result = ttk.Label(root, textvariable=result)
label_result.grid(row=2, column=0, pady=10)

# Canvas para desenhar o resistor
canvas = tk.Canvas(root, width=200, height=50, bg="white")
canvas.grid(row=3, column=0)

# Iniciar o loop da interface
root.mainloop()
