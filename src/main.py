from datetime import datetime

from fastapi import APIRouter, FastAPI

from .api.include_routers import all_routers


app = FastAPI(title="Authentication service")


async def include_routers(routers: tuple) -> None:
    """Includes all api specified in the all_routers tuple"""

    api_router = APIRouter(prefix="/api")

    for router in routers:
        api_router.include_router(router)

    app.include_router(api_router)


@app.on_event("startup")
async def startup() -> None:
    """Executed before the server starts"""

    start_time = datetime.now()

    await include_routers(all_routers)

    end_time = datetime.now()

    print(f"Startup time: {end_time - start_time}")
