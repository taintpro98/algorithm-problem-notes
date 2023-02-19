#include <bits/stdc++.h>
using namespace std;

vector<int> filterIncreasedArray(vector<int> nums)
{
  vector<int> res;
  int n = nums.size();
  for (int i = 0; i < n - 1; i++)
  {
    if (nums[i] < nums[i + 1])
    {
      res.push_back(nums[i]);
    }
  }
  res.push_back(nums[n - 1]);
  return res;
}

int main()
{
  vector<int> a = {1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9};
  vector<int> b = filterIncreasedArray(a);
  for (auto t : b)
  {
    cout << t << endl;
  }
  return 0;
}