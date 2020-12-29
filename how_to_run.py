import key_value_store as data 

#basic CRD operations
data.create("hey",10)
data.read("hey")
data.read("hiii")
data.create("hey",20)
data.modify("hey",30)
data.delete("hey")

#get it by using multiple threads
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()

#code by Nikhil Sharma
