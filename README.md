urmint - a simple interpreter for a minimalist Turing complete model of computation.

2017 / Kalle Viiri

Intro
-----

Unlimited Register Machine is a simple model of computation used by Nigel Cutland in his book 'Computability: An introduction to recursive function theory'. This model is appealing because it is simple, yet Turing-complete. The conceptual computer has an unlimited (yet finite) number of registers which are manipulated using the following instructions (capitals are literals, lower-case letters are numerals):

 * I x, which increments the value in register x by one
 * Z x, which resets the value in register x to zero
 * T x y, which copies the value of register x to register y
 * J x y z, which jumps to the z:th instruction if register x and y have the same value

Execution ends when the program runs out of instructions to execute (or jumps out of bounds). By convention, the register zero's contents at this point are considered to be the output of the program.

Usage
-----

python urmint.py programname [register0 register1 ... register31]

Launches an instance of programname as an URM, with registers initialized as given input. The rest of the registers are initialized to zeroes. Out of convenience, the number of registers is limited to 32 - however, this doesn't really limit the computational power all that much ;)

programname must be a file containing nothing but lines in the aforementioned format, with no empty lines. All values of instructions and registers are indexed from zero.

If successful, urmint prints the state of the computation after each instruction is carried out.

Included are reference programs hello.urm, which simply sets registers to '5, 1, 2' then halts, and divide.urm, which, when given x and y as input, outputs floor(x/y).

Have fun coding in this ridiculously simple yet Turing complete language!
