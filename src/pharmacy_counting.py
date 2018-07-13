# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:29:39 2018

@author: Souzan
"""
import argparse
import os
import csv

from line_profiler import LineProfiler

if __name__=='__main__':
    def main():
        parser = argparse.ArgumentParser(description='Pharmacy Counting')
        parser.add_argument('dbinput', metavar='in', help='Input containing prescribers and drug info')
        parser.add_argument('dboutput', metavar='out', help='Input containing prescribers and drug info')
        args = parser.parse_args()

        # pharmacyinfile = open(args.dbinput, 'r')
        # pharmacyinput = []
        # header = pharmacyinfile.readline().strip('\n').split(',')
        # drugs = []

        # for entry in pharmacyinfile:
        #     entryedited = entry.replace(' ', '').strip('\n').split(',')
        #     entry = entry.strip('\n').split(',')
        #     assert len(entry) == 5, 'Invalid entry %s' % (entry, )
        #     pharmacyinput.append(entry)

        with open(args.dbinput, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)

            # for i in range(500000):
            #     pharmacyinput.append(next(reader))

            # print(len(pharmacyinput))
            drugdict={}
            # dictitems=[]

            # for i in range(len(pharmacyinput)):
            for i, entry in enumerate(reader):
                if i > 500000:
                    break
                if len(entry) == 5:
                    drug = entry[3]
                    prescriber = entry[0]
                    cost = float(entry[4])
                    # if drugdict.has_key(drug):
                    if drug in drugdict:
                        druginfodict = drugdict[drug]
                        # if not druginfodict.has_key(prescriber):
                        if prescriber not in druginfodict:
                            druginfodict[prescriber] = True
                        druginfodict['cost'] = druginfodict['cost'] + cost
                    else:
                        druginfodict = {}
                        drugdict[drug] = druginfodict
                        druginfodict[prescriber] = True
                        druginfodict['cost'] = cost
                else:
                    print('Entry invalid %s of size %d'%(entry, len(entry)))
        # drugs = []
        # numprescribers = []
        # totalcost = []
        # output = []

        # for drug in drugdict.keys():
        #     druginfodict = drugdict[drug]
        #     if len(druginfodict)<2:
        #         del drugdict[drug]

        drugspaired = zip(drugdict.keys(), drugdict.values())
        drugspaired = list(drugspaired)

        drugspaired = sorted(drugspaired, key=lambda row: row[0])
        drugspaired = sorted(drugspaired, key=lambda row: row[1]['cost'], reverse=True)

        with open(args.dboutput, 'w', newline='\n') as pharmacyoutfile:
            fieldnames = ['drug_name', 'num_prescriber', 'total_cost']
            writer = csv.DictWriter(pharmacyoutfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in drugspaired:
                writer.writerow(
                    {'drug_name': entry[0], 'num_prescriber': len(entry[1])-1, 'total_cost': round(entry[1]['cost'])})
            pharmacyoutfile.truncate(pharmacyoutfile.tell() - len(os.linesep))


            #
            # # assert druginfodict.has_key('cost'), 'Invalid drug info dict'
            # assert 'cost' in druginfodict, 'Invalid drug info dict'
            # drugs.append(drug)
            # numprescribers.append(len(druginfodict)-1)
            # totalcost.append(druginfodict['cost'])
            # output.append([drug, len(druginfodict)-1, druginfodict['cost']])

        # def sortingkey(dictvalues):
        #     return dictvalues[1]

        # drugspaired = sorted(drugspaired, key=lambda row: row[0])
        # drugspaired = sorted(drugspaired, key=lambda row: row[1]['cost'], reverse=True)
        #
        # with open(args.dboutput, 'w', newline='\n') as pharmacyoutfile:
        #     fieldnames = ['drug_name', 'num_prescriber', 'total_cost']
        #     writer = csv.DictWriter(pharmacyoutfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for entry in drugspaired:
        #         writer.writerow({'drug_name': entry[0], 'num_prescriber': len(entry[1])-1, 'total_cost': round(entry[1]['cost'])})
        #     pharmacyoutfile.truncate(pharmacyoutfile.tell() - len(os.linesep))

    # import sys, time
    # print(sys.version)
    # main()
    # time.sleep(3600)
    lp = LineProfiler()
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()
