from decimal import Decimal
from django.db.models import Sum, Count, F
from mcp.server.fastmcp import FastMCP

from sales.models import Sale
from salespeople.models import Salespeople

mcp = FastMCP("AssistenteFinanceiroDjango")

@mcp.tool()
def get_total_sales_revenue() -> Decimal:
    """
    Calcula a receita total de todas as vendas.
    """
    total_revenue = Sale.objects.aggregate(total=Sum('sale_price'))['total']
    return total_revenue or Decimal('0.00')

@mcp.tool()
def get_sales_summary_by_salespeople() -> list:
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

    # Converte Decimals para strings para garantir a serialização JSON
    for item in summary:
        if item['total_sold'] is not None:
            item['total_sold'] = str(item['total_sold'])

    return list(summary)

@mcp.tool()
def get_sales_summary_by_dealership() -> list:
    """
    Retorna um resumo de vendas por concessionária.
    """
    summary = Sale.objects.values(
        'dealership__id', 'dealership__name'
    ).annotate(
        number_of_sales=Count('id'),
        total_sold=Sum('sale_price')
    ).order_by('-total_sold')

    # Converte Decimals para strings
    for item in summary:
        if item['total_sold'] is not None:
            item['total_sold'] = str(item['total_sold'])

    return list(summary)

# A função de comissão parecia ter uma chamada a um método que não existe em FastMCP.
# Removi por enquanto para evitar erros. Se precisar dela, podemos reimplementar.