def open_file(prompt, mode = 'r'):
    while True:
        try:
            file_name = input(prompt)
            in_file = open(file_name, mode)
            return in_file
        except FileNotFoundError:
            print('File {} could not be opened.'.format(file_name))
        except IOError:
            print('There was an IO Error for', file_name)
        
def get_min_mpg(inpt):
    while True:
        try:
            min_mpg = float(input(inpt))
            if min_mpg <= 0:
                print('The combined fuel economy must be more than 0 mpg.')
            elif min_mpg > 100:
                print('The combined fuel economy must be below 100 mpg.')
            else:
                return min_mpg
        except ValueError:
            print('Please enter a number.')

min_mpg = get_min_mpg('Enter the minimum MPG: ')
my_file = open_file('Enter the file you would like to open: ')
lines = my_file.readlines()
stats = lines[1:]
car_data = []
out_file = open_file('Enter the file you would like to write to: ', mode = 'w')
for line in stats:
    try:
        lst = line.split('\t')
        if float(lst[7]) >= min_mpg:
            car_data.append([lst[0], lst[1], lst[2], lst[7]])
    except ValueError:
        print('Could not convert value {} for {} {} {}.'.format(lst[7], lst[0], lst[1], lst[2]))

my_file.close()

for line in car_data:
    out_file.write('{:<5}{:<11}{:<40}{:>10}\n'.format(line[0], line[1], line[2], line[3]))
out_file.close()
