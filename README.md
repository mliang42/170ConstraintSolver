This is a series of generators and solvers for a constraint satisfication problem for CS170.
Basic idea of how the problem works: you have a set number of wizards, and you want to figure out an order that sorts them by age, but you are not provided their exact ages.
Instead, you are provided a list of constraints of the form "w1 w2 w3". This means that wizard3's age is NOT between wizard1 and wizard2.

bruteforce.py generates a randomized sequence that meets an input constraint.
ordered.py generates a sequence with a specific order, see code for details.
obfuscator.py obfuscates wizards names and shifts rows around. These three files are only if you want to generate your own inputs.
To run them: python bruteforce.py filename filesize(20, 35, or 50)

The solvers are named bt_solver.py and min_conflicts.py and are in the outputs folder.
The first one uses the backtracking algorithm and the second uses the min-conflicts algorithm.
To run the algorithms, place bt_solver.py, min_conflicts.py, and output_validator.py in the same folder. 
Then, run the following on the command line:
python bt_solver.py path_to_input_file output_file_name
or
python min_conflicts.py path_to_input_file output_file_name

As an example, if my input and output files are in the same directory as the scripts, I can run the solver like
python min_conflicts.py input20.in output20.out
Output files are generated in the same directory as the script. 
If there already exists an output file with the same name,it will be overwritten once the algorithm terminates.

output_validator.py is an edited version of the staff provided validator. It does NOT print out the number of constraints satisfied and
returns it instead. 

The version of python this was tested on is 3.4.3. It should work for almost any version of python3. Developed in conjunction with Shun Lin.
(This was developed in a private repo and moved to a public one once the competition finished)