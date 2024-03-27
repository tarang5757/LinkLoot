import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter
import time
import logging
import tkinter as tk
from tkinter import messagebox


class JobScraper:

    #initialize instance variables
    def __init__(self, position, location):
        self.position = position
        self.location = location
        #will collect data entries and store them in records.
        self.records = []
        self.session = requests.Session()
        self.session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    #get url
    def get_url(self, start):
        template = 'https://www.linkedin.com/jobs/search?keywords={}&location={}&start={}'
        url = template.format(self.position, self.location, start)
        return url
    # Get record of entries
    def get_record(self, card):
        try:
            # Extract data from linkedin
            atag = card.a
            job_title = atag.span.text.strip()
            company = card.find('a', 'hidden-nested-link').text.strip()
            job_location = card.find('span', 'job-search-card__location').text.strip()
            post_date_element = card.find('time', 'job-search-card__listdate')  # Find the time element with the class
            post_date = post_date_element['datetime'] if post_date_element else 'Not Found'  # Extract the datetime attribute

            date = datetime.today().strftime('%Y-%m-%d')
            job_id = atag.get('href').split('?')[0].split('/')[-1]
            link = f"https://www.linkedin.com/jobs/view/{job_id}"
            return (job_title, company, job_location, post_date, date, link)
        except AttributeError:
            logging.warning('Failed to scrape some information from a job card.')
            return None

    def scrape_jobs(self):
        for page in range(0, 100, 25):  # Each page shows 25 results, adjust as needed.
            url = self.get_url(page)
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('div', 'base-card')

            for card in cards:
                record = self.get_record(card)
                if record:
                    self.records.append(record)

            time.sleep(1)  # Delay to avoid rate-limiting

    #Save jobs to an excel file.
    def save_jobs_to_excel(self, fileName):
        workbook = xlsxwriter.Workbook(f'{fileName}.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        headers = ['Job Title', 'Company', 'Location', 'Post Date', 'Extract Date', 'Link']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, bold)

        for row, record in enumerate(self.records, start=1):
            for col, value in enumerate(record):
                worksheet.write(row, col, value)

        # Set specific column widths as provided
        worksheet.set_column('A:A', 55.0)  # Column A
        worksheet.set_column('B:B', 27.0)  # Column B
        worksheet.set_column('C:C', 25.0)  # Column C
        worksheet.set_column('D:D', 13.0)  # Column D
        worksheet.set_column('E:E', 13.0)  # Column E
        worksheet.set_column('F:F', 124.0) # Column F

        workbook.close()


    def run(self, fileName):
        # GUI setup
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Show a starting message
        messagebox.showinfo("Process Started", "Starting the job scraping process. Please wait...")
        
        logging.info('Starting the job scraping process.')
        self.scrape_jobs()
        self.save_jobs_to_excel(fileName)
        
        # Show a finished message
        messagebox.showinfo("Process Completed", f"Job scraping process completed. Results saved to {fileName}.xlsx.")
        
        logging.info(f'Job scraping process completed. Results saved to {fileName}.xlsx.')
        
        root.destroy()  # Close the GUI



