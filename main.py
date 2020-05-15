from Reader import Reader
from Combine import Combine
import csv

filename_kroonen = "files/cognate-sets-kroonen2013.csv"
filename_dellert_cognates = "files/cognates.csv"
filename_dellert_forms = "files/forms.csv"

if __name__ == '__main__':
    Reader = Reader()
    kroonen = Reader.read_csv(filename_kroonen)
    cognates, com_cognates = Reader.read_csv_cognates(filename_dellert_cognates)
    forms, com_forms = Reader.read_csv_forms(filename_dellert_forms)


    print(cognates.get("19564"))

    Combine = Combine()
    combined = Combine.combine_lists(kroonen, cognates, forms)

    combine_all = Combine.combine_other_lists(cognates, forms)

    with open("results.csv", mode='w') as csv_results:
        result_writer = csv.writer(csv_results, delimiter=',')
        result_writer.writerow(['ID', 'cognate', 'lang', 'cognateID', 'borrowed', 'pgmc_forms'])
        for idx, words in enumerate(combined,1):
            result_writer.writerow([idx, words[1], words[2], words[3], '', words[4]])


    with open("results_kroonen_northeuralex.csv", mode='w') as csv_results:
        result_writer = csv.writer(csv_results, delimiter=',')
        result_writer.writerow(['ID', 'cognate', 'lang', 'cognateID', 'borrowed', 'pgmc_forms'])
        for idx, words in enumerate(combine_all,1):
            result_writer.writerow([idx, words[1], words[2], words[3], '', ''])

