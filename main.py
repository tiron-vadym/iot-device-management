import logging

from aiohttp import web

from app.router import routes
from app.database import db
from app.models import ApiUser, Location, Device


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = web.Application()
app.add_routes(routes)


def init_db():
    db.connect()
    db.create_tables([ApiUser, Location, Device])
    db.close()


def main():
    init_db()
    web.run_app(app, port=8000)
    logger.info("Application started")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Error while starting the application: {e}", exc_info=True)
