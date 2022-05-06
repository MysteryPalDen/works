#ifndef POKEMONLIST_H
#define POKEMONLIST_H
#include "pokemon.h"

class List
{
    class Node;
public:
    class Iterator;
    List();
    ~List();
    List(const List&);
    void push_back(const Pokemon&);
    Pokemon pop_back();
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
        Pokemon& operator*();
    private:
        Node *curNode;
    };
private:
    class Node
    {
        friend class List;
        friend class Iterator;
    private:
        Pokemon value;
        Node *next, *prev;
    };
    Node *first, *last;
    size_t length;
};

#endif // POKEMONLIST_H
