from manim import *

class DeducaoHeron(Scene):
    def construct(self):
        # --- TÍTULO ---
        titulo = Text("Dedução da Fórmula de Heron", font_size=40, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # --- PASSO 1 ---
        p1_titulo = Text("1. Aplicação do Teorema de Pitágoras", font_size=32, color=GREEN).to_edge(UP)
        p1_formulas = MathTex(
            r"h^2 = b^2 - x^2 \quad \text{(Triângulo 1)}\\",
            r"h^2 = a^2 - (c - x)^2 \quad \text{(Triângulo 2)}"
        ).next_to(p1_titulo, DOWN, buff=0.6)

        self.play(Write(p1_titulo))
        self.play(Write(p1_formulas))
        self.wait(4)
        self.play(FadeOut(p1_titulo), FadeOut(p1_formulas))

        # --- PASSO 2 ---
        p2_titulo = Text("2. Igualando as Equações e Isolando x", font_size=32, color=GREEN).to_edge(UP)
        p2_formulas = MathTex(
            r"b^2 - x^2 = a^2 - (c^2 - 2cx + x^2)\\",
            r"b^2 = a^2 - c^2 + 2cx\\",
            r"x = \frac{b^2 + c^2 - a^2}{2c}"
        ).scale(0.85).next_to(p2_titulo, DOWN, buff=0.5)

        self.play(Write(p2_titulo))
        self.play(Write(p2_formulas))
        self.wait(5)
        self.play(FadeOut(p2_titulo), FadeOut(p2_formulas))

        # --- PASSO 3 ---
        p3_titulo = Text("3. Introduzindo o Semiperímetro (s)", font_size=32, color=GREEN).to_edge(UP)
        p3_formulas = MathTex(
            r"s = \frac{a + b + c}{2}\\",
            r"\text{Substituindo } x \text{ em } h^2 = b^2 - x^2:\\",
            r"h = \frac{2}{c} \sqrt{s(s-a)(s-b)(s-c)}"
        ).scale(0.85).next_to(p3_titulo, DOWN, buff=0.5)

        self.play(Write(p3_titulo))
        self.play(Write(p3_formulas))
        self.wait(5)
        self.play(FadeOut(p3_titulo), FadeOut(p3_formulas))

        # --- PASSO 4 ---
        p4_titulo = Text("4. Área Final do Triângulo", font_size=32, color=YELLOW).to_edge(UP)
        p4_formulas = MathTex(
            r"A = \frac{\text{base} \times \text{altura}}{2} = \frac{c \times h}{2}\\",
            r"A = \frac{c}{2} \cdot \left[ \frac{2}{c} \sqrt{s(s-a)(s-b)(s-c)} \right]"
        ).scale(0.85).next_to(p4_titulo, DOWN, buff=0.4)

        resultado_final = MathTex(
            r"A = \sqrt{s(s - a)(s - b)(s - c)}"
        ).scale(1.3).set_color(YELLOW).next_to(p4_formulas, DOWN, buff=0.6)

        self.play(Write(p4_titulo))
        self.play(Write(p4_formulas))
        self.wait(3)
        self.play(Write(resultado_final))
        self.wait(6)
        self.play(FadeOut(p4_titulo), FadeOut(p4_formulas), FadeOut(resultado_final))