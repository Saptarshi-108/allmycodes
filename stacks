#include<stdio.h>
#include<stdlib.h>

#define MAX 3
int st[MAX],top=-1;
void push(int st[], int val);
void pop(int st[]);
void peek(int st[]);
void display(int st[]);

int main(){

}

void push(int st[], int val){
    if (top==MAX-1){
        printf("\n stack overflow");
    }
    else{
        top++;
        st[top]=val;
    }
}

void pop(int st[],int val){
    if (top==-1){
        printf("\n stack underflow");
    }
    else{
        top--;
    }
}

void peek(int st[]){
    int i;
    if(top==-1){
        printf("\n STACK IS EMPTY");
    }
    else{
        for (i=top;i>=0;i--){
            printf("\n %d",st[i]);
            printf("\n");
        }
    }
}
