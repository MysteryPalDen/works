#ifndef ATTACK_H
#define ATTACK_H
#include <iostream>

class Move
{
public:
    Move();
    ~Move(){}
    Move(std::string name, std::string type, int accuracy);
    Move(const Move &other);
    std::string getName() const;
    std::string getType() const;
    int getAccuracy() const;
    void setAccuracy(int accuracy);
    void setName(std::string name);
    void setType(std::string type);
    virtual bool getForm() const = 0;
private:
    std::string name;
    std::string type;
    int accuracy;
};

class DamageMove : public Move
{
public:
    DamageMove();
    ~DamageMove(){}
    DamageMove(std::string name, std::string type, int accuracy, std::string category, int attack);
    DamageMove(const DamageMove &other);
    std::string getCategory() const;
    int getAttack() const;
    void setCategory(std::string type);
    void setAttack(int attack);
    bool getForm() const override{return false;}
private:
    std::string category;
    int attack;
};

class UnusualMove : public Move
{
public:
    UnusualMove();
    ~UnusualMove(){}
    UnusualMove(std::string name, std::string type, int accuracy, int healing);
    UnusualMove(const UnusualMove &other);
    void setHealing(int healing);
    int getHealing() const;
    bool getForm() const override{return true;}
private:
    int healing;
};

#endif // ATTACK_H

