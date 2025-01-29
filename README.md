
# Todo List API

RESTful API to allow users to manage their to-do list.

Credits of idea for: https://roadmap.sh/projects/todo-list-api


## Features

- **OAuth**: This API has a token-based authentication system, and its passwords are hashed (Bcrypt) before being stored in the database.
- **CRUD Task**: A CRUD task system that requires prior authentication before being used. Depending on the session, you will be able to use the CRUD with the tasks that correspond to the authenticated user.
- **ORM**: An ORM was used, specifically SQLAlchemy, to manage queries and operations involving the database.


## Technologies
- Python
- FastApi
- MySql
## Installation

To run the app, ensure you have Python installed and follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Alxcccc/Todo-List-API.git

cd Todo-List-API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables:
- Create a .env file: Inside app directory, create a file named .env and add the following lines (you will replace your_generated_secret_key later):
```bash
SECRET_KEY="your_generated_secret_key"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
- Instructions to Generate a New Secret Key: You can generate a secret key with this command in your terminal. If you happen to not have OpenSSL installed, you can visit this website and run the command: https://openssl.tplant.com.au/.:
```bash
openssl rand -hex 32
```
- The generated secret key will be displayed in the console. Users should copy this key.
- Update the .env File: Users should paste the copied secret key into their .env file, replacing your_generated_secret_key:
```bash
SECRET_KEY="your_generated_secret_key"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Set up the database:
- To install the database, you only need to have MySQL and its server. The only thing you need to do is start the server and create a new database using the script located in app/db/scripts.



    
## Usage

Run the file main.py:

- Start the development server:
```bash
python main.py
```
- Access the documentation by navigating to http://127.0.0.1:8000/ in your web browser.



## Documentation
Interactive API documentation is available at [Swagger UI](http://localhost:8000/docs) and [ReDoc](http://localhost:8000/redoc)

