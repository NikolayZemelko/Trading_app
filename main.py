from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fixtures.fixture import get_fixture

app = FastAPI(
    title="Trading app"
)

FAKE_USERS = get_fixture('users')
FAKE_TRADES = get_fixture('trades')


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request,
                                       exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


@app.get('/')
def get_hello():
    return "Hello world!"


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in FAKE_USERS if user.get('id') == user_id]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 1):
    return FAKE_TRADES[offset:][:limit]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(
        filter(
            lambda user: user.get('id') == user_id, FAKE_USERS))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


class TradeType(Enum):
    sell = "sell"
    buy = "buy"


class Trade(BaseModel):
    id: int
    user_id: int
    side: TradeType
    price: int = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    FAKE_TRADES.extend(trades)
    return {"status": 200, "data": FAKE_TRADES}
