
lengths=["km","hm","dam","m","dm","cm","mm"]
#Create the Convertion Funcition 
def convert_a_to_b(a:int,b:str,c:str):
    length=c
    b=int(lengths.index(b)+1)
    c=int(lengths.index(c)+1)
    x=b-c
    s=b-c
    if x!=abs(x):
        x=10**abs(x)
        x=a*x
        return str(x+" "+length)
    elif x==abs(x):
        x=10**abs(x)
        x=a/x 
        return str('{:f}'.format(x)+" "+length)  