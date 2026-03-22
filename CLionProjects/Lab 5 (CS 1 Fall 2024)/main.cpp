// Simar Gill
/*
#include <iostream>
using namespace std;
int main()
{
    char letter = 'a';
    cout << "Enter the letter x to exit the program" << endl;
    do
    {
        cout << "Please enter a letter" << endl;
        cin >> letter;
        cout << "The letter you entered is " << letter << endl;
    }
    while (letter != 'x');

    return 0;
}
*/


/*
// This program illustrates the use of a sentinel in a while loop.
// The user is asked for monthly rainfall totals until a sentinel
// value of -1 is entered. Then the total rainfall is displayed.
// Simar Gill
#include <iostream>
using namespace std;
int main()
{
    int month = 1;
    float total = 0, rain;
    cout << "Enter the total rainfall for month " << month << endl;
    cout << "Enter -1 when you are finished" << endl;

    cin >> rain;
    while (rain != -1)
    {
        total += rain;
        month++;
        cout << "Enter the total rainfall in inches for month "
        << month << endl;
        cout << "Enter -1 when you are finished" << endl;
        cin >> rain;
    }
    if (month == 1)
        cout << "No data has been entered" << endl;
    else
        cout << "The total rainfall for the " << month-1
    << " months is "<< total << " inches." << endl;
    return 0;
}
*/









/*
// This program displays a hot beverage menu and prompts the user to
// make a selection. A switch statement determines which item the user
// has chosen. A do-while loop repeats until the user selects item E
// from the menu.
// Simar Gill
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int number;
    float cost;
    char beverage;


    bool validBeverage;

    cout << fixed << showpoint << setprecision(2);

    do
    {
        cout << endl << endl;
        cout << "Hot Beverage Menu" << endl << endl;
        cout << "A: Coffee $1.00" << endl;
        cout << "B: Tea $ .75" << endl;
        cout << "C: Hot Chocolate $1.25" << endl;
        cout << "D: Cappuccino $2.50" << endl << endl << endl;
        cout << "Enter the beverage A, B, C, or D you desire" << endl;
        cout << "Enter E to exit the program" << endl << endl;
        cin >> beverage;


        switch(beverage)
        {
            case 'a':
            case 'A':
            case 'b':
            case 'B':
            case 'c':
            case 'C':
            case 'd':
            case 'D':
                validBeverage = true;
                break;
            default:
                validBeverage = false;
        }

        if (validBeverage)
        {
            cout << "How many cups would you like?" << endl;
            cin >> number;
        }

        // Fill in the code to begin a switch statement
        // that is controlled by beverage
        switch (beverage)
        {
            case 'a':
            case 'A':
                cost = number * 1.0;
                cout << "The total cost is $ " << cost << endl;
                break;

            case 'b':
                case 'B':
            cost = number * .75;
            cout << "The total cost is $ " << cost << endl;
            break;

            case 'c':
                case 'C':
            cost = number * 1.25;
            cout << "The total cost is $ " << cost << endl;
            break;

            case 'd':
                case 'D':
            cost = number * 2.50;
            cout << "The total cost is $ " << cost << endl;
            break;

            case 'e':
            case 'E':
                cout << " Please come again" << endl;
                break;

            default:
                cout << "Invalid selection." << endl;
                cout << " Try again please" << endl;
        }
    }
    while (beverage != 'e' && beverage != 'E');



    return 0;
}
*/

/*
// This program has the user input a number n and then finds the
// mean of the first n positive integers
// Simar Gill
#include <iostream>
using namespace std;
int main() {
    int value;     // value is some positive number n
    int total = 0; // total holds the sum of the first n positive numbers
    int number;    // the amount of numbers
    float mean;    // the average of the first n positive numbers
    cout << "Please enter a positive integer" << endl;
    cin >> value;

    if (value > 0)
    {
        for (number = 1; number <= value ; number ++)
            {
            total = total + number;
            }  // curly braces are optional since there is only one statement

         mean = static_cast<float>(total) / value; // note the use of typecast
                                                   // operator here

    cout << "The mean average of the first " << value
         << " positive integers is " << mean << endl;
}
else
cout << "Invalid input - integer must be positive" << endl;
return 0;
}
*/

/*
#include <iostream>3
using namespace std;
int main() {
    int value1;
    int value2;
    int total = 0;
    int total1 = 1;
    int number;
    int number1;
    float mean;
    cout << "Please enter a positive integer" << endl;
    cin >> value1;
    cout << "Please enter another positive integer" << endl;
    cin >> value2;

    for (number = value1; number <= value2; number++) {
        total += number;
    }

    number1 = value1;
    while (number1 < value2){
        number1++;
        total1++;

    }


mean = static_cast<float>(total)/total1;
    cout << "The mean of " << value1<< " and " << value2 << " is " << mean << endl;

    return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main() {
    int numStudents;
    int numStudents2;
    float numHours, total, average;
    float numHours2, total2, average2;
    int CSstudent,day = 0;
    int BIOstudent, day1 = 0;
    int numdays;

    cout << "This program will find the average number of hours a day"
    << "that a student spent programming and studying biology over a long weekend\n\n";
    cout <<"How many students are there for programming?" << endl << endl;
    cin >> numStudents;
    cout << "How many students are there for biology?" << endl << endl;
    cin >> numStudents2;
    cout << "How many days is this long weekend?" << endl << endl;
    cin >> numdays;

    for(int CSstudent = 1; CSstudent <= numStudents; CSstudent++) {
        total = 0;
        for (int day = 1; day <= (numdays); day++) {
            cout << "Please enter the number of hours worked by a programming student "
            << CSstudent << " on day" << day << "." << endl;
            cin >> numHours;

            total = total + numHours;
        }

        average = total / (numdays);

        cout << endl;
        cout << "The average number of hours per day spent programming by "
        << "student " << CSstudent << " is " << average
        << endl << endl << endl;
    }

    for (int BIOstudent = 1; BIOstudent <= numStudents2; BIOstudent++) {
        total2 = 0;
        for (int day1 = 1; day1 <= numdays; day1++) {
            cout << "Please enter the number of hours worked by biology student "
                 << BIOstudent << " on day " << day1 << "." << endl;
            cin >> numHours2;

            total2 += numHours2;
        }

        average2 = total2 / numdays;

        cout << endl;
        cout << "The average number of hours per day spent on biology by "
             << "student " << BIOstudent << " is " << average2
             << endl << endl;
    }

    for (int CSstudent = 1; CSstudent <= numStudents && CSstudent <= numStudents2; CSstudent++) {
        if (average > average2) {
            cout << "Student " << CSstudent << " spent more time on programming than biology on average." << endl;
        } else if (average2 > average) {
            cout << "Student " << CSstudent << " spent more time on biology than programming on average." << endl;
        } else {
            cout << "Student " << CSstudent << " spent the same amount of time on programming and biology on average." << endl;
        }
    }

    return 0;
}
*/

// Option 1
// Simar Gill

/*
#include <iostream>
using namespace std;
int main() {
    int person = 0;
    int user_input;
    int Coffee = 0;
    int Tea = 0;
    int Coke = 0;
    int OJ = 0;

    cout << "1. Coffee    2. Tea     3. Coke   4. Orange Juice" << endl;

    while (user_input != -1 ) {
        person++;
        cout << "Please input the favorite beverage of person #" << person <<
        ": Choose 1, 2, 3, or 4 from the above menu or -1 to exit the program " << endl;
        cin >> user_input;
        if (user_input == 1) {
            Coffee = Coffee +1;
        }
        if (user_input == 2) {
            Tea = Tea + 1;
        }
        if (user_input == 3) {
            Coke = Coke + 1;
        }
        if (user_input == 4) {
            OJ = OJ + 1;
        }
        if (user_input > 4) {
            cout << "Sorry, this is not an option, please enter 1, 2, 3, or 4, " << endl;
        }
        if (user_input == 0) {
            cout << "Sorry, this is not an option, please enter 1, 2, 3, or 4, " << endl;
        }
        if (user_input < -1) {
            cout << "Sorry, this is not an option please enter 1, 2, 3, or 4, " << endl;
        }

    }

    cout << "Beverage        Number of Votes" << endl;
    cout << "******************************" << endl;
    cout << "Coffee           "   << Coffee  << endl;
    cout << "Tea              "  <<  Tea  << endl;
    cout << "Coke             " <<   Coke  << endl;
    cout << "Orange Juice     "<<    OJ  << endl;

    return 0;
}
*/

/*
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    const double g = 9.8;
    int height;
    int time;

    cout << "Please input the time of fall in seconds: " << endl;
    cin >> time;
    cout << "Please input the height of the bridge in meters: " << endl;
    cin >> height;


    cout << "Time Falling (Seconds) Distance Fallen (meters)" << endl;
    cout << "**********************************************" << endl;

    for (int t = 0; t <= time; ++t) {
        double distance = .5 * g * t * t;



        // Output the time and corresponding distance
        cout << t << "\t\t\t" << fixed << setprecision(1) << distance << endl;

        if (distance > height) {
            cout << "Warning-Bad data: The distance fallen exceeds the height of the bridge" << endl;
            break;
        }
    }


    return 0;
}
*/

#include <iostream>
using namespace std;

int main() {
    int workers;
    int a;
    int year;
    int sickdays;
    int totalsickdays = 0;



    cout << "How many tellers worked at Nation's Bank during each of the last 3 years?" << endl;
    cin >> workers;


    for (a = 1; a <= workers; a++) {
        int b = 0;
        for (year = 1; year <= 3; year++) {
            cout << "How many days was teller " << a << " out sick during year " << year << "?" << endl;
            cin >> sickdays;
            b += sickdays;
        }

        totalsickdays += b;
    }


     cout <<"The " << workers << " tellers were out sick for a total of " << totalsickdays << " days during the last three years" << endl;

    return 0;
}







