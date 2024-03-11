# CIS6930sp24 -- Assignment1

Name: Aryaan Shaikh <br>
Student ID: 3020-2476

## Contact

Email - am.shaikh@ufl.edu <br>
Project Link: https://github.com/Aryaan03/cis6930sp24-assignment1


## Assignment Description
This is the 2nd project assignment for the CIS6930 Data Engineering course. The main aim of this assignment is to practice processesing plain text documents for detecting and censoring sensitive data to create a new censorored version of the file. The expected outcome of this assignment is to output a .censored version of the text file and print the statistics of number of censored names, phone numbers, dates and addresses. More specifically, this assignment involves processing text documents from ENRON email [dataset link](https://www.cs.cmu.edu/~enron/s). Senstive data like Name, Date, Phone Number, Address, email id should be censored or replaced with a Unicode full block character █ (U+2588) [Unicode](https://symbl.cc/en/2588/) from any email or text file. Moreover, the staistics of how many files are censored along with the stats of how many names, dates, phone numbers and addresses were censored from the text file should also be printed ({'names': 5, 'phones': 2, 'dates': 1, 'addresses': 3}). <br> 

This assignment underscores the importance of censoring sensitive information which is disseminated in the public domain. There is a necessity for a redaction process to conceal names, addresses, phone numbers, dates  and other private information. This is crucial across various documents like police reports, court transcripts, and medical records. However, conventional redaction methods often prove costly and time-intensive. Our goal is to develop a system that accepts plain text documents, detects sensitive information, and performs necessary redactions. The program should execute with a command-line interface, reading input files, censoring sensitive content, and generating statistics on the redaction process. We can use different packages like Spacy, Snorke, Google Natural Language API,  NLTK, etc to attain better accuracy in censoring crucial data.

To Conclude, this is a great assignment that emphasizes on precision in data extraction, sensitivity in handling private information, and efficiency in data processing. It helped us to learn more about data handling, processing and censoring. It also presents a hands-on opportunity to engage with real-world data scenarios, nurturing skills vital in the domain of data engineering.
<br>

### **Parameters**:<br>
o **--input**: Accepts a glob representing acceptable file types. Multiple input flags may be utilized to specify file groups. Appropriate error messages should be displayed for unreadable or uncensorable files.<br>
o **--output**: Specifies a directory for storing censored files. Each censored file should retain the original filename with the appended ".censored" extension.<br>
o **Censor Flags**:<br>
&emsp;&emsp;->	**--names**: Identifies any type of name, with parameters defined by the implementer.<br>
&emsp;&emsp;    ->	**--dates**: Detects written dates in various formats (e.g., 4/9/2025, April 9th, 22/2/22).<br>
&emsp;&emsp;    ->	**--phones**: Identifies phone numbers in their diverse formats.<br>
&emsp;&emsp;    ->	**--address**: Detects physical (postal) addresses, excluding email addresses. Implementers can define parameters for each flag.<br>
o **--stats**: Stats can be directed to a specified file or special files (stderr, stdout), providing a summary of the censoring process. Statistics should include types and counts of censored terms and details of each censored file, offering insights into the censoring process.<br>

### Dataset

For this assignment, the Enron Email Dataset [link](https://www.cs.cmu.edu/~enron/s) is used, it consists of a variety of data and contains around 500,000 email messages. While the full dataset is large, I have utilized a portion of it for this assignment.

### Why white space is censored between words?
We are given a choice to censor both words and white spaces between phrases. For the assignment, I am also censoring the space between words, for example, Let suppose there is a name "John Cena" then the censored text visible in the censored file will be "█████████" and not "████ ████". The reason for this is that, censoring the white space between phrases is more secure as it would be almost impossible to guess the phrase at the censored places. Moreover, it will also difficult to understand the type of entity present at the censored text. 

### Format of the outfile

The format of the outfile for the data pipeline and redacting sensitive information task is a text file with the same name as the original file and the extension .censored (For example, if the input file is test.txt, then the output file will be test.txt.censored). The text wriiten in file has censored text with censored characters replaced by a character of your choice (such as the Unicode full block character '█' (U+2588)).

### How stats helped in developing code?

Stats are very helpful in developing the code that provided insights into the performance and behavior of the code. By collecting statistics on the censoring process, such as the types and counts of censored terms, the statistics helped to identify potential issues or areas for improvement in the code. For example, if the statistics show that a very less number of phone numbers are not being censored in a file that consists of a large number of phone numbers, this could indicate an issue with the phone number recognition logic. Then the logic can be investigated to fix the issue, and re-run the code to see if the statistics improve.<br>

Statistics can also be used for tracking the progress of the code over time. By comparing the statistics from different runs of the code, we can check if the censoring process is becoming more efficient or effective, and identify any areas where further optimization is needed. Moreover, Stats also helped in comparing the performace of different packages. For this assignment, I have used and compared effectiveness of censoring process by Spacy, NLTK, Google Natural Language API and huggingface. Stats helped me in choosing the packages which were giving the best results for different functions and labels.    

Overall, collecting statistics on the censoring process helped in ensuring that code is working correctly and efficiently, and provided valuable insights into the performance and behavior of the code.

### Process of developing code

The process of developing the censoring system involves the following steps:

1. Open and read the text files containing the emails to be censored.<br>
2. Define a function to censor a specific word or phrase in a piece of text. This function takes the text and the word or phrase to be censored as arguments, and replaces all occurrences of the word or phrase with a string of asterisks or another character of the same length.<br>
3. Define a function to censor multiple words or phrases in a piece of text. This function takes the text and a list of words or phrases to be censored as arguments, and applies the censor function to each word or phrase in the list.<br>
4. Define a function to censor words or phrases in a specific context, such as within a certain distance of each other. This function takes the text and a list of words or phrases to be censored as arguments, and uses regular expressions to identify and censor the words or phrases in the specified context.<br>
5. Test the censoring functions on sample text to ensure that they are working correctly.<br>
6. Apply the censoring functions to the emails to be censored, and write the censored emails to new text files with the .censored extension.



## How to install
```
pipenv install 
```

## How to run
Project can be run by using any of the given commands:
```
pipenv run python censoror.py --input '*.txt'\
--names --dates --phones --address \
--output 'files/'\
--stats stderr
```

For testing use command:
```
pipenv run python -m pytest
```

## Demo Implementation 

video link: [Data Engineering Assignment0 demo](https://github.com/Aryaan03/cis6930sp24-assignment0/blob/main/DE-A0_demo.mp4)
<br>The video is also available in the repository in good quality.

## Functions
#### main file
1. `RetrieveIncidents(url)`<br>
    • Description: <br>
        &emsp;- Downloads/Fetches incident data from a given URL.<br>
        &emsp;- The `urllib.request` module is used to execute an HTTP request and retrieve the data.<br>
        &emsp;- Data is stored locally in a local variable and not at any specific location (tmp folder) for using it for both making a SQL database and also for retreiving data.<br>
        &emsp;- Constructs a request with a custom user agent to access the provided URL.<br>
    • Parameters: <br>
        &emsp;- `url`(str), The URL from which the incident data is to be fetched.<br>
    • Returns:<br>
        &emsp;- `data`; The fetched incident data.<br>

2. `ExtractData(IncidentData)`<br>
    • Description: <br>
        &emsp;- This function extracts incident information from the incident PDF file using Pypdf.<br>
        &emsp;- Reads the incident data from a PDF using `pypdf.PdfReader` and `io.BytesIO`.<br>
        &emsp;- Extracts text from each page of the PDF using the layout mode and concatenates it into a single string.<br>
    • Parameters: <br>
        &emsp;- `IncidentData`(bytes), The incident data in PDF format.<br>
    • Returns:<br>
        &emsp;- `ExtractText`; The extracted text from the incident data PDF.<br>

3. `CreateDB(Norman, Tab, Header)`<br>
    • Description: <br>
        &emsp;- This function creates a new SQLite database and a table based on the provided parameters using the `sqlite3` module.<br>
        &emsp;- It will create an SQLite table named "Tab" with specific columns for incident details like known previously like time, number, location, nature, and origin.<br>
        &emsp;- It Drops the table if it already exists and Creates a new table with the schema based on the provided header information.<br>
    • Parameters: <br>
        &emsp;- `Norman`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
        &emsp;- `Header`(list); The header information for the table.<br>
    • Returns:<br>
        &emsp;- None<br>

4. `PopulateDB(Norman, Tab, Line)`<br>
    • Description: <br>
        &emsp;- This function populates the SQLite database with the provided data using the `sqlite3` module.<br>
        &emsp;- Constructs an SQL query to insert the provided data using the `INSERT` query into the specified table.<br>
        &emsp;- Executes the query for each set of data to be inserted into the table.<br>
    • Parameters: <br>
        &emsp;- `Norman`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
        &emsp;- `Line`(list); The data to be inserted into the table.<br>
    • Returns:<br>
        &emsp;- None<br>

5. `Insert(Information)`<br>
    • Description: <br>
        &emsp;- This function processes the incident information into the database.<br>
        &emsp;- It initializes a list and appends the rows in it.<br>
    • Parameters: <br>
        &emsp;- `Information` (list); List of incident information.<br>
    • Returns:<br>
        &emsp;- `Latest`(list); The filtered and inserted information.<br>

6. `Status(Norman, Tab)`<br>
    • Description: <br>
        &emsp;- This function retrieves and displays the status of incidents in the database using SQL queries and the `sqlite3` module.<br>
        &emsp;- It Retrieves and prints a list of incidents and their occurrence count, sorted alphabetically by nature, from the specified database table.<br>
    • Parameters: <br>
        &emsp;- `Norman`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
    • Returns:<br>
        &emsp;- None<br>
        
7. `Calculate(Norman, Tab)`:<br>
    • Description: <br>
       &emsp;- This function executes an SQL query to count the number of entries in the specified database table and returns the count.<br>
       &emsp;- This function also iterstes through all the rows and prints it from the incident table by executing a SQL query using the `sqlite3` module.<br>
       &emsp;- It retrieves and prints all rows from the specified database table. <br>
    • Parameters: <br>
       &emsp;- `Norman`(str); The name of the SQLite database file.<br>
       &emsp;- `Tab`(str); The name of the table to be created.<br>
    • Returns:<br>
       &emsp;- `count`(int); The number of entries in the incident table.<br>

8. `main(url)`:<br>
    • Description: <br>
        &emsp; - Invokes all other functions. <br>
        &emsp;- Calls the `RetrieveIncidents(url)` function to download incident data from the provided URL.<br>
        &emsp;- Calls the `ExtractData()` function to extract text from the downloaded incident data PDF.<br>
        &emsp;- Parses the extracted text to obtain relevant information such as incident time, number, location, nature, and origin. <br>
        &emsp;- Creates a new SQLite database using the `CreateDB` function Populates the database with the parsed information using the `PopulateDB` function.<br>
        &emsp;- Calls the `Status` function to retrieve and display the status of incidents in the populated database.<br>
        &emsp;- Defines a command-line interface using `argparse`.<br>
        &emsp;- Parses the command-line arguments, specifically the `--incidents` argument for the URL.<br>
    • Parameters:<br>
        &emsp; - `url`(str); The URL from which the incident data is to be fetched.<br>
    • Returns:<br>
         &emsp; - List of Nature of incidents along with the number of times it occurred long with the number of times it has happened separated by the pipe character.
        
   
## Database Development

    1. Database Creation:
        - A SQLite database is created to store the incident data.
        - Database is created using `CreateDB()` function.
        - The structure of the incident table is defined based on the extracted header information.
        - Data is stored in a local variable so that it can not only be used for retrieving data but also for populating the databse.

    2. Connect to the Database (`CreateDB()`):
        - Establish a connection to an SQLite database named "normanpd.db" using the `sqlite3` module.
        - Create a cursor to interact with the database.

    3. Data Population(`PopulatedDB()` and `Insert()`:
        - The extracted incident data is inserted into the SQLite database usind `PopulatedDB()` function.
        - Run an SQL command to check if the table already exists, if so delete the 'incidents' table and create a new table.
        - Queries are used to execute SQL statements for creating table and headers.
        - For insertion 'INSERT' statement is used.
        - Implementing the 'INSERT' command using the cursor.
        - Each row of incident data corresponds to an entry in the database table.

    4. Data Status and Printing:
        - The script provides functionality to query the database for statistical analysis of incident data.
        - Running an SQL query to obtain the number of incidents categorized by nature from the 'incidents' table. 
        - Ordering results by count (descending) and then by alphabetically by nature.   
        - Display type of nature of incident along with their respective counts seperated by a pipe '|' symbol. 
        
    5. Command-line Interface:
        - The script can be executed from the command line.
        - Users provide the URL of the incident summary PDF file as a command-line argument.
        

Below is a brief overview on how to establish connection, take data, make table, insert, query and close the connection to database:
        
    -> Begin by establishing a connection to the "normanpd.db" SQLite database using the sqlite3 module and create a cursor to interact with it.
    -> Next, craft an SQL statement to generate a table named "incidents" within the database, outlining the columns like incident_time, incident_number, incident_location, nature, and incident_ori, assigning suitable data types to each, such as TEXT.
    -> Proceed to populate the "incidents" table by iterating through each incident entry in the extracted data. For each entry, formulate an SQL INSERT statement to add the data into the table, executing it with the cursor, and confirming the changes.
    -> Utilize an SQL query to gather the incident count grouped by nature from the "incidents" table. Arrange the results by count in descending order and then alphabetically by nature.
    -> Display the sorted incident data in the format "nature | count," providing a clear overview of the incident nature alongside the corresponding count.
    -> Retrieve all incident data by executing an SQL query to fetch all information from the "incidents" table, returning a list of tuples representing each incident.
    -> Finally, if the "incidents" table already exists, execute an SQL statement to drop it, preventing conflicts when creating a new table.

## Testing

Testing using pytest & mocking is done to make sure that all the functions are working independently and properly. Testing is crucial for early bug detection and maintaining code quality. Testing units of code encourages modular, understandable code and integrates seamlessly into continuous integration workflows, boosting integrity. Ultimately, all major functions like Retrieve, ExtractData, CreateDB and more are tested if they are functioning properly. For example. test_create verifies if a database and table is created or not. 


    1. `test_Retrieve`:
        - Utilizes mocking to validate individual functions.
        - Uses mock versions of urllib.request.urlopen to simulate fetching data from a URL.
        - Dummy data ('Some Dummy data') is provided instead of actual network requests.
        - The URL variable serves as input for testing the fetchIncidents function.

    2. `test_Extraction`:
        - Mocks the PDF library to control page content.
        - Creates dummy pages with predefined text for testing text extraction.
        - Ensures the extracted text matches expected output, validating correct text extraction without real PDFs.

    3. `test_Create`:
        - Uses mocking to verify the createdb function successfully creates a database and table.
        - Checks if sqlite3.connect is called with correct arguments.
        - Verifies expected SQL queries are executed on the mock cursor.
        - Ensures commit and close methods are called on the mock connection.

    4. `test_Populate`:
        - Mocks sqlite3.connect to verify data insertion calls and expected queries.
        - Validates if commit and close occur on the mock connection.
        - Verifies data insertion follows table format, ensuring correct function behavior without a real database.

    5. `test_Status`:
        - Mocks the database connection to return desired data.
        - Captures printed output of the status function.
        - Compares captured output to expected string, verifying correct output generation using mocked data.

## Bugs and Assumptions

• Assuming that the structure of the PDF files provided by the Norman, Oklahoma police department remains consistent across different reports. If the structure changes, it could break the extraction process. <br>
• A large PDF files or a high volume of data exceeding system memory or processing limits, can lead to performance degradation or application crashes.<br>
• Not all columns of a row can be empty at the same time. There should be some entry in atleast one cell of every row.<br>
• All fields, excluding the 'Nature' field will consist of alphanumeric characters.<br>
• Assuming that empty entries are only possible in the 'Nature' column. If there are empty entries in any other column it might break the extraction.<br>
• Known bug: Some pdfs that have unsual formatting are not able to parse.<br> 
• If there are multiple lines in a single cell, then only the first line will be parsed. There is no such cases where the 'Nature' column had multiple lines of text. So, it was not tested. But, if it has, this can be a potential bug.<br>
• No bugs apart from those mentioned above are known/identified.


## Version History

• 0.1 <br>
   &emsp;&emsp; -> Initial Release

## License

This project is licensed by Aryaan Shaikh©2024.

## Acknowledgments

• [Christan Grant](https://github.com/cegme)- Providing the problem Statement <br>
• [Yifan Wang](https://github.com/wyfunique)- Testing our code<br>
• [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)- Helped me in Installing Pipenv <br>
• [Extract Text from a PDF](https://pypdf.readthedocs.io/en/latest/user/extract-text.html)- Helped me in extracting text in a fixed width format and changing cells<br>
