# Job_search-tracker_python-
A simple GUI in python to track your JOBS

# Job Application Tracker

## Overview
The Job Application Tracker is a simple desktop application built with Python's Tkinter library. It allows users to keep track of job applications by entering company names and corresponding job links. It is designed to help job seekers maintain a record of their applications and ensure they meet their daily application goals.

## Features
- GUI for easy interaction.
- Fields to enter company names and job application links.
- Submit button to record each job application.
- Counter to display the number of jobs applied for in a session.
- Target goal of job applications to reach.
- Functionality to export the list of applied jobs to a CSV file for persistence and external use.
- Automatically opens the CSV file with the system's default CSV viewer.

## Prerequisites
Before running the Job Application Tracker, ensure you have the following:
- Python 3.x installed on your system.

## How to Use
1. Clone the repository or download the `job_application_tracker.py` file to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where `job_application_tracker.py` is located.
4. Run the script using the command `python job_application_tracker.py`.
5. The application window will appear. You can now start recording your job applications.

## Recording Job Applications
1. In the text fields provided, enter the company name and the link to the job application.
2. Click the "Submit" button to record each job application.
3. The counter at the bottom will update with the number of jobs you've applied for.
4. If you reach your target for the day, a congratulatory message will appear.

## Viewing Applied Jobs
1. Click on "Show Applied Jobs" to export the list of applied jobs to a CSV file.
2. The CSV file will automatically open, allowing you to view all the jobs you have applied for.

## CSV File
The CSV file `applied_jobs.csv` will be saved in the same directory as the script. Each row contains the company name and the job link you entered.

## Customization
You can modify the target number of job applications by changing the `self.target` value in the code.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
For support, feedback, or contributions, please contact [your-email@example.com].
