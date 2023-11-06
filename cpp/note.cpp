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

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<std::pair<int, int>> pairs = {{3, 7}, {1, 5}, {4, 2}, {2, 6}};

    sort(pairs.begin(), pairs.end());

    for (const auto& pair : pairs) {
        std::cout << "(" << pair.first << ", " << pair.second << ") ";
    }
    return 0;
}

