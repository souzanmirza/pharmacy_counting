import argparse
import os
import csv
import pharmacy_helper
import time

def main():
        """
        input: comma separated file of [prescriber_id, prescriber_fn, prescriber_ln, drug, cost]
        output: comma separated file of drug, number of unique prescribers, total cost in order
                of cost and then alphabetical if cost is the same.
        method: using a hash table implemented by dict the input is read in and processed within a
                dict that uses the drug for a key and a dict as the value which contains the unique
                prescriber_id's and the total cost. the dict is output to a list of tuples
                (key, values) and sorted first alphabetically by drug name (key) and then by
                decreasing cost (values['cost']). the ordered dict is then written as a
                comma separated file of drug, number of unique prescribers, total cost.
        """
        parser = argparse.ArgumentParser(description='Pharmacy Counting')
        parser.add_argument('dbinput', metavar='in', help='Input containing prescribers and drug info')
        parser.add_argument('dboutput', metavar='out',
                            help='Output containing processed info on drugs, prescribers and total cost')
        args = parser.parse_args()

        try:
            with open(args.dbinput, 'r') as pharmacy_infile:
                reader = csv.reader(pharmacy_infile, delimiter=',')
                next(reader)
                drug_dict = {}
                for i, entry in enumerate(reader):
                    pharmacy_helper.addEntry(entry, drug_dict)
        except IOError:
            print('Input file does not exist')
            return


        drugs_paired = zip(drug_dict.keys(), drug_dict.values())
        drugs_paired = list(drugs_paired)
        drugs_paired = sorted(drugs_paired, key=lambda row: (-row[1]['cost'], row[0]))

        with open(args.dboutput, 'w', newline='\n') as pharmacy_outfile:
            fieldnames = ['drug_name', 'num_prescriber', 'total_cost']
            writer = csv.DictWriter(pharmacy_outfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in drugs_paired:
                writer.writerow(
                    {'drug_name': entry[0],
                     'num_prescriber': len(entry[1]) - 1,
                     'total_cost': entry[1]['cost']}
                )
            pharmacy_outfile.truncate(pharmacy_outfile.tell() - len(os.linesep))


if __name__ == '__main__':    
    # start_time = time.time()
    # print(start_time)
    main()
    # print(time.time()-start_time)
