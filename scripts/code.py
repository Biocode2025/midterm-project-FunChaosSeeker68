get = int(input("How would you like to calculate the protein Mass: Monoisotopic - 1 or Average - 2? (1/2)"))
RNA_codon_table = dict () 


def Read_dict(num):
  file1 = open('data/prot.txt','r')
  if num == 1:
    for line in file1:
      lineo=line.split("\t")
      AA_codon=lineo[-3]
      mono_weight=lineo[-2]
      RNA_codon_table[AA_codon]=mono_weight
  else:
    for line in file1:
      lineo=line.split("\t")
      AA_codon=lineo[-3]
      avg_weight=lineo[-1].rstrip("\r\n")
      RNA_codon_table[AA_codon]=avg_weight
  file1.close()
  return RNA_codon_table

codon_tabale=Read_dict(get)

file1 = open('data/short_ba_prot.txt','r')

if get == 1:
  file2 = open("results/Bsub_MW_Monoisotopic",'w')
else:
  file2 = open("results/Bsub_MW_Average",'w')


Mean_protein_mass=0
Number_of_proteins=0
max_header = ""
min_header = ""
current_header = ""
i=0
total = 0
for line in file1:
  line = line.strip(  )
  if line[0] == ">":
    if i == 0:
      file2.write(line+"\n")
      current_header = line
      i= i+1 
      max_header = line
      min_header = line
    elif i == 1:
      currmax=total+float(codon_tabale["H2O"])
      currmin=total+float(codon_tabale["H2O"])
      Mean_protein_mass=total+float(codon_tabale["H2O"])
      i=i+1
      file2.write (str(total+float(codon_tabale["H2O"])))
      file2.write("\n")
      file2.write(line+"\n")
      total=0
      current_header= line
      Number_of_proteins =Number_of_proteins + 1
    else:
      Mean_protein_mass=Mean_protein_mass + total+float(codon_tabale["H2O"])
      if currmax<total+float(codon_tabale["H2O"]):
        currmax=total+float(codon_tabale["H2O"])
        max_header = current_header
      if currmin>total+float(codon_tabale["H2O"]):
        currmin=total+float(codon_tabale["H2O"])
        min_header=current_header
      current_header = line
      file2.write (str(total+float(codon_tabale["H2O"])))
      file2.write("\n")
      file2.write(line+"\n")
      total=0
      Number_of_proteins =Number_of_proteins + 1
  else:
    for letter in line:
      total = total + float(codon_tabale[letter])



file2.write(str(total + float(codon_tabale["H2O"])))
file2.write("\n")
if currmax<total+float(codon_tabale["H2O"]):
  currmax=total+float(codon_tabale["H2O"])
  max_header = current_header
if currmin>total+float(codon_tabale["H2O"]):
  currmin=total+float(codon_tabale["H2O"])
  min_header=current_header

Number_of_proteins =Number_of_proteins + 1
Mean_protein_mass=Mean_protein_mass + total+float(codon_tabale["H2O"])
aveg_Mean_protein_mass = Mean_protein_mass / Number_of_proteins

if get == 1:
  use ="Monoisotopic"
else:
  use = "Average"

print("The protein Mass was calculated based on Atoms "+ use +" Mass")
print("Number of proteins :" + str(Number_of_proteins))
print("Mean protein mass :" + str(aveg_Mean_protein_mass))
print("Protein with highest Mass:")
print(max_header)
print(currmax)
print("Protein with lowest Mass:")
print(min_header)
print(currmin)
