from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from services.steamapi import getPlayerSummaries, getOwnedGames
from utils.card import renderUserCard, renderOwnedGamesCard
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/getPlayerSummaries")
async def playerSummaries():
    steamid = 76561198134424238
    res = await getPlayerSummaries(steamid)
    card = renderUserCard(res['playerName'], res['playerProfileUrl'], res['avatar'])
    headers =  dict({
          "Content-Type": "image/svg+xml",
          "Cache-Control": "public, max-age=7200",
        })
    return Response(content=card, headers=headers)

@app.get("/api/getOwnedGames")
async def playerSummaries():
    steamid = 76561198134424238
    res = await getOwnedGames(steamid,12)
    return res
