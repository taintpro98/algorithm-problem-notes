// A simple C++ program for traversal of a linked list 
#include <bits/stdc++.h> 
using namespace std; 
  
class Node { 
public: 
    int data; 
    Node* next; 
}; 
  
// This function prints contents of linked list 
// starting from the given node 
void print_list(Node* n) 
{ 
    while (n != NULL) { 
        cout << n->data << " "; 
        n = n->next; 
    } 
} 

void insert_after(Node* prev_node, int new_data)   
{ 
    
    // 1. Check if the given prev_node is NULL  
    if (prev_node == NULL)   
    {   
        cout << "the given previous node cannot be NULL";   
        return;   
    }  
    
    // 2. Allocate new node 
    Node* new_node = new Node();  
    
    // 3. Put in the data  
    new_node->data = new_data;   
    
    // 4. Make next of new node as  
    // next of prev_node  
    new_node->next = prev_node->next;   
    
    // 5. move the next of prev_node 
    // as new_node  
    prev_node->next = new_node;   
}  

/* Given a reference (pointer to pointer) to the head  
of a list and an int, appends a new node at the end */
void append(Node** head_ref, int new_data)  
{  
    /* 1. allocate node */
    Node* new_node = new Node(); 
  
    Node *last = *head_ref; /* used in step 5*/
  
    /* 2. put in the data */
    new_node->data = new_data;  
  
    /* 3. This new node is going to be  
    the last node, so make next of  
    it as NULL*/
    new_node->next = NULL;  
  
    /* 4. If the Linked List is empty, 
    then make the new node as head */
    if (*head_ref == NULL)  
    {  
        *head_ref = new_node;  
        return;  
    }  
  
    /* 5. Else traverse till the last node */
    while (last->next != NULL)  
        last = last->next;  
  
    /* 6. Change the next of last node */
    last->next = new_node;  
    return;  
}  

/* Given a reference (pointer to pointer)  
to the head of a list and an int,  
inserts a new node on the front of the list. */
void push(Node** head_ref, int new_data)  
{  
    /* 1. allocate node */
    Node* new_node = new Node();  
  
    /* 2. put in the data */
    new_node->data = new_data;  
  
    /* 3. Make next of new node as head */
    new_node->next = (*head_ref);  
  
    /* 4. move the head to point to the new node */
    (*head_ref) = new_node;  
}  
  
// Driver code 
int main() 
{ 
    Node* head = NULL; 
    Node* second = NULL; 
    Node* third = NULL; 
  
    // allocate 3 nodes in the heap 
    head = new Node(); 
    second = new Node(); 
    third = new Node(); 
  
    head->data = 1; // assign data in first node 
    head->next = second; // Link first node with second 
  
    second->data = 2; // assign data to second node 
    second->next = third; 
  
    third->data = 3; // assign data to third node 
    third->next = NULL; 

    push(&head, 4);
    append(&head, 4);
    print_list(head);

    return 0; 
} 