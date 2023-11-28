import tkinter as tk
from PIL import Image, ImageTk
import random

class JogoMatematica:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("MathKids")
        self.janela.geometry("800x600")
        
        self.nivel = None
        self.max_perguntas = 10  # Limite de 10 perguntas
        self.pontuacao = 0
        self.numero_perguntas = 0
        
        # Imagem de fundo da pasta "static" e ajuste ao tamanho da janela
        imagem_fundo = Image.open("static/background1.jpg")
        imagem_fundo = imagem_fundo.resize((400, 200))
        self.fundo = ImageTk.PhotoImage(imagem_fundo)
        
        # Rótulo para exibir o fundo
        self.label_fundo = tk.Label(self.janela, image=self.fundo)
        self.label_fundo.pack(fill=tk.BOTH, expand=True)
        
        # Texto "Criado por Math Metamorphs"
        self.label_creditos = tk.Label(self.janela, text="Criado por Math Metamorphs", font=("Comic Sans MS", 12), fg="black")
        self.label_creditos.pack(side=tk.BOTTOM)

        # Inicie com a escolha do nível
        self.exibir_escolha_nivel()

    def exibir_escolha_nivel(self):
        # Rótulo para escolher o nível
        label_nivel = tk.Label(self.janela, text="Escolha o nível de dificuldade:", font=("Comic Sans MS", 18), fg="blue")
        label_nivel.pack(pady=20)

        # Botões para escolher o nível
        botao_facil = tk.Button(self.janela, text="Fácil", command=lambda: self.iniciar_jogo("fácil"), font=("Comic Sans MS", 18), bg="green", fg="white")
        botao_medio = tk.Button(self.janela, text="Médio", command=lambda: self.iniciar_jogo("médio"), font=("Comic Sans MS", 18), bg="orange", fg="black")
        botao_dificil = tk.Button(self.janela, text="Difícil", command=lambda: self.iniciar_jogo("difícil"), font=("Comic Sans MS", 18), bg="red", fg="white")

        label_nivel.pack()
        botao_facil.pack()
        botao_medio.pack()
        botao_dificil.pack()

    def iniciar_jogo(self, nivel):
        self.nivel = nivel
        self.pontuacao = 0
        self.numero_perguntas = 0
        
        # Remova os elementos da escolha do nível
        for widget in self.janela.winfo_children():
            widget.pack_forget()

        # Adicione os elementos do jogo
        self.label_pergunta = tk.Label(self.janela, text="", font=("Comic Sans MS", 24), fg="blue")
        self.label_pergunta.pack(pady=20)
        
        self.entry_resposta = None
        
        self.botao_responder = tk.Button(self.janela, text="Responder", command=self.verificar_resposta, font=("Comic Sans MS", 18), bg="green", fg="white")
        self.botao_responder.pack()

        self.botao_feedback = tk.Label(self.janela, text="", font=("Comic Sans MS", 18))
        self.botao_feedback.pack()

        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.botao_responder.config(state=tk.NORMAL)  # Reativar o botão de resposta

        if self.numero_perguntas < self.max_perguntas:
            if self.nivel == "fácil":
                operacao = random.choice(["+", "-"])
                numero1 = random.randint(1, 10)
                numero2 = random.randint(1, 10)
            elif self.nivel == "médio":
                operacao = random.choice(["+", "-", "*", "/"])
                numero1 = random.randint(1, 20)
                numero2 = random.randint(1, 20)
            else:
                operacao = random.choice(["*", "/"])
                numero1 = random.randint(1, 50)
                numero2 = random.randint(1, 10)

            if operacao == "+":
                self.resposta_correta = numero1 + numero2
                pergunta = f"{numero1} + {numero2} = ?"
            elif operacao == "-":
                self.resposta_correta = numero1 - numero2
                pergunta = f"{numero1} - {numero2} = ?"
            elif operacao == "*":
                self.resposta_correta = numero1 * numero2
                pergunta = f"{numero1} * {numero2} = ?"
            else:
                self.resposta_correta = numero1 / numero2
                pergunta = f"{numero1} / {numero2} = ?"

            self.label_pergunta.config(text=pergunta)

            if self.entry_resposta:
                self.entry_resposta.destroy()

            self.entry_resposta = tk.Entry(self.janela, font=("Comic Sans MS", 24))
            self.entry_resposta.pack(pady=10)

            self.botao_feedback.config(text="", fg="black")
        else:
            self.mostrar_resultados()

    def verificar_resposta(self):
        resposta_digitada = self.entry_resposta.get()

        try:
            resposta_digitada = float(resposta_digitada)
            if resposta_digitada == self.resposta_correta:
                self.pontuacao += 1
                self.botao_feedback.config(text="Resposta correta!", fg="green")
            else:
                self.botao_feedback.config(text="Resposta incorreta. Tente novamente.", fg="red")

            self.numero_perguntas += 1
            self.botao_responder.config(state=tk.DISABLED)
            self.janela.after(1000, self.proxima_pergunta)  # Aguarda 1 segundo antes da próxima pergunta
        except ValueError:
            self.botao_feedback.config(text="Por favor, insira um número válido.", fg="red")

    def mostrar_resultados(self):
        self.label_pergunta.config(text=f"Fim do jogo! Sua pontuação: {self.pontuacao}/{self.max_perguntas}")
        self.entry_resposta.destroy()
        self.botao_responder.config(state=tk.DISABLED)
        
        self.botao_recomecar = tk.Button(self.janela, text="Escolher Novo Nível", command=self.exibir_escolha_nivel, font=("Comic Sans MS", 18), bg="blue", fg="white")
        self.botao_recomecar.pack(pady=20)
        

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoMatematica(root)
    root.mainloop()
