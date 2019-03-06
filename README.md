# ARPmap
A simple ARP network scanner  

![ARPmap](http://i68.tinypic.com/2rynjvl.png)  
### About
ARPmap scans a target IP range and prints out which devices are available and their MAC and vendor.  
It works on **OSX** (requires sudo) and **Linux**.  

### Usage
You can start the scan like this:  
``` python3 ARPmap.py -t <target IP range>  ```  
ARPmap also has a help option:  
``` python3 ARPmap.py -h ```  

### Credits
ARPmap uses the macvendors.co API for finding the vendor names.  
