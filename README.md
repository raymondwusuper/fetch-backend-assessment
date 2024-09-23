# fetch-backend-assessment
## Overview
This **FastAPI** application provides a **REST API** to manage user points and transactions, including adding points, spending points, and fetching the current points balance.

## Requirements
- **Python 3.7 or higher**
- **pip**

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/raymondwusuper/fetch-backend-assessment
cd pathname/to/your/downloaded/fetch-backend-assessment
```
2. **Create a Virtual Environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# For Windows
venv\Scripts\activate
```
3. **Install Dependencies:** Install FastAPI and Uvicorn:
```bash
pip3 install fastapi uvicorn #Python 3
```
4. **Run the Application:** Make sure you are in the project directory (refer to step 1 for cd command). Run the server using:
```bash
uvicorn fetch_backend_test:app --reload
```
5. **Access the API:** Open your browser and navigate to:
```
http://127.0.0.1:8000
```
This will display the UI, where you can interact with the API endpoints.

## API Endpoints
1. **Add Points**
   - **Route:** 
