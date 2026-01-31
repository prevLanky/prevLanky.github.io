# How to setup basic FastAPI website

## Installation

### Prerequisites
Start with installing fastapi on your system. (You can create an virtual env (venv) if you feel like you need to.)
```bash
pip install fastapi uvicorn 
```
### main FastAPI code
Put the following code in your 'main.py' file.
```python
def func():
    print("test")
```

## Basic knowledge

### FastAPI
FastAPI is a modern, high-performance Python web framework designed for building APIs. It is based on Python type hints and supports asynchronous programming using async and await.
#### Key Features:
- High performance, comparable to Node.js and Go
- Automatic request validation using type hints
- Automatic generation of interactive API documentation (Swagger UI and ReDoc)
- Built-in support for asynchronous request handling
- Easy integration with authentication, authorization, and dependency injection
#### Core Components
- Routing: Defines API endpoints using decorators (e.g., @app.get, @app.post)
- Data Validation: Uses Pydantic models to validate request and response data
- Dependency Injection: Manages shared resources such as databases and authentication
---
### Uvicorn
Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server for Python. It is responsible for running FastAPI applications and handling incoming HTTP requests.
#### Key Features
- Lightweight and fast
- Fully asynchronous
- Designed for modern Python web frameworks
- Supports HTTP/1.1 and WebSockets
#### Responsibilities
- Listens for incoming network requests
- Manages connections and concurrency
- Forwards requests to the ASGI application
- Returns responses to clients
---
### Relationship Between FastAPI and Uvicorn
FastAPI and Uvicorn are commonly used together to build and run high-performance web APIs in Python. FastAPI provides the application framework for defining API behavior, while Uvicorn acts as the server that executes and serves the application over HTTP.
FastAPI and Uvicorn serve different but complementary roles:
- FastAPI defines the application logic, routes, and data validation
- Uvicorn runs the application and handles HTTP communication
- FastAPI applications require an ASGI server like Uvicorn to operate
