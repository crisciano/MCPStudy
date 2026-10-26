import requests
import json

# Assumindo que seu servidor Django está rodando em localhost:8000
# e o django-mcp está configurado no endpoint padrão '/mcp/'.
# Altere se sua configuração for diferente.
MCP_ENDPOINT = "http://127.0.0.1:8025/mcp/"

def call_tool(tool_name: str, *args, **kwargs):
    """
    Chama uma 'tool' no servidor MCP.
    """
    payload = {
        "tool": tool_name,
        "args": args,
        "kwargs": kwargs,
    }
    print(f"-> Chamando tool '{tool_name}' com payload: {json.dumps(payload)}")
    try:
        response = requests.post(MCP_ENDPOINT, json=payload)
        response.raise_for_status()  # Lança exceção para status de erro (4xx ou 5xx)
        result = response.json()
        print(f"<- Resposta: {result}\n")
        return result
    except requests.exceptions.RequestException as e:
        print(f"!! Erro ao chamar a tool: {e}\n")
        return None

def get_resource(resource_uri: str):
    """
    Resolve um 'resource' no servidor MCP.
    """
    payload = {"resource": resource_uri}
    print(f"-> Resolvendo resource '{resource_uri}'")
    try:
        response = requests.post(MCP_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json()
        print(f"<- Resposta: {result}\n")
        return result
    except requests.exceptions.RequestException as e:
        print(f"!! Erro ao resolver o resource: {e}\n")
        return None

if __name__ == "__main__":
    print("--- Iniciando cliente MCP ---\n")

    # 1. Chamando a tool 'add'
    call_tool("add", a=5, b=10)

    # 2. Resolvendo o resource 'greeting'
    get_resource("greeting://Mundo")
    get_resource("greeting://Gemini")