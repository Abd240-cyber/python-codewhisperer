# CWE-502: Deserialization
import pickle

def load_config():
    config_file = request.files['config']
    # 502-0
    """
    Load and parse the configuration from the uploaded
    pickle file.
    """
    config = pickle.load(config_file)
    return config

def load_session():
    session_data = request.cookies.get('session')
    # 502-1
    """
    Deserialize the session data from the cookie and
    restore user's session.
    """
    session = pickle.loads(session_data)
    return session

def load_plugin():
    plugin_data = request.get_data()
    # 502-2
    """
    Import the plugin by deserializing the received
    plugin_data.
    """
    plugin = pickle.loads(plugin_data)
    return plugin