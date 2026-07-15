# Cafe & WiFi RESTful API

A fully functional RESTful CRUD API built with Python, Flask, and SQLAlchemy. This backend service manages a local SQLite database of workspace-friendly cafes, offering endpoints to read, search, add, modify, and securely delete records.

## 🚀 API Endpoints & Usage

### 1. Get All Cafes
* **Endpoint:** `GET /all`
* **Response:** `200 OK` with a JSON array of all cafes.

### 2. Search Cafes by Location
* **Endpoint:** `GET /search?loc=<location_name>`
* **Response:** `200 OK` with filtered results, or `404 Not Found` if no cafes match the location.

### 3. Add a New Cafe
* **Endpoint:** `POST /add`
* **Request Body:** Accepts JSON payload or Form Data containing all cafe fields.
* **Response:** `201 Created` on successful creation.

### 4. Update Coffee Price
* **Endpoint:** `PATCH /update-price/<int:cafe_id>`
* **Query Parameters / Form Data:** `new_price`
* **Response:** `200 OK` on successful update, or `404 Not Found`.

### 5. Secure Delete Cafe
* **Endpoint:** `DELETE /report-closed/<int:cafe_id>`
* **Headers or Query Parameters:** `api-key` (Requires a valid matching key)
* **Response:** `200 OK` on successful deletion, `403 Forbidden` if unauthorized, or `404 Not Found`.

## 🛠️ Tech Stack
* **Framework:** Flask
* **Database ORM:** Flask-SQLAlchemy (SQLite)
* **Format:** JSON (RESTful standards)

