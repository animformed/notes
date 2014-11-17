Getting started with C
**********************


Your program will start runing from the main(), which has a return type int. If is returns any other value except 0, it means there's a problem.


printf() is used to display or print formatted output. It replaces format characters with the values of variables.


atoi(s), interprets the contents of a string 's' as a number with type int, included in stdlib.h.


To compile and run a code with gcc:


> gcc -std=99 zork.c -o zork && ./zork          // To use the C99 standard.


To declare a character and a string:


char s1 = 'a';               // Single quotes can be used to define a character.
char* s2 = "Shatner";     // String literal
char s3[] = "Shatner";     // Character array, or a string
char s4[] = {'S', 'h', 'a', 't', 'n', 'e', 'r', '\0'};          // Null defining the end of a character array


Static variable values are maintained throughout a program execution. If used inside a function,
it will maintain its value if the function quits and the next time is it called. It can
be initialized only once in a program execution.

void auto_static (void)
{
    static int staticVar = 100;		// Will be initialized only once during program execution.
}

void auto_static (void)
{
    static int staticVar;
	staticVar = 100;		// To initialize it explicitly when the function is called.
							// But it defeats the purpose of using static variables.
							// If we increment it, it will maintain its value.
}

Condition checking
------------------


'&&' checks if both conditions are true:


if((dealer_up_card == 6) && (hand == 11))     {
     ...
}


'||' check if one of the two conditions are true:


if(cupcakes_in_fridge || chips_on_table)




'!' flips the value of a condition:


if(!brad_on_phone){
     ...
}


Using just '&' and '|' will evaluate both conditions, but '&&' and '||' will often skip the second condition. They are also used to perform bitwise operations on individual bits of a number.
                                                                                                                                                                               ------------------


Switch statements
-----------------


switch(train) {                                   // It will only check a single value or a variable.
     case 25:                                   // If train == 25 or 31 or 32, add 10 to the winnings and skip to the end.
     case 31:
     case 32:
          winnings = winnings + 10;
          break;
     case 37:                                   // If train == 37, add 50 to the winnings and skip to the end.
          winnings = winnings + 50;         
          break;
     case 65:                                   // If train == 65, add 80 to the winnings, AND THEN also add 20 to the winnings, and skip to the end.
          puts("Jackpot!");
          winnings = winnings + 80;
     case 12:                                   // If train == 12, just add 20 to the winnings.
          winnings = winnings + 20;
          break;
     default:                                   // For any other value of train, set the winnings to ZERO.
          winnings = 0;
}


The switch loop will keep iterating until int breaks out from it.




while and do-while loops
------------------------


while (<some condition>) {          // It checks the condition each time before running the body, while iterating.
     /* Body */
}


do {                                   // It check the condition each time after a loop iteration, unlike while, which means the loop runs at least once.
     /* Body */
}while(<var>);




Other loop statements: for, break and continue (break is to break out of loops and switch statements).




Writing Functions
-----------------


Function and return types: Most functions have return types, except for void.


Functions with variables as arguments take pass-by-values.




Memory and pointers
*******************


Every time you declare a variable inside the main() function, it stays in the stack area of the memory. If it is declared outside any function or main(),
it is stored in the globals section of memory.


int y = 1;               // Global


int main()
{
     int x = 4;          // Stack
     return 0;
}


To print the address of a variable:
printf("x is stored at %p\n", &x);          // & is the reference operator. %p is the string representation for address (also %li).


Pointers are useful for using as function arguments, when you have to modify a value outside the function. By default, all the arguments are passed by value
to a function, therefore they are stored on the stack. To do this, pass the variable's address to the function. A variable may be stored in a stack multiple times.
To share a memory location where the variable is stored, store the variable's address to a pointer:


int* address_of_x = &x;                         // Take the address of int variable x to an int pointer.
int value_stored = *address_of_x;          // Get the value being pointed.
*address_of_x = 99;                              // Modify the value being pointed.


# include <stdio.h>
void go_south_east(int* lat, int* lon) {          // Create pointers to store addresses.
     *lat = *lat - 1;
     *lon = *lon + 1;
}


int main()
{
     int latitude = 32;
     int longitude = -64;
     gc_south_east(&latitude, &longitide);          // Pass the addresses.
     ....
}


Pointers and arrays
-------------------


void fortune_cookie(char msg[]) {                    // Passed a character array or string, which is a pointer to the first character.
     printf("Message reads: %s\n", msg);
}


The sizeof operator returns the length of an array. For a pointer, it returns 4 or 8 bytes depending on the system (32 or 64-bit):
sizeof("Turtles!");                                        // Returns 9


For an array variable, the name of the array is the address of the first element, but when the string/character array is passed to the function, we pass by value of the array name, which
is the address of the first element. Therefore, the sizeof operator returns the size of the pointer (4 bytes on 32-bit systems and 8 bytes on 64-bit systems):


void fortune_cookie(char msg[]) {                                   // Pass by value of the array variable, which is an address.                   
     printf("Message reads: %s\n", msg);
     printf("msg occupies %i bytes\n", sizeof(msg));               // sizeof(msg) returns the size of the pointer to a string. The function is passed the value of the array variable, which is an address, a pointer.
}


Therefore, every time you pass an array to a function, you're decaying it to a pointer. It will only contain the address of the array, and it will lose it length or size. This is also
true when you assign an array variable to a pointer.


You can also cast a pointer to an ordinary number:


a = (long)p          // p is a pointer, a is a long variable.




If s is a character array or a string:
char s[] = "How big is it?";
char* t = s;                         // Take the value of the array variable, which is an address. Pointer decay happens, since 't' here does not get the size of the array.


&s == s                                   // The address of an array is the address of the array.


s = t          // ERROR: An array cannot point to anything else. The computer will allocate memory to store the array but not the array variable. It simply plugs in the address of the start of the array.




Arrays and pointer arithmetic
-----------------------------


int drinks[] = {4, 2, 3};
printf("1st order: %i drinks\n", drinks[0]);     // Equivalent
printf("1st order: %i drinks\n", *drinks);          // Equivalent


For an array the elements are stored in consecutive memory blocks, which means you can add values to a pointer pointing to an array. To read the third element for array,
add 2 to the pointer for the first element of the array:


printf("3rd order: %i drinks\n", drinks[2]);
printf("3rd order: %i drinks\n", *(drinks+2));


In general, the expression drinks[i] and *(drinks+i) are equivalent. That's why an array begins at 0.


Pointers have types, to support pointer arithmetic on arrays of different data types. The char array elements will be positioned after each byte,
whereas an int array elements will be positioned after every 4 bytes. This is needed for the compiler to adjust pointer arithmetic.


int nums[] = {1, 2, 3};
printf("nums is at %p\n", nums);
printf("nums + 1 is at %p\n" nums + 1);          // Display the next element


Pointers for data entry - scanf() and fgets()
---------------------------------------------


char name[40];
printf("Enter your name: ");
scanf("%36s", name);               // 'name' is a pointer which is passed to the function to read the input data. It will read up to 39 character and the null terminator '\0'.


int age;
printf("Enter your age: ");
scanf("%i", &age);                    // For integer values, pass the address of the interger variable.


Therefore, you can format the string representation of the scanf() input to specify the type of expected input:
char first_name[20];
char last_name[20];
printf("Enter the first and last name: ");
scanf("%19s %19s", first_name, last_name);     // The two string inputs are seperated by a space.


The limitation with scanf() is that for an array input like a string, you must specify the number of characters which has to match the array size minus one. During an input if you type beyond
the limit, you'll cause buffer overflow and segmentation error.


Another function for data entry is fgets(), which is only for string inputs. With this, you don't have to specify the character array size for an input, avoiding any mistakes. Again, use the sizeof
operator for an array, not a pointer. In that case, you'd to provide the length of the string explicitly:
char food[5];
fgets(food, sizeof(food), stdin);          // It takes pointer to buffer, the entire size of the array and the input stream.
// OR
char* t = food;
fgets(t, 5, stdin);


fgets() also sets up a mandatory limit on character input, nothing gets past it, whereas with scanf(), you'd have to add the size of the string to avoid buffer overflows.


scanf() can be used to enter multiple fields of structured data of different data types. fgets() can be used to input only one string, and of string type only.


With scanf() for reading a single string into %s, it stops if you enter space, if you want to use space(s) in a string. To avoid this, you'd have to use regex or
call it more than once. fgets() can read space(s) into a string.




Character pointer and character array
-------------------------------------


char* cards = "JQK";          // This is a pointer to char (for J), a constant read-only memory block. This is also a string literal. The pointer can't be used to modify the string, like, cards[1] = "G";
char cards[] = "JQK";          // This is now an array, which stores a copy of the string and can be modified.


For more info on how the string is loaded into a memory for an array, refer pg.75


If you don't want to use an array to store a string, use a const char* and not a simple, char*. It will avoid any run-time error
if you try to modify the string, and it will be caught during compilation:


char* s = "Some string";
const char* = "Some string";     // Use this option.


For definitions of memory regions, refer pg.80


STRINGS
*******


char tracks[][10] = {"StringAB",               // Array of arrays to store strings
                          "StringB",
                          "StringCEF",
                          "StringD"};
[] - Contains the pointers to individual strings.
[80] - Contains the pointers to individual characters in each string. A size is specified here since, the strings have different number of characters.


C string library functions (some) - string.h


strchr() - Find the location of a character in a string
strcmp() - Compare two strings
strstr() - Find the location of a string inside another string
strcpy() - Copy one string to another
strlen() - Find the length of a string
strcat() - Concatenate two strings


For example, if you want to use strstr():
strstr(<string>, <substring>) will return the first index of the <substring> in <string>.
If it can't find the substring, it returns 0.


The size returned by strlen() can be stored in the data type 'size_t'.
size_t len = strlen(<string>);


char* names[] = {"Bowser", "Bonza", "Snodgrass"};          // Array of pointers to store strings; one pointer pointing at each string literal.


Reversing a string:


void print_reverse(char* s) {
     size_t len = strlen(s);
     char* t = s + len - 1          // Take the last character address by adding (len - 1) to the first index address of the input string
     while(t >= s) {                    // Iterate while the iterator address is greater or equal to the first address of input string.
          printf("%c", *t);          // Deference and print the character.
          t = t - 1;                    // Decrement the address by 1.
     }
     puts("");
}




CREATING SMALL TOOLS
********************


Input and output data streams
-----------------------------


A program should be able to take a suitable input and output as desired. You can use an ASCII file on disk to use for the input data, where the program will
process it and write/output a processed file, in a specific format.


You can re-direct standard input with '<'


> ./program < input.txt


You can re-direct standard output with '>'


> ./program < input.txt > output.txt


You can re-direct standard error with '2>'. By default, the standard error is printed with the display, even if the standard output is re-directed:


> ./program < input.txt > output.txt 2> errors.txt


To check the return/error status after a program has finished:


> echo $?     // On Linux
> echo %ERRORLEVEL%          // On Windows


To print explicitly to standard error standard output, use the fprintf() rather than printf(), which is more generalized:


printf("I like cakes\n");                    // This actually calls fprintf() with standard output.
fprintf(stdout, "I like cakes\n");          // specify the output, stdout is the standard output stream.
fprintf(stderr, "No cakes\n");               // specify the output, stderr is the standard error stream.


Similarly, to take input explicitly from the standard input, use the fscanf():


char word[10];
fscanf(stdin, "%9s", word);


You can also connect the output of one program to the input of another program using the pipe '|'. Both of the programs run at the
same time, as output is produced by the first program, it can be consumed by the second program. You can also connect more programs with pipes
to form a pipeline. When using pipes, the first program in the pipeline will take the standard input (<), and the last program will use the standard output (>):


>(./program1 | ./program2) < input.txt > output.txt          // On windows, you don't need './'




Custom data streams
-------------------


Instead of using just stdin, stdout and stderr, you can use your own data streams using a pointer to a file:
FILE* <file> = fopen(<filename>, <mode>);
FILE* in_file = fopen("input.txt", "r");          // Data stream will read from a file on disk.
FILE* out_file = fopen("output.txt", "w");          // Data stream will write to a file on disk.


To capture any error in processing a file, for e.g, in opening a file for reading:


FILE* in;
if(!(in = fopen("dont_exist.txt", "r"))) {
     fprintf(stderr, "Can't open the file.\n");
     return 1;
}


Now you can print using fprintf() and read using fscanf():


fprintf(out_file, "I like cakes.\n");
char word[10];
fscanf(in_file, "%9s", word);


Now you can close the file using fclose():


fclose(in_file);
fclose(out_file);




Reading program command-line arguments using main()
---------------------------------------------------


When a program is executed using command-line, you can specify arguments with which to run the program:


>./program option1 input1.txt option2 input2.txt output.txt     


These arguments are processed through the main() arguments, where 'argc' contains the number of arguments (including the program name) and argv[] contains the argument list:


int main(int argc, char* argv[])
{
....
}


Here the argument list is:


program - argv[0]
option1 - argv[1]
input1.txt - argv[2]
option2 - argv[3]
input2.txt - argv[4]
output.txt - argv[5]


When using the command-line arguments, you can also use the getopt() to specify the option flags before the arguments:


>./program -e 4 -a option1 input1.txt option2 input2.txt output.txt           // Options -e and -a


The options are processed by executing the getopt() to read the entire argument list:


# include <unistd.h>          // include the header file to include some POSIX libraries to create common set of functions to use across all popular operating systems.


...


while((ch = getopt(argc, argv, "ae:")) != EOF)          // Each time you call getopt(), it returns the next option it finds on the command-line. 'a' means the option is valid, 'e:' means the option needs an argument.
     switch(ch) {                                             // Check the option
          ...
          case 'e':
               engine_count = optarg;                         // optarg stores the option argument.
          ...
     }
argc -= optind;                                                  // optind stores the number of strings read to get past the option.
argv -= optind;                                                  // Shift the string pointer. Now the first item in the argument list argv[0] is the first argument (option1), not the program name.


For more getopt() options, see pg.155








USING MULTIPLE SOURCE FILES
***************************
Data types
----------
char - Stores a single character - takes 1 byte
int - Stores a range of numbers - takes 4 bytes
short - Stores a short range of numbers than int - takes 2 bytes
long - Stores a large count of numbers - takes 4 bytes
long long - Stores a very large count of numbers - takes 8 bytes
float - Stores floating-point numbers - takes 4 bytes
double - Stores high precision floating-point numbers - takes 8 bytes
long double - Stores very high precision floating-point numbers - takes 12 bytes
----------------------------------------------------------------------------------------------------------------------------------------------------------
If you type cast a short to int, it is safe, but the casting from int to short will give an error. Casting from int to long is safe, not long to int.


short x = 15;
int y = x;          // Casting from short to int.
printf("The value of x and y is %hi and %i", x, y);          // string representation for short and int, %hi and %i.


int x = 7;
int y = 2;
float z = (float)x / (float)y;          // Casting of int to float for float division.
float z = (float)x / y;                    // The compiler will also cast y to float.
printf("The value of z is %f", z);           // string representation for float, %f.


Writing functions
-----------------


While writing functions, before its usage/call, declare its prototype first, and then you can write its definition later in the program.


If a compiler finds a call to a function it doesn't know of, it will assume the function returns an int.


If better, collect all the function prototypes in a header file, '.h'.


//totaller.h
float add_with_tax(float f);


//totaller.c
# include <stdio.h>
# include "totaller.h"




Built-in/Reserved words
-----------------------


auto          if               break
int               case          long
char          register     continue
return          default          short
do               sizeof          double
static          else          struct
entry          switch          extern
typedef          float          union
for               unsigned     goto
while          enum          void
const          signed          volatile




Sharing code for multiple programs / using multiple source files
----------------------------------------------------------------


Functions can be shared across programs. Declare and define the function(s) in separate files, and then include the header with function declaration
in the main program file.


//encrypt.h
void encrypt(char*);


//encrypt.c
# include "encrypt.h"
void encrypt(char* message) {
     while(*message) {
          *message = *message ^ 31;
          message++;
     }
}


// message_hider.c
# include <stdio.h>
# include "encrypt.h"
int main()
{
     char msg[80];
     while(fgets(msg, 80, stdin)) {
          encrypt(msg);
          printf("%s", msg);
     }
}


Now compile, the program with all the necessary sources:


gcc message_hider.c encrypt.c -o message_hider




If you want to share variables declared in a header file, use the extern built-in word:


extern int passcode;          // Use can also a prefix for the variable name.




Compiling multiple source files
-------------------------------


While using multiple source files while building a program multiple times for testing, you only have to compile the source file which is being modified;
you can re-use the object files for other source files for re-building.


gcc reaction_control.c pitch_motor.c ... engine.c -o launch          // Skipping few source names




Inside a program directory, you can compile all the source files but not link them:


gcc -c *.c




Now if you modify only one source file, recompile (but not link) only that file:


gcc -c thruster.c




Now link all the object files:


gcc *.o -o launch


 
To avoid keeping track of the filenames while re-compiling or re-linking, use the automake tool. It keeps track of updated/modified files
by their timestamps. If a source file is newer than its pre-compiled object file, it is re-compiled.


On Linux, you have to use the 'make' tool. The 'make' tool prepares a target from a file based on a recipe and its dependencies.


For building programs, first you should provide recipies for all the compiling, and then linking in a makefile.


//makefile


launch.o: launch.c launch.h thruster.h          // <target>: <dependencies>
     gcc -c launch.c                                   //<tab><recipe>
thruster.o: thruster.c thruster.h
     gcc -c thruster.c
launch: launch.o thruster.o
     gcc launch.o thruster.o -o launch
    
Now use the command to automake:


> make launch


To generate makefiles, you can also use a tool called 'autoconf' at http://www.gnu.org/software/autoconf/
To see the other options for gnu 'make', see its manual at http://tinyurl.com/yczmjx


    
STRUCTS, UNIONS AND BITFIELDS
*****************************


Structs
-------


Structures can bundle together different data types under a struct type. Each data inside a struct is given a name and is fixed.


struct fish {
     const char* name;            // Stores a pointer to string. To store a copy, use char name[20]; for eg.
     const char* species;
     int teeth;
     int age;
};
struct fish snappy = {"Snappy", "Piranha", 69, 4};
printf("Name = %s\n", snappy.name);           // Access a member of struct
-------------------------------------------------------------------------------------------------
Structures can be passed as parameters to functions and new data contents can be added without affecting the existing functions, as long as it has all the fields it needs.


void catalog(struct fish f) {
....
}
-------------------------------------------------------------------------------------------------
You can create a copy of struct using an assignment:


struct fish gnasher = snappy;          // In this case it will copy pointer to string for .name and .species; both members in snappy and gnasher will point to the same string in memory.


-------------------------------------------------------------------------------------------------
Structures can be nested as well:


struct preferences {
     const char* food;
     float exercise_hours;
};


struct fish {
     const char* name;
     const char* species;
     int teeth;
     int age;
     struct preferences care;          // Nested structure
}


You can assign values to this struct:

struct fish snappy = {"Snappy", "Piranha", 69, 4, {"Meat", 7.5}};
	// OR (check)
struct fish snappy = {.name="Snappy", .species="Piranha", .teeth=69, .age=4, .care={"Meat", 7.5}};
	// OR (check)
struct fish snappy;
snappy = (struct date){"Snappy", "Piranha", 69, 4, {"Meat", 7.5}};

printf("Snappy likes to eat %s", snappy.care.food);
printf("Snappy likes to exercise for %f hours", snappy.care.exercise_hours);
-------------------------------------------------------------------------------------------------
You can also create an alias for a struct data type using typedef:


typedef struct cell_phone {                    // You can also skip 'typedef struct cell_phone {' to 'typedef struct {'
     int cell_no;
     const char* wallpaper;
     float minutes;
}phone;                              // 'phone' will become an alias for struct cell_phone


phone p = {5557879, "sinatra.jpg", 1.35};                // Now create a struct 'p' using the alias.
--------------------------------------------------------------------------------------------------
If a struct is passed as an argument to a function, it is passed by value. It creates a copy of the struct.


typedef struct {
     const char* name;
     const char* species;
     int age;
}turtle;


void happy_birthday(turtle t) {           // Function takes struct as an argument
     ....
}


turtle myrtle = {"Myrtle", "Leatherback sea turtle", 99};


happy_birthday(myrtle);                         // struct is passed in by value


turtle t = myrtle;                              // same as happy_birthday(myrtle);


The problem with this passed-in struct is that, any member which is not a pointer type, won't be updated outside the function. For this
purpose, we have to pass-in a pointer to struct:


void happy_birthday(turtle* t) {          // Pass-in a pointer to struct turtle
     (*t).age = (*t).age + 1;               // Dereference the pointer-to-struct before accessing or updating its members.
     // t -> age = t -> age + 1;               // You can also use this operation.
     printf("Happy Birthday %s! You are now %i years old!\n", (*t).name, (*t).age);
}


happy_birthday(&myrtle);                    // Pass the address of 'myrtle'
------------------------------------------------------------------------------------------------------------------------------------------------------------
Unions
------
Union is a data structure that can have several data fields like a struct, but can only store one field at a time to conserve memory; so only a space for its largest data field is created. 


typedef union {
     short count;               // Each of these fields will be stored in the same space. A float takes 4 bytes and a short takes 2 bytes, quantity will take 4 bytes.
     float weight;
     float volume;
}quantity;


You can now access the fields using these operations:


quantity q;
q.count = 4;          // Assign a short value to field 'count' using the dot notation.


quantity q = {.weight=1.5};               // Designated initializer sets a union field by a name. Supported by C99.


quantity q = {100};          // The initializer list for a union contains only one initializer. If no union memeber is explicitly designated, the first member named in the union type declaration is initialized.


typedef struct {
     const char* name;
     const char* country;
     quantity amount;
}fruit_order;


Unions are also used with structs:


fruit_order apples = {"apples", "England", .amount.weight=4.2};               // Using a designated initializer for the nested union.
--------------------------------------------------------------------------------------------------------------------------------------------------------
Enums
-----


Data type that can store a list of symbols/keys with numerical ordered values.


enum colors(RED, GREEN, PUCE);       // Here RED = 0, GREEN = 1, PUCE = 2


Any variable that is defined with a type of enum colors can only be set to one of the values from the enum list.


enum colors favourite = PUCE;


----------------------------------------------------------------------------------------------------------------------------
Bitfields
---------


Bitfield is used to store custom number of bit(s) for data. This is useful for storing binary decisions that may require 1 bit of storage, instead of using a short, to conserve memory.


Bitfields are best used when collected/grouped inside a struct. If used outside, the compiler might pad it out to the size of a word.


A bitfield should be declared with an unsigned int.


typedef struct {
     unsigned int low_pass_vcf:1;
     unsigned int filter_coupler:1;
     unsigned int reverb:1;
     unsigned int sequential:1;
     ...
}synth;


To use bitfields efficiently, you have to know how many bits it might store for its use. For eg. to store the months of the year, you can use values from 0-11 which will use 4 bits at most (0-15).
If you store values from 0-7, you need space for 3 bits only.


unsigned int month_no:4;


To know the amount of bitfields required for a data range, convert it into its binary equivalent, and calculate the number of bit places. (15 - 1111 - 4 bits)


DATA STRUCTURES AND DYNAMIC MEMORY
**********************************


Linked Lists
------------


Structures that are linked together in memory. Each structure points to the next structure; each structure is of same type. They're also called recursive structure.


typedef struct island {               // Recursive structures needs a name, even if typedef is used.
     char* name;
     char* opens;
     char* closes;
     struct island* next;      // Pointer to struct
}island;


Now initialize and create the structures:


island amity = {"Amity", "0900", "1700", NULL};
island craggy = {"Craggy", "0900", "1700", NULL};
island isla_nublar = {"Isla Nublar", "0900", "1700", NULL};
island shutter = {"Shutter", "0900", "1700", NULL};


Now link them:


amity.next = &craggy;
craggy.next = &isla_nublar;
isla_nublar.next = &shutter;


With these links, you can insert a new structure between an existing link:


island skull = {"Skull", "0900", "1700", NULL};
islan_nublar.next = &skull;
skull.next = &shutter;


Linked lists and Dynamic memory
-------------------------------
To create space for a data type on the heap, use the malloc() from stdlib.h.
With this you can now create new structures by allocating space for new structures on a required basis. In this example, we'll use a create(), display() and release() functions
to create linked lists while entering data at the prompt, then display them and release any data from the heap after using them:


# include <stdio.h>
# include <stdlib.h>
# include <string.h>


island* create(const char* name) {
     island* i = malloc(sizeof(island));
     i -> name = strdup(name);          // Copies a string by allocating a new space in the heap for copying.
     i -> opens = "0900";
     i -> closes = "1700";
     i -> next = NULL;
     return i;
}


void display(island* start) {
     island* i = start;
     for(; i != NULL; i = i -> next)
          printf("Name: %s Open: %s-%s\n", i -> name, i -> opens, i -> closes);
}


void release(island* start) {
     island* i = start;
     island* next = NULL;
     for(; i != NULL; i = next) {     // Iterate till the next struct address is NULL. Take the value of next after each iteration.
          next = i -> next;               // The value of the next struct is taken before the struct is released.
          free(i -> name);               // Release the name data on the heap.
          free(i);                         // Release the struct.
     }
}


int main()
{
     island* start = NULL;
     island* i = NULL;
     island* next = NULL;
     char name[80];
     for(; fgets(name, 80, stdin) != NULL ; i = next) {
          next = create(name);
          if(start == NULL)
               start = next;
          if(i != NULL)
               i -> next = next;
     }
     display(start);
     return 0;
}
    
Finding memory leaks using Valgrind
-----------------------------------


For using valgrind to find memory errors, you'd have to build a debug version of the program, to add debug info; things like line number are included.


gcc -g program.c -o program


Then run the program with valgrind which will intercept the malloc() calls and use its own version to track memory operarions.


valgrind --leak-check=full ./program


For more details, see pg.302




ADVANCED FUNCTIONS
******************


Function pointers can be passed as arguments to existing functions. This can help to improve a lot of code redundancy while
writing functions. Whenever you create a function, you also create a function pointer with the same name.


int funcName(int arg) {
     // Code
}
funcName(4); // When you call the function, you're using the function pointer. It contains the address of the function.


To declare a function pointer explicitly:


int (*warp_fn)(int); // Return type, function name as pointer and arguments
warp_fn = funcName;
warp_fn(4);          // Same as calling funcName(4);


char** (*names_fn)(char*, int);      // char** is for a string array pointer.


If you want to pass a fucntion as an argument to an existing function, in its definition, write as:


void find(int (*match)(char*)) {             // The passed-in function has to match the return type and the argument type(s).
     if (match("Game"))      // or if ((*match)("Game"))
          printf("OK");
     else
          printf("None");
}
You can cast a void* in a function paramater to point to anything. In the qsort() in the stdlib.h, you can cast the void* parameters in the comparator function, passed-in as an argument:


qsort(void* array, size_t length, size_t item_size, int (*compar)(const void*, const void*));


int compare(const void* score_a, const void* score_b) {      // const is used to make it immutable
     int a = *(int*)score_a;
     int b = *(int*)score_b;
     ......
}


Now, to create an array of function pointers. For more details, see pg, 338:


void (*funcArray[])(int) = {func1, func2, func3};     // Return type (* Pointer variable)(Param types)


To create variadic functions, which can take variable number of arguments. For this purpose, you have to use macros from stdarg.h:


# include <stdarg.h>
void print_ints(int args, ...) {     // args is the number of variable arguments passed. '...' is ellipsis, meaning more arguments are to come.
     va_list ap;                              // Store the variable arguments in a list.
     va_start(ap, args);                    // Specify the last argument, at which the variable arguments start.
     int i;
     for(i = 0; i < args; i++) {
          printf("Argument: %i\n", va_arg(ap, int));                // Extract the arguments using the macro va_arg, with va_list and int as values.
     }
     va_end(ap);                                                            // After finishing reading all the variable arguments, finish.
}
int main()
{
     print_ints(3, 79, 101, 32);                              // Call the function.
     print_ints(5, 79, 101, 32, 45, 62);
     return 0;
}




STATIC AND DYNAMIC LIBRARIES
****************************


Working with static libraries
-----------------------------


To make a static library, compile the '.c' files containing the function definitions using function prototypes in a
header file '.h' as object files, '.o' using the gcc '-c' flag. Then include that header file '.h' in the program
which uses the functions from the compiled library.


gcc -c encrypt.c -o encrypt.o


Now if you write a program which uses the library by including the header file,


// test_code.c
# include <stdio.h>
# include "encrypt.h" // If the file exists in the same directory as the source
int main()
{
     encrypt(<param>);
.....


Now, you can build the program,
gcc test_code.c encrypt.o -o test_code


If a header file is between angle brackets, they are part of the standard library.
On Linux, they may exist in:
/usr/local/include
/usr/include


Or if using a MinGW version of gcc,
C:\MinGW\include


If you want to share a header file, you can copy it into the standard library folder, and use:


# include <encrypt.h>


Or you can tell the gcc compiler where to find them:


gcc -I/home/user/documents/header_files ... test_code.c -o test_code


You can also include the compiled object library files using full path names:


gcc test_code.c /home/user/documents/object_files/encrypt.o -I/home/user/documents/header_files  -o test_code


To avoid listing a whole lot of compiled library files while building, you can create an archive file '.a' from a set of compiled
object files. On Linux, you can use a 'nm' command to list the contents of an archive. Example:


nm libl.a


You can now create a library archive using the archive command 'ar':


ar -rcs libencrypt.a library1.o library2.o


r - Update the archive file if it already exists.
c - Create the archive file without any feedback.
s - Creates an index at the start of the archive file.


Always name the archive beginning with 'lib'.


Now you can put the library archive file in your standard library folder. On Linux,


/usr/local/lib
/usr/lib


Or you can put in a custom directory:


/home/user/documents/lib_files


Now you can build using the libraries if your library files are in the standard library path using -l flag:


gcc test_code.c -I/home/user/documents/header_files -lencrypt -o test_code


You can also use several -l options. While using an -l flag, use the library archive name after the 'lib' prefix.


If you're using a custom library path:


gcc test_code.c -I/home/user/documents/header_files -L/home/user/documents/lib_files -lencrypt -o test_code


To list the contents of an archive file:


ar -t <filename>


To extract a single object file from an archive:


ar -x libhfsecurity.a encrypt.o




Working with dynamic libraries
------------------------------


Dynamic library links to the executable at runtime. A dynamic library can be built from several '.o' files, by properly linking
them together to form a single piece of object code.


First, create the object file:


gcc -c hfcal.c -I/includes -fPIC -o hfcal.o


fPIC - Positive independent code. Decision at run-time where to load it into memory.


Then, create a dynamic library from the object file, or from multiple object files:


gcc -shared hfcal.o -o /libs/libhfcal.so (Linux)
gcc -shared hfcal.o -o /libs/libhfcal.dll.a (Cygwin)
gcc -shared hfcal.o -o /libs/libhfcal.dylib (OSX)
gcc -shared hfcal.o -o C:\libs\hfcal.dll (MinGW on windows) (or libhfcal.dll or libhfcal.dll.a)


Now compile the program which will use the library:
gcc -I/includes -c elliptical.c -o elliptical.o


Now, link the compiled object code with the dynamic library.
gcc elliptical.o -L/libs -lhfcal -o elliptical


To run the program:
On Mac, the full path to the library is stored inside the executable:
> ./elliptical


On Linux, the library had to be added to the library path (LD_LIBRARY_PATH). The executable only stores the name of the library file,
and not its path.
> export LD_LIBRARY_PATH = $LD_LIBRARY_PATH:/libs
>./elliptical


On Windows using Cygwin:
> PATH = "$PATH:/libs"
>./elliptical


On Windows using MinGW:
> PATH = "%PATH%:C:\libs\"
>./elliptical




PROCESSES AND SYSTEM CALLS
**************************


C uses sysmtem calls in the operating system to work with the hardware.


The system() call will execute a command inside its parantheses using the command-line.


system("dir D:")     // Print out the contents of the D: drive.
system("gedit")          // Will launch an editor on Linux.


/* Using system() call */
# include <stdio.h>
# include <stdlib.h>
# include <time.h>


char* now() {                                   // Returns a pointer to a timestamp string
    time_t t;
    time(&t);
    return asctime(localtime (&t));
}


int main()
{
   char comment[60];
   char cmd[120];
   fgets(comment, 80, stdin);
   sprintf(cmd, "echo '%s %s' >> reports.log", comment, now());               // This command will append (>>) the comment to a file
   system(cmd);                                   // Call system() with the inserted command
   return 0;
}


In the above program, the system() call command will break:
(1) if the command inside system() contains apostrophes,
(2) If the PATH variable causes the system() to call the wrong program,
(3) If the program we're calling needs to have a specific set of environment variables set up first.


The system() call will run the program as a separate process.


The system() call is more suitable for general use.


For this purpose, we can use the exec() function. Ths OS has to interpret the command string inside system(), but the exec()
functions runs the specific program called.


The exec() function runs a specific program by replacing the current process, and it will have the exact process ID (PID) as the
current (old) process. These functions are located in "unistd.h".


If you type 'taskmgr' on windows or 'ps -ef' on other OS, you will see a list of processes under their IDs being tracked.


There are two groups of exec() functions, list functions and array functions.


The list functions:


These functions have the first two arguments as the name of the program and then the list of arguments followed by a NULL.


execl("/home/flynn/clu", "/home/flynn/clu", "paranoids", "contract", NULL)          // The first two arguments here provide the full path to the program
                                                                                                    // followed by arguments, ended by a NULL


execlp("clu", "clu", "paranoids", "contract", NULL)               // This searches for a command name to execute (first two arguments).


execle("/home/flynn/clu", "/home/flynn/clu", "paranoids", "contract", NULL, env_vars) // This contains a list a arguments + Environment variables
                                                                                                           // env_vars is an array of strings containing
                                                                                                           // environment variables.
The array functions (if the arguments are stored in an array or a vector of strings):


execv("/home/flynn/clu", my_args);          // Provide a full path to the program
execvp("clu", my_args);                         // Provide a name or a program to be searched


Environment variables with exec() functions
-------------------------------------------


You can read enviornment variables by using the getenv() function included in stdlib.h.


# include <stdio.h>
# include <stdlib.h>


// diner_info.c
int main(int argc, char* argv[]){
{
     printf("Diners: %s\n", argv[1]);
     printf("Juice: %s\n", getenv("JUICE"));          // Get the value of the environment variable "JUICE".
     return 0;
}




You can create a string array of environment variables, and pass them to the execle() function:


char* my_env[] = {"JUICE=peach and apple", NULL};
execle("diner_info", "diner_info", 4, NULL, my_env);


The execle() function will run the "diner_info" and set the command-line arguments and enviornment variables.


On Cygwin, you have to include "PATH=/usr/bin" if we're passing environment variables.


Exceptions with exec() functions
--------------------------------


As an exec() function run a program, it replaces the current process:


execle("diner_info", "diner_info", "4", NULL, my_env);
puts("Dude - the diner_info code is busted");               // With no exception, this code won't run


If a system call fails, it sets the value of errno variable defined in errno.h, along with a whole bunch
of standard error values. For eg:


EPERM=1               // Operation not permitted
ENOENT=2          // No such file or directory
ESRCH=3           // No such process


You can check the value of 'errno' variable against other standard error values in errno.h, or you can
look up a standard piece of error text using a function in string.h called strerror().


puts(strerror(errno));               // It converts an error number into a message.


For example, if the system can't find the program you're running and it sets the errno variable to ENOENT,
the above code will diaplay the message:


No such file or directory


// Example: The program tries to run the /sbin/ifconfig, if that fails, it will try the ipconfig command.


# include <stdio.h>
# include <unistd.h>
# include <errno.h>
# include <string.h>


int main()
{
     if (execl("/sbin/ifconfig", "/sbin/ifconfig", NULL) == -1)
          if (execlp("ipconfig", "ipconfig", NULL) == -1) {
               fprintf(stderr, "Cannot run ipconfig: %s", strerror(errno));
               return 1;
          }
     return 0;
}


# include <stdio.h>
# include <stdlib.h>


// Candidate program, coffee.c
int main(int argc, char* argv[])
{
     char* w = getenv("EXTRA");
     if(!w)
          w = getenv("FOOD");
     if(!w)
          w = argv[argc-1];
     char* c = getenv("EXTRA");
     if(!c)
          c = argv[argc-1];
     printf("%s with %s\n", c, w);
     return 0;
}


# include <string.h>
# include <stdio.h>
# include <errno.h>
int main()
{
     char* my_env[] = {"FOOD=coffee", NULL};
     if (execle("./coffee", "./coffee", "donuts", NULL, my_env) == -1)
     {
          fprintf(stderr, "Can't run process 0: %s\n", strerror(errno));
          return 1;
     }
     return 0;
}


See page 412 for more examples.




RSS Feeds
---------


// This program will execute RSS feeds by running the python script "rssgossip.py" by creating a process.
// But this program will stop after the first RSS feed is executing. To prevent this and to continue the
// program, we have to clone the current process.


int main(int argc, char* argv[])
{
     char* feeds[] = {"http://www.cnn.com/rss/celevs.xml",
                         "http://www.rollingstone.com/rock.xml",
                         "http://www.eonline.com/gossip.xml"};
     int times = 3;
     char* phrase = argv[1];
     int i;
     for (i = 0; i < times; i++) {
          char var[255];
          sprintf(var, "RSS_FEED=%s", feeds[i]);
          char* vars[] = {var, NULL};
          if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", phrase, NULL, vars) == -1) {
               fprintf(stderr, "Can't run script: %s\n", strerror(errno));
               return 1;
          }
     }
     return 0;
}


Cloning a process with fork()
-----------------------------


A process which relays to another process by using a exec() function will be terminated. To preserve its execution,
you can clone the current process using fork(). Currently, it is only supported under Mac and Linux, and under
Cygwin under Windows (it runs a little slower). It assigns a new process ID to the current process, and it will continue running.
This new process will be called the child process and the original process is called the parent process.


All these processes will run at the same time.


The technique is to call exec() on the child process.


The child process will receive 0 from fork() function and a non-zero value to the parent process.


To clone the exsiting process, use:


pid_t pid = fork();


pid_t is an integer data type, depending on the OS that will store the return data from the fork().


// Using the fork() function with the previous example


for (i = 0; i < times; i++) {
     char var[255];
     sprintf(var, "RSS_FEED=%s", feeds[i]);
     char* vars[] = {var, NULL};
     pid_t pid = fork();
     if (pid == -1) {
          fprintf(stderr, "Can't fork process: %s\n", strerror(errno));
          return 1;
     }
     if (!pid) {
          if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", phrase, NULL, vars) == -1) {
               fprintf(stderr, "Can't run script: %s\n", strerrno(errno));
               return 1;
          }
     }
}
    
If you want to use a similar implementation of fork() on windows, use a function called CreateProcess(),
which is like an enhanced version of system(). To find more about it, go to http://msdn.microsoft.com
and search for "CreateProcess".




To simplify error code, you can create a function that takes in the error message as an input, and then
you can call it:


void error(char* msg)
{
     fprintf(stderr, "%s: %s\n", msg, strerror(errno));
     exit(1);                                   // Terminate the program with status 1
}




Now you can replace multiple error-checking code:


pid_t pid = fork();
if (pid == -1) {
     error("Can't fork process");
}
if (execle(...) == -1) {
     error("Can't run script");
}




Interprocess Communication
**************************


Data stream redirection
-----------------------


Data stream descriptors for a program is fixed by default, where:


0 - Keyboard - Standard Input
1 - The screen - Standard Output
2 - The screen - Standard Error
3 - Other - Database connection


You can do redirection using the command-line by using the > and < operators:


$ ./myprog > output.txt 2> errors.log


On unix-based systems, you can redirect standard error to standard output:


$ ./myprog 2>&1                // &1 means to the standard input




For a custom data / file stream:


FILE* my_file = fopen("guitar.mp3", "r");


The OS will also skim through the descriptor table until it finds an empty slot and register the new file there.


0 - Keyboard - Standard Input
1 - The screen - Standard Output
2 - The screen - Standard Error
3 - Other - Database connection
4 - File - guitar.mp3


The slots in the descriptor table is from 0 to 255.


Once you've the file pointer, you can find it in the descriptor table by calling the fileno().
fileno() doesn't return -1


int descriptor = fileno(my_file)          // Pass-in the file pointer


You can also change a data stream already registered against a descriptor. For instance, if you want
to plug file descriptor 4 to 3, you can use the dup2() function:


dup2(4, 3);


0 - Keyboard - Standard Input
1 - The screen - Standard Output
2 - The screen - Standard Error
3 - File - guitar.mp3
4 - File - guitar.mp3


Now the data stream (the FILE*) is now registered with file descriptors 3 and 4.


// Redirecting the standard output to a custom file stream in newshound.c
    
int main(int argc, char* argv[])
{
     char* phrase = argv[1];
     char* vars[] = {"RSS_FEED=http://www.cnn.com/rss/celebs.xml", NULL};
     FILE* f = fopen("stories.txt", "w");
     if (!f) {
          error("Can't open stories.txt");
     }
     pid_t pid = fork();
     if (pid == -1) {
          error("Can't fork process");
     }
     if (!pid) {
          if (dup2(fileno(f), 1) == -1)
               error("Can't redirect standard output");
          }
          if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", phrase, NULL, vars) == -1) {
               error("Can't run script");
          }
     }
     return 0;
}


Waiting for a process to complete
---------------------------------


This program fails to write to a "stories.txt" because it has to wait for the child process to complete.


You have to use the waitpid() function, which accepts a process ID for the child process, and it won't return
until the child process dies.


waitpid() takes three parameters:


waitpid(pid, &pid_status, options)


pid - process ID given by fork() when it created a child process.
pid_status - This will store exit informaton about the child process, and it need to be ane exit int pointer.
options - Options for waitpid(), typing man waitpid will give you more info. Options 0 means the function
            will wait until the process finishes.


We need to include "wait.h" to use waitpid() function.


# include <sys/wait.h>
.......
     int pid_status;
     if (waitpid(pid, &pid_status, 0) == -1 {
          error("Error waiting for child process");
     }
     return 0;
}


To find out about the exit status about a child process, you'd have to pass the "pid_status" value
through a macro called WEXITSTATUS(). This macro reads the first 8 bits of the value that contain the
exit information.


if (WEXITSTATUS(pid_status))          // If the exit status is non-zero
     puts("Error status non-zero");






Reading real-time data from a child process
-------------------------------------------


It is also possible to read the real-time data from a child process. If you're using the command-line, for example,
you can connect the output of a program to another using a pipe "|", as we've seen before.


$ python rssgossip.py -u 'pajama death' | grep 'http'     // -u tells the script to include story links. grep finds all lines containing "http".
     http://www.rock-news.com/exclusive/24.html
     http://www.rolling-stone.com/pdalbum.html




To create this mechanism in C, you need to use the pipe() function. It creates a pipe and two descriptors, adds them
to the descriptor table. It stores the file descriptors in a two-dimensional array:


int fd[2];                                        // Descriptors will be stored in this array
if (pipe(fd) == -1) {                         // Pass the name of the array to the pipe()
     error("Can't create the pipe");
}


0 - Keyboard - Standard Input
1 - The screen - Standard Output
2 - The screen - Standard Error
3 - Read-end of the pipe
4 - Write-end of the pipe


Here, the fd[0] is the descriptor that reads from the pipe. fd[1] is the descriptor that writes to the pipe.


In the child process, you have to close the read-end of the pipe, fd[0], and then change the child's
process standard output to point to the write-end of the pipe fd[1].


close(fd[0]);               // Close the read-end
dup2(fd[1], 1);               // Connect the write-end to the Standard output


In the parent process, you have to close the write-end of the pipe, fd[1], and then connect the read-end
of the pipe, fd[0] to the standard input.


close(fd[1]);
dup2(fd[0], 0);


With this, everything that the child writes to the pipe will be read through the standard input of the
parent process.


// An example, which connects the parent and the child process to a pipe.


void open_url(char* url) {
     char launch[255];
     sprintf(launch, "cmd /c start %s", url);     // launch in windows
     system(launch);
     sprintf(launch, "x-www-browser '%s' &", url);     // launch in linux
     system(launch);
     sprintf(launch, "open '%s'", url);     // launch in mac
     system(launch);
}


int main(int argc, char* argv[])
{
     char* phrase = argv[1];
     char* vars[] = {"RSS_FEED=http://www.cnn.com/rss/celebs.xml", NULL};
     int fd[2];          // This array will store the descriptors for the pipe.
     if (pipe(fd) == -1) {
          error("Can't create the pipe");
     }
     pid_t pid = fork();
     if (pid == -1) {
          error("Can't fork process");
     }
     if (!pid) {                    // You're in the child process
          close(fd[0]);
          dup2(fd[1], 1);
          // "-u" tells the script to display URLs for the stories
          if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", "-u", phrase, NULL, vars) == -1) {
               error("Can't run script");
          }
     }
     // Parent process here
     close(fd[1]);
     dup2(fd[0], 0);
     char line[255];
     while(fgets(line, 255, stdin)) {          // Read from standard input, which is connected to the pipe
          if (line[0] == '\t')                    // If the line starts with a tab, then it's a URL
               open_url(line + 1);                    // "line + 1" is the string starting after the tab character
     }
     return 0;
}


Other command-line programs for the web:
curl/wget - talk to web servers using command line
mail/mutt - send email from the command line
convert - convert one image format to another


When the child process dies, the pipe is closed and the fgets() command receives an end-of-file, which means
the fgets() function returns 0, and the loop ends.


You can also connect the pipe the other way around, so that the parent sends data to the child process.


For multidirectional communication, you can create two pipes, from parent t child, and from child to parent.


To create a file based pipe, you can use the mkfifo() system call. See http://tinyurl.com/cdf6ve5




The death of a process
----------------------


A process is ended using Ctrl-C. This happens because the OS sends an interrupt signal to the program.


The signal is just a short message: a single integer value.


Each signal is mapped to a function called to a signal handler. The default signal handler for interrupt signal
calls exit() function.


Process signal mappings
-----------------------
SIGURG          Do nothing
SIGINT          Call exit()               // This is the interrupt signal. It has value 2.


The OS can also kill a program, but signal table will let you run your own code when a process receives a signal.


To run your own code, you have to use "sigaction" struct, which is a function wrapper for the interrupt handler.


struct sigaction action;               // Create a new action
action.sa_handler = diediedie;          // Name of the function to be called as interrupt handler
sigemptyset(&action.sa_mask);          // The mask is a way of filtering the signals that the sigaction will handle.
action.sa_flags = 0;


The function handler returns void type and takes in an int signal value.


void diediedie(int sig)
{
     // Careful about writing to standard output and standard error. They may not be available during interrupt.
     puts("Goodbye");    
     exit(1);
}


The "sigaction" struct is registered with sigaction(). This function will return -1 if it fails,
and then it will set the errno :


sigaction(signal_no, &new_action, &old_action);


signal_no - The integer value of the signal you want to handle. You want to pass one of the
               standard signal symbols, like SIGINT or SIGQUIT.
new_action - Address of the new sigaction you want to register.
old_action - Address of the old (current) handler that you're about to replace.


You can write a function, "catch_signal" that will accept and register a new signal handler:


int catch_signal(int sig, void (*handler)(int))
{
     struct sigaction action;
     action.sa_handler = handler;
     sigemptyset(&action.sa_mask);
     action.sa_flags = 0;
     return sigaction(sig, &action, NULL);
}


// Example program that registers a custom interrupt handler


# include <stdio.h>
# include <signal.h>
# include <stdlib.h>


void diediedie(int sig)
{
     puts("Goodbye");
     exit(1);
}


int catch_signal(int sig, void (*handler)(int))
{
     struct sigaction action;
     action.sa_handler = handler;
     sigemptyset(&action.sa_mask);
     action.sa_flags = 0;
     return sigaction(sig, &action, NULL);
}


int main()
{
     if(catch_signal(SIGINT, diediedie) == -1) {          // SIGINT is interrupt signal
          fprintf(stderr, "Can't map the handler");
          exit(2);
     }
     char name[30];
     printf("Enter name: ");
     fgets(name, 30, stdin);
     printf("Hello %s\n", name);
     return 0;
}


Signal mappings:


SIGINT - The process was interrupted
SIGQUIT - Someone asked the process to stop and dump the memory in a core dump file
SIGFPE - Floating-point error         
SIGTRAP - The debugger asks where the process is
SIGSEGV - The process tried to access illegal memory    
SIGWINCH - The terminal window changed size         
SIGTERM - Someone just asked the kernel to kill the process
SIGPIPE - The process wrote to a pipe that nothing's reading    




Killing processes
-----------------


On unix-style systems, you can use the "kill" command to send a SIGTERM signal, but you can also use other signals
if you like.


To kill a process, you have to use it process id (PID)


$ kill 78222               // send SIGTERM to a program
$ kill -INT 78222          // send SIGINT to the program
$ kill -SEGV 78222          // send SIGSEGV to the program
$ kill -KILL 78222          // send SIGKILL, which can't be ignored. This will always kill the program




Raise a signal
--------------


You can also raise a signal inside a process using a raise() command inside custom signal handlers. It means your code
can receive a signal for something minor and then choose to raise a more serious signal.


raise(SIGTERM);               // send a signal to be raised




Send an alarm signal
--------------------


You can use an alarm signal, SIGALRM, created by the process's interval timer.


alarm(120);                              // This will send a SIGALRM in 120 seconds
do_important_busy_work();                    // Meanwhile, you can do something else
do_more_busy_work();


After the SIGALRM signal is sent, it will stop the process. So, most of the time, you'd want to set the handler to
do something else.


catch_signal(SIGALRM, custom_handler);
alarm(120);


If you need to run a particular job every few seconds, or if you want to limit the amount of time you spend doing
a job, alarm signals are a great way of getting a program to interrupt itself.


Don't use alarm() and sleep() signals at the same time. They both use the same interval timer, and will interfere.


If you have set a previous timer with alarm(), calling alarm() again will reset it and set a new timer.


To set an alarm for less than a second, you need to use a different function, called setitimer(). See, http://tinyurl.com/3o7hzbm




Restore the default signal handler
----------------------------------


To restore the default signal handler, "signal.h" has a special symbol SIG_DFL, which means handle it the default way.


catch_signal(SIGTERM, SIG_DFL);




Ignore a signal
---------------


The "signal.h" has a symbol that tells a process to completely ignore a signal. You should be careful before you choose
to ignore a signal.


catch_signal(SIGINT, SIG_IGN);




// Program that tests the users math skills. It asks the user to work the answer to a simple multiplication problem
// and keeps track of how many answers he got right. The program will keep running forever, unless:
// 1. The user presses Ctrl-C, or
// 2. The user takes more than five seconds to answer the question.
// When the program ends, it will display the final score and set the exit status to 0.


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <string.h>
#include <errno.h>
#include <signal.h>


int score = 0;


void end_game(int sig)
{
     printf("\nFinal score: %i\n", score);
     exit(0);                                             // Set the exit status to 0 and stop
}


int catch_signal(int sig, void (*handler)(int))
{
     struct sigaction action;
     action.sa_handler = handler;
     sigemptyset(&action.sa_mask);
     action.sa_flags = 0;
     return sigaction (sig, &action, NULL);
}


void times_up(int sig)
{
     puts("\nTIME'S UP!");
     raise(SIGINT);                                        // Raising SIGINT will make the program display the final score and end_game()
}


void error(char *msg)
{
     fprintf(stderr, "%s: %s\n", msg, strerror(errno));
     exit(1);
}


int main()
{
     catch_signal(SIGALRM,times_up);
     catch_signal(SIGINT,end_game);
     srandom (time (0));
     while(1) {
          int a = random() % 11;
          int b = random() % 11;
          char txt[4];
          alarm(5);                                             // Set the alarm to 5 seconds. As long as we're in loop, it will keep re-setting.
          printf("\nWhat is %i times %i? ", a, b);
          fgets(txt, 4, stdin);
          int answer = atoi(txt);
          if (answer == a * b)
               score++;
          else
               printf("\nWrong! Score: %i\n", score);
     }
     return 0;
}






 












    
    
    
     