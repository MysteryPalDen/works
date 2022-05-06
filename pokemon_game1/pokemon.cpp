#include "pokemon.h"

Pokemon::Pokemon(std::string name, std::string type, std::string move1, std::string move2, std::string move3, std::string move4, int attack, int defence, int specialAttack, int specialDefence, int speed, int hp): name(name), type(type), move1(move1), move2(move2), move3(move3), move4(move4), attack(attack), defence(defence), specialAttack(specialAttack), specialDefence(specialDefence), speed(speed), hp(hp){}

Pokemon::Pokemon(){
    name = "_";
    type = "_";
    attack = 0;
    defence = 0;
    specialAttack = 0;
    specialDefence = 0;
    speed = 0;
    hp = 0;
}

Pokemon::Pokemon(const Pokemon &other){
    name = other.name;
    type = other.type;
    attack = other.attack;
    defence = other.defence;
    specialAttack = other.specialAttack;
    specialDefence = other.specialDefence;
    speed = other.speed;
    hp = other.hp;
}

std::string Pokemon::getName() const{
    return name;
}

std::string Pokemon::getType() const{
    return type;
}

std::string Pokemon::getMove1() const{
    return move1;
}

std::string Pokemon::getMove2() const{
    return move2;
}

std::string Pokemon::getMove3() const{
    return move3;
}

std::string Pokemon::getMove4() const{
    return move4;
}

int Pokemon::getAttack() const{
    return attack;
}

int Pokemon::getDefence() const{
    return defence;
}

int Pokemon::getSpecialAttack() const{
    return specialAttack;
}

int Pokemon::getSpecialDefence() const{
    return specialDefence;
}

int Pokemon::getSpeed() const{
    return speed;
}

int Pokemon::getHp() const{
    return hp;
}

void Pokemon::setName(std::string name){
    Pokemon::name = name;
}

void Pokemon::setType(std::string type){
    Pokemon::type = type;
}

void Pokemon::setMove1(std::string move1){
    Pokemon::move1 = move1;
}

void Pokemon::setMove2(std::string move2){
    Pokemon::move2 = move2;
}

void Pokemon::setMove3(std::string move3){
    Pokemon::move3 = move3;
}

void Pokemon::setMove4(std::string move4){
    Pokemon::move4 = move4;
}

void Pokemon::setAttack(int attack){
    Pokemon::attack = attack;
}

void Pokemon::setDefence(int defence){
    Pokemon::defence = defence;
}

void Pokemon::setSpecialAttack(int specialAttack){
    Pokemon::specialAttack = specialAttack;
}

void Pokemon::setSpecialDefence(int specialDefence){
    Pokemon::specialDefence = specialDefence;
}

void Pokemon::setSpeed(int speed){
    Pokemon::speed = speed;
}

void Pokemon::setHp(int hp){
    Pokemon::hp = hp;
}
