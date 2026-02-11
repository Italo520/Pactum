
import re

input_file = 'inserts_postgres.sql'
output_file = 'inserts_fixed.sql'

# Table-specific configuration
# key: table name (lowercase as it appears in INSERT INTO generally)
# value: dict with 'quote' (set of cols) and 'rename' (dict of col->new_col)

table_config = {
    'projetos': {
        'quote': {'codProjeto', 'dataInicio', 'dataEncerramento'},
        'rename': {}
    },
    'contrato': {
         'quote': {'numContrato', 'codOrdem', 'tipoPessoa', 'dataInicio', 'dataFim', 'dataParcelaInicial'},
         'rename': {}
    },
    'itens_contrato': {
        'quote': {'numContrato'},
        'rename': {
            'codLancamento': 'cod_lancamento',
            'dataLancamento': 'data_lancamento',
            'numParcela': 'num_parcela',
            'valorParcela': 'valor_parcela',
            'dataVencimento': 'data_vencimento',
            'valorPago': 'valor_pago',
            'dataPagamento': 'data_pagamento'
        }
    },
    'requisicao': {
        'quote': {'codRequisicao', 'codProjeto', 'dataSolicitacao', 'dataLimite'},
        'rename': {}
    },
    'ordem': {
        'quote': {'codOrdem', 'codRequisicao', 'dataSolicitacao', 'dataLimite'},
        'rename': {}
    },
    'itens_ordem': {
        'quote': {'codOrdem'},
        'rename': {
            'codItem': 'cod_item',
            'dataSolicitacao': 'data_solicitacao',
            'dataLimite': 'data_limite',
            'dataRecebido': 'data_recebido'
        }
    }
}

def process_line(line):
    # Match INSERT INTO table (col1, col2, ...) VALUES ...
    match = re.match(r'(INSERT INTO (\w+) \()(.+?)(\) VALUES .+)', line)
    if match:
        prefix = match.group(1)
        table = match.group(2).lower()
        cols_str = match.group(3)
        suffix = match.group(4)
        
        config = table_config.get(table, {'quote': set(), 'rename': {}})
        quote_cols = config['quote']
        rename_cols = config['rename']
        
        # Split by comma and strip whitespace
        cols = [c.strip() for c in cols_str.split(',')]
        new_cols = []
        
        for col in cols:
            if col in rename_cols:
                new_cols.append(rename_cols[col])
            elif col in quote_cols:
                new_cols.append(f'"{col}"')
            else:
                new_cols.append(col)
        
        new_cols_str = ', '.join(new_cols)
        return f"{prefix}{new_cols_str}{suffix}\n"
    return line

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        fout.write(process_line(line))

print(f"Processed {input_file} to {output_file}")
