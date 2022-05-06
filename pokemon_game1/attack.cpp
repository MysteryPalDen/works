#include "attack.h"

Move::Move(std::string name, std::string type, int accuracy): name(name), type(type), accuracy(accuracy){}

Move::Move(){
    name = "_";
    type = "_";
    accuracy = 0;
}

Move::Move(const Move &other){
    name = other.name;
    type = other.type;
    accuracy = other.accuracy;
}

std::string Move::getName() const{
    return name;
}

std::string Move::getType() const{
    return type;
}

int Move::getAccuracy() const{
    return accuracy;
}

void Move::setName(std::string name){
    Move::name = name;
}

void Move::setType(std::string type){
    Move::type = type;
}

void Move::setAccuracy(int accuracy){
    Move::accuracy = accuracy;
}


DamageMove::DamageMove(): category("_"), attack(0){}

DamageMove::DamageMove(std::string name, std::string type, int accuracy, std::string category, int attack): Move(name, type, accuracy), category(category), attack(attack){}

DamageMove::DamageMove(const DamageMove &other): Move(other){
    category = other.category;
    attack = other.attack;
}

std::string DamageMove::getCategory() const{
    return category;
}

void DamageMove::setCategory(std::string category){
    DamageMove::category = category;
}

void DamageMove::setAttack(int attack){
    DamageMove::attack = attack;
}

int DamageMove::getAttack() const{
    return attack;
}



UnusualMove::UnusualMove(): healing(0){}

UnusualMove::UnusualMove(std::string name, std::string type, int accuracy, int healing): Move(name, type, accuracy), healing(healing){}

UnusualMove::UnusualMove(const UnusualMove &other): Move(other){
    healing = other.healing;
}

void UnusualMove::setHealing(int healing){
    UnusualMove::healing = healing;
}

int UnusualMove::getHealing() const{
    return healing;
}
