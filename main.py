"""Main.py"""

import uvicorn

from src.core.db import settings

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=int(settings.PORT), reload=True)
