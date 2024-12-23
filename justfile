set dotenv-load := true

setup:
   uv sync --frozen
   uv run pre-commit install

check:
   ruff check --fix .

sync:
   uv sync --frozen

dev: sync
   uv run fastapi dev src/main.py

run: sync
   uv run fastapi run src/main.py --workers={{num_cpus()}} --port 8080

test: sync
   uv run pytest --capture=no
   