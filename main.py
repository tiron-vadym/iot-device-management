from aiohttp import web
from dependencies import init_db
from app.router import routes

app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    db = init_db()
    web.run_app(app, port=8000)
