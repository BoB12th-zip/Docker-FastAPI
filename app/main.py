from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/oxdjww")
async def root():
    return RedirectResponse(url="https://oxdjww.site", status_code=302)
