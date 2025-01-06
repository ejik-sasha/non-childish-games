from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
