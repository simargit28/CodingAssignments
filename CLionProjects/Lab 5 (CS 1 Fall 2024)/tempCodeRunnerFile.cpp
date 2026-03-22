#include <iostream>

using namespace std;

int main() {
    int numLines;

    cout << "Enter the number of lines: ";
    cin >> numLines;

    for (int a = 0; a < numLines; a++) {
        for (int b = 0; b <= a; b++) {
            cout << "* ";
        }
        cout << endl;
    }

    return 0;
}
