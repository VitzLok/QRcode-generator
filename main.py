import qrcode
import validators
import requests

# Função para verificar se o site é acessível
def website_acessivel(url):
    if not validators.url(url):
        return False
    try:
        # Verificar se o site responde com status 200
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Loop para validar o link e gerar o QR Code
while True:
    link = input("Cole aqui seu link de site: ")
    if website_acessivel(link):
        print("Site válido. Gerando QRcode...")
        img = qrcode.make(link) 
        img.save("qrcode.png")  
        print("QR Code gerado com sucesso e salvo como 'qrcode.png'!")
        break
    else:
        print("Site inválido. Tente novamente com um link acessível.")
