sequence= input("Provide a valid DNA sequence!: ")

sequence = sequence.upper()  # Convert to uppercase
valid_nucleotides = {'A', 'T', 'G', 'C'}  # Set of valid DNA bases
print (valid_nucleotides)
    
filtered_sequence = [base for base in sequence if base in valid_nucleotides]
print(filtered_sequence)

