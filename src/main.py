from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup():
    print("Starting up...")
