# Flask-Scrapy Web Scraper

This project is a web application built with Flask and Scrapy. It allows users to specify a range of numbers, run a web scraper, and view or download the scraped data. The project includes a form to input the range, displays a loader during the scraping process, and shows the results in a paginated table.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Form to input a range of numbers for scraping.
- Loader animation while scraping is in progress.
- Paginated table to display scraped results.
- Download scraped data as a CSV file.
- Error handling and validation.

## Requirements

- Python 3.8 or higher
- Flask 2.0 or higher
- Scrapy 2.5 or higher
- pandas

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the start and end numbers in the form and submit.
3. Wait for the loader animation to complete.
4. View the scraped results in the paginated table.
5. Click the download button to download the results as a CSV file.
6. To run another scrape, click the "Scrape Again" button.

## Project Structure

Safer/
├── flask_app/
│ ├── templates/
│ │ └── index.html
│ │ └── success.html
│ │ └── error.html
│ ├── static/
│ │ ├── css/
│ │ └── styles.css
│ │ ├── js/
│ │ └── loader.js
│ │ └── images/
│ │ └── loader.gif
│ ├── init.py
│ ├── app_routes.py
├── safer/
│ ├── safer/
│ │ ├── spiders/
│ │ │ └── init.py
│ │ │ └── scraper.py
│ │ ├── init.py
│ │ ├── items.py
│ │ ├── middlewares.py
│ │ ├── pipelines.py
│ │ └── settings.py
│ └── scrapy.cfg
├── venv/
├── requirements.txt
└── README.md


- **flask_app/**: Contains the Flask application files.
  - **templates/**: HTML templates for the web application.
  - **static/**: Static files like CSS, JavaScript, and images.
  - **__init__.py**: Flask application initialization file.
  - **app.py**: Main Flask application file.
  - **email_utils.py**: Utility functions for sending emails.

- **scrapy_project/**: Contains the Scrapy project files.
  - **scrapy_project/**: Directory for Scrapy project settings and spiders.
    - **spiders/**: Directory for Scrapy spiders.
    - **__init__.py**: Scrapy project initialization file.
    - **items.py**: Defines items to be scraped.
    - **middlewares.py**: Middleware settings for Scrapy.
    - **pipelines.py**: Pipelines for processing scraped data.
    - **settings.py**: Scrapy project settings.
  - **scrapy.cfg**: Scrapy configuration file.

- **venv/**: Virtual environment directory (not included in version control).
- **requirements.txt**: List of Python dependencies.
- **README.md**: Project documentation.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

