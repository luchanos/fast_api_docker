from fastapi import FastAPI
import uvicorn
import psycopg2
from envparse import Env

app = FastAPI()
env = Env()

DATABASE_URL = env.str("DATABASE_URL")


@app.get(path="/user")
def create_user():
    database = app.state.db
    cursor = database.cursor()
    cursor.execute("""INSERT INTO users (username) VALUES (%s);""", ("test_user", ))
    database.commit()
    return {"msg": "user has been created"}

@app.delete(path="/user/{user_id}")
def delete_user(user_id: int):
    database = app.state.db
    cursor = database.cursor()
    cursor.execute("""DELETE FROM users WHERE user_id = %s;""", (user_id, ))
    database.commit()
    return {"msg": "user has been deleted"}


def create_app():
    db = psycopg2.connect(DATABASE_URL)
    app.state.db = db
    return app


if __name__ == "__main__":
    uvicorn.run(create_app())
