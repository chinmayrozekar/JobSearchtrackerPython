# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:09:51 2024

@author: crozekar
"""

import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
import csv
import os

class JobApplicationTracker:
    def __init__(self, master):
        self.master = master
        master.title("Job Application Tracker")
        master.geometry('500x200')  # Setting the window size

        self.counter = 0
        self.target = 50
        self.applied_jobs = []  # List to store dictionaries of company names and job links

        self.label = Label(master, text="Have you applied for a job today?")
        self.label.pack()

        Label(master, text="Enter the company name:").pack()
        self.company_entry = Entry(master, width=50)
        self.company_entry.pack()

        Label(master, text="Enter the job link:").pack()
        self.link_entry = Entry(master, width=50)
        self.link_entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.record_application)
        self.submit_button.pack()

        self.counter_label = Label(master, text="Jobs applied for today: 0")
        self.counter_label.pack()

        self.target_label = Label(master, text=f"Target applications: {self.target}")
        self.target_label.pack()

        self.show_list_button = Button(master, text="Show Applied Jobs", command=self.export_applied_jobs)
        self.show_list_button.pack()

    def record_application(self):
        company_name = self.company_entry.get()
        job_link = self.link_entry.get()
        if company_name and job_link:
            self.counter += 1
            self.counter_label.config(text=f"Jobs applied for today: {self.counter}")
            self.applied_jobs.append({'Company': company_name, 'Link': job_link})
            self.company_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            if self.counter >= self.target:
                messagebox.showinfo("Congratulations!", "You've reached your target for today!")

    def export_applied_jobs(self):
        with open('applied_jobs.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Company', 'Link'])
            writer.writeheader()
            for job in self.applied_jobs:
                writer.writerow(job)
        os.startfile('applied_jobs.csv')  # Opens the CSV with the default application

def main():
    root = tk.Tk()
    app = JobApplicationTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
