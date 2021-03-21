import plotly.graph_objects as go
import plotly.io as pio


fig = go.Figure()
"""
subRubros = ['I Serv. Consultoria Individual','I Equipos de Computación','II Honorarios Profesionales',
'II Serv. Consultoria Individual','III Serv. Consultoria Individual','III Serv. Comunicaciones',
'IV Honorarios Profesionales','V Energía Elécttrica','V Alquileres de Edif y Locales',
'V Honorarios Profesionales']
subRubrosValue = [7612,630543,5373,6010,2388,480597,64856,1844,76250,287207]

rubros=['I Servicios técnicos y profesionales','I Adq. De Eq. De Ofic y Computación','II Personal Contratado',
'II Servicios técnicos y profesionales','III Servicios técnicos y profesionales','IV Personal Contratado',
'V Servicios Básicos','V Alquileres y Derechos','V Personal Contratado']

rubrosValue=[7612,630543,5373,6010,482985,64856,1844,76250,287207]
"""
rubros = ['Ir Servicios técnicos y profesionales','Is Serv. Consultoria Individual','Ir Adq. De Eq. De Ofic y Computación','Is Equipos de Computación',
'IIr Personal Contratado','IIs Honorarios Profesionales','IIr Servicios técnicos y profesionales','IIs Serv. Consultoria Individual',
'IIrI Servicios técnicos y profesionales','IIIs Serv. Consultoria Individual','IIIs Serv. Comunicaciones','IVr Personal Contratado',
'IVs Honorarios Profesionales','Vr Servicios Básicos','Vs Energía Elécttrica','Vr Alquileres y Derechos',
'Vs Alquileres de Edif y Locales','Vr Personal Contratado','Vs Honorarios Profesionales']

rubrosValue=[7612,7612,630543,630543,5373,5373,6010,6010,482985,2388,480597,
64856,64856,1844,1844,76250,76250,287207,287207]

tituloText = "Agenda Digital Ejecutado Detalle (Febrero 2021)"
tituloY = "Dolares Americanos (US$)"
tituloX = "Rubros"
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

#fig.add_trace(go.Bar(x=subRubros, y=subRubrosValue))
fig.add_trace(go.Bar(x=rubros, y=rubrosValue))

fig.update_layout(title=go.layout.Title(text = tituloText, font= fontRockwell))
fig.update_layout(xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=tituloX, font= fontEjeRockwell)))
fig.update_layout(yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=tituloY, font= fontEjeRockwell)))

#fig['layout']['xaxis'].update(side='top')

fig.show()

pio.write_html(fig, file='../_includes/plotly-barraEjecutadoDetalleFebrero2021.html', auto_open=True)
