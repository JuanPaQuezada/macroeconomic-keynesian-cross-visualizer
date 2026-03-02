import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

consumo_init = 15000.0
inversion_init = 20000.0
pmc_init = 0.8
limite_grafica = 250000

print("TABLA DE ANALISIS SENSITIVO")
print(f"{'Ingreso (Y)':<15} | {'Consumo (C)':<15} | {'Gasto Planeado (DA)':<15}")
print("-" * 50)
for y_val in range(0, 200001, 40000):
    c_val = consumo_init + (pmc_init * y_val)
    da_val = c_val + inversion_init
    print(f"${y_val:<14,.2f} | ${c_val:<14,.2f} | ${da_val:<14,.2f}")
print("="*50 + "\n")

Y_range = np.linspace(0, limite_grafica, 100)

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.35) 

line_45, = ax.plot(Y_range, Y_range, '--', color='blue', label='Y = Gasto (45°)')

def calc_DA(C0, I, c):
    return (C0 + I) + (c * Y_range)

def calc_Eq(C0, I, c):
    return (C0 + I) / (1 - c)

y_inicial = calc_DA(consumo_init, inversion_init, pmc_init)
line_y, = ax.plot(Y_range, y_inicial, lw=2, color='teal', label='Demanda Agregada (C+I)')

eq_x = calc_Eq(consumo_init, inversion_init, pmc_init)
punto_eq, = ax.plot(eq_x, eq_x, 'ro', markersize=8, label='Equilibrio')

ax.set_ylim(0, limite_grafica)
ax.set_xlim(0, limite_grafica)
ax.grid(True, linestyle='--')
ax.set_xlabel('Ingreso Nacional (Y)')
ax.set_ylabel('Demanda Agregada / Gasto')
ax.legend()

multiplicador_init = 1 / (1 - pmc_init)
ax.set_title(f"Multiplicador (k): {multiplicador_init:.2f} | Ingreso Eq: ${eq_x:,.2f}")


# Consumo Autónomo
ax_slider_c0 = fig.add_axes([0.15, 0.22, 0.55, 0.03])
slider_c0 = Slider(ax_slider_c0, 'Consumo (C0)', 0, 50000, valinit=consumo_init, color='green')
slider_c0.valtext.set_visible(False)
ax_box_c0 = fig.add_axes([0.72, 0.22, 0.15, 0.03])
text_box_c0 = TextBox(ax_box_c0, '', initial=str(consumo_init))

# Inversión Planeada
ax_slider_i = fig.add_axes([0.15, 0.14, 0.55, 0.03])
slider_i = Slider(ax_slider_i, 'Inversión (I)', 0, 60000, valinit=inversion_init, color='orange')
slider_i.valtext.set_visible(False)
ax_box_i = fig.add_axes([0.72, 0.14, 0.15, 0.03])
text_box_i = TextBox(ax_box_i, '', initial=str(inversion_init))

# Propensión Marginal al Consumo PMS
ax_slider_pmc = fig.add_axes([0.15, 0.06, 0.55, 0.03])
slider_pmc = Slider(ax_slider_pmc, 'PMC (c)', 0.01, 0.99, valinit=pmc_init, color='purple')
slider_pmc.valtext.set_visible(False)
ax_box_pmc = fig.add_axes([0.72, 0.06, 0.15, 0.03])
text_box_pmc = TextBox(ax_box_pmc, '', initial=str(pmc_init))

def update_plot(val):
    C0 = slider_c0.val
    I = slider_i.val
    c = slider_pmc.val
    
    y_nuevo = calc_DA(C0, I, c)
    line_y.set_ydata(y_nuevo)
    
    nuevo_eq_x = calc_Eq(C0, I, c)
    punto_eq.set_data([nuevo_eq_x], [nuevo_eq_x])
    
    mult = 1 / (1 - c)
    ax.set_title(f"Multiplicador (k): {mult:.2f} | Ingreso Eq: ${nuevo_eq_x:,.2f}")
    fig.canvas.draw_idle()

def update_from_sliders(val):
    text_box_c0.set_val(f"{slider_c0.val:.0f}")
    text_box_i.set_val(f"{slider_i.val:.0f}")
    text_box_pmc.set_val(f"{slider_pmc.val:.2f}")
    update_plot(val)

def submit_c0(text):
    try: slider_c0.set_val(float(text))
    except ValueError: text_box_c0.set_val(f"{slider_c0.val:.0f}")

def submit_i(text):
    try: slider_i.set_val(float(text))
    except ValueError: text_box_i.set_val(f"{slider_i.val:.0f}")

def submit_pmc(text):
    try:
        val = float(text)
        if val >= 1: val = 0.99
        if val <= 0: val = 0.01
        slider_pmc.set_val(val)
    except ValueError:
        text_box_pmc.set_val(f"{slider_pmc.val:.2f}")

# Conectar los eventos
slider_c0.on_changed(update_from_sliders)
slider_i.on_changed(update_from_sliders)
slider_pmc.on_changed(update_from_sliders)

text_box_c0.on_submit(submit_c0)
text_box_i.on_submit(submit_i)
text_box_pmc.on_submit(submit_pmc)

plt.show()