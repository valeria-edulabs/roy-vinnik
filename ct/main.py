import pprint
from csv import DictReader

from ct.data.ct_report import TaxReporter

if __name__ == '__main__':

    with open('data/main_process.csv') as f:
        list_of_jobs = list(DictReader(f))

        # access item 'steps_tab' on the second row
        # print(list_of_jobs[1]['steps_tab'])

        for job in list_of_jobs:
            pprint.pprint(job)
            # print(job['steps_tab'])
            reporter = TaxReporter(
                intake_file=job['customer_intake'],
                website_url=job['url'],
                steps_file=job['steps_tab'])
            reporter.submit()


    # ct_reporter = TaxReporter(data_file='./data/ct_data1.csv',
    #                           website_url="https://drs.ct.gov/eservices/_/#2",
    #                           steps_file='data/ct_process.csv')
    # ct_reporter.report()