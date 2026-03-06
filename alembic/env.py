import asyncio
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from src.core.config import settings
from src.core.db import Base

# import all tables to register them in metadata

config = context.config
target_metadata = Base.metadata


def run_migrations_online() -> None:
    connectable = create_async_engine(
        settings.database_url,
        pool_pre_ping=True,
    )

    def do_run_migrations(sync_conn) -> None:
        context.configure(
            connection=sync_conn,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

    async def run_async_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    asyncio.run(run_async_migrations())


run_migrations_online()
