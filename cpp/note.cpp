#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int countOnesInBinary(int n)
{
  int count = 0;

  while (n > 0)
  {
    if (n & 1)
    {
      count++;
    }
    n >>= 1;
  }
  return count;
}

int main()
{
  return 0;
}
