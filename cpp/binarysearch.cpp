#include <bits/stdc++.h>
using namespace std;

// numbers is a sorted array
int binarySearch(vector<int> &numbers, int target)
{
	int l = 0, r = numbers.size() - 1;

	while (l <= r)
	{
		int pivot = (l + r) / 2;
		if (numbers[pivot] == target)
			return pivot;
		if (target < numbers[pivot])
		{
			r = pivot - 1;
		}
		else
		{
			l = pivot + 1;
		}
	}
	return -1;
}

int main()
{
	vector<int> arr = {1, 2, 3, 5, 7, 9};
	int res = binarySearch(arr, 1);
	cout << res << endl;
	return 0;
}