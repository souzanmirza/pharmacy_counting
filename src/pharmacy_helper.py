import math

def positiveNumber(field):
    """
    Checks if field is a positive float.
    :param field: string
    :return: float(field) if positive float. False otherwise.
    """
    try:
        tmp = float(field)
        if tmp < 0:
            return False
        if math.isnan(tmp):
            return False
        return tmp
    except ValueError:
        return False
    except TypeError:
        return False


def validEntry(entry):
    """
    Checks if the entry is valid. Calls isPositiveNumber to check if the prescriber_id and cost are positive floats.
    :param entry: [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
    :return: True if valid and entry with updated fields. False otherwise.
    """
    if entry is None:
        return False
    if not len(entry) == 5:
        return False
    field0 = positiveNumber(entry[0])
    field4 = positiveNumber(entry[4])
    if field0 is not False and field4 is not False:
        entry[0] = field0
        entry[4] = field4
        try:
            entry[3] = entry[3].replace('-', ' ')
        except AttributeError:
            return False
    else:
        return False
    return entry


def addEntry(entry, dict):
    """
    Adds an entry to the dictionary. drug is the key with a dictionary value containing the unique prescriber_id's and total cost.
    :param entry: [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
    :param dict: dictionary of entries
    :return: dict with entry added or updated
    """
    if validEntry(entry):
        try:
            entry_dict = {}
            if entry[3] in dict:
                entry_dict = dict[entry[3]]
                if entry[0] not in entry_dict:
                    entry_dict[entry[0]] = True
                entry_dict['cost'] = entry_dict['cost'] + entry[4]
            else:
                dict[entry[3]] = entry_dict
                entry_dict[entry[0]] = True
                entry_dict['cost'] = entry[4]
        except TypeError:
            print('Invalid dictionary')
            return False
    else:
        print('Invalid entry %s' % entry)
        return False
    return True
