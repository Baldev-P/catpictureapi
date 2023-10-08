# Cat Picture API

  Cat Picture API is a RESTful API for uploading and managing cat pictures. It allows you to perform various operations, including uploading, deleting, updating, and fetching   cat pictures. This API is built using Django and Django REST framework.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)


## Getting Started

### Prerequisites

  Before you begin, ensure you have met the following requirements:

  - Python 3.11.5 installed
  - Pip package manager installed
  - Virtual environment 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Baldev-P/catpictureapi.git

2. Navigate to the project directory:

    ```bash
     cd catpictureapi

3. Create a virtual environment :

    ```bash
    python3.11 -m venv venv

4. Activate the virtual environment :
   
    On Windows:

       .\venv\Scripts\activate

    On macOS and Linux:

        source venv/bin/activate

6. Install the project dependencies:

    ```bash
    pip install -r requirements.txt

7. Apply database migrations:

    ```bash
    python manage.py migrate

8. Run the development server:

   ```bash
    python manage.py runserver

9. The API should now be accessible at http://127.0.0.1:8000/.
   
10. Navigate to API documentation at http://127.0.0.1:8000/swagger/ for details.




## Usage
  You can use this API to perform various operations on cat pictures, such as uploading new cat pictures, fetching cat pictures, updating cat pictures, and deleting cat   pictures.



## API Endpoints
     GET /catpictures/: Fetch a list of all cat pictures or create a new cat picture.  

     POST /catpictures/create: Create a new cat picture.  

     GET /catpictures/{cat_picture_id}: Retrieve details of a specific cat picture by its ID.  

     PUT /catpictures/{cat_picture_id}: Update a specific cat picture by its ID.  

     DELETE /catpictures/{cat_picture_id}: Delete a specific cat picture by its ID.  

  For detailed documentation on how to use each endpoint, refer to the API documentation.  



## Testing
  To run the test suite for this project, you can use Django's test runner. In the project directory, run the following command:

      python manage.py test

## Contributing
  Contributions are welcome! Feel free to open issues or pull requests to improve this project.

## License
  This project is licensed under the MIT License.
