// This program tests whether or not an initialized value
// is equal to a value input by the user
// Simar Gill
/*
#include <iostream>
using namespace std;
int main( )
{
    int num1;
    int num2;
    cout << "Please enter an integer" << endl;
    cin >> num1 >> num2;
    cout << "num1 = " << num1 << " and num2 = " << num2 << endl;
    if (num1 == num2)
    {
        cout << "The values are the same\n";
        cout << "Hey, that’s a coincidence!" << endl;
    }
    else (num1 != num2);
        cout << "The values are not the same" << endl;
    return 0;
}
*/


/*
// This program prints "You Pass" if a student's average is
// 60 or higher and prints "You Fail" otherwise
// Simar Gill
#include <iostream>
using namespace std;
int main()
{
    float average; // holds the grade average
    cout << "Input your average:" << endl;
    cin >> average;
    if (average >= 60 && average <= 79)
        cout << "You Pass" << endl;
    else if (average >= 0 && average <= 59)
        cout << "You Fail" << endl;
    else if (average >= 90 && average <= 100 )
        cout << "A" << endl;
    else if (average >= 80 && average <= 89 )
        cout << "B" << endl;
    else if (average > 100)
        cout << "Invalid data" << endl;
    return 0;
}
*/


/*
// This program illustrates the use of logical operators
// Simar Gill
#include <iostream>
using namespace std;
int main()
{
    char year;
    float gpa;
    cout << "What year student are you ?" << endl;
    cout << "Enter 1 (freshman), 2 (sophomore), 3 (junior), or 4 (senior)"
    << endl << endl;
    cin >> year;
    cout << "Now enter your GPA" << endl;
    cin >> gpa;
    if (gpa >= 2.0 && year == '4')
        cout << "It is time to graduate soon" << endl;
    else if (year != '4'|| gpa <2.0)
        cout << "You need more schooling" << endl;
    return 0;
}
*/

/*
// Simar Gill
#include <iostream>
using namespace std;

int main() {
    char grade;
    cout << "What grade did you earn in Programming I ?" << endl;
    cin >> grade;

    if (grade == 'A') {
        cout << "an A - excellent work !" << endl;
    }
    else if (grade == 'B') {
        cout << "you got a B - good job" << endl;
    }
    else if (grade == 'C') {
        cout << "earning a C is satisfactory" << endl;
    }
    else if (grade == 'D') {
        cout << "while D is passing, there is a problem" << endl;
    }
    else if (grade == 'F') {
        cout << "you failed - better luck next time" << endl;
    }
    else {
        cout << "You did not enter an A, B, C, D, or F" << endl;
    }

    return 0;
}
*/

/*
#include <iomanip>
#include <iostream>
using namespace std;
int main() {

    float q1;
    float q2;
    float q3;
    float q4;
    float average;

    cout << "Please input your quarterly water bill for quarter 1" << endl;
    cin >> q1;

    cout << "Please input your quarterly water bill for quarter 2" << endl;
    cin >> q2;

    cout << "Please input your quarterly water bill for quarter 3" << endl;
    cin >> q3;

    cout << "Please input your quarterly water bill for quarter 4" << endl;
    cin >> q4;

    cout << fixed << setprecision(2);

average = (q1 + q2 + q3 + q4) / 12;
    if (average > 75) {
cout << "Your average monthly bill is $" << average  <<  ". You are using excessive amounts of water" << endl;
    }
    else if ( average > 25 && average < 75) {
        cout << "Your average monthly bill is $" << average << ". You are using a typical amount of water" << endl;
    }
    else if (average < 25) {
        cout << "Your average monthly bill is $" << average << ". Great job on conserving water!" << endl;
    }


    return 0;
}
*/

/*
#include <iostream>
#include <iomanip>

using namespace std;
int main() {
    float shirts;
    float price;
    cout << "How many shirts would you like ?" << endl;
    cin >> shirts;

    if (shirts > 5 && shirts  < 10) {
        price = (shirts * 12) * .10;
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $" << price << "."  << endl;
    }
    else if (shirts > 0 && shirts < 5) {
        price = (shirts * 12);
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $" << price << "."  << endl;
    }
    else if (shirts > 10 && shirts < 20) {
        price = (shirts * 12) * .15;
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $" << price << "."  << endl;
    }
    else if (shirts > 20 && shirts < 30) {
        price = (shirts * 12) * .20;
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $" << price << "."  << endl;
    }
    else if (shirts >= 31) {
        price = (shirts * 12) *.25;
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $" << price << "."  << endl;
    }
    else if (shirts == 0) {
        cout << setprecision(2) << fixed << "The cost per shirt is $12 is $0.00" << endl;
    }
    else if (shirts < 0 ) {
        cout << "This is invalid, you have to enter a positive amount of shrits" << endl;
    }
    return 0;
}
*/

#include <iostream>
using namespace std;

int main() {
    char residency, roomAndBoard;
    int totalBill = 0;


    cout << "Please input \"I\" if you are in-state or \"O\" if you are out-of-state: ";
    cin >> residency;

    // Set tuition based on residency
    if (residency == 'I' || residency == 'i') {
        totalBill = 3000;
    } else if (residency == 'O' || residency == 'o') {
        totalBill = 4500;
    }

    cout << "Please input \"Y\" if you require room and board and \"N\" if you do not: ";
    cin >> roomAndBoard;


    if (roomAndBoard == 'Y' || roomAndBoard == 'y') {
        if (residency == 'I' || residency == 'i') {
            totalBill += 2500;
        } else if (residency == 'O' || residency == 'o') {
            totalBill += 3500;
        }
    }
    cout << "Your total bill for this semester is $" << totalBill << endl;

    return 0;
}
