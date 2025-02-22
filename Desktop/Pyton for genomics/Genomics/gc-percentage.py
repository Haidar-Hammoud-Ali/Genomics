sequence= input("Provide a valid DNA sequence!: ")

sequence = sequence.upper()  # Convert to uppercase
valid_nucleotides = {'A', 'T', 'G', 'C'}  # Set of valid DNA bases  
filtered_sequence = [base for base in sequence if base in valid_nucleotides]
print(filtered_sequence)

gc_count = filtered_sequence.count('G') + filtered_sequence.count('C')
total_valid_bases = len(filtered_sequence)
print (gc_count)
print(total_valid_bases)