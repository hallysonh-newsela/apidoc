import uvicorn
from app import main

if __name__ == "__main__":
    uvicorn.run(main.app, host="localhost", port=8000)
