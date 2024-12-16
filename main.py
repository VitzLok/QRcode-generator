import qrcode
import validators
import requests
from tkinter import Tk, Label, Entry, Button, filedialog, Canvas, messagebox
from tkinter.ttk import Style
from PIL import Image, ImageTk

# Verificação do site
def website_acessivel(url):
    if not validators.url(url):
        return False
    try:
        response = requests.get(url, timeout=7)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Gerar QR code
def gerar_qrcode():
    link = entrada_link.get().strip()
    if not website_acessivel(link):
        messagebox.showerror("Erro", "O link inserido não é válido ou acessível.")
        return

    # Selecionar local e nome do arquivo para salvar
    caminho_arquivo = filedialog.asksaveasfilename(
        title="Salvar QR Code como",
        defaultextension=".png",
        filetypes=[("Imagens PNG", "*.png")]
    )
    if not caminho_arquivo:
        messagebox.showinfo("Informação", "Operação cancelada. Nenhum arquivo foi salvo.")
        return

    # Gerar o QR Code
    img = qrcode.make(link)
    img.save(caminho_arquivo)

    # Mostrar o QR Code na interface
    img_pillow = Image.open(caminho_arquivo).resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_pillow)
    canvas_qrcode.create_image(100, 100, image=img_tk)
    canvas_qrcode.image = img_tk

    messagebox.showinfo("Sucesso", f"QR Code gerado e salvo em: {caminho_arquivo}")

# Config da interface
root = Tk()
root.title("Gerador de QR Code")
root.geometry("400x400")
root.resizable(False, False)

# Estilização com ttk
style = Style()
style.configure("TButton", font=("Arial", 10, "bold"))
style.configure("TLabel", font=("Arial", 12))

# Rótulo e entrada para o link
Label(root, text="Insira o link do site:").pack(pady=10)
entrada_link = Entry(root, width=40, font=("Arial", 12))
entrada_link.pack(pady=5)

# Botão para gerar o QR Code
btn_gerar = Button(root, text="Gerar QR Code", command=gerar_qrcode, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_gerar.pack(pady=20)

# Canvas para exibir o QR Code
canvas_qrcode = Canvas(root, width=200, height=200, bg="white", relief="sunken", borderwidth=2)
canvas_qrcode.pack(pady=10)

# Rótulo de instrução
Label(root, text="O QR Code será exibido aqui.").pack(pady=10)

# Loop principal
root.mainloop()

