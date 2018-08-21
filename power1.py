def power(base,expt):
    if(expt==1):
        return(base)
    if(expt!=1):
        return(base*power(base,expt-1))
base=int(input("Enter base: "))
expt=int(input("Enter exponential value: "))
print("Result:",power(base,expt))
