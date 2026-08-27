"""python3 -m seat_mcp"""

from .auth import ensure_token_file
from .jobs import ensure_jobs_dir
from .server import serve


def main() -> None:
    ensure_token_file()
    ensure_jobs_dir()
    serve()


if __name__ == "__main__":
    main()
