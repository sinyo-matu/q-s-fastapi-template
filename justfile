set dotenv-load := true

setup:
   uv sync --frozen
   uv run pre-commit install

check:
   ruff check --fix .

dev:
   uv run fastapi dev src/main.py

run:
   uv run fastapi run src/main.py --workers={{num_cpus()}} --port 8080

