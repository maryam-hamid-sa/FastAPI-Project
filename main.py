from fastapi import FastAPI

app = FastAPI()

# 1. Home Endpoint
@app.get("/")
def home():
    return {"message": "Hello World"}

# 2. About Endpoint
@app.get("/about")
def about():
    return {
        "Institute": "BanoQabil",
        "Course": "python"
    }

# 3. Profile Endpoint
@app.get("/profile")
def profile():
    return {
        "Username": "Maryam",
        "Status": "Active"
    }

# 4. Contact Endpoint
@app.get("/contact")
def contact():
    return {
        "Email": "maryam@gmail.com",
        "Support": "11111111111"
    }