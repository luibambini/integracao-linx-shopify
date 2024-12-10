import requests
from shopify import Product
from error_handler import enviar_email_erro

LINX_API_URL = "http://webapi.microvix.com.br/1.0/api/integracao"
LINX_API_KEY = "b94bea24-fd12-4270-8693-784d0e150891"
SHOPIFY_STORE_URL = "https://luibambini-9396.myshopify.com"
SHOPIFY_API_KEY = "b9e7513997763cf4ff17cce636b8a175"

def atualizar_estoque_linx_para_shopify(estoque):
    """
    Atualiza o estoque no Shopify com base nos dados do Linx.
    """
    try:
        for item in estoque:
            produto_shopify = Product.find(item["id_produto_shopify"])
            produto_shopify.variants[0].inventory_quantity = item["quantidade"]
            produto_shopify.save()
            print(f"Estoque atualizado no Shopify: {item['nome']} ({item['quantidade']})")
    except Exception as e:
        enviar_email_erro(f"Erro ao atualizar estoque: {str(e)}")