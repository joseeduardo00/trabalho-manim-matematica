from manim import *

class TesteInstalacao(Scene):
    def construct(self):
        # Cria um quadrado vermelho
        quadrado = Square(color=RED)
        quadrado.set_fill(RED, opacity=0.5)
        
        # Cria um texto abaixo
        texto = Text("Manim Funcionando!", font_size=36).next_to(quadrado, DOWN)
        
        # Transforma o quadrado em um círculo azul
        circulo = Circle(color=BLUE)
        circulo.set_fill(BLUE, opacity=0.5)
        
        # Executa as animações na tela
        self.play(DrawBorderThenFill(quadrado))
        self.play(Write(texto))
        self.wait(1)
        self.play(Transform(quadrado, circulo))
        self.wait(2)