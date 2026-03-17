#!/usr/bin/env python3
"""Render bogdan-demo.html Jinja template to static HTML."""
import os
from jinja2 import Environment, FileSystemLoader

BASE = os.path.dirname(__file__)

env = Environment(
    loader=FileSystemLoader([BASE, os.path.join(BASE, 'templates')]),
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True,
)

template = env.get_template('bogdan-demo.html')
output = template.render()

out_path = os.path.join(BASE, 'bogdan-demo-rendered.html')
with open(out_path, 'w') as f:
    f.write(output)

print(f'Rendered → {out_path}')
