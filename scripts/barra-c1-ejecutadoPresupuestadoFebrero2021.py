import plotly.graph_objects as go
import plotly.io as pio


fig = go.Figure()
ejeXr = [
'Servicios técnicos y profesionales',
'Adq. De Eq. De Ofic y Computación'
]
"""
ejeXs = [
'Serv. Consultoria Individual',
'Equipos de Computación'
]
"""
presupuestado = [1598125, 2216059]
ejecutado = [7612,630543]

tituloText = "Agenda Digital Componente I (Febrero 2019-2021)"
tituloY = "Dolares Americanos (US$)"
tituloX = "Componentes"
titleSize = 24
ejeSize = 14
fontRockwell = dict(
            family="Rockwell", 
            size=titleSize,
            color="black"
        )
fontEjeRockwell = dict(
            family="Rockwell", 
            size=ejeSize,
            color="black"
        )

fig.add_trace(go.Bar(x=ejeXr, y=presupuestado, name='Presupuestado'))
fig.add_trace(go.Bar(x=ejeXr, y=ejecutado, name='Ejecutado'))

fig.update_layout(title=go.layout.Title(text = tituloText, font= fontRockwell))
fig.update_layout(xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=tituloX, font= fontEjeRockwell)))
fig.update_layout(yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=tituloY, font= fontEjeRockwell)))

#fig['layout']['xaxis'].update(side='top')

fig.show()

pio.write_html(fig, file='../_includes/plotly-barra-ci-ejecutadoFebrero2021.html', auto_open=True)
