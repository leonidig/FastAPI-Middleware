from typing import Callable

from fastapi import (Request,
                     Response,
                     status
                    )

async def check_headers(request: Request, call_next: Callable) -> Response:
    if "/main" in request.url.path:
        x_custom_header = request.headers.get("X-Custom-Header")
        if not x_custom_header or x_custom_header.strip() == "":
            return Response(
                "X-Custom-Header is missing or empty",
                status_code=status.HTTP_400_BAD_REQUEST
            )
    response = await call_next(request)
    return response
