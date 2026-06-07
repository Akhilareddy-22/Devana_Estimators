# DEVANA Construction Estimator

## Overview

DEVANA Construction Estimator is a Streamlit-based web application that helps users estimate construction costs and material requirements based on the built-up area of a project.

## Features

* Project cost estimation
* Cement requirement calculation
* Steel requirement calculation
* Brick quantity estimation
* User-friendly web interface
* MySQL database integration
* Report generation and storage

## Technologies Used

* Python
* Streamlit
* MySQL
* Pandas

## Project Structure

DEVANA_CONSTRUCTION_ESTIMATOR/

├── app.py

├── database.py

├── devana_estimator.sql

├── requirements.txt

├── README.md

└── generated_reports/

## Installation

1. Clone the repository

git clone <repository_url>

2. Navigate to the project folder

cd DEVANA_CONSTRUCTION_ESTIMATOR

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

## Usage

1. Enter the project name.
2. Enter the built-up area in square feet.
3. Click "Generate Estimate".
4. View the estimated cost and material requirements.

## Future Enhancements

* PDF report generation
* Excel export
* Material price customization
* Multi-project management
* Cloud deployment


