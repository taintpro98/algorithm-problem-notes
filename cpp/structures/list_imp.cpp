#include <bits/stdc++.h>
using namespace std;
int main(){
    list<int> L;
    for (int i=1; i<=5; i++){
        L.push_back(i);
    }
    list<int>::iterator it;
    it = find(L.begin(), L.end(), 3);
    L.insert(it, 10);
    for(it = L.begin(); it != L.end(); it++){
        cout << *it << endl;
    }
}