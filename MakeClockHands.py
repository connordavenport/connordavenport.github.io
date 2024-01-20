i = '/Users/connordavenport/Downloads/Iskra Orange_files/REPLACE.svg'

for t in [("minute",400), ("hour",288)]:
    newPage()
    time,size = t
    
    print(size)
    fill(58/255, 181/255, 91/255)
    rect(495,457,8,size)
    saveImage(i.replace("REPLACE", time)) 


newPage()
fill(58/255, 181/255, 91/255)
oval(495,827,20,20)
saveImage(i.replace("REPLACE", "second"))     
