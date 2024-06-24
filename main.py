"""
Project Name: Was Clinton Right?
Author: Cody Behling
Course: CS1400-X01

My program is designed to analyze data regarding private-sector jobs created between 1961 - 2012.
The program will organize the data into Democratic/Republican parties to determine whether Clinton's claim was correct.
The data will be compared and the program will print the conclusion.
While developing this program, I learned about the epoch function to create datetimes.
This program requires two files in order to run successfully, the BLS_private.csv file and the presidents.txt file.
The data provided in the BLS_private.csv file was initially incorrect. It was renamed badData.csv.
In order to execute the program, run the main() function.
"""

import csv
import datetime


def partisan(data):
    """function to calculate the differences between democratic and republican parties"""
    dPos = 0
    dNeg = 0
    rPos = 0
    rNeg = 0
    prevJobs = data[0]['Jobs']
    for row in data:
        newJobs = row['Jobs'] - prevJobs
        if newJobs >= 0:
            if row['Party'] == 'Republican':
                rPos += newJobs
            elif row['Party'] == 'Democrat':
                dPos += newJobs
        elif newJobs < 0:
            if row['Party'] == 'Republican':
                rNeg -= newJobs
            elif row['Party'] == 'Democrat':
                dNeg -= newJobs
        prevJobs = row['Jobs']
    dNet = dPos - dNeg
    rNet = rPos - rNeg
    return dNet*1000, rNet*1000, dPos*1000, rPos*1000, dNeg*1000, rNeg*1000


def epoch_conversion(year, month):
    """function to convert epoch numbers into datetimes"""
    if month < 10:
        date_str = f'{year}-0{month}'
    else:
        date_str = f'{year}-{month}'
    str_to_dt = datetime.datetime.strptime(date_str, '%Y-%m')
    newDate = int(str_to_dt.timestamp())
    return newDate


def combine_data(pres_data, job_data):
    """function to combine the data from the csv and txt files"""
    newList = []
    for data in job_data:
        for president in pres_data:
            if president['startDate'] <= data['epoch'] <= president['endDate']:
                newDict = {
                    'Name': president['name'],
                    'Party': president['party'],
                    'Month': data['month'],
                    'Year': data['year'],
                    'Jobs': data['jobs']
                }
                newList.append(newDict)
    return newList


def month_lookup(month_name):
    """function to convert month names into number designations"""
    monthNumber = 0
    if month_name == 'Jan':
        monthNumber = 1
    elif month_name == 'Feb':
        monthNumber = 2
    elif month_name == 'Mar':
        monthNumber = 3
    elif month_name == 'Apr':
        monthNumber = 4
    elif month_name == 'May':
        monthNumber = 5
    elif month_name == 'Jun':
        monthNumber = 6
    elif month_name == 'Jul':
        monthNumber = 7
    elif month_name == 'Aug':
        monthNumber = 8
    elif month_name == 'Sep':
        monthNumber = 9
    elif month_name == 'Oct':
        monthNumber = 10
    elif month_name == 'Nov':
        monthNumber = 11
    elif month_name == 'Dec':
        monthNumber = 12
    return monthNumber


def txt_format():
    """function to read and format the data from the txt file"""
    presData = []
    txtData = open("presidents.txt", "r")
    for x in txtData:
        splitValues = x.split('|')
        president = {
            'name': splitValues[0].strip(),
            'party': splitValues[1].strip(),
            'startDate': epoch_conversion(int(splitValues[3].strip()), month_lookup(splitValues[2].strip())),
            'startMonth': month_lookup(splitValues[2].strip()),
            'startYear': int(splitValues[3].strip()),
            'endDate': epoch_conversion(int(splitValues[5].strip()), month_lookup(splitValues[4].strip())),
            'endMonth': month_lookup(splitValues[4].strip()),
            'endYear': int(splitValues[5].strip())
        }
        presData.append(president)
    txtData.close()
    return presData


def csv_format():
    """function to read and format the data from the csv file"""
    jobData = []
    with open('BLS_private.csv', 'r') as csvData:
        jobReader = csv.reader(csvData, delimiter=',')

        for i, row in enumerate(jobReader):
            if i > 12:
                jan = {
                    'epoch': epoch_conversion(int(row[0]), 1),
                    'year': int(row[0]),
                    'month': 1,
                    'jobs': int(row[1])
                }
                jobData.append(jan)
                feb = {
                    'epoch': epoch_conversion(int(row[0]), 2),
                    'year': int(row[0]),
                    'month': 2,
                    'jobs': int(row[2])
                }
                jobData.append(feb)
                mar = {
                    'epoch': epoch_conversion(int(row[0]), 3),
                    'year': int(row[0]),
                    'month': 3,
                    'jobs': int(row[3])
                }
                jobData.append(mar)
                apr = {
                    'epoch': epoch_conversion(int(row[0]), 4),
                    'year': int(row[0]),
                    'month': 4,
                    'jobs': int(row[4])
                }
                jobData.append(apr)
                may = {
                    'epoch': epoch_conversion(int(row[0]), 5),
                    'year': int(row[0]),
                    'month': 5,
                    'jobs': int(row[5])
                }
                jobData.append(may)
                jun = {
                    'epoch': epoch_conversion(int(row[0]), 6),
                    'year': int(row[0]),
                    'month': 6,
                    'jobs': int(row[6])
                }
                jobData.append(jun)
                jul = {
                    'epoch': epoch_conversion(int(row[0]), 7),
                    'year': int(row[0]),
                    'month': 7,
                    'jobs': int(row[7])
                }
                jobData.append(jul)
                aug = {
                    'epoch': epoch_conversion(int(row[0]), 8),
                    'year': int(row[0]),
                    'month': 8,
                    'jobs': int(row[8])
                }
                jobData.append(aug)
                sep = {
                    'epoch': epoch_conversion(int(row[0]), 9),
                    'year': int(row[0]),
                    'month': 9,
                    'jobs': int(row[9])
                }
                jobData.append(sep)
                october = {
                    'epoch': epoch_conversion(int(row[0]), 10),
                    'year': int(row[0]),
                    'month': 10,
                    'jobs': int(row[10])
                }
                jobData.append(october)
                try:
                    nov = {
                        'epoch': epoch_conversion(int(row[0]), 11),
                        'year': int(row[0]),
                        'month': 11,
                        'jobs': int(row[11])
                    }
                except ValueError:
                    nov = {
                        'epoch': epoch_conversion(int(row[0]), 11),
                        'year': int(row[0]),
                        'month': 11,
                        'jobs': 0
                    }
                jobData.append(nov)
                try:
                    dec = {
                        'epoch': epoch_conversion(int(row[0]), 12),
                        'year': int(row[0]),
                        'month': 12,
                        'jobs': int(row[12])
                    }
                except ValueError:
                    dec = {
                        'epoch': epoch_conversion(int(row[0]), 12),
                        'year': int(row[0]),
                        'month': 12,
                        'jobs': 0
                    }
                jobData.append(dec)
    return jobData


def place_value(number):
    """formatting numbers to include commas as needed"""
    return ("{:,}".format(number))


def main():
    """main function to call other functions and print conclusions"""
    try:
        jobs = csv_format()
        presidents = txt_format()
        data = combine_data(presidents, jobs)
        democratNet, republicanNet, democratPos, republicanPos, democratNeg, republicanNeg = partisan(data)

        print("From January 1961 to December 2012, these are the statistics for private sector-jobs created:")
        print('')
        print(f'Gross jobs created during Democratic presidencies: {place_value(democratPos)}')
        print(f'Gross jobs created during Republican presidencies: {place_value(republicanPos)}')
        print(f'Gross jobs lost during Democratic presidencies: {place_value(democratNeg)}')
        print(f'Gross jobs lost during Republican presidencies: {place_value(republicanNeg)}')
        print(f'Net jobs created during Democratic presidencies: {place_value(democratNet)}')
        print(f'Net jobs created during Republican presidencies: {place_value(republicanNet)}')
        print('')
        print('In 2012, former president Bill Clinton stated:\n'
              '"Since 1961, for 52 years now, the Republicans have held the White House 28 years, the Democrats 24.\n'
              "In those 52 years, our private economy has produced 66 million private-sector jobs.\n"
              'So what\'s the jobs score? Republicans 24 million, Democrats 42 (million)."')
        print('')
        if democratPos > republicanPos:
            posDiff = democratPos - republicanPos
            print(f"As you can see, Democratic presidencies produced {place_value(posDiff)} more jobs than Republican ones.")
            print("This statistic is favorable to Clinton's claim.")
            if democratNet > republicanNet:
                netDiff = democratNet - republicanNet
                print(f"The net difference of {place_value(netDiff)} also exceeded that of Republican presidencies.")
                print('')
                print("Given these two factors, I conclude that Clinton was correct in his 2012 claim.")
            elif democratNet < republicanNet:
                netDiff = republicanNet - democratNet
                print(f"However, the net difference of {place_value(netDiff)} favored the Republican party.")
                print("While Democratic presidencies may have produced more jobs, one cannot ignore the jobs lost.")
                print('')
                print("Given these factors, I conclude that Clinton was incorrect in his 2012 claim.")
        elif democratPos < republicanPos:
            posDifference = republicanPos - democratPos
            print(f"As you can see, Republican presidencies produced {place_value(posDifference)} more jobs than Democratic ones.")
            print("This statistic is unfavorable to Clinton's claim.")
            if democratNet < republicanNet:
                netDiff = democratNet - republicanNet
                print(f"The net difference of {place_value(netDiff)} also exceeded that of Democratic presidencies.")
                print('')
                print("Given these two factors, I conclude that Clinton was incorrect in his 2012 claim.")
            elif democratNet > republicanNet:
                netDiff = republicanNet - democratNet
                print(f"However, the net difference of {place_value(netDiff)} favored the Democratic party.")
                print("While Republican presidencies may have produced more jobs, one cannot ignore the jobs lost.")
                print('')
                print("Given these factors, I conclude that Clinton was correct in his 2012 claim.")

    except ValueError:
        print("There was an error.")
    return


if __name__ == "__main__":
    main()
