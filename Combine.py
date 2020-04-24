
class Combine:
    def __init__(self):
        pass

    def combine_lists(self, kroonen, cognates, forms):
        printer_list = []
        lang = {"danish":"dan", "german":"deu", "english":"eng", "dutch":"nld", "norwegianbokmal":"nob","swedish":"swe", "icelandic":"isl"}
        lang_2 = {"dan":"da", "deu":"de", "eng":"en" , "nld":"nl", "nob":"nb", "swe":"sv", "isl":"is"}
        count = 0
        all = []
        for tups in kroonen:
            if tups[1] in forms:
                forms_tup = forms.get(tups[1])
                if tups[2] == lang.get(forms_tup[1]):
                    cognates_tup = cognates.get(forms_tup[0])
                   # print(cognates_tup[3])
                    new_tuple = tups[0], tups[1], lang_2.get(tups[2]), cognates_tup[3], tups[3]
                    #print(tups[1], forms_tup, cognates_tup)
                    #print(new_tuple)
                    count+=1
                    all.append(new_tuple)
        print(count)
        return all

