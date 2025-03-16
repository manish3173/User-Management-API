# User Management API

## Description
This is a User Management API built with FastAPI. It allows users to create, read, update, search, and delete user information. The API is designed to manage user data efficiently and provides a simple interface for interacting with user records.

## Features
- Create a new user
- Search users by name
- Read user details by ID
- Update user information
- Delete a user by ID

## Installation

1. Clone the repository:
   ```bash
   https://github.com/manish3173/User-Management-API.git
   ```

2. Install the required packages:
   ```bash
   pip install fastapi uvicorn
     ```

## Usage

To run the API, execute the following command:
```bash
python -m uvicorn main:app --reload
```


The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /users/**: Create a new user
  - Request Body: 
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "phone_no": "123-456-7890",
      "address": "123 Main St"
    }
    ```

- **GET /users/search**: Search users by name
  - Query Parameter: `name` (string)

- **GET /users/{user_id}**: Read user details by ID

- **PUT /users/{user_id}**: Update user information
  - Request Body:
    ```json
    {
      "name": "John Doe",
      "phone_no": "098-765-4321",
      "address": "456 Elm St"
    }
    ```

- **DELETE /users/{user_id}**: Delete a user by ID

## Documentation
Access the API documentation at `/docs` after running the server. You can view it at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). You can perform CRUD operations using this API.



## License
This project is licensed under the MIT License.
