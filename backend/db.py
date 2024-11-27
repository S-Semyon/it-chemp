from tortoise import Tortoise, run_async

db_url='postgres://flet_app:kupcake@localhost:5432/project'

async def init_db():
    await Tortoise.init(
        db_url,
        modules={'models': ['models']},
    )

    await Tortoise.generate_schemas()
