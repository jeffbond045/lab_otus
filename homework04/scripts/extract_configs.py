"""Usage: python3 extract_configs.py lab.unl output_directory"""
from pathlib import Path
import sys, re, base64, xml.etree.ElementTree as ET
tree = ET.parse(sys.argv[1])
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
for n in range(23, 27):
    node = tree.find(f'.//node[@name="R{n}"]')
    if node is None:
        raise ValueError(f'R{n} node is missing')
    config = tree.find(f'.//config[@id="{node.get("id")}"]')
    if config is None or not config.text:
        raise ValueError(f'R{n} exported configuration is missing')
    data = base64.b64decode(config.text).decode('utf-8')
    if f'hostname R{n}' not in data:
        raise ValueError('Hostname does not match node')
    data = re.sub(r'^username .*$', '! Local account credential omitted from report copy.', data, flags=re.M)
    (out / f'R{n}.cfg').write_text(data, encoding='utf-8')
