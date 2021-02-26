from fastapi import FastAPI, Response,Path, Query
from fastapi.responses import JSONResponse
from typing import Optional
from services.steamapi import getPlayerSummaries, getOwnedGames
from utils.card import renderUserCard, renderOwnedGamesCard
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/favicon.ico")
async def favicon():
    return {"message": "Hello World"}


@app.get("/api/getPlayerSummaries/{steamId}")
async def playerSummaries(steamId: str = Path(...,max_length=30),
                          bgColor: Optional[str] = Query('ffffff',min_length=6, max_length=6),
                          textColor: Optional[str] =  Query('000000',min_length=6,max_length=6),
                          borderColor: Optional[str] =  Query('000000',min_length=6,max_length=6),
                          borderWidth: Optional[int] = Query(2,gt=-1, lt=20) ):
    #hex or transparent
    width = 150
    height= 160
    res = await getPlayerSummaries(steamId)
    card = renderUserCard(res['playerName'], res['playerProfileUrl'],
                          res['avatar'],width,height, bgColor, textColor,borderColor,borderWidth)
    contentControlHeader = "public, max-age={}".format(os.getenv('CACHE_AGE'))
    headers = dict({
        "Content-Type": "image/svg+xml",
        "Cache-Control": contentControlHeader,
    })
    return Response(content=card, headers=headers)


@app.get("/api/getOwnedGames/{steamId}")
async def playerSummaries(steamId: str = Path(...,max_length=30),
                          limit: Optional[int] = Query(6,gt=0, lt=13),
                          row: Optional[int] = Query(1,gt=1, lt=13),
                          col: Optional[int] = Query(6,gt=1, lt=13),
                          bgColor: Optional[str] = Query('ffffff',min_length=6,max_length=6),
                          textColor: Optional[str] =  Query('000000',min_length=6,max_length=6),
                          borderColor: Optional[str] =  Query('000000',min_length=6,max_length=6),
                          borderWidth: Optional[int] = Query(2,gt=-1, lt=20) ):
    if (limit < col):
        col = limit
    res = await getOwnedGames(steamId, limit)
    width = 120
    height= 70
    card = renderOwnedGamesCard(res, row, col,width,height,bgColor,textColor,borderColor,borderWidth)
    contentControlHeader = "public, max-age={}".format(os.getenv('CACHE_AGE'))

    headers = dict({
        "Content-Type": "image/svg+xml",
        "Cache-Control": contentControlHeader,
    })
    return Response(content=card, headers=headers)
