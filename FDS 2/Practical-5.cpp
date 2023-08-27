#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *left, *right;
    bool leftThread;
    bool rightThread;
};

Node *newNode(int data)
{
    Node *node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    node->leftThread = node->rightThread = false;
    return node;
}

Node *leftmost(Node *node)
{
    if (node == NULL)
        return NULL;
    while (node->left != NULL)
        node = node->left;
    return node;
}

void inorder(Node *root)
{
    if (root == NULL)
        return;

    Node *cur = leftmost(root);
    cout << "-999 --> ";
    while (cur != NULL)
    {
        cout << cur->data << " "
             << "next thread --> ";

        if (cur->rightThread)
            cur = cur->right;
        else
            cur = leftmost(cur->right);
    }
    if (cur == NULL)
    {
        cout << "-999";
    }
}

void populateInorderSuccessor(Node *root, Node **last)
{
    if (root == NULL)
        return;

    populateInorderSuccessor(root->right, last);
    if (*last != NULL)
    {
        root->right = *last;
        root->rightThread = true;
    }
    *last = root;
    populateInorderSuccessor(root->left, last);
}

void convertToThreaded(Node *root)
{
    Node *last = NULL;
    populateInorderSuccessor(root, &last);
}

int main()
{
    Node *head = newNode(-999);
    Node *root = newNode(6);
    root->left = newNode(3);
    root->right = newNode(8);
    root->left->left = newNode(1);
    root->left->right = newNode(5);
    root->right->left = newNode(7);
    root->right->right = newNode(11);

    convertToThreaded(root);

    cout << "Predecessor and succsesor of Inorder traversal of double threaded binary tree: \n";
    inorder(root);

    return 0;
}