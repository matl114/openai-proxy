# config.py

import os 
from dotenv import load_dotenv

load_dotenv()
UPSTREAM_BASE_URL = os.getenv("UPSTREAM_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")

proxied_hosts_config = {"" : UPSTREAM_BASE_URL}

print(f"Load host mapping : {proxied_hosts_config}")

proxied_model_name_mapping = {}

MODEL_MAPPING=os.getenv("MODEL_MAPPING")

if MODEL_MAPPING:
    for pair in MODEL_MAPPING.split(","):
        if '=' in pair:
            client, real = pair.split("=", 1)
            proxied_model_name_mapping[client] = real


print(f"Load model name mapping : {proxied_model_name_mapping}")

service_port = int(os.getenv('PROXY_SERVICE_PORT', "9191"))

auto_reload = os.getenv("PROXY_SERVICE_AUTORELOAD", "False") == "True"