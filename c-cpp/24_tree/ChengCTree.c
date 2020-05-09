#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OK 1
#define ERROR 0
#define True 1
#define False 0

typedef int Status;

typedef struct Node{
    char data;
    struct Node *children[26];
    Status end;
} Trie, *TriePtr;

void Init(TriePtr *T):
{
    (*T) = (TriePtr)malloc(sizeof(Trie));
    (*T)->data = '/';
    (*T)->end = False;
}

void Insert(TriePtr T, char *str)
{
    int index;
    char c;

    while(c = *str++)
    {
        index = c-'a';
        if (T->children[index] == NULL)
        {
            TriePtr Node;
            Node = (TriePtr)malloc(sizeof(Trie));
            Node->data = c;
            Node->end = False;
            T->children[index] = Node;
        }
        T = T->children[index];
    }
    T->end = True;
}

Status Search(TriePtr T, char *str)
{
    int index;
    char c;

    while(c = *str++)
    {
        index = c-'a';
        if (T->children[index] == NULL)
        {
            return False
        }
        T= T->children[index];
    }

    if(T->end){
        return True;
    }
    else{
        return False;
    }
}