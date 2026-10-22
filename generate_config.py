import json
import os
import re
from pathlib import Path

slug = os.environ.get(
    "CONFIG_SLUG",
    "example-panorama"
)

if not re.fullmatch(r"[a-z0-9-]{1,100}", slug):
    raise ValueError("Invalid config slug")

config = {
    "autoLoad": True,
    "pitch": 0,
    "yaw": 0,
    "type": "equirectangular",
    "panorama": "https://pannellum.org/images/alma.jpg",
    "hotSpots": []
}

output = Path("configs") / f"{slug}.json"
output.parent.mkdir(parents=True, exist_ok=True)

output.write_text(
    json.dumps(config, indent=2) + "\n",
    encoding="utf-8"
)

print(f"Generated: {output}")
