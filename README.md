# FastAPI-Project

A lightweight and efficient RESTful API built with Python and FastAPI. This project demonstrates basic API routing and JSON response handling.

##  Features
This project includes the following API endpoints:
*   `GET /` - Root endpoint returning a simple greeting.
*   `GET /about` - Returns institutional and course information (BanoQabil - Python).
*   `GET /profile` - Fetches active user profile data.
*   `GET /contact` - Provides support contact details and email.

##  Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites
Make sure you have Python installed on your system (Python 3.7+ is recommended).

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/maryam-hamid-sa/FastAPI-Project.git](https://github.com/maryam-hamid-sa/FastAPI-Project.git)
   cd FastAPI-Project
   
**Create a virtual environment:**
It is best practice to use a virtual environment to manage dependencies.

Bash
python -m venv .venv
Activate the virtual environment:

**On Windows:**

Bash
.venv\Scripts\activate

**On macOS and Linux:**

Bash
source .venv/bin/activate
Install required dependencies:

Bash
pip install -r requirements.txt

**▶️ Running the Server**
Start the FastAPI server using Uvicorn with live reloading enabled:

Bash
uvicorn main:app --reload
The server will start running at http://127.0.0.1:8000.

**📖 Interactive API Documentation**
FastAPI automatically generates interactive API documentation. Once the server is running, you can explore and test the endpoints directly from your browser:

Swagger UI: Navigate to http://127.0.0.1:8000/docs

ReDoc: Navigate to http://127.0.0.1:8000/redoc

Developed by Maryam Hamid
