# Green Vision - Plant Disease Detection Website

## Overview

Green Vision is a web application developed for plant disease detection using Flask and deep learning Convolutional Neural Networks (CNN). The application is designed to identify diseases in 12 major crops grown in Karnataka by analyzing images uploaded by users. Users can register, choose a crop, upload an image of a diseased plant, and receive disease predictions. The website also features a remedies section providing information on how to manage and treat identified diseases for each crop.

## Project Directory

The project directory is structured as follows:

- **class_labels:** Contains files with the names of diseases for each of the 12 major crops.

- **models:** Contains .h5 files of trained CNN models for each of the 12 crops.

- **static:** Holds static files such as images, CSS, and JavaScript for the web application.

- **templates:** Contains HTML templates used to render the web pages.

- **app.py:** The main Flask application file that handles routing, user input, and communicates with the deep learning models.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Green-Vision.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd Green-Vision
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open a web browser and go to [http://localhost:5000](http://localhost:5000).

4. If you are a new user, click on the "Sign Up" link to create an account. Otherwise, log in with your existing credentials.

5. After logging in, choose a crop from the list of 12 major crops.

6. Upload an image of a plant leaf that you suspect is diseased.

7. Click on the "Detect Disease" button to get a prediction for the disease.

8. Explore the "Remedies" section to find information on how to manage and treat the identified disease for the selected crop.

## Project Structure

- **Class Labels:**
  - Each crop has a separate file in the `class_labels` directory containing the names of diseases for that crop.

- **Models:**
  - The `models` directory holds individual .h5 files for each crop, representing the trained CNN models.

- **Static:**
  - Static files such as images, stylesheets, and JavaScript used by the web application.

- **Templates:**
  - HTML templates used for rendering web pages.

- **app.py:**
  - The main Flask application file that handles routing, user input, and communicates with the deep learning models.

## Remedies Section

The website features a "Remedies" section providing users with information on managing and treating diseases for each crop. This section is accessible after a disease prediction is made for an uploaded image.

## Acknowledgments

- The plant disease datasets used for training the models were obtained from different aggricultural website and Kaggle.

