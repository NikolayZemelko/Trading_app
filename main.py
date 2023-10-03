from fastapi import FastAPI
from fixtures.fixture import get_fixture

app = FastAPI(
    title="Trading app"
)

FAKE_USERS = get_fixture('users')
FAKE_TRADES = get_fixture('trades')


@app.get('/')
def get_hello():
    return "Hello world!"


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in FAKE_USERS if user.get('id') == user_id]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 1):
    return FAKE_TRADES[offset:][:limit]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, FAKE_USERS))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
