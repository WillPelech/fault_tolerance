import os 
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config"/ "cluster.yaml"
ENV_PATH =BASE_DIR /"docker"/".env"
def create_env(file_path = ".env"):
    with open(CONFIG_PATH,'r') as file:
        config_data = yaml.safe_load(file)
    if not config_data:
        raise ValueError("cluster.yaml is mapping to None type")

    lines = []
    lines.append(f"PROJECT_NAME={config_data['project']['name']}")
    pg = config_data['postgres']
    lines.append(f"PG_USER={pg['user']}")
    lines.append(f"PG_PASSWORD={pg['password']}")
    lines.append(f"PG_DB={pg['database']}")

    for node in config_data["nodes"]:
        node_id = node["id"]
        port = node["port"]
        lines.append(f"NODE{(node_id)}_PORT={(port)}")
    print("made it here")
    print(lines)
    print(ENV_PATH)
    ENV_PATH.write_text("\n".join(lines)+"\n")

def main():
    create_env()
if __name__ == "__main__":
    main()
    
