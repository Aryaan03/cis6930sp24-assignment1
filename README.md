# CIS6930sp24 -- Assignment1

Name: Aryaan Shaikh <br>
Student ID: 3020-2476

## Contact

Email - am.shaikh@ufl.edu <br>
Project Link: https://github.com/Aryaan03/cis6930sp24-assignment1


## Assignment Description
This is the 2nd project assignment for the CIS6930 Data Engineering course. The main aim of this assignment is to practice processesing plain text documents for detecting and censoring sensitive data to create a new censorored version of the file. The expected outcome of this assignment is to output a (.censored) version of the text file and print the statistics of number of censored names, phone numbers, dates and addresses. More specifically, for this assignment we have used the text documents from ENRON email [dataset link](https://www.cs.cmu.edu/~enron/s) for censoring data and also as a testing measure to accurately output results. Senstive data like Name, Date, Phone Number, Address, email id should be censored or replaced with a Unicode full block character █ (U+2588) [Unicode](https://symbl.cc/en/2588/) from any email or text file. Moreover, the staistics of how many files are censored along with the stats of how many names, dates, phone numbers and addresses were censored from the text file should also be printed ({'Censored Names': 5, 'Censored Date': 2, 'Censored Phone Numbers': 1, 'Censored Addresses': 3}). <br> 

This assignment underscores the importance of censoring sensitive information which is disseminated in the public domain. There is a necessity for a redaction process to conceal names, addresses, phone numbers, dates and other private information. This is crucial across various documents like emails, police reports, court transcripts, and medical records. Our goal is to develop a system that accepts plain text documents, detects sensitive information, and performs necessary redactions. The program should execute with a command-line interface, reading input files, censoring sensitive content, and generating statistics on the redaction process. We can use different packages like Spacy, Snorke, Google Natural Language API,  NLTK, etc to attain better accuracy in censoring crucial data.

To Conclude, this is a great assignment that emphasizes on precision in data extraction, sensitivity in handling private information, and efficiency in data processing. It helped us to learn more about data handling, processing and censoring. It also presents a hands-on opportunity to engage with real-world data scenarios, nurturing skills vital in the domain of data engineering.
<br>

### **Parameters**:<br>
o **--input**: Accepts a glob representing acceptable file types. Multiple input flags may be utilized to specify file groups. Appropriate error messages should be displayed for unreadable or uncensorable files.<br>
o **Censor Flags**:<br>
&emsp;&emsp;->	**--names**: Identifies any type of name, with parameters defined.<br>
&emsp;&emsp;    ->	**--dates**: Detects written dates in various formats (e.g., 4/9/2025, April 9th, 22/2/22).<br>
&emsp;&emsp;    ->	**--phones**: Identifies phone numbers in their diverse formats.<br>
&emsp;&emsp;    ->	**--address**: Detects physical (postal) addresses, excluding email addresses. Parameters can be defined for each flag.<br>
o **--output**: Specifies a directory for storing censored files. Each censored file should retain the original filename with the appended ".censored" extension.<br>
o **--stats**: Stats can be directed to a specified file or special files (stderr, stdout), providing a summary of the censoring process. Statistics should include types and counts of censored terms and details of each censored file, offering insights into the censoring process.<br>

### Dataset

For this assignment, the Enron Email Dataset [link](https://www.cs.cmu.edu/~enron/s) is used, it consists of a variety of data and contains around 500,000 email messages. While the full dataset is large, I have only utilized a portion of it for this assignment.

### Why white space is censored between words?
We are given a choice to censor both words and white spaces between phrases. For the assignment, I am also censoring the space between words, for example, let's suppose there is a name "John Cena" then the censored text visible in the censored file will be "█████████" and not "████ ████". The reason for this is that, censoring the white space between phrases is more secure as it will be almost impossible to guess the phrase at the censored places. Moreover, in some cases it will also difficult to understand the type of entity present at the censored text. 

### Format of the outfile

The format of the outfile for the data pipeline and redacting sensitive information task is a text file with the same name as the original file and the extension .censored (For example, if the input file is test.txt, then the output file will be test.txt.censored). The text wriiten in file has censored text with censored characters replaced by a character of your choice (such as the Unicode full block character '█' (U+2588)).

### How stats helped in developing code?

Stats were very helpful in the development the code that provided insights into the performance and behavior of the code. By collecting statistics on the censoring process, such as the types and counts of censored terms, the statistics helped to identify potential issues or areas for improvement in the code. For example, if the statistics show that a very less number of phone numbers are being censored in a file that consists of a large number of phone numbers, this could indicate an issue with the phone number recognition logic. Then the logic can be investigated to fix the issue, and re-run the code to see if the statistics improve.<br>

Statistics can also be used for tracking the progress of the code over time. By comparing the statistics from different runs of the code, we can check if the censoring process is becoming more efficient or effective, and identify any areas where further optimization is needed. Moreover, stats also helped in comparing the performace of different packages. For this assignment, I have used and compared effectiveness of censoring process by Spacy, NLTK, Google Natural Language API and huggingface. Stats helped me in choosing the packages which were giving the best results for different functions and labels.    

Overall, collecting statistics on the censoring process helped in ensuring that code is working correctly and efficiently, and provided valuable insights into the performance and behavior of the code.

### Why I have prefered en_core_web_md spacy model over en_core_web_lg model?

While the large model (en_core_web_lg) might offer slightly better performance in terms of accuracy and generalization, especially for this assignment for the purpose of entity recognition(PERSON NAMES), the medium model (en_core_web_md) often provides sufficient performance for many applications without sacrificing too much accuracy. As the large model is big, in some cases it detects some extra entities that are not "PERSON NAMES" to be censored. This can make censoring somewhat not reliable. Due to this I choose en_core_web_md model!!  

### Process of developing code

The process of developing the code involves the following steps:

1. **Research existing libraries and API's (some are provided in the assignment description)**: I have explored various libraries and APIs that offer natural language processing (NLP) capabilities for entity recognition and text manipulation. SpaCy and Google Cloud Natural Language API libraries are chosen for this assignment.<br>
2. **Defining the command-line interface**: The argparse module is used to define command-line arguments for reading specifying input files, censoring flags, writing in output directory, and printing stats.<br>
3. **Implementing functions**: Functions like parg() for argument parsing, analyze_entities() for entity recognition, censor() for censoring sensitive information, and others are implemented.<br>
4. **Error handling**: The code includes some exception handling to manage errors that might occur during file reading, writing or processing.<br>
5. **Testing**:<br>
   i) The code is manually tested with various input files containing different types of sensitive information to ensure that it correctly identifies and censors them.<br>
   ii) Unit testing using pytest written to verify the functionality of individual functions.<br>
   iii) Test with edge cases such as empty files, files with no sensitive information, and files containing only sensitive information.<br>
6. Review the code for performance and accuracy using stats for various libraries to check and choose best libraries.



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

video link: [Data Engineering Assignment1 demo](https://github.com/Aryaan03/cis6930sp24-assignment1/blob/main/DE_Assignment-1_Demo.mp4)
<br>
![](https://github.com/Aryaan03/cis6930sp24-assignment1/blob/main/DE_Assignment-1_DemoGIF.gif)<br>
The video is also available in the repository in good quality.<br>

## Functions
#### main 

   1. `Argparse()`<br>
         • Description:<br>
         &emsp;&emsp;- This function sets up an argument parser using the `argparse` module to parse command-line arguments.<br>
         &emsp;&emsp;- It defines various command-line arguments such as input files, output directory, censoring flags (names, dates, phones, address), and statistics.<br>
         • Parameters:<br>
      &emsp;&emsp;- None<br>
         • Return:<br>
         &emsp;&emsp;- Parsed arguments object (`argparse.Namespace`) object containing the parsed arguments.<br>

  2. `CenName(MailData)`<br>
        • Description:<br>
          &emsp;&emsp;- This function utilizes the spaCy model to extract names (entities labeled as "PERSON") from the input text.<br>
          &emsp;&emsp;- Extracts person names from the provided text data.<br>
         • Parameters:<br> 
       &emsp;&emsp;- `MailData` - Input text data. <br>
         • Returns: <br>
       &emsp;&emsp;- A list containing the extracted person names from the provided text data..<br>

  3. `CenDate(MailData)`<br>
         • Description: <br>
           &emsp;&emsp;- This function uses the Google Cloud Natural Language API to analyze entities in the text and extracts dates.<br>
           &emsp;&emsp;- Extracts dates from the provided text data.<br>
         • Parameters:<br>
         &emsp;&emsp;- `MailData` - Input text data.<br>
        • Returns: <br>
        &emsp;&emsp;- A list containing the extracted dates from the provided text data.<br>
    
  5. `CenNum(MailData)`<br>
         • Description: <br>
           &emsp;&emsp;- Similar to CenDate(), this function uses the Google Cloud Natural Language API to analyze entities and extracts phone numbers. <br>
           &emsp;&emsp;- Extracts phone numbers from the provided text data.<br>
         • Parameters:<br>
         &emsp;&emsp;- `MailData` - Input text data.<br>
         • Returns: <br>
          &emsp;&emsp;- A list containing the extracted phone numbers from the provided text data.<br>
    
  5. `CenLoc(MailData)`<br>
         • Description: <br>
                 &emsp;&emsp;- Similar to the CenDate() and CenNum() functions, it uses the Google Cloud Natural Language API to extract addresses from the input text.<br>
                 &emsp;&emsp;- Extracts addresses from the provided text data.<br>
            • Parameters: <br>
            &emsp;&emsp;- `MailData` - Input text data.<br>
            • Returns: <br>
            &emsp;&emsp;- A list containing the extracted addresses from the provided text data.<br>

   6. `analyze_entities(MailData, FlaTyp)`<br>
        • Description: <br>
         &emsp;&emsp;- This function coordinates the analysis of entities based on the flags provided..<br>
         &emsp;&emsp;- It calls other functions based on the flags set in FlaTyp and collects statistics.<br>
        • Parameters:<br>
           &emsp;&emsp;- `MailData`: The input text to be analyzed.<br>
           &emsp;&emsp;- `FlaTyp`: Dictionary containing flags indicating which types of entities to analyze.<br>
        • Return: <br>
        &emsp;&emsp;- A tuple containing a list of entities found in the text and a list of statistics regarding the entities (statistics of dates, phone numbers, addresses, and person names).<br>
    
  7. `censor(info, type)`<br>
   • Description: <br>
        &emsp;&emsp;- This function replaces sensitive information in a given string with a block character.<br>
        &emsp;&emsp;- Uses unicode character '█' (U+2588) to censor sensitive data.<br>
        • Parameters:<br>
            &emsp;&emsp;`info`: The input string containing sensitive text.<br>
            &emsp;&emsp;`type`: A list of strings representing sensitive text.<br>
        • Return:<br>
         &emsp;&emsp;- The input string with sensitive information replaced by block characters.<br>

   8. `CenP(data, FlaTyp)`<br>
        • Description: <br>
        &emsp;&emsp;- This function censors sensitive information based on the flags provided.<br>
        &emsp;&emsp;- calls `analyze_entities` and `censor` function to replace identified entities with block characters to obscure sensitive details.<br>
        &emsp;&emsp;- It also prints or writes statistics about the censored information.<br>
        • Parameters:<br>
            &emsp;&emsp;- `data`: The text data to be censored.<br>
            &emsp;&emsp;- `FlaTyp`: Dictionary containing flags indicating which types of entities to analyze.<br>
        • Return: <br>
        &emsp;&emsp;- The censored text data.<br>

   9.    `case(x)`<br>
        • Description: <br>
        &emsp;&emsp;- This function filters out tokens using Regex.<br>
        &emsp;&emsp;- Prepares a list of tokens excluding digit-only entries for subsequent processing.
        • Parameters:<br>
            &emsp;&emsp;- `x`: A list of strings (tokens).<br>
        • Return: <br>
        &emsp;&emsp;- Filtered list of elements.<br>

   10. `Read(Xtemp, CCd, FlaTyp)`<br>
        • Description: <br>
        &emsp;&emsp;- This function reads input files, calls `CenP()` function to censore sensitive information in the text.<br>
        &emsp;&emsp;- Writing censored text to a new file.<br>
        &emsp;&emsp;- Ensures secure handling of sensitive text during file processing.<br>
        • Parameters:<br>
            &emsp;&emsp;- `Xtemp`: A list of file paths to be read.<br>
            &emsp;&emsp;- `CCd`: The directory where censored files will be saved.<br>
            &emsp;&emsp;- `FlaTyp`: Dictionary containing censoring flags.<br>
        • Return: <br>
        &emsp;&emsp;- None.<br>

   11. `main()`<br>
        • Description: <br>
        &emsp;&emsp;- This function serves as the main entry point of the script.<br>
        &emsp;&emsp;- It parses command-line arguments, identifies input files, processes them, and performs censorship based on specified flags.<br>
        &emsp;&emsp;- Creates an output directory if it doesn't exist.<br>
        &emsp;&emsp;- Handles some exceptions like Printing an error message to prompt user for specifing censoring flags.<br>
        &emsp;&emsp;- Prints error message if input files is not found.<br>
        • Parameters: <br>
        &emsp;&emsp;- None<br>
        • Return: <br>
        &emsp;&emsp;- None.<br>
        
        
## Testing

Testing using pytest & mocking is done to make sure that all the functions are working independently and properly. Testing is crucial for early bug detection and maintaining code quality. Testing units of code encourages modular, understandable code and integrates seamlessly into continuous integration workflows, boosting integrity. The given unittesting code tests various functions related to censoring sensitive information such as names, dates, addresses, and phone numbers in a given text. Ultimately, all major functions like test_names, test_dates, test_addresses, test_phone_numbers and more are tested if they are functioning properly. For example. test_names verifies if the spacy model is able to identify names in the given text file. 

    1.  `test_censor`
        Purpose: 
        - Tests the `censor` function, which is expected to replace sensitive information in a given text with a block character.
        Steps:
            -> Defines test data including the input text (tempdata), detected entities (Detected), and the expected output after censoring (out).
            -> Invokes the `censor` function with the test data.
            -> Asserts that the output matches the expected output

     2. `test_CenName` 
        Purpose: 
        -  Tests the `CenName` function, which is expected to detect names in a given text.
        Steps:
             -> Mocks the Spacy model using the @patch decorator.
             -> Defines mock data for the Spacy model to return.
             -> Sets up test data containing input text (tempdata) and the expected detected names (out).
             -> Invoke the `CenName` function with the test data.
             -> Assert that the detected names match the expected output.

    3. `test_CenDate`
        Purpose: 
        - Tests the `CenDate` function, which is expected to detect dates in a given text.
        Steps:
             -> Mock the Google Cloud NLP API using the @patch decorator.
             -> Define mock data for the API response.
             -> Set up test data containing input text (tempdata) and the expected detected dates (out).
             -> Invoke the `CenDate` function with the test data.
             -> Assert that the detected dates match the expected output.

    4. `test_CenLoc`
        Purpose: 
        - Tests the `CenLoc` function, which is expected to detect addresses in a given text.
        Steps:
             -> Mock the Google Cloud NLP API using the @patch decorator.
             -> Define mock data for the API response.
             -> Set up test data containing input text (tempdata) and the expected detected addresses (out).
             -> Invoke the `CenLoc` function with the test data.
             -> Assert that the detected addresses match the expected output.

    5. `test_CenNum`
        Purpose: 
        - Tests the CenLoc function, which is expected to detect phone numbers in a given text.
        Steps:
              -> Mock the Google Cloud NLP API using the @patch decorator.
              -> Define mock data for the API response.
              -> Set up test data containing input text (tempdata) and the expected detected phone numbers (out).
              -> Invoke the `CenNum` function with the test data.
              -> Assert that the detected phone numbers match the expected output.



##### General Classes in test: 

1. `TestCensoringFunctions` class: This is the main test class that inherits from unittest.TestCase. It contains several test methods to test different functionalities of the censoring functions.

2. `MockEntity` class: A mock class to simulate entities detected by Spacy.

3. `MockResponse` class: A mock class to simulate responses from the Google Cloud NLP API or similar services.

4. `MockGoogleEntity` class: A mock class to simulate entities returned by the Google Cloud NLP API or similar services.

## Bugs and Assumptions

• Assuming that atleast any one of the flag should be given in the run command. <br>
• A large text files or a high volume of data exceeding system memory or processing limits, can lead to performance degradation or application crashes.<br>
• All the entities are not accurately detected, it leaves some entities according to the model selected.<br>
• I have used en_core_web_md model as given in assignment description. I could have used the large model(en_core_web_md) but it detects some extra data which should not be sensored compared to the Spacy medium English model.<br>
• Known bug: Some txt files with unsual formatting are not able to parse.<br> 
• It does not check censor names in email addresses. <br>
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
• [Google API services](https://cloud.google.com/products?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-b-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422238-ADGP_Hybrid+%7C+BKWS+-+MIX+%7C+Txt-Google+Products-Google+Products+General-KWID_43700077225654153-kwd-305853018146&utm_term=KW_google%20cloud%20api-ST_google+cloud+api&gad_source=1&gclid=CjwKCAiA0bWvBhBjEiwAtEsoW4c9xSrIqN7aa-RqxnDZEvpJvMpjHFvof4xKSOGmutlJ6hapBB_iPBoCW4kQAvD_BwE&gclsrc=aw.ds)- Helped me in understanding google natural language API usage<br>
• [Cloud Natural Language API](https://cloud.google.com/natural-language/docs/reference/rest)- Documentation reference for understanding GCP Cloud Natural Language API<br> 
• [Spacy Models](https://spacy.io/models/en)- Documentation for English Spacy Models <br>
• [NLTK Tokenize](https://www.nltk.org/api/nltk.tokenize.html)- Documentation for nltk.tokenize package <br>
