import requests
from shopify import Product
from error_handler import enviar_email_erro

LINX_API_URL = "http://webapi.microvix.com.br/1.0/api/integracao"
LINX_API_KEY = "b94bea24-fd12-4270-8693-784d0e150891"

def sincronizar_imagens_linx_para_shopify():
    """
    Sincroniza imagens do Linx para o Shopify.
    """
    try:
        response = requests.post(f"{LINX_API_URL}/LinxProdutosImagens", json={"chave": LINX_API_KEY})
        if response.status_code == 200:
            imagens = response.json()
            for imagem in imagens:
                produto_shopify = Product.find(imagem["id_produto_shopify"])
                produto_shopify.images = [{"src": imagem["url"]}]
                produto_shopify.save()
                print(f"Imagem sincronizada para o produto {imagem['id_produto_shopify']}")
        else:
            enviar_email_erro(f"Erro ao buscar imagens no Linx: {response.text}")
    except Exception as e:
        enviar_email_erro(f"Erro ao sincronizar imagens: {str(e)}")