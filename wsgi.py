import sys

from treasure_map.app import app


if __name__ == "__main__":
    port = int(sys.argv[1])

    remote_config = {
        "db_path": "sqlite:////usr/local/share/treasure/treasure.db",
        "proxy": None,
    }

    local_config = {
        "db_path": "sqlite:///treasure.db",
        "proxy": None,
        "debug": True,
    }

    app = create_app(remote_config)

    if len(sys.argv) > 1:
        local_app = create_app(local_config)
        local_app.run(host='0.0.0.0', port=port)
