# Getting started

Currently not working but should run like

1. `PORT=8421 make serve-dev`
2. `export EIDOLON_API_URL=http://localhost:8421`
3. `export H_PID=$(eidolon-cli processes create --agent HelloWorld)`
4. `eidolon-cli actions converse --process-id $H_PID --body "Hi! I made you"`