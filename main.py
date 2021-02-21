from fastapi import FastAPI
from services.steamapi import getPlayerSummaries, getOwnedGames
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/getPlayerSummaries")
async def playerSummaries():
    steamid = 76561198134424238
    res = await getPlayerSummaries(steamid)
    return res

@app.get("/api/getOwnedGames")
async def playerSummaries():
    steamid = 76561198134424238
    res = await getOwnedGames(steamid,10)
    return res
    