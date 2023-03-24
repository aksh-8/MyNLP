Name: Akash Biswal
netID: axb200166

This zip folder contains two files [tagger.py and post_rnn.py] 
1. PART-1 : tagger.py - This is the implemetation of Part - 1: POST using HMMs
               It contains the code for loading the corpus, initializing HMM probabilities and Viterbi Algorithm.
               Assumptions: 
			- We are allowed to use packages in python like numpy and pandas
			- I have used this to create probability matrices and dataframes for ease of access
			- The packages that need to installed in python3 are: numpy and pandas
				Commands on terminal:
					pip3 install numpy
					pip3 install pandas 
			- The packages must be available for python3 as I have written the code in python3.
			- ISSUES FACED: These packages were not installed by default on the UTD server and I do not have sudo permissiion to install them, therefore I tested tagger.py locally on my computer and have attached the results.
		  - Once you have installed the packages on the server to run the code
			1. extract the zip file
			2. open a terminal in the folder where my "tagger.py" file is present
			3. Run - python3 tagger.py <Appropriate full path to the modified_brown folder in your system>
				 - for example in my system it is:
					python3 tagger.py /home/011/a/ax/axb200166/NLP/MyNLP/Homework-2/modified_brown


2. post_rnn.py - This is the implemetation of Part - 2: POST using RNNs
   This is a .py version of the code in my Colab notebook
   Link to the notebook: https://drive.google.com/file/d/1FU8BgJqkYICqSsV-tVZwJClPhIBd0Ijk/view?usp=sharing
   Assumptions :-
	- Your personal google drive has the modified_brown folder in it, !!! please upload your folder directly to you drive, and do not keep it inside any sub folder !!! 
	  (This is because the path in colab is "/content/drive/MyDrive/modified_brown"), So please upload "modified_brown" to the default/home directory in your google drive
   
   To Run: 
	- Open the link to the notebook
	- Click "Runtime" in the task bar and "Run All"
	- You will get a prompt to provide the cloab runtime with permission to your drive, provide the permission and proceed, these steps are self explanatory








