#!/bin/bash

curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d @ask_request.json
