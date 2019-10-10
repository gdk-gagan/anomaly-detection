from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the Anomaly_Detection_Facilities_Panel.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "Anomaly_Detection_Facilities_Panel.ipynb", "--allow-websocket-origin=*"])
