#ifndef ATTACKLIST_H
#define ATTACKLIST_H
#include "attack.h"

class AttackList
{
    class Node;
public:
    class Iterator;
    AttackList();
    ~AttackList();
    AttackList(const AttackList&);
    void push_back(Move &object);
    void pop_back();
    void clear();
    size_t size() const { return length; }
    Iterator find(std::string name) const;
    void read(const std::string&);
    void write(const std::string&) const;
    Iterator begin() const { return Iterator(first); }
    Iterator end() const { return Iterator(nullptr); }
    class Iterator
    {
    public:
        Iterator(Node *node) { curNode = node; }
        Iterator& operator=(const Iterator &it);
        Iterator operator++(int);
        Iterator operator--(int);
        bool operator!=(const Iterator& iterator);
        bool operator==(const Iterator& iterator);
        Move*& operator*();
    private:
        Node *curNode;
    };
private:
    class Node
    {
        friend class AttackList;
        friend class Iterator;
    private:
        Move *value;
        Node *next, *prev;
    };
    void sort();
    Node *first, *last;
    size_t length;
};

#endif // ATTACKLIST_H
