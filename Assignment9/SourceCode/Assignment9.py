import csv

def read_in_file(user_input):
    full_file = []
    while True:
        try:
            with open(user_input, newline='') as new_file:
                file_info = csv.reader(new_file)
                for row in file_info:
                    full_file.append(row)
                return full_file
        except FileNotFoundError:
            print('Could not find file {}.'.format(user_input))
            user_input = input('Enter new file name: ')

def month_from_number(num):
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
             7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    if num in months:
        return months[num]
    else:
        print('Number must be 1-12')

def create_reported_date_dict(file):
    dates_reported = {}
    for i in file[1:]:
        date = i[1]
        if date in dates_reported:
            dates_reported[date] += 1
        else:
            dates_reported[date] = 1
    return dates_reported
    
def create_reported_month_dict(lst):
    reported_month_dict = {}
    for row in lst[1:]:
        date = row[1]
        mdy = date.split('/')
        if mdy[0] not in reported_month_dict:
            reported_month_dict[mdy[0]] = 1
        else:
            reported_month_dict[mdy[0]] += 1
    return reported_month_dict

def create_offence_dict(lst):
    offence_dict = {}
    for row in lst[1:]:
        offence = row[7]
        if offence in offence_dict:
            offence_dict[offence] += 1
        else:
            offence_dict[offence] = 1
    return offence_dict

def create_offence_by_zip(lst):
    offence_by_zip = {}
    for row in lst[1:]:
        offence, zipcode = row[7], row[13]
        if offence not in offence_by_zip:
            offence_by_zip[offence] = {}
        if zipcode not in offence_by_zip[offence]:
            offence_by_zip[offence][zipcode] = 1
        else:
            offence_by_zip[offence][zipcode] += 1
    return offence_by_zip

if __name__ == "__main__":
    user_file = input('Please enter a file name: (csv) ')
    file = read_in_file(user_file)
    month_dict = create_reported_month_dict(file)
    month, monthly_high = '', 0
    for key, value in month_dict.items():
        if value > monthly_high:
            month, monthly_high = key, value
    month = month_from_number(int(month.strip('0')))
    print('\nThe month with the highest number of crimes is {} with {} offences.'.format(month, monthly_high))
    offences_dict = create_offence_dict(file)
    offence, off_high = '', 0
    for key, value in offences_dict.items():
        if value > off_high:
            offence, off_high = key, value
    print('The offence with the highest number of crimes is {} with {} offences.'.format(offence, off_high))
    offences_by_zip_dict = create_offence_by_zip(file)
    offence_search = input('Enter an offence: ')
    while offence_search not in offences_by_zip_dict:
        print('Could not find {} as an offence reported.'.format(offence_search))
        offence_search = input('\nEnter an offence: ')
    print('{} offences by Zipcode'.format(offence_search))
    print('{:<10}{:>10}'.format('Zipcode', '# Offences'))
    print('=' * 20)
    offence_search_dict = offences_by_zip_dict[offence_search]
    for i in offences_by_zip_dict[offence_search]:
        print('{:<10}{:>10}'.format(i, offence_search_dict[i]))
