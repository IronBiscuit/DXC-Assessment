# DXC Encoding Assessment
 
### Introduction:

This repository serves as my response to DXC's "Encoding" coding assessment. There were a few assumptions made when working on this assessment, in which I will highlight below.

### Assumptions:

As the coding assessment did not specify certain details, I did my best to adhere to as close to the requirements as possible. The assumptions that I made to do so were as follows:

<ul> 
 <li> There was no hard restriction on the coding language specified. Therefore, I chose to complete the assessment using Python3.8. The methods required in the constraints have been implemented using Python syntax.</li>
 <li> I assumed that the characters in the reference table are case sensitive. Therefore, any characters in the plain text / specified offset character that is not found in the specified reference table would be treated as not within the reference table, even if it is just the lower-case version of the characters</li>
 <li> As the assessment required me to cater to custom offset characters, I implemented my encode() and decode() functions to take in an additional argument that specifies the offset character, which I assume it is alright to do so. </li>
</ul>
 
### Instructions:

To run the program, ensure that you have python3 installed and that you have pulled the repository to your local set-up.

The target program is Solution.py, and it takes in three command line arguments:

<ul> 
 <li> -c : The command type. Valid commands include Encode and Decode, and these commands are not case sensitive. </li>
 <li> -t : The target text. If there are space-type characters within the target text, ensure that it is surrounded by quotation marks (""). </li>
 <li> -o : The offset character. If an invalid offset character(s) is specified, an exception would be thrown and handled by the program by printing the error message. Quotation marks aren't necessary unless there are spaces specified. </li>
</ul>
 
Here are some examples of valid commands:
<ul> 
 <li> <code>python3 Solution.py -c Encode -t "HELLO WORLD" -o B </code> </li>
 <li> <code>python3 Solution.py -c dECOde -t "GDKKN VNQKC" -o "B" </code> </li>
 <li> <code>python3 Solution.py -c DeCODe -t "C/GGJ RJMG." -o F </code> </li>
 <li> <code>python3 Solution.py -c encode -t "!!!!!!!!!!" -o H </code> </li>
</ul>

Here are some examples of invalid commands:
<ul> 
 <li> <code>python3 Solution.py -c encode -t HELLO WORLD -o B </code> missing quotations around HELLO WORLD </li>
 <li> <code>python3 Solution.py -c dECOde -t "GDKKN VNQKC" -o "B 1" </code> program executes but an exception would be thrown as offset character is not recognized </li>
 <li> <code>python3 Solution.py -c dECOde -t "GDKKN VNQKC" -o "b" </code> program executes but an exception would be thrown as offset character is not recognized </li>
 <li> <code>python3 Solution.py -c DeCODer -t "C/GGJ RJMG." -o F </code> unrecognized -c argument </li>
</ul>

 
