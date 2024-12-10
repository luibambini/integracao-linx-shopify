import requests
from error_handler import enviar_email_erro

LINX_API_URL = "http://webapi.microvix.com.br/1.0/api/integracao"
LINX_API_KEY = "b94bea24-fd12-4270-8693-784d0e150891"

def criar_pedido_no_linx(pedido):
    """
    Cria um pedido no Linx com base no pedido recebido do Shopify.
    """
    try:
        payload = {
            "chave": LINX_API_KEY,
            "pedido": {
                "id": pedido["id"],
                "cliente": pedido["customer"]["email"],
                "produtos": [
                    {"codigo": item["sku"], "quantidade": item["quantity"], "valor_unitario": item["price"]}
                    for item in pedido["line_items"]
                ],
                "status": "Aberto"
            }
        }
        response = requests.post(f"{LINX_API_URL}/LinxPedidosVenda", json=payload)
        if response.status_code == 200:
            print(f"Pedido {pedido['id']} criado no Linx com sucesso.")
        else:
            enviar_email_erro(f"Erro ao criar pedido no Linx: {response.text}")
    except Exception as e:
        enviar_email_erro(f"Erro ao criar pedido no Linx: {str(e)}")