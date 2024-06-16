import os
import gradio as gr
from fastapi import FastAPI


app = FastAPI()

def render_template(data):
    filename = os.path.join("Template",data.get("filename"))
    content = data.get("content")
    with open(filename, "r") as file:
        template = file.read()
        rendered_template = template.format(**content)
    return rendered_template

@app.get("/") #return main page
async def _():
    pass
@app.get("/v1/temprender")
async def temprender_template(data: dict):
    # 渲染模板
    rendered_template = render_template(data)
    return {"result": rendered_template}

@app.get("/v1/wf/{action}")
def wf(action):
    match action:
        case "create": pass  #create workflow
        case "delete": pass  #delete local workflow
        case "maintain":pass #maintain workflow
        case "render":pass   #open a workflow app
        case "execute":pass  #execute workflow
        case "":pass         #list all workflow and related informaiton


@app.get("/v1/w/{action}")
def wf(action):
    match action:
        case "download": pass  #create weight
        case "delete": pass    #delete weight
        case "maintain":pass   #maintain weight
        case "":pass         #list all weight and related informaiton


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)