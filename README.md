# README
## GeneFinder
### Description
GeneFinder is a command line tool that accepts an input DNA sequence, and will return the **DNA sequence** of the **longest possible gene** with its corresponding **mRNA sequence** and **protein sequence**. 

GeneFinder is written in Python 3.8. 

### How to Run this Program
1. Download the project repository. There is no need to install the program. However, python must be installed. 
2. Open any command line tool (CMD, Git Bash, Terminal, etc). Move to the directory of this project.
    `cd DirectoryWhereYouPutTheProjectFolder/ECS129_Project5_GeneFinder`  
3. The input file should be a txt file that contains the DNA sequence in a form of
`5' TargetDNASequence 3'`
 The first three and the last three index of the sequence      should be "5' " and " 3'", or there must be **three spaces before and after** the real sequence.
4. To run the program, simply type:
`python GeneFinder.py DirectoryToFile/file_name`
5. The output will print on the screen. There will also be a summary result file generated under the **Results** directory in the project folder. 

### Trial Files
There are some trial files under the trial_files folder. "test_seq_website.txt" contains the sequence in the original instruction. 

```
5’ TCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACT 3’
```

To run GeneFinder on this file, move to the project directory and type the following code in the terminal:
`
python GeneFinder.py trial_files/test_seq_website.txt
`

The output on the screen will look like:
```
$ python GeneFinder.py trial_files/test_seq_website.txt

The input sequence is:  TCAATGTAACGCGCTACCCGGAGCTCTGGGCCCAAATTTCATCCACT

After analyzing all the six open reading frames, the DNA sequence of the longest possible gene is:
ATGAAATTTGGGCCCAGAGCTCCGGGTAGCGCGTTACATTGA

The mRNA sequence of the gene is:
AUGAAAUUUGGGCCCAGAGCUCCGGGUAGCGCGUUACAUUGA

The protein sequence of the gene is:
MKFGPRAPGSALH*
```

The output file under the Results folder is like:
```
The file is the result of the gene finder program on trial_files/test_seq_website.txt

The DNA sequence of longest possible gene is: ATGAAATTTGGGCCCAGAGCTCCGGGTAGCGCGTTACATTGA
The mRNA sequence of the gene is: AUGAAAUUUGGGCCCAGAGCUCCGGGUAGCGCGUUACAUUGA
The protein sequence of the gene is: MKFGPRAPGSALH*
```


