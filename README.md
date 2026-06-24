Project Overview

This project is a simple medicine management system built using FastAPI and Python.

It allows users to:

* View all medicines
* Add a new medicine
* Update a medicine
* Delete a medicine

The project also includes a CLI tool that allows users to manage medicines from the terminal.

---

Project Files

* database.py → stores medicine data
* schemas.py → defines data validation models using Pydantic
* main.py → contains all API endpoints
* cli.py → connects and interacts with the API

---

* API Endpoints

->Get All Medicines

GET /medicines
Returns a list of all medicines.

->Get Medicine By ID

GET /medicines/{medicine_id}
Returns a specific medicine.

->Create Medicine

POST /medicines
Adds a new medicine.

->Update Medicine

PUT /medicines/{medicine_id}
Updates an existing medicine.

->Delete Medicine

DELETE /medicines/{medicine_id}
Deletes a medicine.

---

CLI Commands

List Medicines:
python cli.py list

Add Medicine:
python cli.py add Panadol 50

Delete Medicine:
python cli.py delete 1

----------
* Libraries Used

FastAPI:
->Used to create the API endpoints.

Pydantic:
->Used to validate the input data.

Requests:
->Used to send requests from the CLI to the API.

Argparse:
->Used to read commands from the terminal.

Uvicorn:
->Used to run the FastAPI application.