#include <bits/stdc++.h>
using namespace std;
int main(){
    map<int, int> m;
    for (int i=1; i<=5; i++) m.insert(pair<int, int> (i, 10*i));
    m[6] = 100;
    for(int k=1; k<=6; k++) cout << m[k] << endl;
    map<string, string> m1;
    m1["abc"] = "abcabc";
    m1["xyz"] = "xyzxyz";
    string s = "abc";
    cout << m1[s] << endl;
}