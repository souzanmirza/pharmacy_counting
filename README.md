# Table of Contents
1. [Problem](README.md#problem)
2. [Solution Implementation](README.md#solution-implementation)
3. [Installation](README.md#installation)
4. [Sample Test](README.md#sample-test)
5. [Testing](README.md#testing)

# Problem

Insight coding challenge problem was to generate a list a list of all the prescribed drugs, the number of unique prescribers and total cost of the drug given a list of drugs, prescribers and the cost the drug was prescribed for. The solution is intended to be well tested, documented and scalable. You are allowed to chose the programming language for implementation but you are limited to that language's built-in data types and libraries.

# Solution Implementation

I implemented my solution in python. The main objective of my code was for it to be fast to process large dataset inputs. My code is processes the records using a hashtable implemented in the dict built-in data type. I chose a hashtable because search and insert functions take on average O(1) time and they require unique entries. Since the problem was centered around the type of drug being prescribed, the drug was used as the key in the drug_dict. Each drug entry in the drug_dict had a dict called dictinfodict which stored the unique ID's of the prescribers and the total cost.

For example:

```
drug_dict = {
             'drugA': {'prescriber1:True; 'cost':100},
	     'drugB': {'prescriber1:True; 'cost':200}
	    }
```

where druginfodict for *drugA* is `{'prescriber1:True; 'cost':100}.`

The csv reader library was used to read the entries from the input file. Each entry was checked to see if it was valid which was defined as
1. Length of entry is 5.
2. 1st entry (prescriber_id) can be cast to positive float.
3. 5th entry (cost) can be cast to positive float.
4. 4th entry (drug) is converted to remove any symbols and replace them with spaces to assure any grammatical differences in the drug names are accounted for ie. '-' is replaced with a ' '.

If valid the entry is added to drug_dict:
1. If the *drug* key does not already exist in drug_dict the *drug* key is added, druginfodict is created and set to `druginfodict={'prescriber_id'=True, 'cost'=cost}.`
2. If *drug* key already in drug_dict the *prescriber_id* is checked in druginfodict for the *drug*.
	1. If *prescriber_id* exists in the druginfodict, add the *cost* from this entry to `druginfodict['cost'] +=cost.`
	2. If *prescriber_id* does not exists in the druginfodict, add `druginfodict = {'prescriber_id':True}` and add the *cost* from this entry to `druginfodict['cost'] +=cost.`

Once all the entries have been read in from the input file the drug_dict is put in descending order by cost and if two drugs have the same cost in alphabetical order and then output to a file as comma separate entries of drug name, number of unique prescribers and total cost.

# Installation

To run the solution use the run.sh file which runs the src/pharmacy_main.py with input/itcont.txt and output/top_drug_cost.txt. 

## Repo directory structure
```
pharmacy_counting
|   README.md
|   run.sh
|   run_unittests.sh
|
+---input
|       itcont.txt
+---insight_testsuite
|   |   run_tests.sh
|   \---tests
|       +---test_1
|       |   +---input
|       |   |       itcont.txt
|       |   \---output
|       |           top_cost_drug.txt
|       +---test_2
|       |   +---input
|       |   |       itcont.txt
|       |   \---output
|       |           top_cost_drug.txt
|       +---test_3
|       |   +---input
|       |   |       itcont.txt
|       |   \---output
|       |           top_cost_drug.txt
|       +---test_4
|       |   +---input
|       |   |       itcont.txt
|       |   \---output
|       |           top_cost_drug.txt   
|       +---test_5
|       |   +---input
|       |   |       itcont.txt  
|       |   \---output
|       |           top_cost_drug.txt        
|       \---test_6  
|           +---input
|           |       itcont.txt   
|           \---output
|                   top_cost_drug.txt 
+---output
|       top_cost_drug.txt
+---src
|   |   pharmacy_helper.py
|   |   pharmacy_main.py
|   |   README.md
|   |   __init__.py
\---unit_tests
    |   results.txt
    |   test_addEntry.py
    |   test_positiveNumber.py
    |   test_validEntry.py
    |   __init__.py
```            

# Testing

Sample input in `input/itcont.txt`, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

Sample output `output/top_cost_drug.txt` is
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

## Unit Tests

Unit test classes were developed for functions in src/pharamcy_helper.py. 
* The function validEntry checks if an entry from the input file is valid and if valid returns entry processed with the *prescriber_id* and *cost* converted to floats and any grammatical symbols in *drug* replaced with whitespaces. 
* The function positiveNumber checks if the *prescriber_id* and *cost* are positive numbers and converts them to floats if they are.
* The function addEntry adds entries to the *drug_dict* if they entries and dictionary are valid.

To run the unit tests use the 
## Testsuite Tests

Describe and show how to run the tests with code examples.
