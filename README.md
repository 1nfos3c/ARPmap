# ARPmap
A simple ARP network scanner  

![ARPmap](http://i64.tinypic.com/2w3pz7b.jpg)  
### About
ARPmap scans a target IP range and prints out which devices are available and their MAC and vendor.  
It works on **OSX** and **Linux**.  

### Usage
You can start the scan like this:  
``` sudo python3 ARPmap.py -t <target IP range>  ```  
ARPmap also has a help option:  
``` sudo python3 ARPmap.py -h ```  

### Credits
ARPmap uses the macvendors.co API for finding the vendor names.  
