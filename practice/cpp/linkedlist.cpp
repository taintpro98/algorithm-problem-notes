#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode
{
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Helper functions to create and print linked list (for testing)
ListNode *createLinkedList(vector<int> &values)
{
  ListNode *head = nullptr;
  ListNode *tail = nullptr;
  for (int val : values)
  {
    ListNode *newNode = new ListNode(val);
    if (!head)
    {
      head = newNode;
      tail = newNode;
    }
    else
    {
      tail->next = newNode;
      tail = newNode;
    }
  }
  return head;
}

void printLinkedList(ListNode *head)
{
  while (head)
  {
    cout << head->val << " ";
    head = head->next;
  }
  cout << endl;
}

ListNode *reverseLinkedList(ListNode *head)
{
  ListNode *ptr = head;
  ListNode *prev = NULL;
  while (ptr)
  {
    ListNode *tmp = ptr->next;
    ptr->next = prev;
    prev = ptr;
    ptr = tmp;
  }
  return prev;
}

class Solution
{
public:
  int pairSum(ListNode *head)
  {
    ListNode *slow = head;
    ListNode *fast = head;
    while (fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode *reversed = reverseLinkedList(slow);
    ListNode *h = head;
    ListNode *k = reversed;
    int ans = 0;
    while (k)
    {
      ans = max(ans, k->val + h->val);
      k = k->next;
      h = h->next;
    }
    return ans;
  }
};

int main()
{
  // input
  freopen("practice/in.txt", "r", stdin);
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  // cout.tie(0);

  // solution
  Solution solution;

  // run
  int T = 3;
  while (T--)
  {
    int n;
    cin >> n;
    vector<int> v;
    while (n--)
    {
      int tmp;
      cin >> tmp;
      v.push_back(tmp);
    }
    ListNode *head = createLinkedList(v);

    int res = solution.pairSum(head);
    cout << res << endl;
  }
  return 0;
}