import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse

app = FastAPI()

# This finds the absolute path to your templates folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/registration")
async def register(request: Request):
    return templates.TemplateResponse(request, "registration.html")

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(request, 'about.html')

@app.get("/travel")
def travel(request: Request):
    return templates.TemplateResponse(request, 'travel.html')

@app.get("/important_dates")
async def importantdates(request: Request):
    return templates.TemplateResponse(request, 'timetable.html')

@app.get("/sitemap.xml")
async def get_sitemap(request: Request):
    return templates.TemplateResponse(request, "sitemap.xml", media_type="application/xml")

@app.get("/robots.txt", response_class=PlainTextResponse)
async def get_robots():
    with open("templates/robots.txt", "r") as f:
        content = f.read()
    return content
