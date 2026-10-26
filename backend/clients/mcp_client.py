import httpx
from pprint import pprint
import sys

# URL base do servidor MCP que está rodando via 'make runmcp'
BASE_URL = "http://localhost:8000"

def call_tool(tool_name: str, args: dict = None):
    """
    Função genérica para chamar uma ferramenta no servidor MCP.

    Args:
        tool_name: O nome da ferramenta a ser chamada.
        args: Um dicionário com os argumentos para a ferramenta.
    """
    url = f"{BASE_URL}/sse"
    
    # Constrói o corpo da requisição no formato esperado pelo endpoint /sse
    json_body = {
        "tool": tool_name,
        "arguments": args or {}
    }

    try:
        with httpx.Client() as client:
            print(f"--- Chamando ferramenta: {tool_name} com args: {json_body} ---")
            # O cliente MCP espera uma resposta SSE, mas para chamadas de ferramenta simples, uma resposta JSON funciona.
            response = client.post(url, json=json_body, timeout=10)
            
            # Lança um erro para respostas 4xx ou 5xx
            response.raise_for_status()
            
            result = response.json()
            pprint(result)
            return result

    except httpx.ConnectError:
        print(f"\n[ERRO] Não foi possível conectar ao servidor em {BASE_URL}.", file=sys.stderr)
        print("Você iniciou o servidor com 'make runmcp'?", file=sys.stderr)
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"\n[ERRO] O servidor retornou um erro: {e.response.status_code}", file=sys.stderr)
        print("Detalhes:", e.response.text, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    """
    Bloco principal para executar os testes do cliente.
    Rode este script com: python backend/clients/mcp_client.py
    """
    
    # 1. Testar ferramenta sem argumentos
    call_tool("get_total_sales_revenue")

    print("\n" + "="*50 + "\n")

    # 2. Testar outra ferramenta sem argumentos
    call_tool("get_sales_summary_by_dealership")

    print("\n" + "="*50 + "\n")

    # 3. Testar outra ferramenta sem argumentos
    call_tool("get_sales_summary_by_salespeople")

    print("\n" + "="*50 + "\n")

    # 4. Testar ferramenta com argumentos
    # Supondo que exista um vendedor com ID = 1
    commission_args = {
        "salespeople_id": 1,
        "commission_rate": 0.05  # Testando com uma taxa de 5%
    }
    call_tool("calculate_salespeople_commission", args=commission_args)

    print("\n" + "="*50 + "\n")

    # 5. Testar ferramenta com ID de vendedor que pode não existir
    commission_args_invalid = {
        "salespeople_id": 999,
        "commission_rate": 0.02
    }
    call_tool("calculate_salespeople_commission", args=commission_args_invalid)