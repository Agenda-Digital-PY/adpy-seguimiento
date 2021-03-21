import plotly.graph_objects as go
import plotly.io as pio


fig = go.Figure()
ejeXr = [
'Servicios Básicos',
'Alquileres y Derechos',
'Personal Contratado'
]
"""
ejeXs = [
'Serv. Consultoria Individual',
'Equipos de Computación'
]
"""
presupuestado = [41973, 89676, 936113]
ejecutado = [1844,76250,287207]

tituloText = "Agenda Digital Componente V (Febrero 2019-2021)"
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

pio.write_html(fig, file='../_includes/plotly-barra-cv-ejecutadoFebrero2021.html', auto_open=True)
