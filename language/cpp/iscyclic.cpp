#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

bool isCyclic(int V, vector<int> adj[])
{
  vector<bool> visited(V, false);
  vector<bool> on_stack(V, false);
  stack<int> st;

  for (int w = 0; w < V; w++)
  {
    if (visited[w])
      continue;
    st.push(w);

    while (!st.empty())
    {
      int s = st.top();

      if (!visited[s])
      {
        visited[s] = true;
        on_stack[s] = true;
      }
      else
      {
        on_stack[s] = false;
        st.pop();
      }

      for (const auto &v : adj[s])
      {
        if (!visited[v])
        {
          st.push(v);
        }
        else if (on_stack[v])
        {
          return true;
        }
      }
    }
  }
  return false;
}

int main()
{
  return 0;
}