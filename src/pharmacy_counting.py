# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:29:39 2018

@author: Souzan
"""
import argparse
import os


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Pharmacy Counting')
    parser.add_argument('dbinput', metavar='in', help='Input containing prescribers and drug info')
    parser.add_argument('dboutput', metavar='out', help='Input containing prescribers and drug info')
    args = parser.parse_args()
   
    pharmacyinfile = open(args.dbinput, 'r')
    pharmacyoutfile = open(args.dboutput, 'w')
    
    pharmacyinput = []
    header = pharmacyinfile.readline().strip('\n').split(',')
    drugs = []
    
    for entry in pharmacyinfile:
        entryedited = entry.replace(' ', '').strip('\n').split(',')
        entry = entry.strip('\n').split(',')
        assert len(entry) == 5, 'Invalid entry'
        pharmacyinput.append(entry)
    
    drugdict={}
    dictitems=[]
    
    for i in range(len(pharmacyinput)):
        drug = pharmacyinput[i][3]
        prescriber = pharmacyinput[i][1] + pharmacyinput[i][2]
        cost = int(pharmacyinput[i][4])
        if drugdict.has_key(drug):
            druginfodict = drugdict[drug]
            if not druginfodict.has_key(prescriber):
                druginfodict[prescriber] = True
            druginfodict['cost'] = druginfodict['cost'] + cost 
        else:
            druginfodict = {}
            drugdict[drug] = druginfodict
            druginfodict[prescriber] = True
            druginfodict['cost'] = cost
            
    
    drugs = []
    numprescribers = []
    totalcost = []
    output = []
    
    for drug in drugdict.keys():
        druginfodict = drugdict[drug]
        assert len(druginfodict)>=2, 'Invalid drug info dict'
        assert druginfodict.has_key('cost'), 'Invalid drug info dict'
        drugs.append(drug)
        numprescribers.append(len(druginfodict)-1)
        totalcost.append(druginfodict['cost'])
        output.append([drug, len(druginfodict)-1, druginfodict['cost']])
                
    output.sort(key=lambda row: row[0])
    output.sort(key=lambda row: row[2], reverse=1)
    
    pharmacyoutfile.write('drug_name,num_prescriber,total_cost\n')
    for line in output:
        pharmacyoutfile.writelines('%s,%d,%d\n'%(line[0], line[1], line[2]))
    pharmacyoutfile.truncate(pharmacyoutfile.tell()-len(os.linesep))
    pharmacyoutfile.close()