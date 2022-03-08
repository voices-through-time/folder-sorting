# folder-sorting

This script will rename transcript '.txt' files with the correct archive number, in place of the zooniverse ID


1. Approve and download transcribed data from ALICE Zooniverse. Groups of downloaded documents will be downloaded in a zip file. 

2. Unzip the files and place each folder within this directory, at the same level of the sorting script. i.e
- sorting-script.py
- folder-of-approved-transcripts-1
- folder-of-approved-transcrips-2

4. Double check the 

3. run the script from the command line with python:
`$ python sorting-script`

4. You should have have a new 'transcribed' folder in the directory, with a '.txt' and '.csv' versions of each transcript. Upload these to sharepoint.


## Important notes
This script has been configured for the 'Petitions Admitted' documents, which has a archive reference 21 digits long.

When extracting transcripts from other documents, you must check how long the reference numbers are and update the script accordingly. This is highlighted in lines 48 - 53 of the text. 

For example, in the 'Billet Books' records, the archive reference is 17 digits long. In this case the line at 51 will need to be changed to look like this:
`document_number = internal_id[0 : 17]`

Do not mix types of records when using this script. i.e, do not mix 'Petitions Admitted' with 'Billet Books'. Only extract one type of record at a time.

