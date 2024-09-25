# fetch-backend-assessment
## Overview
This **FastAPI** application provides a **REST API** to manage user points and transactions, including adding points, spending points, and fetching the current points balance.

## Requirements
- **Python 3.7 or higher**
- **pip3**

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/raymondwusuper/fetch-backend-assessment
cd pathname/to/your/downloaded/fetch
```
2. **Create a Virtual Environment (optional but recommended):**
```bash
python3 -m venv venv
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
python3 -m uvicorn main:app --reload
```
5. **Access the API:** Open your browser and navigate to:
```
http://127.0.0.1:8000/docs
```
This will display the UI, where you can interact with the API endpoints. </br>
Click the dropdown arrow on a method, and select `Try it out`. Then paste the request in the corresponding format and click execute:
- **add:**
```json
{
   "payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"
}
```
- **spend**
```json
{
   "points": 5000
}
```
- **balance**
   - nothing to paste, just click execute

Alternatively, you can directly add the information as a json in a new terminal window in the following format:
```bash
#add
#transaction should be formatted like '{ "payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z" }'
curl -X POST "http://127.0.0.1:8000/add" -H "Content-Type: application/json" -d '[transaction]'

#spend
#transaction should be formatted like '{ "points": 5000 }'
curl -X POST "http://127.0.0.1:8000/spend" -H "Content-Type: application/json" -d '[transaction]'

#balance
curl -X GET "http://127.0.0.1:8000/balance"
```

## API Endpoints
1. **Add Points**
   - **Route:** `/add`
   - **Method:** `POST`
   - **Request Body:**
   - ```json
      {
        "payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"
      }
     ```
   - **Response:**
      - `200 OK` in terminal if successful.
      - `400 Bad Request` if point request results in negative balance.
2. **Spend Points**
   - **Route:** `/spend`
   - **Method:** `POST`
   - **Request Body:**
   - ```json
      {
        "points": 5000
      }
     ```
   - **Response:**
     - `200 OK` with details of points allocation.
     - `400 Bad Request` if not enough points are available.
3. **Get Points Balance**
   - **Route:** `/balance`
   - **Method:** `GET`
   - **Response:**
   - ```json
      {
        "DANNON": 1000,
        "UNILEVER": 0,
        "MILLER COORS": 5300
      }
     ```
## Code Structure
- `main.py`: Contains the main FastAPI application code with the API endpoints.
- `summary.txt`: Contains the information detailing the choice of tools, libraries, advantages/disadvantages, and favorite school/personal project.

## Conclusion
This documentation provides a guide to install and run the Fetch Backend API assessment. Follow these steps carefully, and reach out for any questions or issues.
