def setup_plutoserver(port):
    return {
        "command": ["
            julia", "-e", 
            f"import Pluto; Pluto.run(host=\"0.0.0.0\", port={port}, launch_browser=false, require_token_for_open_links=false)"
        ],
        "timeout": 60,
        "launcher_entry": {
            "title": "Pluto.jl",
        },
    }
    