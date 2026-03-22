/*


// This program prints the proverb
// "Now is the time for all good men to come to the aid of their party"
// in a function (procedure) called writeProverb that is called by the main function
//Simar Gill
#include <iostream>
using namespace std;
void writeProverb(); //This is the prototype for the writeProverb function
int main() {

writeProverb();

return 0;
}

void writeProverb() {
cout << " Now is the time for all good men to the aid of their party" << endl;
}
*/

// This program will allow the user to input from the keyboard
// whether the last word to the following proverb should be party or country

// "Now is the time for all good men to come to the aid of their _____"
// Inputting a 1 will use the word party. Any other number will the word country.

// Simar Gill

#include <iostream>
#include <string>
using namespace std;

//Fill in the prototype of the function writeProverb.
void writeProverb(int);

int main()
{


int wordCode;

cout << "Given the phrase:" << endl;
cout << "Now is the time for all good men to come to the aid of their ___"
<< endl;
cout << "Input a 1 if you want the sentence to be finished with party"
<< endl;
cout << "Input any other number for the word country" << endl; cout << "Please input your choice now" << endl;
cin >> wordCode;
cout << endl;
writeProverb(wordCode);
return 0;

}

void writeProverb(int number)
{
cin >> number;
if (number == 1)
cout << "Party" << endl;
}
