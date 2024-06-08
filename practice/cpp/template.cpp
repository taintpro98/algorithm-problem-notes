#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
  string decodeString(string s)
  {
    stack<char> st;

    for (auto c : s)
    {
      if (c != ']')
      {
        st.push(c);
      }
      else
      {
        string tmp;
        string tmpres;
        while (!st.empty() && isalpha(st.top()))
        {
          char ch = st.top();
          st.pop();
          tmp = ch + tmp;
        }
        if (!st.empty() && st.top() == '[')
          st.pop();

        string numchar;
        while (!st.empty() && isdigit(st.top()))
        {
          char ch = st.top();
          st.pop();
          numchar = ch + numchar;
        }
        int num = stoi(numchar);

        for (int i = 0; i < num; i++)
        {
          tmpres += tmp;
        }

        for (auto t : tmpres)
        {
          st.push(t);
        }
      }
    }
    string result;
    while (!st.empty())
    {
      char top = st.top();
      st.pop();
      result = top + result;
    }
    return result;
  }
};

int main()
{
  // input
  freopen("practice/in.txt", "r", stdin);
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string s;

  // solution
  Solution solution;

  // run
  int T = 3;
  while (T--)
  {
    cin >> s;
    string res = solution.decodeString(s);
    cout << res << endl;
  }
  return 0;
}