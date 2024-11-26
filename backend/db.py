from tortoise import Tortoise, run_async

async def init_db():
    await Tortoise.init(
        db_url='postgres://postgres:czena135@localhost:5432/secure-voice-chat',
        modules={'models': ['models']}
    )

    await Tortoise.generate_schemas()
