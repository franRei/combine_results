
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

                    new_tuple = tups[0], tups[1], lang_2.get(tups[2]), cognates_tup[3], tups[3]

                    count+=1
                    all.append(new_tuple)
        print(count)
        return all

    def combine_other_lists(self, cognates, forms):
        lang = {"danish": "dan", "german": "deu", "english": "eng", "dutch": "nld", "norwegianbokmal": "nob",
                "swedish": "swe", "icelandic": "isl"}
        lang_2 = {"dan": "da", "deu": "de", "eng": "en", "nld": "nl", "nob": "nb", "swe": "sv", "isl": "is"}
        liste = []
        for tups in forms.items():

            if tups[1][1] in lang:
                cog_set = cognates[tups[1][0]]

                word_group = tups[1][0], tups[0], lang_2.get(lang.get(tups[1][1])), cog_set[3]

                liste.append(word_group)
                print(word_group)
        print("Hier", len(liste))
        return liste



