from typing import Callable
import logging
import time

from fastapi import (Request,
                     Response)


logger = logging.getLogger("middleware_logger")
logging.basicConfig(level=logging.INFO)


async def log_requests(request: Request, call_next: Callable) -> Response:
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    logger.info(
        f"Request -> {request.method} {request.url} -> Process time ={process_time} ms."
    )
    return response