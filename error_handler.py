import smtplib
from email.mime.text import MIMEText

def enviar_email_erro(mensagem):
    """
    Envia um e-mail com o erro detectado.
    """
    remetente = "seuemail@gmail.com"
    destinatario = "evozago@gmail.com"
    senha = "SUA_SENHA"

    msg = MIMEText(f"Erro detectado: {mensagem}")
    msg["Subject"] = "Erro na Integração Shopify-Linx"
    msg["From"] = remetente
    msg["To"] = destinatario

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("E-mail de erro enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")