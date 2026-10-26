# backend/sales/management/commands/runmcp.py
from django.core.management.base import BaseCommand
import uvicorn

# Importante: O caminho de importação depende da sua estrutura de projeto.
# Como 'services' está no mesmo nível que 'backend', precisamos ajustar o sys.path
# ou garantir que o diretório raiz esteja no PYTHONPATH.
# Uma forma mais simples é mover o diretório 'services' para dentro de 'backend'.
# Assumindo que você moveu 'services' para 'backend/services':
from services.mcp_finance import mcp

class Command(BaseCommand):
    help = 'Inicia o servidor MCP com o ambiente Django carregado'

    def add_arguments(self, parser):
        parser.add_argument('--host', type=str, default='0.0.0.0', help='Host para o servidor')
        parser.add_argument('--port', type=int, default=8000, help='Porta para o servidor')

    def handle(self, *args, **options):
        host = options['host']
        port = options['port']

        self.stdout.write(self.style.SUCCESS(f'Iniciando servidor MCP em http://{host}:{port}'))

        # Como este é um comando Django, o ambiente já está configurado.
        # As importações de modelos em mcp_finance.py funcionarão.
        uvicorn.run(mcp, host=host, port=port)

