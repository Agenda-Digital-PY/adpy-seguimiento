import plotly.graph_objects as go

labels = ['e-Gob','Empresarial','Infraestructura','Organización','Adminsitración']
values = [638155, 11383, 482985, 64856, 354298]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
import plotly.io as pio

pio.write_html(fig, file='ejecutadoAcumuladoFebrero2021.html', auto_open=True)
