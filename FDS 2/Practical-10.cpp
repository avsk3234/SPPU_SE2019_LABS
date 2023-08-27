#include <iostream>
using namespace std;
// Function to heapify a subtree rooted at index i in
void heapify(int arr[], int n, int i)
{
    int largest = i;       // Initialize largest as root
    int left = 2 * i + 1;  // Left child
    int right = 2 * i + 2; // Right child
    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;
    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;
    // If largest is not root
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}
// Function to build a max heap
void buildHeap(int arr[], int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}
// Function to find the maximum and minimum marks
void findMinMaxMarks(int arr[], int n)
{
    // Build max heap
    buildHeap(arr, n);
    // Find the maximum marks
    int maxMarks = arr[0];
    // Convert the max heap into a min heap
    for (int i = n - 1; i > 0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
    // Find the minimum marks
    int minMarks = arr[0];
    // Print the maximum and minimum marks
    cout << "Maximum Marks: " << maxMarks << endl;
    cout << "Minimum Marks: " << minMarks << endl;
}
int main()
{
    // Read the marks obtained by students
    int num;
    cout << "Enter no. of students : ";
    cin >> num;
    int marks[10];
    for (int i = 0; i < num; i++)
    {
        cout << "marks : ";
        cin >> marks[i];
    }
    // Find the maximum and minimum marks
    findMinMaxMarks(marks, num);
    return 0;
}