#include "attacklist.h"
#include <iostream>
#include <cmath>
#include <assert.h>
#include <fstream>

void AttackList::write(const std::string& path) const
{
    std::ofstream outputFile(path + ".txt");
    for (AttackList::Iterator it = this->begin(); it != this->end(); it++)
    {
        if((*it)->getForm())
        {
            outputFile << "UNUSUAL_MOVE" << std::endl << (*it)->getName() << std::endl << (*it)->getType() << std::endl << (*it)->getAccuracy() << std::endl << ((UnusualMove*)(*it))->getHealing() << std::endl ;
        }
        else
            outputFile << "DAMAGE_MOVE" << std::endl << (*it)->getName() << std::endl << (*it)->getType() << std::endl << ((DamageMove*)(*it))->getCategory() << std::endl << (*it)->getAccuracy() << std::endl << ((DamageMove*)(*it))->getAttack() << std::endl;
    }
    outputFile.close();
}

void AttackList::read(const std::string& path)
{
    this->clear();
    std::ifstream inputFile(path);
    std::string name[3], s;
    int number[2];
    int i = 0;
    while (getline(inputFile, s))
    {
        if(s == "DAMAGE_MOVE"){
            i = 0;
            while(i<=5){
                if (i < 3)
                {
                    getline(inputFile, s);
                    name[i] = s;
                }
                else if (i < 5)
                {
                    getline(inputFile, s);
                    number[i-3] = stoi(s);
                }
                else
                {
                    DamageMove d(name[0], name[1], number[0], name[2], number[1]);
                    this->push_back(d);
                }
                i++;
            }
        }
        else if(s == "UNUSUAL_MOVE"){
            i = 0;
            while(i<=4){
                if (i < 2)
                {
                    getline(inputFile, s);
                    name[i] = s;
                }
                else if (i < 4)
                {
                    getline(inputFile, s);
                    number[i-2] = stoi(s);
                }
                else
                {
                    UnusualMove d(name[0], name[1], number[0], number[1]);
                    this->push_back(d);
                }
                i++;
            }
        }
    }
    inputFile.close();
}

AttackList::Iterator AttackList::find(std::string name) const
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
        if ((*it)->getName() == name)
        {
            ans = it;
            return ans;
        }
    }
    return ans;
}
/*
void AttackList::sort()
{
    for ( Node *i=first; i!=last; i=i->next)
    {
        for (Node *j=i->next; j!=nullptr; j=j->next)
        {
            if ((i->value)->energy()>(j->value)->energy())
            {
                std::swap(i->value, j->value);
            }
        }
    }
}
*/
AttackList::Iterator& AttackList::Iterator::operator=(const Iterator &it)
{
    curNode = it.curNode;
    return *this;
}

AttackList::Iterator AttackList::Iterator::operator++(int)
{
    Iterator temp = *this;
    if (curNode)
        curNode = curNode->next;
    return temp;
}

AttackList::Iterator AttackList::Iterator::operator--(int)
{
    Iterator temp = *this;
    if (curNode)
        curNode = curNode->prev;
    return temp;
}

bool AttackList::Iterator::operator!=(const Iterator& iterator)
{
    return curNode != iterator.curNode;
}

bool AttackList::Iterator::operator==(const Iterator& iterator)
{
    return curNode == iterator.curNode;
}

Move*& AttackList::Iterator::operator*()
{
    return curNode->value;
}

void AttackList::clear()
{
    while (this->length)
    {
       this->pop_back();
    }
}

void AttackList::push_back(Move &element)
{
    Node *newNode=new Node;
    if(element.getForm()){
       UnusualMove *d = new UnusualMove(*(dynamic_cast<UnusualMove*>(&element)));
       newNode->value=d;
    }
    else{
       DamageMove *d = new DamageMove(*(dynamic_cast<DamageMove*>(&element)));
       newNode->value=d;
    }
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

void AttackList::pop_back()
{
    if (!first) return;
    if (first == last)
    {
        delete(last->value);
        delete(last);
        first = last = nullptr;
    }
    else
    {
        Node *temp = last;
        last = last->prev;
        last->next = nullptr;
        delete(temp->value);
        delete(temp);
    }
    length--;
}

AttackList::AttackList()
{
    first = last = nullptr;
    length=0;
}

AttackList::~AttackList()
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

AttackList::AttackList(const AttackList& m)
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
