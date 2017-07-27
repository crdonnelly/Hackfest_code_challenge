"""""
four_letters_in_common(source, dictionary) function
Version 0.9
Description:
Takes a source string and dictionary list as arguments and returns a list of
dictionary words that match at least 4 consecutive letters in common with the
source word.

Arguments:
source: An english word as a string (Must be at least 4 letters long) - Type str
dictionary: A list of English words - Type list

Returns:
output_list: A list of English words that match the criteria - Type list

By Cameron Donnelly 27/07/2017
"""""

def four_letters_in_common(source, dictionary):

    permutations = [] #List which holds all 4 letter permutations of the source word
    index = 0
    output_list = [] # List of dictionary words that will be returned
    
    if len(source) < 4:
        print("Source word must be at least 4 characters long")
        return
    else:
        permutations += [source[index:index + 4]]
        index += 1
        while index + 4 <= len(source):
            permutations += [source[index:index + 4]]
            index += 1
        for i in range(len(dictionary)):
            for j in range(len(permutations)):
                if permutations[j] in dictionary[i]:
                    if dictionary[i] not in output_list:
                        output_list += [dictionary[i]]

    return output_list

                
def four_letters_in_common_test():
    tests_completed = 0
    sample_dictionary = ["AMPLITUDE", "AMPLITUDES", "APLITE", "APLITES", "APLITIC", "DISPLING", "EARSPLITTING", "HAIRSPLITTER", "HAIRSPLITTERS", "HAIRSPLITTING", "HAIRSPLITTINGS", "HAPLITE", "HAPLITES", "HAPLITIC", "HOPLITE", "HOPLITES", "HOPLITIC", "LAMPLIT", "POPLITEAL", "POPLITEI", "POPLITEUS", "POPLITIC", "PRESPLIT", "RESPLICE", "RESPLICED", "RESPLICES", "RESPLICING", "RESPLIT", "RESPLITS", "RESPLITTING", "SHINSPLINTS", "SIDESPLITTING", "SIDESPLITTINGLY", "SPLICE", "SPLICED", "SPLICER", "SPLICERS", "SPLICES", "SPLICING", "SPLICINGS", "SPLIFF", "SPLIFFS", "SPLINE", "SPLINED", "SPLINES", "SPLINING", "SPLINT", "SPLINTED", "SPLINTER", "SPLINTERED", "SPLINTERIER", "SPLINTERIEST", "SPLINTERING", "SPLINTERS", "SPLINTERY", "SPLINTING", "SPLINTLIKE", "SPLINTS", "SPLINTWOOD", "SPLINTWOODS", "SPLISH", "SPLISHED", "SPLISHES", "SPLISHING", "SPLIT", "SPLITS", "SPLITTED", "SPLITTER", "SPLITTERS", "SPLITTING", "SPLITTINGS", "SPLITTISM", "SPLITTISMS", "SPLITTIST", "SPLITTISTS", "TRIPLITE", "TRIPLITES", "UNSPLINTERABLE", "UNSPLIT", "UPLIT", "WASPLIKE", "WISPLIKE"]
    try:
        four_letters_in_common("SPLIT", sample_dictionary)
        tests_completed += 1
    except:
        print("Error with Test 1")
    finally:
        try:
            four_letters_in_common("SPL", sample_dictionary)
            tests_completed += 1
        except:
            print("Error with Test 2")
        finally:
            print(str(tests_completed) + "/2 Tests completed")
        
