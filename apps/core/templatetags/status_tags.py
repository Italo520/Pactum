from django import template

register = template.Library()

@register.filter
def get_status_badge(status_code, tipo='padrao'):
    """
    Retorna a classe CSS do badge baseada no código de status.
    Args:
        status_code: O código do status (1, 2, etc)
        tipo: O tipo de objeto ('padrao' para projeto/contrato, 'requisicao' para requisição)
    """
    status_code = str(status_code)
    
    if tipo == 'requisicao':
        # Mapeamento para Requisição
        # 1: Aguardando Início (Info)
        # 2: Em andamento (Primary)
        # 3: Suspensa (Warning)
        # 4: Cancelada (Danger)
        # 5: Concluída (Success)
        mapping = {
            '1': 'badge-info',
            '2': 'badge-primary',
            '3': 'badge-warning',
            '4': 'badge-danger',
            '5': 'badge-success',
        }
    else:
        # Mapeamento padrão (Projetos e Contratos)
        # 1: Aguardando Início / Pendente
        # 2: Em andamento / Ativo
        # 3: Paralisado
        # 4: Suspenso
        # 5: Cancelado
        # 6: Concluído
        mapping = {
            '1': 'badge-info',      # Aguardando
            '2': 'badge-primary',   # Em andamento
            '3': 'badge-warning',   # Paralisado
            '4': 'badge-warning',   # Suspenso
            '5': 'badge-danger',    # Cancelado
            '6': 'badge-success',   # Concluído
        }
    
    return mapping.get(status_code, 'badge-secondary')
