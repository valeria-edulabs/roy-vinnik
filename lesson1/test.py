# import datetime
from datetime import date, timedelta


def get_working_days(from_date, to_date):
    print(f"Inside get_working_days, from {from_date}, to: {to_date}")
    counter = 0
    list_of_dates = []
    # list_of_dates = list()
    curr_date = from_date
    while curr_date <= to_date:
        # working days are between 0 and 4 including
        # 0 is monday
        if 0 <= curr_date.weekday() <= 4:
            # counter = counter + 1
            counter += 1
            list_of_dates.append(curr_date)

        curr_date = curr_date + timedelta(days=1)

    return counter, list_of_dates

# Service_type - this is the type of monthly service: Sales tax, income tax, SOS
# freq - this is how often we need to submit the reports. monthly, qtr or annually
# date_of_the_month - this is the date of the month that we need to file the report (based on the freq)

def generate_due_dates_based_of_service_type_and_freq( freq, date_of_the_month):
    pass


# print(dir())
# from_date = date.today()
# to_date = date(2023, 5, 23)
# working_days, list_of_dates = get_working_days(from_date, to_date)
# print(f"Amount of working days excluding weekends between {from_date} and {to_date} is: {working_days}")
# print(list_of_dates)
# for one_date in list_of_dates:
#     # print(type(one_date))
#     print(one_date.strftime("%m/%d/%Y, %A"))


service_type_to_freq = {
    'sales_tax': ['annually', 'monthly', 'quarterly'],
    'income_tax': {
        'federal': {
            'without_extension': {'month': 4, 'date': 15},
            'with_extension': {'month': 10, 'date': 15}
        },
        'state': {
            'NY': {
                'without_extension': {'month': 2, 'date': 15},
                'with_extension': {'month': 8, 'date': 15}
            },
            'NJ': {
                'without_extension': {'month': 1, 'date': 15},
                'with_extension': {'month': 7, 'date': 15}
            }
        }
    },
    'sos': ['annually'],
    'property_tax': ['annually']
}
print(service_type_to_freq['income_tax']['state']['NJ']['with_extension'])
# print(service_type_to_freq['sos'])
# print(service_type_to_freq['sales_tax'])


# s = 5 + 6
# s = sum([3,4,5,6])
# l = [1,2,3,4]
# x = l.append(5)
