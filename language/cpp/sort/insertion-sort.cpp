#include <bits/stdc++.h>
using namespace std;

void insertionSort(vector<int> &arr)
{
  int n = arr.size();
  for (int i = 1; i < n; i++)
  {
    int t = i - 1;
    int tmp = arr[i];
    while (t >= 0 && tmp < arr[t])
    {
      arr[t + 1] = arr[t];
      t--;
    }
    arr[t + 1] = tmp;
  }
}

int main()
{
  vector<int> test = {3, 5, 1, 7, 8, 2, 10, 4};
  insertionSort(test);
  for(auto c: test){
    cout << c << " ";
  }
  return 0;
}