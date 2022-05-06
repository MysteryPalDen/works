#include "pokemonlist.h"
#include <iostream>
#include <cmath>
#include <assert.h>
#include <fstream>

void List::write(const std::string& path) const
{
    std::ofstream outputFile(path);

    for (List::Iterator it = this->begin(); it != this->end(); it++)
    {
        outputFile << (*it).getName() << std::endl << (*it).getType() << std::endl
                   << (*it).getMove1() << std::endl << (*it).getMove2() << std::endl
                   << (*it).getMove3() << std::endl << (*it).getMove4() << std::endl
                   << (*it).getAttack() << std::endl << (*it).getDefence() << std::endl
                   << (*it).getSpecialAttack() << std::endl << (*it).getSpecialDefence()
                   << std::endl << (*it).getSpeed() << std::endl << (*it).getHp() << std::endl;
    }
    outputFile.close();
}

void List::read(const std::string& path)
{
    this->clear();
    std::ifstream inputFile(path);
    std::string s, name[6];
    int a[6];
    int i = 0;
    while (getline(inputFile, s))
    {
        if (i < 6)
        {
            name[i] = s;
        }
        else if (i<12)
        {
            a[i-6]=stoi(s);
        }
        else
        {
            Pokemon d(name[0], name[1], name[2], name[3], name[4], name[5], a[0], a[1], a[2], a[3], a[4], a[5]);
            this->push_back(d);
            i=0;
            name[0]=s;
        }
        i++;
    }
    Pokemon d(name[0], name[1], name[2], name[3], name[4], name[5], a[0], a[1], a[2], a[3], a[4], a[5]);
    this->push_back(d);
    inputFile.close();
}

List::Iterator List::find(std::string name) const
{
    assert (length!=0);
    auto it=this->begin(), ans=it;
    if (length==1)
    {
        return it;
    }
    it++;
    for(;it!=this->end(); it++)
    {
        if ((*it).getName() == name)
        {
            ans = it;
            return ans;
        }
    }
    return ans;
}

List::Iterator& List::Iterator::operator=(const Iterator &it)
{
    curNode = it.curNode;
    return *this;
}

List::Iterator List::Iterator::operator++(int)
{
    Iterator temp = *this;
    if (curNode)
        curNode = curNode->next;
    return temp;
}

List::Iterator List::Iterator::operator--(int)
{
    Iterator temp = *this;
    if (curNode)
        curNode = curNode->prev;
    return temp;
}

bool List::Iterator::operator!=(const Iterator& iterator)
{
    return curNode != iterator.curNode;
}

bool List::Iterator::operator==(const Iterator& iterator)
{
    return curNode == iterator.curNode;
}

Pokemon& List::Iterator::operator*()
{
    return curNode->value;
}

void List::clear()
{
    while (this->length)
    {
       this->pop_back();
    }
}

void List::push_back(const Pokemon& d)
{
    Node *newNode=new Node;
    newNode->value=d;
    newNode->next=newNode->prev=nullptr;
    if (!first)
    {
        first = last = newNode;
    }
    else
    {
        last->next = newNode;
        newNode->prev = last;
        last = last->next;
    }
    length++;
    //this->sort();
}

Pokemon List::pop_back()
{
    Pokemon temp;
    if (!first) return temp;

    temp=last->value;

    if (first == last)
    {

        delete(last);
        first = last = nullptr;
    }
    else
    {
        Node *temp = last;
        last = last->prev;
        last->next = nullptr;
        delete(temp);
    }
    length--;
    return temp;
}

List::List()
{
    first = last = nullptr;
    length=0;
}

List::~List()
{
    Node *cur, *temp;
    cur=temp=first;
    while (cur)
    {
        cur=cur->next;
        delete (temp);
        temp=cur;
    }
}

List::List(const List& m)
{
   first = last = nullptr;
   length = 0;
   for (Node *it = m.first; it; it = it->next)
   {
       Node* newNode = new Node;
       newNode->value = it->value;
       newNode->next = newNode->prev = nullptr;
       if (!first)
       {
           first = last = newNode;
       }
       else
       {
           last->next = newNode;
           newNode->prev = last;
           last = last->next;
       }
       length++;
   }
}
