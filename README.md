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
#### main 

   1. `parg()`<br>
         • Description:<br> This function parses command-line arguments using the argparse module.<br>
         • Parameters:<br> None<br>
         • Return:<br> An argparse.Namespace object containing the parsed arguments.<br>

   2. `case(x)`<br>
        • Description: <br> This function filters out tokens that are entirely composed of digits.<br>
        • Parameters:<br>
            x: A list of strings (tokens).<br>
        • Return: <br>A list of strings (tokens) that do not consist solely of digits.<br>

  3. `censor(info, type)`<br>
        • Description: <br>This function replaces sensitive information in a given string with a block character.<br>
        • Parameters:<br>
            info: The input string containing sensitive information.<br>
            type: A list of strings representing sensitive information.<br>
        • Return:<br>The input string with sensitive information replaced by block characters.<br>

   4. `analyze_entities(MailData)`<br>
        • Description: <br>This function analyzes entities in text using both SpaCy and Google Cloud Natural Language API.<br>
        • Parameters:<br>
            MailData: The text to be analyzed.<br>
        • Return: <br>A tuple containing a list of entities found in the text and a list of statistics regarding the entities (number of dates, phone numbers, addresses, and person names).<br>

   5. `CenP(data)`<br>
        • Description: <br>This function censors sensitive information in text data.<br>
        • Parameters:<br>
            data: The text data to be censored.<br>
        • Return: <br>The censored text data.<br>

   6. `Read(Xtemp, CCd)`<br>
        • Description: <br>This function reads files, censors sensitive information, and writes the censored data to new files.<br>
        • Parameters:<br>
            Xtemp: A list of file paths to be read.<br>
            CCd: The directory where censored files will be saved.<br>
        • Return: <br>None.<br>

   7. `main()`<br>
        • Description: <br>This function serves as the main entry point of the script. It parses command-line arguments, identifies input files, processes them, and performs censorship based on specified flags.<br>
        • Parameters: <br>None<br>
        • Return: <br>None.<br>
        
        
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
