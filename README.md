# Aviato Task

## Task Definition

To create a single API endpoint that accepts a JSON object with a dynamic number of fields and stores this JSON. The model should be designed to handle dynamic JSON without defining any static fields.

## End Points

### Create User
* **Endpoint:** `POST /add_users`
* **Request Body:** JSON containing user details (e.g., username, email, project_id)
* **Response:** JSON with user details and a unique user ID

### Get User Details
* **Endpoint:** `GET /get_users`
* **Response:** JSON with user details

### Update User Details
* **Endpoint:** `PATCH /update_users`
* **Request Body:** JSON with updated user details
* **Response:** JSON with updated user details

### Delete User
* **Endpoint:** `DELETE /delete_users`
* **Response:** JSON confirming deletion
