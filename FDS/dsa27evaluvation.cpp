#include<iostream>
#include<cctype>
#include<stack>
using namespace std;

int eval(int op1, int op2, char operate) {
   switch (operate) {
      case '*': return op2 * op1;
      case '/': return op2 / op1;
      case '+': return op2 + op1;
      case '-': return op2 - op1;
      default : return 0;
   }
}
int getWeight(char ch) {
   switch (ch) {
      case '/':
      case '*': return 2;
      case '+':
      case '-': return 1;
      default : return 0;
   }
}

int evalPostfix(char postfix[], int size) {
   stack<int> s;
   int i = 0;
   char ch;
   int val;
   while (i < size) {
      ch = postfix[i];
      if (isdigit(ch)) {
         s.push(ch-'0');
      }
      else {
         
         int op1 = s.top();
         s.pop();
         int op2 = s.top();
         s.pop();
         val = eval(op1, op2, ch);
         s.push(val);
      }
      i++;
   }
   return val;
}

int main() {
   char postfix[] = {'a','b','c','+','*','d','/'};
   int i=0;
   while(postfix[i]!='\0')
   {
   	if(getWeight(postfix[i])==0)
   	{
   		cout<<" Enter value for "<<postfix[i]<<" = ";
   		cin>>postfix[i];
	   }
	   i++;
   }
   int size = sizeof(postfix);
   int val = evalPostfix(postfix, size);
   cout<<"\nExpression evaluates to "<<val;
   cout<<endl;
   return 0;
}