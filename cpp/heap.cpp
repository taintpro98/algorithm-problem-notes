#include <queue>
#include <iostream>

using namespace std;

class KthLargest
{
private:
  int k;
  priority_queue<int, vector<int>, greater<int>> pq;

public:
  KthLargest(int k, vector<int> &nums)
  {
    this->k = k;
    auto endPointer = nums.begin() + min(k, (int)nums.size());
    pq = priority_queue<int, vector<int>, greater<int>>(nums.begin(), endPointer);
    for (int i = k; i < nums.size(); ++i)
    {
      pq.push(nums[i]);
      pq.pop();
    }
  }

  int add(int val)
  {
    pq.push(val);
    if (pq.size() > k)
    {
      pq.pop();
    }
    return pq.top();
  }
};

int main()
{
  vector<int> nums = {4, 5, 8, 2};
  KthLargest *obj = new KthLargest(3, nums);
  int param_1 = obj->add(3);
  int param_2 = obj->add(5);
  int param_3 = obj->add(10);
  int param_4 = obj->add(9);
  int param_5 = obj->add(4);
  cout << param_1 << " " << param_2 << " " << param_3 << " " << param_4 << " " << param_5 << endl;
  delete obj;
  return 0;
}