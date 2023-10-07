from fastapi import FastAPI, APIRouter

from src.routers.base import all_routers

app = FastAPI(title='Authentication service')


async def include_routers(routers):
    """Includes all routers specified in the all_routers tuple"""

    api_router = APIRouter(prefix='/api')

    for router in routers:
        api_router.include_router(router)

    app.include_router(api_router)


@app.on_event("startup")
async def startup():
    """Executed before the server starts"""

    print("Starting up...")
    await include_routers(all_routers)
    print('Successful start')
