#include <bits/stdc++.h>
using namespace std;
int main(){
    set<int> Y;
    for(int i=1; i<=10; i++){
        Y.insert(i);
    }
    for(set<int>::iterator it = Y.begin(); it != Y.end(); it++){
        cout << *it << endl;
    }
    if (Y.find(7) != Y.end()) cout << "Y contains 7" << endl;
    else cout << "Y does not contain 7" << endl;
}