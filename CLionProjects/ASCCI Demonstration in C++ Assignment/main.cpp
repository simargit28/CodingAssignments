
#include <iostream>
using namespace std;

int main() {
    cout << "Character        ACII Value" << endl;
    cout << "---------------------------" <<endl;

    for (char n = '0'; n <= '9'; n++) {

       cout << n << "                           " << int(n) << endl;
    }

    for (char A = 'A'; A <= 'Z'; A++) {
        cout << A << "                           " << int(A) << endl;
    }

    for ( char a = 'a'; a <= 'z'; a++) {
        cout << a << "                           " << int(a) << endl;
    }

    return 0;
}

