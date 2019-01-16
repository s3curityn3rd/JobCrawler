# JobCrawler
Created 01/13/2019
Version 1.0

Designed to be modifiable the objective was to keep an eye out for a few select jobs that I wanted.

Currently as it stands, I'm seeking a few specific roles from the three companies whose names are present. For my privacy, I've removed the titles and locations from this script. (Unless you are a hiring manager at those places, in which case, @S3curityN)

The looking_for lists on  each function are designed to put the title of the job you are seeking.

avoid should be set to a list of specific flags you are trying to avoid in a job title. (Ex. Engineer, Senior, Junior, Technician, etc.)

location should be replaced to match the formatting from the respective job company. 

This program requires a twilio account in order to send yourself a text once it's found a match. 

Replace the account_sid and auth_token variables with information provided from your twilio account. 
Replace the to_ and from_ parameters in text_me() to the appropriate twilio information. 

I'm by no means a professional programmer, I just like fun ways to push my limtis and challenge myself. I'm also in the job market. 
