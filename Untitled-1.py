#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../Spring 2019/Discrete Structure'))
	print(os.getcwd())
except:
	pass

#%%
def BinToDec(binary_in):

    # initialize

    decimal_out = 0

    # add up the binary expression of the decimal number

    for position in range(0, len(binary_in)):

        decimal_out = decimal_out + binary_in[len(binary_in)-position-1]*(2**position
        )

    return (decimal_out)


#%%
BinToDec([1,0,0,0,0,0,0 ])


#%%
def ParityParty(num):
    if not isinstance(num, int):
        print ("Please enter an interger!")
    else:
        if num%2==0:
            return [0,int(num/2)]
        else:
            return [1, int((num-1)/2)]


#%%
ParityParty("meme")


#%%
def DecToBin(value):
    if not isinstance(value, int) or value <0:
        print ("Please enter a positive interger!")
        return None
    else:
        binary=[]
        if value ==0:
            return [0]
        while value >=1:
            if value%2==0:
                binary.append(0)
                value=value/2
            else:
                binary.append(1)
                value=((value-1)/2)
                print (value)
        return list(reversed(binary))


#%%
m=DecToBin(3)


#%%
m


#%%
BinToDec(m)


#%%



