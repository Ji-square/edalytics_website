"""
edalytics_style.py
══════════════════════════════════════════════════════════════════
Módulo de estilo oficial para notebooks de edalytics.
Importa al inicio de cualquier notebook con:

    from edalytics_style import *

Proporciona: COLORS, BASE_LAYOUT, add_title(), add_source()
══════════════════════════════════════════════════════════════════
"""

import plotly.graph_objects as go

# ── Paleta de colores edalytics ───────────────────────────────────────────────
COLORS = [
    '#2c3e50',  # azul marino    — color principal
    '#e74c3c',  # rojo           — acento / alerta
    '#27ae60',  # verde          — positivo
    '#3498db',  # azul claro     — secundario
    '#e67e22',  # naranja        — terciario
    '#9b59b6',  # púrpura        — cuaternario
]

# ── Layout base reutilizable ──────────────────────────────────────────────────
BASE_LAYOUT = dict(
    font=dict(family='Georgia, serif', size=12, color='#2c3e50'),
    paper_bgcolor='#fafaf8',
    plot_bgcolor='#fafaf8',
    xaxis=dict(
        gridcolor='#e8e8e4',
        gridwidth=0.5,
        linecolor='#2c3e50',
        showgrid=False,
        tickfont=dict(color='#2c3e50')
    ),
    yaxis=dict(
        gridcolor='#e8e8e4',
        gridwidth=0.8,
        linecolor='#2c3e50',
        tickfont=dict(color='#2c3e50'),
        zeroline=True,
        zerolinecolor='#2c3e50',
        zerolinewidth=1
    ),
    legend=dict(
        bgcolor='#fafaf8',
        bordercolor='#e8e8e4',
        borderwidth=1,
        font=dict(color='#2c3e50')
    ),
    margin=dict(t=110, b=60)
)


def add_title(fig, title: str, subtitle: str = '') -> None:
    """
    Añade título y subtítulo al gráfico con línea de firma edalytics.

    Uso:
        add_title(fig, 'Mi título', 'Subtítulo opcional | Fuente')

    Parámetros:
        fig      : figura Plotly
        title    : título principal (sin etiquetas HTML)
        subtitle : subtítulo en gris (período, unidades, fuente)
    """
    fig.add_annotation(
        text=f'<b>{title}</b>',
        xref='paper', yref='paper',
        x=0, y=1.15,
        showarrow=False,
        font=dict(size=15, color='#2c3e50', family='Georgia, serif'),
        align='left'
    )
    if subtitle:
        fig.add_annotation(
            text=subtitle,
            xref='paper', yref='paper',
            x=0, y=1.08,
            showarrow=False,
            font=dict(size=11, color='#888888', family='Georgia, serif'),
            align='left'
        )
    # Línea de firma debajo del título — sello visual edalytics
    fig.add_shape(
        type='line',
        xref='paper', yref='paper',
        x0=0, x1=0.45, y0=1.03, y1=1.03,
        line=dict(color='#2c3e50', width=2)
    )


def add_source(fig, source: str = 'edalytics.com') -> None:
    """
    Añade nota de fuente en la parte inferior izquierda del gráfico.

    Uso:
        add_source(fig, 'World Bank WDI | Estimación propia')
        add_source(fig)  # usa 'edalytics.com' por defecto

    Parámetros:
        fig    : figura Plotly
        source : texto de la fuente
    """
    fig.add_annotation(
        text=f'Fuente: {source}',
        xref='paper', yref='paper',
        x=-1, y=-0.12,
        showarrow=False,
        font=dict(size=10, color='#888888', family='Georgia, serif'),
        align='left'
    )


# ── Ejemplo de uso ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    # Gráfico de ejemplo
    fig = go.Figure()
    x = list(range(2010, 2024))
    for i, name in enumerate(['País A', 'País B', 'País C']):
        fig.add_trace(go.Scatter(
            x=x,
            y=np.random.randn(14).cumsum() + 5,
            name=name,
            mode='lines',
            line=dict(color=COLORS[i], width=2)
        ))

    fig.update_layout(**BASE_LAYOUT, title=None)
    add_title(fig, 'Ejemplo de gráfico edalytics', '2010–2023 | Datos simulados')
    add_source(fig, 'Fuente simulada | edalytics.com')
    fig.show()
    print("edalytics_style cargado correctamente ✓")
