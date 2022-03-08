import os
import pathlib
import pandas as pd
import shutil
import time
import csv

# finding the path of where you are
path = pathlib.Path(__file__).parent.resolve()

# grabbing the current directories in the path
dirs = os.listdir( path ) # this grabs where you are

# Check to see if trasncribed directory exists
# if it doesn't exist - it will make a new one
if not os.path.isdir(str(path) +'/transcribed'):
  print('making new directory')
  os.mkdir(str(path) +'/transcribed')

# defining the directory where we will put the transcribed documents
transcribed_documents_path = str(path) +'/transcribed/'




def collect_data(dir, directory_name):
  # getting a dataframe of the metadat to extract internal_id
  metadata = pd.read_csv(dir + '/transcriptions_metadata.csv',index_col=False)
  metadata.columns = 'transcription_id','internal_id','reducer','caesar_parameters','date_approved','user_who_approved','text_edited','number_of_pages'

  transcripts = os.listdir( dir )

  # get inside each individual transcript directory, e.g 'transcription_NUMBER'
  for transcription_directory in transcripts:
    # saving the directory name for inside transcription directory
    tdir = dir + '/' + transcription_directory

    
    if (os.path.isdir(tdir)):
      for file in os.listdir(tdir):
        # getting every .txt file to rename
        if file.endswith(".txt"):

          # get the Zooniverse ID number from the file name
          file_name = str(file)
          number = int(''.join(filter(str.isdigit, file_name)))


          # commented out - useful for debugging
          # print(number)
          # if number == 62619571:
          #   import code; code.interact(local=dict(globals(), **locals()))

          # Getting internal_id from metadata dataframe
          row = metadata.loc[metadata['transcription_id'] == number]
          row_index = row.index[0]
          
          internal_id = str(metadata.loc[metadata.index[row_index], 'internal_id'])
          new_file_name = internal_id + '.txt'
          csv_file_name = internal_id + '.csv'
            
          # Get the document number for the file name
          document_number = internal_id[0 : 21]

          old_file = tdir + '/' + file
          new_file = transcribed_documents_path + '/' + document_number + "/" + new_file_name
          new_csv_file = transcribed_documents_path + '/' + document_number + "/csv/" + csv_file_name

          
          # check if directory currently exists
          if not os.path.isdir(transcribed_documents_path + '/' + document_number):
            print("Making directory")
            os.mkdir(transcribed_documents_path + '/' + document_number)
            os.mkdir(transcribed_documents_path + '/' + document_number + '/csv/') 
            

          # copying and renaming file          
          shutil.copy(old_file, new_file)

          # create csv file of the same
          df = pd.read_fwf(old_file)
          df.to_csv(new_csv_file)

  

# Iterate through folders in directory
for item in dirs:
  item_dir = str(path) + "/" + str(item)
  if (os.path.isdir(item_dir)):

    # make sure the transcribed data isn't indexed
    if not item_dir + '/' == transcribed_documents_path:
      collect_data(item_dir, item)



