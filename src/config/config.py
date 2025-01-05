from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "openai": {
        "api_key": os.getenv("OPENAI_KEY")
    },
    "kafka": {
        "sasl.username": os.getenv("KAFKA_CLUSTER_API_KEY"),
        "sasl.password": os.getenv("KAFKA_CLUSTER_API_SECRET"),
        "bootstrap.servers": os.getenv("KAFKA_CLUSTER_BOOTSTRAP_SERVER_URL"),
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 50000
    },
    "schema_registry": {
        "url": os.getenv("SCHEMA_REGISTRY_URL"),
        "basic.auth.user.info": f"{os.getenv('SR_API_KEY')}:{os.getenv('SR_API_SECRET')}"
    }
}
