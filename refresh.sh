#!/bin/bash
rm -rf dist
npm run build
cp -rd ~/ruri/ ./dist/static/
python3 web.py
