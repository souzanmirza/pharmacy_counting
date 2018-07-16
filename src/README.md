This folder contains the source files which implement the solution. *pharmacy_main.py* reads in the input file and uses the helper functions in *pharmacy_helper.py* to process the input in a dict and outputs the sorted results to a file. Below is the documentation for the source files.

NAME
    pharmacy_main

FUNCTIONS
```
    main()
        input: comma separated file of [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
        output: comma separated file of drug, number of unique prescribers, total cost in order
                of cost and then alphabetical if cost is the same.
        method: using a hash table implemented by dict the input is read in and processed within a
                dict that uses the drug for a key and a dict as the value which contains the unique
                prescriber_id's and the total cost. the dict is output to a list of tuples
                (key, values) and sorted first alphabetically by drug name (key) and then by
                decreasing cost (values['cost']). the ordered dict is then written as a
                comma separated file of drug, number of unique prescribers, total cost.
```

NAME
    pharmacy_helper

FUNCTIONS
```
    addEntry(entry, dict)
        Adds an entry to the dictionary. drug is the key with a dictionary value containing the 
        unique prescriber_id's and total cost.
        :param entry: [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
        :param dict: dictionary of entries
        :return: dict with entry added or updated
    
    positiveNumber(field)
        Checks if field is a positive decimal number.
        :param field: string
        :return: Decimal(field) if decimal float. False otherwise.
    
    validEntry(entry)
        Checks if the entry is valid. Calls isPositiveNumber to check if the prescriber_id and 
        cost are positive decimals.
        :param entry: [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
        :return: True if valid and entry with updated fields. False otherwise.

```
