from uvicorn import run as start
from backend import app


if __name__ == "__main__":
    start("run:app", host="127.0.0.1", port=8080, reload=True)
