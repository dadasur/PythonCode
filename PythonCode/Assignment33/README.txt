README File Requirements
Create a file named:
README.md
The README file should contain the following sections:
1. Project Title
Duplicate File Removal Automation
2. Project Description
Explain that the script periodically scans a directory, detects duplicate files using checksums, deletes duplicate 
copies, creates a detailed log file, and sends the log file through email.
3. Features
Mention features such as:
* Recursive directory scanning
* Checksum-based duplicate detection
* Automatic duplicate-file deletion
* Timestamp-based log generation
* Periodic execution
* Email notification
* Log-file attachment
* Input validation
* Exception handling
* Modular programming
4. Requirements
Mention:
* Supported Python version
* Required Python libraries
* Internet connection for sending email
* Email application password or SMTP credentials
5. Project Structure
Explain the purpose of every Python module and directory.
6. Command-Line Options
Document all required arguments:
Directory path
Time interval in minutes
Receiver email address
7. Execution Command
python DuplicateFileRemoval.py E:/Data/Demo 50 
marvellousinfosystem@gmail.com
8. Help Command
python DuplicateFileRemoval.py --help
9. Usage Command
python DuplicateFileRemoval.py --usage
10. Log-File Information
Explain where the logs are stored and how the log filename is generated.
11. Email Configuration
Explain how sender email credentials should be configured securely.
12. Important Notes
Mention that:
* Deleted files may not be recoverable.
* Testing should first be performed on a sample directory.
* Email passwords should not be hard-coded.
* The first file from each duplicate group should be preserved.
* Files should be considered duplicates only when their checksums are identical.
