# pcap-Hex-Analyser
This helps to find out the data type of a file from its raw (Hex Signature) encoding.  
It will be helpful in Digital Investigation.

How to use      

 1. Open a pcap file in Wireshark     
 2. Add HTTP as a filter     
 3. Find all the GET request packets     
 4. Follow the TCP Stream of the packet     
 5. Change the encoding type to Raw from ASCII     
 6. Copy the raw to raw.txt and run the program  

Output 

 -> The output of programs define the file extension. 
 -> After all completing all these steps the output will be saved to Output.txt 
 -> Output.txt contains the formatted output 
 -> Copy the source of Output.txt into HxD Editor and then save as that file in the extension of the output
 
 !Note
 
 raw.txt contains the sample hex for a jpg file. Please change raw.txt accordingly.
