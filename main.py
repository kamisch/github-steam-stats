from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from typing import Optional
from services.steamapi import getPlayerSummaries, getOwnedGames
from utils.card import renderUserCard, renderOwnedGamesCard
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/getPlayerSummaries/{steamId}")
async def playerSummaries(steamId:str, bgColor: Optional[str] = 'transparent', textColor: Optional[str] = 'black' ):
    #hex or transparent
    res = await getPlayerSummaries(steamId)
    card = renderUserCard(res['playerName'], res['playerProfileUrl'], res['avatar'], bgColor, textColor)
    headers =  dict({
          "Content-Type": "image/svg+xml",
          "Cache-Control": "public, max-age=7200",
        })
    return Response(content=card, headers=headers)

@app.get("/api/getOwnedGames/{steamId}")
async def playerSummaries(steamId:str):
    res = await getOwnedGames(steamId,12)
    card = renderOwnedGamesCard(res)
    headers =  dict({
          "Content-Type": "image/svg+xml",
          "Cache-Control": "public, max-age=7200",
        })
    # return res
    return Response(content=card, headers=headers)
