#ifndef POKEMON_H
#define POKEMON_H
#include <iostream>

class Pokemon
{
public:
    Pokemon();
    ~Pokemon(){}
    Pokemon(std::string name, std::string type, std::string move1, std::string move2, std::string move3, std::string move4, int attack, int defence, int specialAttack, int specialDefence, int speed, int hp);
    Pokemon(const Pokemon &other);
    std::string getName() const;
    std::string getType() const;
    std::string getMove1() const;
    std::string getMove2() const;
    std::string getMove3() const;
    std::string getMove4() const;
    int getAttack() const;
    int getDefence() const;
    int getSpecialAttack() const;
    int getSpecialDefence() const;
    int getSpeed() const;
    int getHp() const;
    void setName(std::string name);
    void setType(std::string type);
    void setMove1(std::string type);
    void setMove2(std::string type);
    void setMove3(std::string type);
    void setMove4(std::string type);
    void setAttack(int attack);
    void setDefence(int defence);
    void setSpecialAttack(int specialAttack);
    void setSpecialDefence(int specialDefence);
    void setSpeed(int speed);
    void setHp(int hp);
private:
    std::string name;
    std::string type;
    std::string move1;
    std::string move2;
    std::string move3;
    std::string move4;
    int attack;
    int defence;
    int specialAttack;
    int specialDefence;
    int speed;
    int hp;
};

#endif // POKEMON_H
