from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'name':'sarthak'}}

@app.get('/about')
def about():
    return {'data':'about page'}

<<<<<<< HEAD
=======
@app.get('/blog/id')
def index_blog_id():
    return {'data':'blog id'}

@app.get('/blog/{id}')
def show(id):
    # fetch blog with id = id
    return {'data':id}
>>>>>>> 1b2eee4d633d195be0f5e7bd836468ae8f113413
