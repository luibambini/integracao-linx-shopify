from flask import Flask, request, jsonify
from sync_orders import criar_pedido_no_linx
from sync_inventory import atualizar_estoque_linx_para_shopify
from error_handler import enviar_email_erro

app = Flask(__name__)

@app.route('/webhook/orders', methods=['POST'])
def webhook_orders():
    try:
        pedido = request.json
        criar_pedido_no_linx(pedido)
        return jsonify({"status": "sucesso"}), 200
    except Exception as e:
        enviar_email_erro(f"Erro no Webhook de Pedidos: {str(e)}")
        return jsonify({"status": "erro"}), 500

@app.route('/webhook/estoque', methods=['POST'])
def webhook_estoque():
    try:
        estoque = request.json
        atualizar_estoque_linx_para_shopify(estoque)
        return jsonify({"status": "sucesso"}), 200
    except Exception as e:
        enviar_email_erro(f"Erro no Webhook de Estoque: {str(e)}")
        return jsonify({"status": "erro"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)