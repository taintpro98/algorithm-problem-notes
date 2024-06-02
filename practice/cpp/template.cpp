#include <bits/stdc++.h>

using namespace std;
namespace fs = filesystem;

class Solution
{
public:
  string removeStars(string s)
  {
    stack<char> st;
    for (char c : s)
    {
      if (c != '*')
      {
        st.push(c);
      }
      else
      {
        if (!st.empty())
          st.pop();
      }
    }
    string result = "";
    while (!st.empty())
    {
      result += st.top();
      st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
  }
};

int main()
{
  // input
  freopen("handon/in.txt", "r", stdin);
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string s;

  // solution
  Solution solution;

  // run
  int T = 2;
  while (T--)
  {
    cin >> s;
    string res = solution.removeStars(s);
    cout << res << endl;
  }
  return 0;
}