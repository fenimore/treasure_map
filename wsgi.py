import sys

from treasure_map.app import create_app

remote_config = {
    "db_path": "sqlite:////usr/local/share/treasure/treasure.db",
    "proxy": None,
}

app = create_app(remote_config)


if __name__ == "__main__":
    port = int(sys.argv[1])

    local_config = {
        "db_path": "sqlite:///treasure.db",
        "proxy": None,
        "debug": True,
    }

    local_app = create_app(local_config)
    local_app.run(host='0.0.0.0', port=port)
