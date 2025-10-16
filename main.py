# ----------------------------- Importing Libraries ---------------------------------- #
import requests  # For making HTTP requests
from datetime import datetime  # For getting the current date and time

# ----------------------------- Constants and Endpoints ---------------------------------- #
NUTRIX_ID = ""  # Your Nutritionix App ID
NUTRIX_API = ""  # Your Nutritionix App Key
nutrix_endpoint = ""  # Nutritionix API endpoint for exercise tracking
sheety_endpoint = ""  # Sheety API endpoint for storing workout data

# Headers for Nutritionix API requests
headers = {
    "x-app-id": NUTRIX_ID,  # App ID for Nutritionix API
    "x-app-key": NUTRIX_API,  # API Key for Nutritionix API
    "Content-Type": "application/json"  # Setting content type to JSON
}

# ----------------------------- Getting User Input ---------------------------------- #
# Replace the placeholder below with an actual user input for testing purposes
# Uncomment the line below to prompt the user for input
# user_input = input("Tell me about what you did today? ")
user_input = "ran 5 kilometers"  # Example input for testing

# ----------------------------- Nutritionix API Request ---------------------------------- #
# Preparing the data payload for the API request
exercise_data = {"query": user_input}

# Sending a POST request to Nutritionix API with user input and headers
nutrix_response = requests.post(nutrix_endpoint, json=exercise_data, headers=headers)
nutrix_result = nutrix_response.json()["exercises"][0]  # Extracting the first exercise from the response

# Extracting details about the exercise
exercise = nutrix_result["user_input"].title()  # Exercise name, formatted in title case
duration = nutrix_result["duration_min"]  # Duration of the exercise in minutes
calories = nutrix_result["nf_calories"]  # Calories burned during the exercise

# ----------------------------- Preparing Data for Sheety API ---------------------------------- #
# Creating a data dictionary for the Sheety API request
sheety_data = {
    "workout": {
        "date": datetime.now().date().strftime("%d/%m/%Y"),  # Current date in DD/MM/YYYY format
        "time": datetime.now().time().strftime("%H:%M:%S"),  # Current time in HH:MM:SS format
        "exercise": exercise,  # Extracted exercise name
        "duration": duration,  # Extracted duration
        "calories": calories,  # Extracted calorie count
    }
}

# ----------------------------- Sending Data to Sheety API ---------------------------------- #
# Sending a POST request to the Sheety API to log the workout data
sheety_response = requests.post(url=sheety_endpoint, json=sheety_data)

# ----------------------------- Debugging and Logs ---------------------------------- #
# Printing the Sheety API response status for debugging
print(sheety_response.status_code)  # Response status code (e.g., 200 for success)
print(sheety_response.json())  # Response content in JSON format (if needed for debugging)