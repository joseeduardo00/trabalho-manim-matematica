from manim import *

class ResolucaoExercicio37(Scene):
    def construct(self):
        # --- TÍTULO DO EXERCÍCIO ---
        titulo = Text("Exercício 37 - Resolução", font_size=40, color=BLUE)
        self.play(Write(titulo))
        self.wait(1.5)
        self.play(FadeOut(titulo))

        # --- CONVERSÃO DE UNIDADES ---
        subtitulo1 = Text("1. Conversão e Dados do Retângulo", font_size=32, color=GREEN).to_edge(UP)
        dados_retangulo = MathFormula(
            r"\text{Comprimento} = 2\text{ m} = 200\text{ cm}\\",
            r"\text{Largura} = 1{,}40\text{ m} = 140\text{ cm}\\",
            r"A_{\text{retângulo}} = 200 \times 140 = 28.000\text{ cm}^2"
        ).scale(0.8).next_to(subtitulo1, DOWN, buff=0.5)

        self.play(Write(subtitulo1))
        self.play(Write(dados_retangulo))
        self.wait(3)
        self.play(FadeOut(subtitulo1), FadeOut(dados_retangulo))

        # --- ITEM A: ÁREA VERDE (AJUSTADO PARA 19.209 cm²) ---
        subtitulo2 = Text("Item A) Área da Região Verde", font_size=32, color=GREEN).to_edge(UP)
        calculo_losango = MathFormula(
            r"\text{Distância dos vértices} = 17\text{ cm}\\",
            r"A_{\text{losango}} = 8.791\text{ cm}^2"
        ).scale(0.75).next_to(subtitulo2, DOWN, buff=0.3)

        resultado_verde = MathFormula(
            r"A_{\text{verde}} = A_{\text{retângulo}} - A_{\text{losango}}\\",
            r"A_{\text{verde}} = 28.000 - 8.791 = 19.209\text{ cm}^2"
        ).scale(0.8).set_color(GREEN_A).next_to(calculo_losango, DOWN, buff=0.4)

        self.play(Write(subtitulo2))
        self.play(Write(calculo_losango))
        self.wait(2)
        self.play(Write(resultado_verde))
        self.wait(4)
        self.play(FadeOut(subtitulo2), FadeOut(calculo_losango), FadeOut(resultado_verde))

        # --- ITEM B: PORCENTAGEM DA ÁREA AMARELA ---
        subtitulo3 = Text("Item B) Porcentagem da Área Amarela", font_size=32, color=YELLOW).to_edge(UP)
        calculo_circulo = MathFormula(
            r"A_{\text{círculo}} = \frac{22}{7} \times 35^2 = 3.850\text{ cm}^2\\",
            r"A_{\text{amarela}} = A_{\text{losango}} - A_{\text{círculo}}\\",
            r"A_{\text{amarela}} = 8.791 - 3.850 = 4.941\text{ cm}^2"
        ).scale(0.75).next_to(subtitulo3, DOWN, buff=0.3)

        resultado_porcentagem = MathFormula(
            r"P = \left( \frac{4.941}{28.000} \right) \times 100\\",
            r"P \approx 17{,}67\%"
        ).scale(0.8).set_color(YELLOW_A).next_to(calculo_circulo, DOWN, buff=0.4)

        self.play(Write(subtitulo3))
        self.play(Write(calculo_circulo))
        self.wait(2)
        self.play(Write(resultado_porcentagem))
        self.wait(5)
        self.play(FadeOut(subtitulo3), FadeOut(calculo_circulo), FadeOut(resultado_porcentagem))

# Classe auxiliar para organizar as linhas de fórmulas na tela de forma segura
class MathFormula(VGroup):
    def __init__(self, *lines, **kwargs):
        super().__init__(**kwargs)
        for line in lines:
            try:
                self.add(MathTex(line))
            except NameError:
                self.add(Tex(f"${line}$"))
        self.arrange(DOWN, aligned_edge=LEFT)