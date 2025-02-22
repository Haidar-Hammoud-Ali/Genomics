sequence= input("Provide a valid DNA sequence!: ")

sequence = sequence.upper()
valid_nucleotides = {'A', 'T', 'G', 'C'}
filtered_sequence = [base for base in sequence if base in valid_nucleotides]
print("The valid sequence I am working on is: ","".join(filtered_sequence))

gc_count = filtered_sequence.count('G') + filtered_sequence.count('C')
total_valid_bases = len(filtered_sequence)
print ("The number of 'g' and 'c' bases in the provided DNA sequence is = ",gc_count)
print("The total valid bases in the provided DNA sequence is = ",total_valid_bases)

if total_valid_bases == 0:
    print (0.0)

gc_percentage = (gc_count/total_valid_bases)*100
print ("The 'gc' % in this DNA sequence is = ",round(gc_percentage,3), "%")

