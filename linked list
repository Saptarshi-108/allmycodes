#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<malloc.h>

struct node{
    int data;
    struct node *next;
};

struct node *start=NULL;

struct node *create(struct node*);
struct node *display(struct node*);
struct node *insert_beg(struct node*);
struct node *insert_end(struct node*);
struct node *delete_beg(struct node*);
struct node *delete_end(struct node*);
struct node *insert_after(struct node*);
struct node *insert_before(struct node*);
struct node *delete_after(struct node*);
struct node *delete_before(struct node*);
struct node *sort(struct node*);

int main(){

    printf("\n     1. Create a list\n     2. Display the list\n    3. Add a node at the beggining\n    4. Add a node the end\n    5. Add a node before a given node\n    6. Add a node after a given node\n    7. Delete a node at the beggining\n    8. Delete a node at the end\n    9. Delete a node before a given node\n    10. Delete a node after a given node\n11. Delete the entire list.\n12. Sort the list \n");
    int ans;
    printf("Enter the choice =");
    scanf("%d",&ans);
    switch(ans)
    {
        case 1:
        start=create(start);
        printf("Linked list created.");

        case 2:
        start=display(start);
        break;

        case3: 
        start=insert_beg(start);
        break;

        case 4:
        start=insert_end(start);
        break;

        case 5:
        start=insert_before(start);
        break;

        case 6
    }
}   
struct node *create(struct node *start){
    struct node *newnode, *ptr;
    int num;
    printf("\n Enter -1 to data \n");
    printf("Enter the data : ");
    scanf("%d",&num);
    while(num!=-1)
    {
        newnode=(struct node*)malloc(sizeof(struct node));
        newnode->data=num;
        if(start==NULL)
        {
            newnode->next=NULL;
            start=newnode;
        }
        else
        {
            ptr=start;
            while(ptr->next!=NULL)
            {
                ptr=ptr->next;
                ptr->next=newnode;
                newnode->next=NULL;
            }
        }
        printf("\n Enter the data : ");
        scanf("%d",&num);
    }
    return start; 
}

struct node *display(struct node *start){
    struct node *ptr;
    ptr=start;
    while(ptr!=NULL){
        printf(" %d",ptr->data);
        ptr=ptr->next;
    }
    return start;
}

struct node *insert_beg(struct node * start){
    struct node *newnode;  
    int num;
    printf("Enter the data : ");
    scanf("%d",&num);
    newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=num;
    newnode->next=start;
    start=newnode;
    return start;
}

struct node *insert_end(struct node * start){
    struct node *newnode, *ptr;
    int num;
    printf("Enter the data : ");
    scanf("%d",&num);
    newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=num;
    newnode->next=NULL;
    ptr=start;
    while (ptr->next!=NULL){
        ptr=ptr->next;
        ptr->next=newnode;
    }
}
struct node * insert_bef(struct node *start){
    struct node *ptr,*newnode,*preptr;
    int num,pos;
    printf("\n Enter the data :");
    scanf("%d",&num);
    printf("\n Enter the position :");
    scanf("%d",&pos);
    newnode=(struct node *)malloc(sizeof(struct node));
    newnode->data=num;
    ptr=start;
    while (ptr->data!=pos){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=newnode;
    newnode->next=ptr;
    return start;
}
struct node *insert_beg(struct node *start){
    struct node *ptr,*preptr,*
}
