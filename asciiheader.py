# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
------------------------------------------------------------------------------------------------------------------
ASCII GRID HEADER CHANGER

File name: asciiheader.py
Description: This is a simple python script to change an ESRI ascii header for several files at a time, using csv, 
glob and numpy python libraries..
Author:Carolina Arias Munoz
Date Created: 08/03/2016 ‎
Python version: 2.7
------------------------------------------------------------------------------------------------------------------
"""
import csv, numpy
import glob



grid_ncols = 177
grid_nrows = 174
grid_xllcorner = 417146.09000
grid_yllcorner = 4916522.59000
grid_cellsize = 1500
grid_nodata = -9999

#Grid headers for ESRI
grid_header = 'ncols %d\n' % grid_ncols
grid_header += 'nrows %d\n' % grid_nrows
grid_header += 'xllcorner %s\n' % grid_xllcorner
grid_header += 'yllcorner %s\n' % grid_yllcorner
grid_header += 'cellsize %s\n' % grid_cellsize
grid_header += 'nodata_value %d\n' % grid_nodata

data_path = '/media/sf_2_PhD_2013_-2014/1PhD_WorkDocs/PhD_Data-calculations/data/OI_precipitazione_nov_dic_2013/'
data_files = glob.glob(data_path + '*.txt')

for data_file in data_files:
     
    filename = ''.join(['/media/sf_2_PhD_2013_-2014/1PhD_WorkDocs/PhD_Data-calculations/data/rainascii/',data_file[99:120],'.asc'])
    inputFile = open(data_file, "r+") 
    outputFile = open(filename, "w")
    header1 = inputFile.readline()
    header2 = inputFile.readline()
    header3 = inputFile.readline()
    header4 = inputFile.readline()   
    header5 = inputFile.readline()   
    header6 = inputFile.readline() 
    outputFile.write('                                                                                              ')
#    outputFile.write('\n')
    for line in inputFile:
        outputFile.write(line)
        #print line
#   outputFile.writelines(inputFile.readlines()[6:181])
    inputFile.close()
    outputFile.close()

print 'Values written in a txt files. Adding the header...'
        
for data_file in data_files:
     
    filename = ''.join(['/media/sf_2_PhD_2013_-2014/1PhD_WorkDocs/PhD_Data-calculations/data/rainascii/',data_file[99:120],'.asc'])
    outputFile = open(filename, "r+")
    outputFile.write('ncols 177'+ '\n')
    outputFile.write('nrows 174'+ '\n')
    outputFile.write('xllcorner 417146.09'+ '\n')
    outputFile.write('yllcorner 4916522.59'+ '\n')
    outputFile.write('cellsize 1500'+ '\n')
    outputFile.write('nodata_value -9999'+'\n')
    outputFile.close()
    
print 'Done. Check your ascii files'
    
    
    
    
    