import uvicorn
from env import server_options

if __name__ == "__main__":
    uvicorn.run("fastapi_example:app", **server_options())