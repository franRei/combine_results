import csv

class Reader:
    def __init__(self):
        pass

    def read_csv(self,filename):
        with open(filename) as csv_data:
            line_count = 0
            words = []
            reader = csv.DictReader(csv_data)

            for lines in reader:
                word_group = lines["ID"].strip(), lines["form"].strip(), lines["lang_id"],lines["PGer"].strip()
                words.append(word_group)
                line_count+=1
        print(line_count)
        return words

    def read_csv_cognates(self,filename):
        with open(filename) as csv_data:
            line_count = 0
            words = {}
            reader = csv.DictReader(csv_data)
            com_words = []
            for lines in reader:
                word_group = lines["ID"].strip(), lines["Form_ID"].strip(), lines["Form"],lines["Cognateset_ID"].strip()
                words[lines["Form_ID"]] = word_group
                #print(word_group)
                line_count+=1
                com_words.append(word_group)
        print(line_count)
        return words, com_words

    def read_csv_forms(self,filename):
        with open(filename) as csv_data:
            line_count = 0
            words = {}
            reader = csv.DictReader(csv_data)
            com_words = []
            for lines in reader:
                word_group = lines["ID"].strip(), lines["Language_ID"].strip(), lines["Orthography"]
                words[lines["Orthography"]] = word_group
                line_count+=1
                com_words.append(word_group)
        print(line_count)
        return words, com_words