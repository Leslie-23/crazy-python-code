import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# Function to scrape weather data
def get_weather_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the temperature and time elements (modify selectors based on the actual website's structure)
    temp_elements = soup.select('.temperature-class')  # Replace with actual CSS selector
    time_elements = soup.select('.time-class')  # Replace with actual CSS selector

    temps = [temp.get_text() for temp in temp_elements]
    times = [time.get_text() for time in time_elements]

    return times, temps

# URL of the weather website (replace with actual URL)
weather_url = 'http://example.com/weather'  # Replace with the actual weather URL

# Initialize an empty DataFrame to store the data
weather_df = pd.DataFrame(columns=['Time', 'Temperature'])

# Loop to scrape data periodically (every 10 minutes in this example)
for _ in range(6):  # Modify the range for the number of iterations
    times, temps = get_weather_data(weather_url)

    # Append new data to the DataFrame
    new_data = pd.DataFrame({'Time': times, 'Temperature': temps})
    weather_df = pd.concat([weather_df, new_data], ignore_index=True)

    # Wait for 10 minutes before the next scrape
    time.sleep(600)

# Convert the Temperature column to numeric (assuming temperatures are in degrees Celsius)
weather_df['Temperature'] = pd.to_numeric(weather_df['Temperature'].str.replace('°C', ''))

# Plot the temperature trends
plt.figure(figsize=(10, 5))
plt.plot(weather_df['Time'], weather_df['Temperature'], marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trends Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
