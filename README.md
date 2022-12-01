# Advent of Code 2022
My solutions for Advent of Code 2022.

Keep in mind that I usually do these between 11pm and 12am local time when I should probably be sleeping. I might spend a few moments polishing the code after I successfully solve the day's problem, but generally I'll push the code to Github within minutes of getting confirmation my answer is correct.

The code here is not necessarily what I'd consider to be good nor efficient code. 

## How to interpret my work
Each day gets its own folder. In general, each problem in each day gets its own file. Part 2 of each day generally builds off of part 1 in a way that you can use the same code to solve both parts. But frankly making code fit together cleanly is more effort than I'd like to expend at 1am so instead I just create two files: one for each part even if there's no refactoring required.

Each day's text will be saved to `dayXX_problem.txt` (where `XX` is the 0-padded day). Each day's input (which is custom to each player in AOC) will saved to `input.txt`. Sometimes it is faster/easier to hand modify the `input.txt` to get some specific formatting than it is to implement the formatting in code. In those cases, the saved `input.txt` file will not match what was actually provided by AOC. 

Sometimes to help me troubleshoot, I'll also create a `sample.txt` file which is generally either:

* the simple example provided in the problem statement
* an example made up by me to help me debug my code

### Running code
For AOC 2022, I intend to mostly (if not exclusively) use Python. `XX` stands for the 0-padded day. `Y` stands for the part number.

#### Running Python files
For Python files, `cd` into the appropriate day's folder and run `python <file>` (e.g. `cd dayXX && python dayXXpY.py`). All Python files will target 3.x.

#### Running Go files
For Go files, `cd` into the appropriate day's folder and run `go run <file>` (e.g. `cd dayXX && go run dayXXpY.go`).
