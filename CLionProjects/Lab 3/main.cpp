/*
//
//  main.cpp
//  Lab 3
//
//  Created by Simar on 9/15/24.
//

// This program will read in the quantity of a particular item and its price.
// It will then print out the total price.
// The input will come from the keyboard and the output will go to
// the screen.
// Simar Gill
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int quantity; // contains the amount of items purchased
    float itemPrice; // contains the price of each item
    float totalBill; // contains the total bill.
    cout << setprecision(4) << fixed << showpoint; // formatted output
    cout << "Please input the number of items bought" << endl;
    cin >> quantity;

    cout << "Please input the price of the items bought" << endl;
    cin >> itemPrice;

    totalBill = quantity * itemPrice;
    cout << "The total bill is $" << totalBill << endl;

    // Fill in the input statement to bring in the quantity.
    // Fill in the prompt to ask for the price.
    // Fill in the input statement to bring in the price of each item.
    // Fill in the assignment statement to determine the total bill.
    // Fill in the output statement to print total bill,
    // with a label to the screen.
    return 0;
}
*/

/*
// This program will bring in two prices and two quantities of items
// from the keyboard and print those numbers in a formatted chart.
//Simar Gill
#include <iostream>
#include <sstream>

// formatted output.
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    float price1, price2;
    int quantity1, quantity2;
    cout << setprecision(2) << fixed << showpoint; // Set formatting for output


    cout << "Please input the price and quantity of the first item" << endl;
    cin >> price1 >> quantity1;


    cout << "Please input the price and quantity of the second item" << endl;
    cin >> price2 >> quantity2;


    cout << setw(15) << "PRICE" << setw(12) << "QUANTITY\n\n";


    cout << setw(15) << price1 << setw(12) << quantity1 << endl;


    cout << setw(15) << price2 << setw(12) << quantity2 << endl; // Added the missing semicolon

    return 0;
}
*/

/*
// This program will input the value of two sides of a right triangle and then
// determine the size of the hypotenuse.
// Simar Gill
 #include <iostream>
#include <cmath> // needed for math functions like sqrt()
#include <iomanip>
using namespace std;
int main()
{
    float a,b; // the smaller two sides of the triangle
    float hyp; // the hypotenuse calculated by the program
    cout << "Please input the value of the two sides" << endl;
    cin >> a >> b;
    // Fill in the assignment statement that determines the hypotenuse
    hyp = sqrt(a*a + b*b);

    cout << "The sides of the right triangle are " << a << " and " << b << endl;
    cout << "The hypotenuse is " << fixed << setprecision(2) << hyp << endl;
    return 0;
}
*/

/*
// This program will determine the batting average of a player.
// The number of hits and at bats are set internally in the program.
// Simar Gill
#include <iomanip>
#include <iostream>
using namespace std;
const int AT_BAT = 421;
const int HITS = 123;
int main()
{
   float batAvg;
    batAvg = static_cast<float>(HITS) / AT_BAT; // an assignment statement
    cout << "The batting average is "  << fixed << setprecision(6) << batAvg << endl; // output the result
    return 0;
}
*/
// This program will read in the quantity of a particular item and its price.
// It will then print out the total price.
// The input will come from a data file and the output will go to
// an output file.
// PLACE YOUR NAME HERE
// This program will read in the quantity of a particular item and its price.
// It will then print out the total price.
// The input will come from a data file and the output will go to
// an output file.
// PLACE YOUR NAME HERE

/*
// This program will read in the quantity of a particular item and its price.
// It will then print out the total price.
// The input will come from a data file and the output will go to
// an output file.
// PLACE YOUR NAME HERE
/
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream dataIn; // defines an input stream for a data file
    ofstream dataOut; // defines an output stream for an output file
    int quantity; // contains the amount of items purchased
    float itemPrice; // contains the price of each item
    float totalBill; // contains the total bill, i.e. the price of all items

    dataIn.open("transaction.dat"); // Open the input file
    dataOut.open("bill.out"); // Open the output file

    // Check if files opened successfully
    if (!dataIn) {
        cerr << "Error opening input file." << endl;
        return 1;
    }
    if (!dataOut) {
        cerr << "Error opening output file." << endl;
        return 1;
    }

    // Read the quantity and price of the item from the input file
    dataIn >> quantity >> itemPrice;

    // Compute the total bill
    totalBill = quantity * itemPrice;

    // Output the total bill with a label to the output file
    dataOut << "The total bill is $" << setprecision(2) << fixed << totalBill << endl;

    // Close the files
    dataIn.close();
    dataOut.close();

    return 0;
}
*/

/*
#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

int main()
{
    float grade1;
    float grade2;
    float grade3;
    float average;

    cout << "Please enter the first grade" << endl;
    cin >> grade1;

    cout << "Please enter a second grade" <<endl;
    cin >> grade2;

    cout << "Please enter a third grade" << endl;
    cin >> grade3;

average = (grade1 + grade2 + grade3) / 3;
    cout << "The average is " << fixed << setprecision(2) << average << endl;

    return 0;
}
*/




/*
#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    float American;
    float French;
    float modern;

    float Americantotal;
    float Frenchtotal;
    float moderntotal;

    float totalsales;



    cout << "Please input the number of American Colonial chairs sold" << endl;
    cin >> American;

    Americantotal = American * 85;

    cout <<"Please input the number of French chairs sold" << endl;
    cin >> French;

    Frenchtotal = French * 57.50;

    cout << "Please input the number of Modern Chairs sold" << endl;
    cin >> modern;

    moderntotal = modern *127.75;

cout << "The total sales of American colonial sales is " << fixed << setprecision(2) << Americantotal << endl;

    cout << "The total sales of French classical chairs is " << fixed << setprecision(2) << Frenchtotal << endl;

    cout << "The total sales of modern chairs is " << fixed << setprecision(2) << moderntotal << endl;

    totalsales = Americantotal + Frenchtotal + moderntotal;

    cout << "The total sales of all chairs is " << fixed << setprecision(2) << totalsales << endl;

    return 0;
}
*/

/*
#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    float totalsales;
    float statetax;
    float localtax;

    float statetax2;
    float localtax2;

    cout << "Please enter the total sales for the month" << endl;
    cin >> totalsales;

    cout << "Please input the state tax percentage in decimal form (.02 for 2%)" << endl;
    cin >> statetax;

    statetax2 = statetax * totalsales;

    cout << "Please input the local tax percentage in decimal form (.02 for 2%)" << endl;
    cin >> localtax;

    localtax2 = localtax * totalsales;

    cout << "The total sales for the month is " << totalsales << endl;

    cout << "The total state tax for the month is " <<fixed << setprecision(2) << statetax2 << endl;

    cout << "The local tax for the month is " << fixed << setprecision(2) << localtax2 << endl;

    return 0;
}
*/

