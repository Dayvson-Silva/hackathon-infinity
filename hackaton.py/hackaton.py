# import random

# def rolar_d20():
#     return random.randint(1,20)

# resultado = rolar_d20()
# if resultado <= 1 and resultado >= 5: 
#     print
# else:
#     print("falhou")
    
    
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Exemplo Flet"

#     def on_click(e):
#         page.add(ft.Text("Olá do Flet!"))

#     button = ft.ElevatedButton(text="Batalha dos 1000 Anos", on_click=on_click)
#     page.add(button)

# ft.app(target=main)

# import flet as ft

# def main(page):
    
#     img = ft.Image(src="URL_DA_IMAGEM", width=300, height=200 ,  )
    

#     btn = ft.ElevatedButton(text="Vamos Para a Guerra!", on_click=lambda e: page.add(ft.Text("Botão clicado!")))

   
#     page.add(img, btn)

# ft.app(target=main)


import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def iniciar_game():
    
    print("Bem Vindo!")

def exibir_instrucoes():
    
    instrucoes = "Use os botões para jogar!\nClique em 'Iniciar Jogo' para começar."
    instrucoes_label.config(text=instrucoes)

janela = tk.Tk()
janela.title("A Batalha dos dois Mundos")
janela.geometry("800x600")  


imagem = Image.open('batalha.jpg')
imagem = imagem.resize((700, 500)) 
imagem = ImageTk.PhotoImage(imagem)

w = tk.Label(janela, image=imagem)
w.imagem = imagem
w.pack()





iniciar_botao = tk.Button(janela, text="Iniciar Jogo", command=iniciar_game)
iniciar_botao.pack(pady=10)

instrucoes_botao = tk.Button(janela, text="Instruções", command=exibir_instrucoes)
instrucoes_botao.pack(pady=10)


instrucoes_label = tk.Label(janela, text="")
instrucoes_label.pack(pady=10)

janela.mainloop()
