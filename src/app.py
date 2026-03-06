"""
Main entry
"""

from fastapi import FastAPI

from src.core.error_handler import add_global_exception_handlers
from src.features.user.get_all_user.get_all_user import get_all_user_router

app = FastAPI()
add_global_exception_handlers(app)

app.include_router(get_all_user_router)
