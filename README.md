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

ie. Drug_dict = {
				'drugA': {'prescriber1:True; 'cost':100}, 
				'drugB': {'prescriber1:True; 'cost':200}
				} 
where druginfodict for drugA is {'prescriber1:True; 'cost':100}.

The csv reader library was used to read the entries from the input file. Each entry was checked to see if it was valid which was defined as
1) Length of entry is 5.
2) 1st entry (prescriber_id) can be cast to positive float.
3) 5th entry (cost) can be cast to positive float.
4) 4th entry (drug) is converted to remove any symbols and replace them with spaces to assure any grammatical differences in the drug names are accounted for ie. '-' is replaced with a ' '.

If valid the entry is added to drug_dict:
1) If the 'drug' key does not already exist in drug_dict the 'drug' key is added, druginfodict is created and set to druginfodict={'prescriber_id'=True, 'cost'=cost}.
2) If 'drug' key already in drug_dict the 'prescriber_id' is checked in druginfodict for the 'drug'.
a) If 'prescriber_id' exists in the druginfodict, add the cost from this entry to druginfodict['cost'] +=cost.
b) If 'prescriber_id' does not exists in the druginfodict, add druginfodict = {'prescriber_id':True} and add the cost from this entry to druginfodict['cost'] +=cost.

Once all the entries have been read in from the input file the drug_dict is put in descending order by cost and if two drugs have the same cost in alphabetical order and then output to a file as comma separate entries of drug name, number of unique prescribers and total cost.

# Installation

## Repo directory structure

pharmacy_counting
|   README.md
|   run.sh
|   run_unittests.sh
|
+---input
|       itcont.txt
|       
+---insight_testsuite
|   |   run_tests.sh
|   |   
|   \---tests
|       +---test_1
|       |   +---input
|       |   |       itcont.txt
|       |   |       
|       |   \---output
|       |           top_cost_drug.txt
|       |           
|       +---test_2
|       |   +---input
|       |   |       itcont.txt
|       |   |       
|       |   \---output
|       |           top_cost_drug.txt
|       |           
|       +---test_3
|       |   +---input
|       |   |       itcont.txt
|       |   |       
|       |   \---output
|       |           top_cost_drug.txt
|       |           
|       +---test_4
|       |   +---input
|       |   |       itcont.txt
|       |   |       
|       |   \---output
|       |           top_cost_drug.txt
|       |           
|       +---test_5
|       |   +---input
|       |   |       itcont.txt
|       |   |       
|       |   \---output
|       |           top_cost_drug.txt
|       |           
|       \---test_6
|           |   
|           +---input
|           |       itcont.txt
|           |       
|           \---output
|                   top_cost_drug.txt
|                   
+---output
|       top_cost_drug.txt
|       
|       
+---src
|   |   pharmacy_helper.py
|   |   pharmacy_main.py
|   |   README.md
|   |   __init__.py
|           
|       
\---unit_tests
    |   results.txt
    |   test_addEntry.py
    |   test_positiveNumber.py
    |   test_validEntry.py
    |   __init__.py
            


To run the cost use the run.sh file in the parent




# Testing

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Unit Tests

## Testsuite Tests

Describe and show how to run the tests with code examples.