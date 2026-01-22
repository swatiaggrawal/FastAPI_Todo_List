# FastAPI Todo List 🚀

This project is a simple **FastAPI** application that demonstrates how to build REST APIs using Python.
It implements a basic **in-memory Todo items API** with request validation, path parameters, and automatic documentation.

---

## 📌 What This Project Does

* Creates a FastAPI application
* Defines API endpoints using decorators (`@app.get`, `@app.post`)
* Uses **Pydantic models** for request validation
* Stores items temporarily in memory (Python list)
* Handles errors using `HTTPException`
* Exposes interactive API documentation using Swagger UI

---

## ⚙️ API Endpoints

### 1️⃣ Root Endpoint

```http
GET /
```

**Description:**
Returns a simple welcome message.

**Response:**

```json
{
  "message": "Hello,World"
}
```

---

### 2️⃣ Create a New Item

```http
POST /items
```

**Request Body:**

```json
{
  "text": "Buy groceries",
  "is_done": false
}
```

* `text` is **required**
* `is_done` is optional (defaults to `false`)

**Response:**
Returns the updated list of items.

---

### 3️⃣ List Items

```http
GET /items?limit=10
```

* Returns a list of items
* `limit` controls how many items are returned (default: 10)

---

### 4️⃣ Get Item by ID

```http
GET /items/{item_id}
```

* Retrieves an item using its index
* Returns `404` if the item does not exist

---

## 📦 Installing Dependencies

Make sure you have Python 3.9+ installed.

Install **FastAPI** and **Uvicorn** using pip:

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the Server with Uvicorn

**Uvicorn** is an ASGI server used to run FastAPI applications.

Run the application using:

```bash
uvicorn main:app --reload
```

### Explanation:

* `main` → name of the Python file (`main.py`)
* `app` → FastAPI instance (`app = FastAPI()`)
* `--reload` → automatically reloads the server on code changes (useful during development)

Once started, the server will run at:

```
http://127.0.0.1:8000
```

---

## 🧪 API Testing with `/docs`

FastAPI automatically generates interactive API documentation.

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

Using `/docs`, you can:

* Test all endpoints directly from the browser
* Send GET and POST requests
* Validate request bodies
* See response schemas

This makes testing **very easy without Postman or curl**.

---

## 📝 Notes

* Data is stored **in memory**, so it resets when the server restarts
* This project is ideal for learning:

  * FastAPI basics
  * Request/response validation
  * REST API design



