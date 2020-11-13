import sys
import yaml

from treasure_map.app import create_app


config = yaml.safe_load(open("config.yml"))

app = create_app(config)

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
