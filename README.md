
# Link Loot

Link Loot is a Python application designed to help job seekers find job postings from LinkedIn. It provides a user-friendly graphical interface for entering job search criteria, such as job title and location, and saves the search results to an Excel file for easy access and analysis.

## Features

- **Customizable Search**: Users can specify the job title and location to tailor the job search to their preferences.
- **Excel Export**: The application scrapes job postings from LinkedIn and exports the details to an Excel file, including job title, company, location, posting date, and link to the job listing.
- **Simple GUI**: Built with `customtkinter`, the application offers a straightforward and easy-to-use interface.

## Installation

Before running the application, ensure you have Python installed on your system. This application requires Python 3.6 or newer.

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/job-finder.git
cd LinkLoot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:
- `customtkinter`
- `requests`
- `beautifulsoup4`
- `xlsxwriter`

3. **Run the application:**

```bash
python gui.py
```

## Usage

1. **Start the Application**: Run `gui.py` to open the Job Finder GUI.
2. **Enter Job Criteria**: In the provided fields, enter the job title, location, and the name of the Excel file where you want to save the search results.
3. **Start Search**: Click the "search" button to begin the job scraping process. The application will notify you once the scraping starts and again when it completes, indicating where the results are saved.

## Demo Of The Application
[![Alt text](https://i3.ytimg.com/vi/tJ_P_j5EKw4/maxresdefault.jpg)](https://www.youtube.com/watch?v=tJ_P_j5EKw4&ab_channel=TarangPatel "Hover text")
 

## Contributing

Contributions to Link Loot are welcome! Please feel free to fork the repository, make changes, and submit pull requests. For major changes or new features, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- This project uses `customtkinter` for its graphical user interface, providing an enhanced appearance and functionality over the standard Tkinter module.
- Job scraping is performed with `requests` and `beautifulsoup4`, making web scraping accessible and efficient.
- `xlsxwriter` is used for creating Excel files, allowing easy export and formatting of the job postings data.
