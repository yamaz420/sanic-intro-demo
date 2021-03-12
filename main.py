# py -m venv venv
# venv/Scripts/activate.bat
# py -m pip install sanic databases[sqlite] //DONE

# Node.js                       //DONE 
# npm install -g nodemon        //DONE
# nodemon --exec py main.py 

# =====CRUD===== 
#Action - METHOD - route
#Create - POST   - @app.post()
#Read -   GET    - @app.get()
#Update - PUT    - @app.put()
#Delete - DELETE - @app.delete()

from sanic import Sanic, response as res

from database import *
from database import get_todos, get_todo_by_id

# from time import *

#instantiate the app instance
app = Sanic('app')

#register route handlers 
@app.get('/rest/todos')
async def get_all_todos(req):
    todos = await get_todos() #1
    return res.json(todos) #2
    
    # return res.json(await get_todos())
    # ^skriva #1 och #2 på en rad istället^

@app.get('/rest/todos/<todo_id:int>')
async def get_one_todo(req, todo_id: int):
    todo = await get_todo_by_id(todo_id)
    if len(todo) > 0:
        return res.json(todo[0])
    else:
        return res.text('No  todo found with id {}'.format(todo_id))

# route to insert a new todo to the database
@app.post('/rest/todos')
async def create_todo(req):
    todo = req.json

    todo['timestamp'] = time()
    id = await insert_todo(todo)
    todo['id'] = id

# @app.post('/rest/todos')
# async def create_todo(req):
#     todo = req.json
#     todo['timestamp'] = time()
#     id = await insert_todo(todo)
#     todo['id'] = id
#     #return todo with updated values
#     return res.json(todo) 
    #====================





# req == request
# res == response
@app.get('/hello')
async def hello_world(req): 
    hello = {
        "message": "Hello as JSON!"
    } 
    return res.json(hello) #returns a JSON object

    # return res.text('Hello from Sanic server! heh')

@app.get('/greeting/<name:string>')

async def greeting(req, name: str):
    return res.text('Greetings {}!'.format(name))

# @app.get('/greeting/<name:string>')
# async def greeting(req, name:str):
#     return res.text('Greetings {}!'.format.(name))
    
#start the webserver
if __name__ == '__main__':
    app.run(port=5000)

