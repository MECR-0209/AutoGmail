from customtkinter import * # Importa o TKinter, para a interface visual.
from PIL import Image, ImageTk, ImageDraw # Importa o Pillow, necessário para fazer a imagem.
import pyautogui # Importa o AutoGUI, para automatizar o processo.
import pyperclip # Importa o Pyperclip, para automatizar o CTRL C.
import webbrowser # Importa o Webbrowser, para abrir o navegador patrão através de atalho.
import time # Importa o módulo da hora, necessário para fazer a pausa no programa, para que não corra muito rápido.
import emoji # Importa os emojis, para colocarmos nos créditos.

janela = CTk() # Criar janela.
janela._set_appearance_mode("dark_blue") # Aparência conforme o tema do sistema do usuário.
janela.iconbitmap("_internal/arquivos/bostini.ico") # Ícone que irá aparecer na barra.
janela.geometry("300x300") # Escolher o tamanho no qual ela irá abrir.
janela.resizable(width = "false", height = "false") # Impedir do usuário mudar o tamanho da janela.
janela.title("Gmail Script v0.1") # Título na barra.

def creditos(event=None): # Janela de créditos.
    def desativarselecaotexto(event):
        janelacreditotexto.tag_remove("sel", "1.0", "end")
        return "break" # Remove a capacidade de seleção de texto nos créditos.
    
    janelacredito = CTkToplevel(janela) # Criar janela secundária dos créditos.
    janelacredito.geometry("300x100") # Escolher o tamanho no qual ela irá abrir.
    janelacredito.title("Feito por:") # Título na barra.
    janelacredito.iconbitmap("_internal/arquivos/bostini.ico") # Ícone que irá aparecer na barra.
    janelacredito.resizable(width = "false", height = "false") # Impedir do usuário mudar o tamanho da janela.
    janelacreditotexto = CTkTextbox(janelacredito, width = 300, height = 120, fg_color = "transparent") # Caixa de texto dos créditos, transparente.
    janelacreditotexto.configure(state = "normal") # Configura a janela como normal.
    janelacreditotexto.bind("<Button-1>", desativarselecaotexto) # Remove a capacidade de seleção de texto com o botão do mouse nos créditos.
    janelacreditotexto.place (x = 1, y = 1) # Posicionamento do texto.
    textocreditos = emoji.emojize("Bosta: Henrique Contini (Rique) :pile_of_poo: \nMerda: Maria Campos (Duda) :pile_of_poo: \n\nUm salve para Guilherme Menezes (Xepa)! :moai:\nOutro salve para Ruan Augusto (Telha)! :axe:\nE um últimosalve para João Victor (JV)!")
    janelacreditotexto.insert("0.0", textocreditos)

def comousar(event=None):
    def desativarselecaotexto2(event):
        janelausartexto.tag_remove("sel", "1.0", "end")
        return "break" # Remove a capacidade de seleção de texto nos créditos.
    
    janelausar = CTkToplevel(janela)
    janelausar.geometry("300x100")
    janelausar.title("Como usar o programa")
    janelausar.iconbitmap("_internal/arquivos/bostini.ico") # Ícone que irá aparecer na barra.
    janelausar.resizable(width = "false", height = "false") # Impedir do usuário mudar o tamanho da janela.
    janelausartexto = CTkTextbox(janelausar, width = 300, height = 120, fg_color = "transparent") # Caixa de texto de como usar, transparente.
    janelausartexto.configure(state = "normal") # Configura a janela como normal.
    janelausar.bind("<Button-1>", desativarselecaotexto2) # Remove a capacidade de seleção de texto com o botão do mouse nos créditos.
    janelausartexto.place (x = 1, y = 1)
    textousar = ("1. Preencha no destinatário o endereço de e-mail.\n2. Preencha no assunto o assunto do e-mail.\n3. Preencha na caixa a mensagem do e-mail.\n\nLembrando que é necessário habilitar as teclas\nde atalho nas opções do Gmail.")
    janelausartexto.insert("0.0", textousar)


def mudar_cursor_enter(event):
    label_botao.configure(cursor = "hand2")
    label_botao2.configure(cursor = "hand2")

def mudar_cursor_leave(event):
    label_botao.configure(cursor = "arrow")
    label_botao2.configure(cursor = "arrow")

# Carregar a imagem do botão e redimensioná-la se necessário
imagem = Image.open("_internal/arquivos/bostamijo.jpg")
tamanho = (40, 40)  # Especificar o tamanho desejado do botão
imagem_redimensionada = imagem.resize(tamanho)

# Criar uma máscara para o botão redondo
mascara = Image.new("L", tamanho, 0)
draw = ImageDraw.Draw(mascara)
draw.ellipse((0, 0) + tamanho, fill=255)

# Aplicar a máscara à imagem
imagem_redonda = Image.new("RGBA", tamanho, 0)
imagem_redonda.paste(imagem_redimensionada, mask=mascara)

# Converter a imagem para o formato que o CTkinter pode usar
imagem_tk = ImageTk.PhotoImage(imagem_redonda)

# Criar um Label com a imagem do botão
label_botao = CTkLabel(janela, image=imagem_tk, text = "")
label_botao.bind("<Button-1>",creditos)  # Associar o evento de clique ao Label
label_botao.bind("<Enter>", mudar_cursor_enter)
label_botao.place(x=5, y=255)  # Posicionar o Label na janela

# Carregar a imagem do botão e redimensioná-la se necessário
imagem2 = Image.open("_internal/arquivos/fullofcoco.jpg")
tamanho2 = (40, 40)  # Especificar o tamanho desejado do botão
imagem_redimensionada2 = imagem2.resize(tamanho2)

# Criar uma máscara para o botão redondo
mascara2 = Image.new("L", tamanho2, 0)
draw2 = ImageDraw.Draw(mascara2)
draw2.ellipse((0, 0) + tamanho2, fill=255)

#Aplicar a máscara à imagem
imagem_redonda2 = Image.new("RGBA", tamanho2, 0)
imagem_redonda2.paste(imagem_redimensionada2, mask=mascara2)

#Converter a imagem para o formato que o CTkinter pode usar
imagem_tk2 = ImageTk.PhotoImage(imagem_redonda2)

label_botao2 = CTkLabel(janela, image=imagem_tk2, text = "")
label_botao2.bind("<Button-1>",comousar)  # Associar o evento de clique ao Label
label_botao2.bind("<Enter>", mudar_cursor_enter)
label_botao2.place(x=50, y=255)  # Posicionar o Label na janela

url = "https://gmail.com" # Definindo a URL para o Gmail.
inputdestinatario = StringVar(janela) # Definindo a variável do destinatário.
inputassunto = StringVar(janela) # Definindo a variável do assunto.

def script(): # Script inteiro.

    webbrowser.open(url)
    time.sleep(2.5)
    pyautogui.PAUSE = 1 # Aqui definimos a URL como o Gmail, usamos o atalho do Webbrowser para abrir o navegador, e definimos o tempo das pausas.

    pyautogui.hotkey("c")
    pyperclip.copy(inputdestinatario.get()) # Aqui usamos o atalho "C" para escrever, e a função Copy para copiar o e-mail do destinatário.

    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab") # Aqui usamos o atalho CTRL + V para colar o e-mail, e o TAB para ir até o assunto.

    pyperclip.copy(inputassunto.get())
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab") # Aqui usamos o atalho Copy novamente para copiar o assunto, o CTRL + V para colar ele, e o TAB novamente para ir para o texto.

    pyperclip.copy(entradaemail.get("1.0", "end-1c"))   
    pyautogui.hotkey("ctrl", "v") # Aqui usamos o atalho Copy novamente para copiar a mensagem e o CTRL + V para colar ela.

    pyautogui.hotkey("ctrl", "enter") # E, por último, usamos o atalho CTRL + ENTER para enviar o e-mail.

executar = CTkButton(janela, text = "Executar o script", command = script, fg_color="midnightblue").place (x = 150, y = 260) # Botão para executar o script.
entradadestinatario = CTkEntry(janela, textvariable = inputdestinatario, width = 150, height = 30).place (x = 100, y = 10) # Caixa de texto do destinatário.
entradaassunto = CTkEntry(janela, textvariable = inputassunto, width = 150, height = 30).place (x = 100, y = 50) # Caixa de texto do assunto.
entradaemail = CTkTextbox(janela, width = 300, height = 150) # Caixa de texto do corpo do e-mail.
entradaemail.place(x = 0, y = 95) # Posicionamento da caixa de texto.

emaildestinatariolabel = CTkLabel(janela, text = "Destinatário:").place (x = 10, y = 10) # Label demarcando aonde é para colocar o destinatário.
assuntolabel = CTkLabel(janela, text = "Assunto:").place (x = 10, y = 50) # Label demarcando aonde é para colocar o assunto.

janela.mainloop() # Impede o programa de encerrar sozinho. 