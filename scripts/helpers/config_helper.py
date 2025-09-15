<<<<<<< HEAD
import yaml

def load_config(path="config.yaml"):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
=======
import yaml

def load_config(path="config.yaml"):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
>>>>>>> cf7e4c4243711c8621ae31df9ac4a97d9aadf6cb
    return config