import plotly.graph_objects as go
import plotly.io as pio

tituloText = "Agenda Digital"
tituloY = "Dolares Americanos (US$)"
tituloX = "Componentes"
ejeX = ['e-Gob','Empresarial','Infraestructura','Organización','Administración']
ejeY = [32600000, 29600000, 47900000, 13400000, 6500000]
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

fig = go.Figure()

fig.add_trace(go.Pie(labels=ejeX, values=ejeY))

fig.update_layout(title=go.layout.Title(text = tituloText, font= fontRockwell))

fig.show()

pio.write_html(fig, file='../_includes/plotly-tortaTotal.html', auto_open=True)
