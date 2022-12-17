
# coding: utf-8

# In[ ]:


from pyopenms import *
seq = AASequence.fromString("VAKA")
mfull = seq.getMonoWeight() # weight of M
print("Monoisotopic mass of peptide [M] is", mfull)
seqv = AASequence.fromString("V")
mfullV = seqv.getMonoWeight() 
print("Monoisotopic mass of V [M] is", mfullV)
seqA = AASequence.fromString("A")
mfullA = seqA.getMonoWeight() # weight of M
print("Monoisotopic mass of A [M] is", mfullA)
seqK = AASequence.fromString("K")
mfullK = seqK.getMonoWeight() # weight of M
print("Monoisotopic mass of K [M] is", mfullK)
sum=mfullV+(mfullA+mfullA)+mfullK
print(sum)
print()
print("mass(VAKA)=",mfull,"< mass(V)=",mfullV," + mass(A)=",mfullA," + mass(K)=",mfullK," + mass(A)=",mfullA,"\nThe mass of a peptide is less than the sum of the masses of its constituent amino acids.")
print("Because of  the loss of water occurred which happened  During the association of amino acids with each other to form the peptide,\nwhich affected the mass of the peptide in what\nis known as the condensation process.")

# general solution 
S = input('Enter a peptide Sequence :\n')
seq = AASequence.fromString(S)
mfull = seq.getMonoWeight() # weight of M
sum,i = 0,0
for AA in seq:
    #print("the mass of", AA.getName(), "= ", AA.getMonoWeight())
    i=i+1
    sum = sum + AA.getMonoWeight()
    print("the mass(",AA.getName(),") +", end = ' ')
print("=",sum)

