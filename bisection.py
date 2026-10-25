import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 1 

def g(x):
    return x**3 - 7*(x**2) + 14*x - 6

def h(x):
    return x - 2*np.sin(x)

def k(x):
    return x - np.tan(x)

def m(x):
    return x**2 - 1 - np.e**(1-x**2)

def n(x):
    return (x + 3) * (x + 1)**2 * x * (x - 1)**3 * (x - 3)

def volumen(h, l=10, r=1, v=12.4):
    return l * (0.5 * np.pi * (r**2) - (r**2) * np.arcsin(h / r) - h * ((r**2) - (h**2))**0.5) - v


def caida(t, s0 = 300,m = 0.25,g = 9.81,k = 0.1,):

    return s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - np.exp(-k * t / m))


def bisection(f, a, b, tolerancia=1e-02, iteraciones=100):
    fa = f(a)
    
    for i in range(1, iteraciones + 1):
        p = a + (b - a) / 2
        fp = f(p)
        
        print(f'Iteración {i}: p = {p:.6f}')
        
        if fp == 0 or (b - a) / 2 < tolerancia:
            return p

        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

    raise RuntimeError("Se alcanzó el número máximo de iteraciones")

if __name__ == '__main__':
    print('Seccion 1')
    resultado = bisection(f, 1, 2, 1e-04)
    print(f'\nResultado obtenido: {resultado:.6f}')

    print('Seccion 2')
    
    resultado = bisection(g, 0, 1, 1e-02)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(g, 1, 3.2, 1e-02)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(g, 3.2, 4, 1e-02)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(h, 1.6, 2.2, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(k, 4.4, 4.6, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')
    
    resultado = bisection(m, -2, 0, 1e-03)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(k, 1, 2, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')

    print('Seccion 3')

    resultado = bisection(n, -3.5, 2.5, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(n, -1.5, 0.6, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')
    
    resultado = bisection(n, 0.4, 2.2, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')

    resultado = bisection(n, 2, 3.7, 1e-05)
    print(f'\nResultado obtenido: {resultado:.6f}')

    print('Seccion 4')

    h_res = bisection(volumen, 0, 1, 1e-02)
    print(f'\nh = {h_res:.6f} cm')

    profundidad = 1 - h_res
    print(f'Profundidad del agua = {profundidad:.6f} cm')

    resultado = bisection(caida, 14, 15, 1e-02)
    print(f'\nTiempo de caida = {resultado:.6f} s')

    print('Seccion 5')
    raiz = bisection(k, 4.4, 4.6, 1e-05)
    print(f"Solución: x = {raiz:.6f}")

    x = np.linspace(0, 5, 4000)
    y1 = x
    y2 = np.tan(x)

    y2[np.abs(np.cos(x)) < 0.035] = np.nan
    y2[np.abs(y2) > 10] = np.nan

    plt.figure(figsize=(10, 6))

    plt.plot(x, y1, label="y = x")
    plt.plot(x, y2, label="y = tan(x)")

    plt.axvline(np.pi / 2, color="gray", linestyle="--",
                label="Asíntotas de tan(x)")
    plt.axvline(3 * np.pi / 2, color="gray", linestyle="--")

    plt.scatter(raiz, raiz, color="red", zorder=5,
                label=f"Solución: x = {raiz:.4f}")

    plt.annotate(
        f"x ≈ {raiz:.4f}",
        xy=(raiz, raiz),
        xytext=(3.2, 7.2),
        arrowprops=dict(arrowstyle="->")
    )

    plt.xlim(0, 5)
    plt.ylim(-10, 10)
    plt.xlabel("x (radianes)")
    plt.ylabel("y")
    plt.title("Gráficas de y = x e y = tan(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("grafica_x_tanx.png", dpi=180)
    plt.show()

