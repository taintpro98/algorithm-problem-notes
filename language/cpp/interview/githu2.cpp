// https://ntucoder.net/Submission/Submit/?problemid=2231
#include <iostream>
using namespace std;

long long cal(long long m)
{
  long long sum = 0;
  while (m)
  {
    m /= 5;
    sum += m;
  }
  return sum;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++)
  {
    long long n, mid, m;
    cin >> n;
    long long l = 4 * n, r = 5 * n;
    while (l <= r)
    {
      mid = (l + r) / 2;
      long long ans = cal(mid);
      if (ans < n)
      {
        l = mid + 1;
      }
      else
      {
        m = mid;
        r = mid - 1;
      }
    }
    cout << m << endl;
  }
}