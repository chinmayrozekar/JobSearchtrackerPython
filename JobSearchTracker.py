# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:09:51 2024

@author: crozekar
"""



import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
import csv
import os
from datetime import datetime

class JobApplicationTracker:
    def __init__(self, master):
        self.master = master
        master.title("Job Application Tracker")
        master.geometry('500x250')  # Adjusted window size for the extra input field
        master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind the close event

        self.csv_file = 'applied_jobs.csv'  # The name of the CSV file
        self.applied_jobs = []  # List to store dictionaries of company names, job titles, and job links
        self.load_applied_jobs()  # Load existing jobs from CSV

        self.counter = len(self.applied_jobs)  # Set the initial counter value based on loaded jobs
        self.target = 50

        self.label = Label(master, text="Have you applied for a job today?")
        self.label.pack()

        Label(master, text="Enter the company name:").pack()
        self.company_entry = Entry(master, width=50)
        self.company_entry.pack()

        Label(master, text="Enter the position/Job Title:").pack()
        self.title_entry = Entry(master, width=50)
        self.title_entry.pack()

        Label(master, text="Enter the job link:").pack()
        self.link_entry = Entry(master, width=50)
        self.link_entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.record_application)
        self.submit_button.pack()

        self.counter_label = Label(master, text=f"Jobs applied for today: {self.counter}")
        self.counter_label.pack()

        self.target_label = Label(master, text=f"Target applications: {self.target}")
        self.target_label.pack()

        self.show_list_button = Button(master, text="Show Applied Jobs", command=self.export_applied_jobs)
        self.show_list_button.pack()

    def load_applied_jobs(self):
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.applied_jobs = [row for row in reader]
        except FileNotFoundError:
            pass

    def record_application(self):
        company_name = self.company_entry.get()
        job_title = self.title_entry.get()
        job_link = self.link_entry.get()
        today_date = datetime.now().strftime("%m/%d/%Y")  # Get today's date in the desired format
        if company_name and job_title and job_link:
            new_job = {'Date': today_date, 'Company': company_name, 'Title': job_title, 'Link': job_link}
            self.applied_jobs.append(new_job)
            self.counter += 1
            self.counter_label.config(text=f"Jobs applied for today: {self.counter}")
            self.company_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            self.export_applied_jobs()  # Save to CSV each time a job is submitted
            if self.counter >= self.target:
                messagebox.showinfo("Congratulations!", "You've reached your target for today!")

    def export_applied_jobs(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['Date', 'Company', 'Title', 'Link']  # Add 'Date' to the fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for job in self.applied_jobs:
                writer.writerow(job)

    def on_closing(self):
        self.export_applied_jobs()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = JobApplicationTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
