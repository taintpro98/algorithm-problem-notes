#include <bits/stdc++.h>
using namespace std;

struct TrieNode
{
  TrieNode *children[26];
  bool is_end_string;
};

class Trie
{
private:
  TrieNode *root;

public:
  Trie()
  {
    root = new TrieNode();
  }

  void insert(string word)
  {
    TrieNode *current = root;
    for (const char &c : word)
    {
      int idx = int(c) - 97;
      if (!current->children[idx])
        current->children[idx] = new TrieNode();
      current = current->children[idx];
    }
    current->is_end_string = true;
  }

  bool search(string word)
  {
    TrieNode *current = root;
    for (const char &c : word)
    {
      int idx = int(c) - 97;
      if (!current->children[idx])
        return false;
      current = current->children[idx];
    }
    return current->is_end_string;
  }

  bool startsWith(string prefix)
  {
    TrieNode *current = root;
    for (const char &c : prefix)
    {
      int idx = int(c) - 97;
      if (!current->children[idx])
        return false;
      current = current->children[idx];
    }
    return true;
  }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

int main()
{
  Trie *obj = new Trie();
  obj->insert(word);
  bool param_2 = obj->search(word);
  bool param_3 = obj->startsWith(prefix);
  return 0;
}