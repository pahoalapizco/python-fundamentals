from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1> This is a HTML page from Python :D</h1>
        </body>
    </html>
    """


@app.get("/list")
def get_list():
  return [1,2,3,4]



@app.get("/dict")
def get_dictionary():
  return {
    "key 1": "Value 1",
    "key 2": "Value 2",
    "key 3": "Value 3"
  }
