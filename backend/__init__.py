from fastapi import FastAPI

from .routes import main_router
from .middlewares import (
                            check_headers,
                            log_requests
                        )

app = FastAPI(debug = True)

app.include_router(main_router)

app.middleware("http")(log_requests)
app.middleware("http")(check_headers)