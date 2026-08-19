"""
new_notebook.py
══════════════════════════════════════════════════════════════════
Script para crear un nuevo notebook edalytics con plantilla oficial.

Uso:
    python3 new_notebook.py <nombre_del_post> [carpeta_destino]

Ejemplos:
    python3 new_notebook.py inflacion_spain
    python3 new_notebook.py inflacion_spain posts/
══════════════════════════════════════════════════════════════════
"""

import json
import os
import sys


def create_notebook(name: str, base_path: str = 'posts') -> str:
    post_dir = os.path.join(base_path, name)
    notebook_path = os.path.join(post_dir, f'{name}.ipynb')
    os.makedirs(post_dir, exist_ok=True)

    if os.path.exists(notebook_path):
        print(f'⚠️  Ya existe: {notebook_path}')
        overwrite = input('¿Sobreescribir? (s/n): ').strip().lower()
        if overwrite != 's':
            print('Cancelado.')
            sys.exit(0)

    yaml = "\n".join([
        "---",
        f'title: "{name.replace("_", " ").title()}"',
        "author:",
        "  - name: Eduard Romero",
        "    url: https://ji-square.github.io/edalytics_website/",
        "    affiliation: edalytics",
        "    affiliation-url: https://ji-square.github.io/edalytics_website/",
        "    attributes:",
        "      corresponding: true",
        "    degrees:",
        "      - MSc Data Analysis, London Metropolitan University",
        "      - Máster en Economía, En curso",
        "date: today",
        'date-format: "MMMM D, YYYY"',
        "image: thumbnails.jpg",
        'description: "Descripción breve del análisis para la página de blog."',
        "categories:",
        "  - Python",
        "format:",
        "  html:",
        "    toc: true",
        "    toc-depth: 3",
        "    toc-location: left",
        "    theme: cosmo",
        "    code-fold: true",
        "    code-tools: true",
        "    fig-width: 9",
        "    fig-height: 5",
        "    number-sections: true",
        "    margin-header: |",
        '      <div style="',
        "        position: sticky;",
        "        top: 20px;",
        "        text-align: center;",
        "        padding: 1rem;",
        "        border: none;",
        "        border-radius: 4px;",
        "        background: #fafaf8;",
        '      ">',
        '        <img src="thumbnails.jpg" style="',
        "          width: 80px;",
        "          height: 80px;",
        "          border-radius: 50%;",
        "          object-fit: cover;",
        "          border: 2px solid #fafaf8;",
        "          display: block;",
        "          margin: 0 auto 0.5rem;",
        '        ">',
        "        <strong>Eduard Romero</strong><br>",
        "        <small>Economista aplicado</small><br>",
        "        <small>edalytics</small><br><br>",
        '        <a href="https://x.com/edalytics_" style="margin:2px">🐦</a>',
        '        <a href="https://www.linkedin.com/in/eduard-de-jesus-romero-mercedes-580753125/" style="margin:2px">💼</a>',
        '        <a href="https://github.com/ji-square" style="margin:2px">🐙</a>',
        "      </div>",
        "execute:",
        "  echo: true",
        "  eval: false",
        "  warning: false",
        "  message: false",
        "---"
    ])

    imports = "\n".join([
        "import sys",
        'sys.path.insert(0, "../../")',
        "from edalytics_style import *",
        'print("Estilo cargado ✓")'
    ])

    test_data = "\n".join([
        "import numpy as np",
        "import pandas as pd",
        "",
        "np.random.seed(42)",
        "years = list(range(2010, 2024))",
        "",
        "df_test = pd.DataFrame({",
        "    'year'  : years,",
        "    'País A': np.random.randn(14).cumsum() + 10,",
        "    'País B': np.random.randn(14).cumsum() + 8,",
        "    'País C': np.random.randn(14).cumsum() + 6,",
        "})",
        "",
        "df_test.round(2)"
    ])

    test_plot = "\n".join([
        "fig = go.Figure()",
        "",
        "for i, country in enumerate(['País A', 'País B', 'País C']):",
        "    fig.add_trace(go.Scatter(",
        "        x=df_test['year'],",
        "        y=df_test[country],",
        "        name=country,",
        "        mode='lines',",
        "        line=dict(color=COLORS[i], width=2)",
        "    ))",
        "",
        "fig.update_layout(**BASE_LAYOUT, title=None)",
        "fig.update_yaxes(ticksuffix='%')",
        "add_title(fig, 'Gráfico de prueba edalytics', '2010–2023 | Datos simulados')",
        "add_source(fig, 'Datos simulados | edalytics.com')",
        "fig.show()"
    ])

    workflow = "\n".join([
        "---",
        "",
        "> **Flujo de publicación edalytics**",
        ">",
        "> 1. Desarrolla el análisis en Positron",
        "> 2. Ejecuta y guarda outputs desde la raíz del proyecto:",
        ">",
        "> ```bash",
        f"> jupyter nbconvert --to notebook --execute --inplace posts/{name}/{name}.ipynb",
        "> ```",
        ">",
        "> 3. `quarto preview` para verificar",
        "> 4. `quarto publish` para publicar"
    ])

    nb = {
        'cells': [
            {'cell_type': 'raw',     'id': 'yaml-header',       'metadata': {}, 'source': [yaml]},
            {'cell_type': 'markdown','id': 'intro',             'metadata': {}, 'source': ['## 1. Resumen\n\nEscribe aquí el resumen ejecutivo del análisis.']},
            {'cell_type': 'markdown','id': 'data-section',      'metadata': {}, 'source': ['## 2. Datos\n\n### 2.1 Fuentes y variables']},
            {'cell_type': 'code',    'id': 'imports',           'metadata': {}, 'outputs': [], 'execution_count': None, 'source': [imports]},
            {'cell_type': 'markdown','id': 'test-md',           'metadata': {}, 'source': ['### 2.2 Test de estilo\n\n> **Elimina esta sección** cuando empieces el análisis real.']},
            {'cell_type': 'code',    'id': 'test-data',         'metadata': {}, 'outputs': [], 'execution_count': None, 'source': [test_data]},
            {'cell_type': 'code',    'id': 'test-plot',         'metadata': {}, 'outputs': [], 'execution_count': None, 'source': [test_plot]},
            {'cell_type': 'markdown','id': 'workflow-reminder', 'metadata': {}, 'source': [workflow]},
        ],
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.12.0'}
        },
        'nbformat': 4,
        'nbformat_minor': 5
    }

    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return notebook_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        print('Error: debes especificar el nombre del post.')
        print('Ejemplo: python3 new_notebook.py inflacion_spain')
        sys.exit(1)

    name = sys.argv[1].strip().lower().replace(' ', '_').replace('-', '_')
    base = sys.argv[2] if len(sys.argv) > 2 else 'posts'

    path = create_notebook(name, base)

    print(f'✓ Notebook creado: {path}')
    print(f'✓ Carpeta:         {os.path.dirname(path)}')
    print()
    print('Próximos pasos:')
    print('  1. Edita título, descripción y categorías en la celda YAML')
    print('  2. Añade thumbnails.jpg a la carpeta del post')
    print('  3. Desarrolla el análisis en Positron')
    print(f'  4. jupyter nbconvert --to notebook --execute --inplace posts/{name}/{name}.ipynb')
    print('  5. quarto preview')
