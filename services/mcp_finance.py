from decimal import Decimal
from django.db.models import Sum, Count, F

# Supondo que fastmcp seja uma biblioteca para cálculos financeiros rápidos.
# Como não tenho o código-fonte dela, vou simular seu uso.
# import fastmcp
from mcp.server.fastmcp import FastMCP

from backend.sales.models import Sale
from backend.salespeople.models import Salespeople

mcp = FastMCP("AssistenteFinanceiro")


class MCPFinance:
    """
    Serviço para controle financeiro e cálculos de vendas da MCP.
    """

    @mcp.tool()
    def get_total_sales_revenue(self):
        """
        Calcula a receita total de todas as vendas.
        """
        total_revenue = Sale.objects.aggregate(total=Sum('sale_price'))['total']
        return total_revenue or Decimal('0.00')
    
    @mcp.tool()
    def get_sales_summary_by_salespeople(self):
        """
        Retorna um resumo de vendas por vendedor, incluindo o número de vendas
        e o valor total vendido.
        """
        summary = Salespeople.objects.annotate(
            number_of_sales=Count('sale'),
            total_sold=Sum('sale__sale_price')
        ).values(
            'id',
            'name',
            'number_of_sales',
            'total_sold'
        ).order_by('-total_sold')

        return list(summary)

    @mcp.tool()
    def get_sales_summary_by_dealership(self):
        """
        Retorna um resumo de vendas por concessionária.
        """
        summary = Sale.objects.values(
            'dealership__id', 'dealership__name'
        ).annotate(
            number_of_sales=Count('id'),
            total_sold=Sum('sale_price')
        ).values(
            'dealership__id',
            'dealership__name',
            'number_of_sales',
            'total_sold'
        ).order_by('-total_sold')

        return list(summary)

    @mcp.tool()
    def calculate_salespeople_commission(self, salespeople_id: int, commission_rate: float = 0.02):
        """
        Calcula a comissão para um vendedor específico usando a biblioteca fastmcp.
        """
        salespeople_sales = Sale.objects.filter(salespeople_id=salespeople_id)
        
        if not salespeople_sales.exists():
            return Decimal('0.00')

        total_sold = salespeople_sales.aggregate(total=Sum('sale_price'))['total']

        # Utilizando a biblioteca fastmcp para o cálculo da comissão
        commission = FastMCP.calculate_commission(total_sold, commission_rate)
        
        return commission