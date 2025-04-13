# Web Scraping and Email Notification System

This project is a Python-based web scraping and email notification system. It periodically scrapes a webpage for upcoming tour events, stores new events in a SQLite database, and sends an email notification when a new event is found.

## Project Structure
data.db # SQLite database file for storing events extract.yaml # YAML file defining the CSS selector for scraping main.py # Main Python script for scraping, storing, and sending notifications


## Features

- Scrapes tour event data from a webpage.
- Stores unique events in a SQLite database.
- Sends email notifications for new events.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `selectorlib`
  - `smtplib` (built-in)
  - `ssl` (built-in)
  - `sqlite3` (built-in)

Install external dependencies using `pip`:

```bash
pip install requests selectorlib

Collecting workspace information```markdown
# Web Scraping and Email Notification System

This project is a Python-based web scraping and email notification system. It periodically scrapes a webpage for upcoming tour events, stores new events in a SQLite database, and sends an email notification when a new event is found.

## Project Structure

```
data.db                # SQLite database file for storing events
extract.yaml           # YAML file defining the CSS selector for scraping
main.py                # Main Python script for scraping, storing, and sending notifications
```

## Features

- Scrapes tour event data from a webpage.
- Stores unique events in a SQLite database.
- Sends email notifications for new events.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `selectorlib`
  - `smtplib` (built-in)
  - `ssl` (built-in)
  - `sqlite3` (built-in)

Install external dependencies using `pip`:

```bash
pip install requests selectorlib
```

## Configuration

1. **Email Credentials**:
   Update the `username` and `password` variables in the `send_email` function in `main.py` with your Gmail credentials. Ensure that "Allow less secure apps" is enabled for your Gmail account.

2. **Webpage URL**:
   The URL to scrape is defined in the `URL` variable in `main.py`. Update it if needed.

3. **CSS Selector**:
   The CSS selector for scraping is defined in `extract.yaml`. Modify it to match the structure of the webpage being scraped.

## How It Works

1. The script scrapes the webpage defined in the `URL` variable using the CSS selector from `extract.yaml`.
2. If a new event is found, it is stored in the `data.db` SQLite database.
3. An email notification is sent to the recipient defined in the `send_email` function.

## Usage

Run the script using Python:

```bash
python main.py
```


The script will run in an infinite loop, scraping the webpage every 10 seconds.

## Database Schema

The SQLite database (`data.db`) contains a single table named `events` with the following schema:

| Column | Type    | Description          |
|--------|---------|----------------------|
| band   | TEXT    | Name of the band     |
| city   | TEXT    | City of the event    |
| date   | TEXT    | Date of the event    |

## Security Note

Avoid hardcoding sensitive information like email credentials in the script. Use environment variables or a configuration file for better security.

## License

This project is licensed under the MIT License.
```