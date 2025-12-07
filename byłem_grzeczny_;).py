import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon, Circle, Rectangle, Ellipse
import numpy as np
from matplotlib.colors import to_hex, to_rgb

def draw_realistic_santa(main_color):
    """
    Rysuje Świętego Mikołaja w Matplotlib, używając podanego koloru głównego.
    """
    # Kolory główne (zmieniane przez użytkownika)
    RED = main_color
    
    # Obliczenie ciemniejszego odcienia dla cieniowania (Matplotlib to_rgb)
    # Konwersja na RGB (0-1)
    rgb_main = to_rgb(RED)
    
    # Stworzenie ciemniejszego odcienia poprzez zmniejszenie wartości RGB
    # Używamy prostego przyciemnienia o 20%
    darker_rgb = tuple(max(0, c * 0.8) for c in rgb_main)
    SHADE_RED = to_hex(darker_rgb)

    # Inne stałe kolory
    DARK_RED = '#AA1D1A' # Używany tylko do cienia nosa
    WHITE = '#F0F0F0'
    SKIN = '#F7C6A6'
    SHADE_SKIN = '#DDAA88'
    BLACK = '#000000'
    GOLD = '#FFD700'

    # Utwórz figurę i oś
    fig, ax = plt.subplots(figsize=(7, 9))

    # Ustawienia osi
    ax.set_xlim(-8, 8) 
    ax.set_ylim(-10, 8)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # --- 1. Tułów (Ciało) ---
    body_points = [
        (-2.8, -5.5), (2.8, -5.5), 
        (3.5, -0.5), (3.0, 0.5),
        (-3.0, 0.5), (-3.5, -0.5)
    ]
    # Użycie koloru głównego
    ax.add_patch(Polygon(body_points, fc=RED, ec=BLACK, lw=1.5, zorder=1))

    # Cieniowanie płaszcza (lewa strona)
    shade_points = [(-2.8, -5.5), (-2.5, -5.5), (-2.5, 0.0), (-3.0, 0.5), (-3.5, -0.5)]
    # Użycie koloru cieniowania
    ax.add_patch(Polygon(shade_points, fc=SHADE_RED, ec='none', zorder=1.5, alpha=0.8))

    # Czarny pas
    belt = Rectangle((-3.5, -1.8), 7, 1.0, fc=BLACK, ec=BLACK, lw=1.5, zorder=2)
    ax.add_patch(belt)

    # Złota klamra pasa
    buckle = Rectangle((-0.7, -1.6), 1.4, 0.6, fc=GOLD, ec=BLACK, lw=1.5, zorder=3)
    ax.add_patch(buckle)
    
    # Białe futro na dole kurtki
    fur_bottom_points = np.array([
        [-3.5, -5.5], [-2.5, -6.0], [-1.0, -5.7], [0, -6.2], 
        [1.0, -5.7], [2.5, -6.0], [3.5, -5.5]
    ])
    ax.add_patch(Polygon(fur_bottom_points, fc=WHITE, ec=BLACK, lw=1.5, zorder=2))


    # --- 2. Ręce i Rękawiczki ---
    # Lewe ramię (Użycie koloru głównego)
    arm_left_poly = Polygon([(-3.5, -0.5), (-3.0, -4.0), (-4.5, -4.5), (-5.0, -0.0)], 
                            closed=True, fc=RED, ec=BLACK, lw=1.5, zorder=0)
    ax.add_patch(arm_left_poly)
    # Lewy mankiet
    ax.add_patch(Circle((-4.0, -4.0), 1.2, fc=WHITE, ec=BLACK, lw=1.5, zorder=1))
    # Lewa dłoń
    ax.add_patch(Circle((-4.0, -4.0), 0.7, fc=BLACK, ec=BLACK, lw=1.5, zorder=2))

    # Prawe ramię (Użycie koloru głównego)
    arm_right_poly = Polygon([(3.5, -0.5), (3.0, -4.0), (4.5, -4.5), (5.0, -0.0)], 
                             closed=True, fc=RED, ec=BLACK, lw=1.5, zorder=0)
    ax.add_patch(arm_right_poly)
    # Prawy mankiet
    ax.add_patch(Circle((4.0, -4.0), 1.2, fc=WHITE, ec=BLACK, lw=1.5, zorder=1))
    # Prawa dłoń
    ax.add_patch(Circle((4.0, -4.0), 0.7, fc=BLACK, ec=BLACK, lw=1.5, zorder=2))


    # --- 3. Głowa i Twarz (Bez zmian kolorów) ---
    face = Ellipse((0, 0), 2.2 * 2, 2.5 * 2, fc=SKIN, ec=BLACK, lw=1.5, zorder=3)
    ax.add_patch(face)
    shade = Ellipse((0.2, -0.2), 3.0, 3.5, fc=SHADE_SKIN, ec='none', alpha=0.4, zorder=3.5)
    ax.add_patch(shade)
    ax.add_patch(Circle((-0.7, 0.8), 0.15, fc=BLACK, zorder=4))
    ax.add_patch(Circle((0.7, 0.8), 0.15, fc=BLACK, zorder=4))
    ax.add_patch(Circle((0, 0.0), 0.3, fc=RED, ec=BLACK, lw=1.5, zorder=4))
    ax.add_patch(Circle((0.0, 0.0), 0.25, fc=DARK_RED, ec='none', alpha=0.5, zorder=4.5))


    # --- 4. Czapka (Użycie koloru głównego) ---
    cap_cone = Polygon([(0, 2.5), (-2.8, 4.0), (0, 7.5), (2.8, 4.0)], closed=True, fc=RED, ec=BLACK, lw=1.5, zorder=2)
    ax.add_patch(cap_cone)
    
    pom_pom = Circle((0.5, 7.0), 0.8, fc=WHITE, ec=BLACK, lw=1.5, zorder=2)
    ax.add_patch(pom_pom)

    cap_band = Rectangle((-3.2, 1.5), 6.4, 1.2, fc=WHITE, ec=BLACK, lw=1.5, zorder=3)
    ax.add_patch(cap_band)

    # --- 5. Brody i Wąsy (Bez zmian kolorów) ---
    beard_shape = [
        Circle((-2.5, -0.8), 1.6, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
        Circle((0, -2.5), 2.5, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
        Circle((2.5, -0.8), 1.6, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
        Circle((-1.5, -3.5), 1.5, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
        Circle((1.5, -3.5), 1.5, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
        Circle((0, -4.5), 1.8, fc=WHITE, ec=BLACK, lw=1.0, zorder=3),
    ]
    for p in beard_shape:
        ax.add_patch(p)

    mustache_left_poly = Polygon([(-1.5, 0), (-0.5, 0.5), (0, -0.3), (-1.0, -0.8)], closed=True, fc=WHITE, ec=BLACK, lw=1.5, zorder=4)
    mustache_right_poly = Polygon([(1.5, 0), (0.5, 0.5), (0, -0.3), (1.0, -0.8)], closed=True, fc=WHITE, ec=BLACK, lw=1.5, zorder=4)
    
    ax.add_patch(mustache_left_poly)
    ax.add_patch(mustache_right_poly)
    
    # --- 6. Nogi i Buty (Użycie koloru głównego) ---
    leg_left_poly = Polygon([(-2.5, -8.0), (0, -8.0), (0, -5.5), (-2.5, -5.5)], fc=RED, ec=BLACK, lw=1.5, zorder=1)
    ax.add_patch(leg_left_poly)

    leg_right_poly = Polygon([(0, -8.0), (2.5, -8.0), (2.5, -5.5), (0, -5.5)], fc=RED, ec=BLACK, lw=1.5, zorder=1)
    ax.add_patch(leg_right_poly)
    
    # Buty 
    boot_left_poly = Polygon([(-3.0, -9.0), (0.0, -9.0), (-0.5, -8.0), (-2.5, -8.0)], closed=True, fc=BLACK, ec=BLACK, lw=1.5, zorder=2)
    ax.add_patch(boot_left_poly)
    
    boot_right_poly = Polygon([(3.0, -9.0), (0.0, -9.0), (0.5, -8.0), (2.5, -8.0)], closed=True, fc=BLACK, ec=BLACK, lw=1.5, zorder=2)
    ax.add_patch(boot_right_poly)
    
    plt.title(f"Mikołaj w kolorze: {RED} 🌟")
    
    return fig

# ---------------- Streamlit App ----------------

def main():
    st.set_page_config(page_title="Streamlit Santa", page_icon="🎅")
    st.title("🎅 Interaktywny Święty Mikołaj w Matplotlib i Streamlit")
    st.markdown("Użyj selektora kolorów poniżej, aby zmienić **kolor płaszcza i czapki** Mikołaja.")
    
    # --- WIDŻET STREAMLIT DO WYBORU KOLORU ---
    default_red = '#E62E2A'
    selected_color = st.sidebar.color_picker('Wybierz kolor płaszcza Mikołaja:', default_red)
    
    # Wywołanie funkcji rysującej z wybranym kolorem
    santa_fig = draw_realistic_santa(selected_color)
    st.pyplot(santa_fig)
    
    st.caption("Zmiana koloru głównego automatycznie aktualizuje cieniowanie (przyciemniając wybrany kolor).")

if __name__ == "__main__":
    main()
