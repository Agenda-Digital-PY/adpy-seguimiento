import plotly.graph_objects as go
import plotly.io as pio


fig = go.Figure()
ejeX = ['e-Gob','Empresarial','Infraestructura','Organización','Administración']
ejeY = [638155, 11383, 482985, 64856, 354298]
tituloText = "Agenda Digital Ejecutado (Febrero 2021)"
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

fig.add_trace(go.Bar(x=ejeX, y=ejeY))

fig.update_layout(title=go.layout.Title(text = tituloText, font= fontRockwell))
fig.update_layout(xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=tituloX, font= fontEjeRockwell)))
fig.update_layout(yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=tituloY, font= fontEjeRockwell)))

#fig['layout']['xaxis'].update(side='top')

fig.show()

pio.write_html(fig, file='../_includes/plotly-barraFebrero2021.html', auto_open=True)
