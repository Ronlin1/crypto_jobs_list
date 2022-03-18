# import modules
import requests
from bs4 import BeautifulSoup

# Create a list of URLs to loop through
urls = []
# Since we are only scraping the first 15 pages
page = [num for num in range(1,16)]
for num in page:
    url = f"https://crypto.jobs/?page={num}"
    urls.append(url)

# We loop through each URL scraping its content
for url in urls:
    # Initiate an GET HTTP request
    response = requests.get(url)
    
    # Create an HTML Parser from the response (200)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Get the table rows that contain our data
    data_row = soup.find("tbody").find_all("tr")
    
    # Create a temp storage for each job page data
    job_pages = []
    
    # loop through the table rows
    for row in data_row: 
        # Selecting the second 'td' tag    
        job_data = row.select_one(":nth-child(2)") 
        
        # Let's try getting text from non-None types data      
        try:
            job_pages.append(job_data.get_text().strip())
        except:
            pass

    # Print individual job data        
    for job_page in job_pages:
        print(job_page.strip())
              
              
        

        
