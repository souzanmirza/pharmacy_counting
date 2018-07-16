# Table of Contents
1. [Problem](README.md#problem)
2. [Summary](README.md#summary)
3. [Solution](README.md#solution)
4. [Testing](README.md#testing)

# Problem

The Insight coding challenge was to generate a output list of all prescribed drugs, number of unique prescribers and total cost of the drug given an input list of drugs, prescribers and the cost the drug was prescribed for. The solution must be well tested, documented and scalable. You are allowed to chose any programming language for the implementation but you are limited to that language's built-in data types and libraries.

# Summary
* A hash table using built-in data type dict was chosen to implement the solution because it takes O(1) time for search and insert operations.
* Error handling for file I/O and type casting errors and robust checking of input entries.
* On 24 million+ test dataset achieved a runtime of ~2 min.

# Solution

I implemented my solution in python using the argparse, os, csv and decimal built-in libraries. The main objective of my solution was to be able process large dataset inputs quickly. My code take the input database entries and hashes them in a dict built-in data type. I chose a hashtable because search and insert functions take on average O(1) time and they contain only unique entries. Since the problem was concerned with collecting information about the unique drugs being prescribed, the drug was used as the key in the *drug_dict*. Each drug entry in the *drug_dict* had a value called *dictinfodict* which stored the unique ID's of the prescribers and the total cost in a dict type.

For example:

```
drug_dict = {
             'drugA': {'prescriber1:True; 'cost':100},
	     'drugB': {'prescriber1:True; 'cost':200}
	    }
```

where *druginfodict* for *drugA* is `{'prescriber1:True; 'cost':100}.`

The csv library was used to read the entries from the input file. Each entry was checked to see if it was valid which was defined as:
1. Length of entry is 5.
2. 1st entry (*prescriber_id*) can be cast to positive float represented as a Decimal.
3. 5th entry (*cost*) can be cast to positive float represented as a Decimal.
4. 4th entry (*drug*) is a string with symbols removed and replaced with whitespaces to account for any differences in spelling ie. '-' is replaced with a whitespace.

If valid the entry is added to *drug_dict*:
1. If the *drug* key does not already exist in *drug_dict* the *drug* key is added, *druginfodict* is created and set to `druginfodict={'prescriber_id'=True, 'cost'=cost}.`
2. If *drug* key already in drug_dict the *prescriber_id* is checked in the drug's corresponding *druginfodict*:
	1. If *prescriber_id* exists in the *druginfodict*, add the *cost* from this entry to `druginfodict['cost'] +=cost.`
	2. If *prescriber_id* does not exists in the *druginfodict*, add `druginfodict = {'prescriber_id':True}` and add the *cost* from this entry to `druginfodict['cost'] +=cost.`

Once all the entries have been read in from the input file the *drug_dict* is put in descending order by cost and if two drugs have the same cost in alphabetical order. Once ordered it is then output to a file as comma separate entries of drug name, number of unique prescribers and total cost using the csv library.

## Installation
Run the solution using [run.sh](https://github.com/souzanmirza/pharmacy_counting/blob/master/run.sh) in the pharmacy_counting directory. The bash file runs the [pharmacy_main.py](https://github.com/souzanmirza/pharmacy_counting/blob/master/src/pharmacy_main.py) with [itcont.txt](https://github.com/souzanmirza/pharmacy_counting/blob/master/input/itcont.txt) as input and [top_drug_cost.txt](https://github.com/souzanmirza/pharmacy_counting/blob/master/output/top_cost_drug.txt) as output. 

# Testing

A sample test is given with input `itcont.txt` as
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

The sample output given in `top_cost_drug.txt` is
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

## Unit Tests

To run the unit tests use the [run_unittests.sh](https://github.com/souzanmirza/pharmacy_counting/blob/master/run_unittests.sh) file to run the unit test classes in [pharmacy_helper.py](https://github.com/souzanmirza/pharmacy_counting/blob/master/src/pharmacy_helper.py). The results of the unit tests are output to a file unit_tests/results.txt. Unit test classes were developed for functions in [pharmacy_helper.py](https://github.com/souzanmirza/pharmacy_counting/blob/master/src/pharmacy_helper.py). 
* validEntry(entry): checks if an entry is valid and if true returns it return the processed entry with the *prescriber_id* and *cost* converted to floats and any grammatical symbols in *drug* replaced with whitespaces. 
* positiveNumber(field): checks if field is a positive number and converts it to a floats if true.
* addEntry(entry, dict): adds entries to the dict if the entry and dict are valid.

## Testsuite Tests

The testsuite tests can be run using the [run_tests.sh](https://github.com/souzanmirza/pharmacy_counting/blob/master/insight_testsuite/run_tests.sh) file to run the sample test in [test_1](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_1). Five other tests were implemented which test the following:
* [test_2](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_2): tests the result when the cost of an entry in itcont.txt is invalid.
* [test_3](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_3): tests the result when the entries from itcont.txt are copied 268 times and given unique *prescriber_id's*.
* [test_4](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_4): tests the result when the cost of an entry in itcont.txt is set to zero. This test also checks the floating point precision of the output to assure it is the same as the input.
* [test_5](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_5): tests the result when the *prescriber_id* of an entry in itcont.txt is invalid.
* [test_6](https://github.com/souzanmirza/pharmacy_counting/tree/master/insight_testsuite/tests/test_6): tests the result when an extra entry is added to itcont.txt which has the same name as another drug but with a '-' instead of a whitespace.

## Repo Directory Structure
```
pharmacy_counting
|   README.md
|   run.sh
|   run_unittests.sh
+---input
|       itcont.txt
+---output
|       top_cost_drug.txt
+---src
|   |   pharmacy_helper.py
|   |   pharmacy_main.py
|   |   README.md
|   |   __init__.py
+---unit_tests
|   |   test_addEntry.py
|   |   test_positiveNumber.py
|   |   test_validEntry.py
|   |   __init__.py
\---insight_testsuite
    |   run_tests.sh
    \---tests
        +---test_1
        |   +---input
        |   |       itcont.txt
        |   \---output
        |           top_cost_drug.txt
        . . . 
        . . .
        . . .
        \---test_6  
            +---input
            |       itcont.txt   
            \---output
                    top_cost_drug.txt 
```            


