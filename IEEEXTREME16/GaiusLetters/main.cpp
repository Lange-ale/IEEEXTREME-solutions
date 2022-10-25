#include "bits/stdc++.h"
using namespace std;    

string codifica(const string& s, int avanti_di) {
    string risultato;
    for (char i: s) {
        if (i + avanti_di > 'z' && i <= 'z' || i + avanti_di > 'Z' && i <= 'Z')
            risultato += i + avanti_di - 26;
        else if (i >= 'a' && i + avanti_di <= 'z' || i >= 'A' && i + avanti_di <= 'Z')
            risultato += i + avanti_di;
        else
            risultato += i;
    }
    return risultato;
}

int main()
{
    string messaggio;
    getline(cin, messaggio);
    cout << codifica(messaggio, 14);;
    return 0;
}
