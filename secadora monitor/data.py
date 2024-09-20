from firebase_admin import firestore
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json

db = firestore.client()


def get_latest_temperature():
    docs = db.collection('temperaturas').order_by(
        'timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()
    for doc in docs:
        return doc.to_dict()
    return None


def get_temperature_history():
    docs = db.collection('temperaturas').order_by(
        'timestamp', direction=firestore.Query.DESCENDING).limit(100).stream()
    return [doc.to_dict() for doc in docs]


def generate_insights():
    temp_history = get_temperature_history()

    # Calcular média, máximo e mínimo
    temps = [doc['temperatura'] for doc in temp_history]
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    # Criar gráfico
    trace = go.Scatter(
        x=[doc['timestamp'] for doc in temp_history],
        y=temps,
        mode='lines+markers'
    )
    layout = go.Layout(title='Histórico de Temperatura')
    fig = go.Figure(data=[trace], layout=layout)
    graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    return {
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'graph_json': graph_json
    }
