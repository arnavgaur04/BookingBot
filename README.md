# Booking.com Info Scraper

### Overview

This project is a Python-based web scraper that uses Selenium to extract information from Booking.com. The bot fetches details about hotels and displays them in the terminal. This can include hotel names, prices, ratings, locations, and other relevant information.

### Features

- Extracts hotel information from Booking.com
- Displays hotel names, prices, ratings, and locations in the terminal
- Configurable search parameters (destination, check-in/check-out dates, etc.)

### Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver
### Installation

- Clone the repository:

```
git clone https://github.com/arnavgaur04/BookingBot
cd BookingBot
```

- Download and install ChromeDriver according to your browser.

- Run the scraper:

```
python3 run.py
```
- The script will open a Chrome browser window, navigate to Booking.com, perform the search, and display the results in the terminal.

### Project Structure

- run.py: The main script that runs the Selenium bot.
- Booking/booking: Contains all the fuction inside.
- Booking/constants: Contains all the constants inside.


```
Enter Place you wanna go : New York
Enter from date (DD MonthName Year) : 20 June 2024
Enter to date (DD MonthName Year): 24 June 2024

// Output

Hotel Name: The Plaza
Rating: 9.0
Price: $850

Hotel Name: Marriott Marquis
Rating: 8.5
Price: $450

...
```

#### Acknowledgements

Selenium WebDriver
Booking.com for providing the data. If you have any questions or need further assistance, please let me know!
