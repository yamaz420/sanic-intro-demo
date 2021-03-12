from databases import Database
from time import time

# connect to a SQLite database file
db = Database('sqlite:databas-mars12.db')

#SELECT * FROM databas-mars12
async def get(query, values = {}):
    rows = await db.fetch_all(query=query, values=values) #typ prepared statement
    dicts = []
    for row in rows:
        dicts.append(dict(row)) #konverterar row till dictionary
    return dicts

# INSERT, UPDATE, DELETE

async def run(query, values):
    return await db.execute(query=query, values=values)

# database functions

async def get_todos():
    return await get('SELECT * FROM todos')

async def get_todo_by_id(id):
    return await get('SELECT * FROM todos WHERE id = :id', { "id": id })
   

# route to insert a new todo to the database


async def create_todo(req):
    todo = req.json
    todo['timestamp'] = time() # 1654335443.23654
    id = await insert_todo(todo) # returns incremented id
    todo['id'] = id
    return res.json(todo)

  # return todo with updated values
  #========================================


# async def insert_todo(todo):
#     #INSERT returns the incremented id
#     return await run('INSERT INTO todos(text, timestamp) VALUES(:text, :timestamp)', todo)
#     # {
#     #     "text": todo['text'],
#     #     "timestamp": todo['timestamp']
#     # }