
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


# Alembic Config object
config = context.config

# Set sqlalchemy.url from environment variable
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise RuntimeError("Missing DATABASE_URL environment variable")
config.set_main_option("sqlalchemy.url", db_url)

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your models to register them with SQLAlchemy
from backend.app.db.db_connect import Base
from backend.app.model import  product, product_image, color  # Add all model files here

# Set the metadata for 'autogenerate' support
target_metadata = Base.metadata

# Run migrations
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()