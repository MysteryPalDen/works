#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <cassert>
#include <QPixmap>
#include <QMovie>
#include <QMessageBox>
#include <QTimer>
#include <thread>
#include <chrono>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowFlags(Qt::Widget | Qt::MSWindowsFixedSizeDialogHint);
    this->setFixedSize(QSize(900, 600));
    QPixmap pix(":/data/data/background.png");
    ui->label_3->setPixmap(pix);
    buttonsetter(false);
    ui->textEdit->setReadOnly(true);
    starting();
}

void MainWindow::starting(){
    list.read("../pokemon_game1/data/pokemon_data.txt");
    for (List::Iterator it = list.begin(); it != list.end(); it++){
        ui->comboBox->addItem(QString::fromLatin1((*it).getName().data(), (*it).getName().size()));
        ui->comboBox_2->addItem(QString::fromLatin1((*it).getName().data(), (*it).getName().size()));
    }
    attacklist.read("../pokemon_game1/data/move_data.txt");
}

void MainWindow::check(){
    ui->textBrowser->setText(QString::number(Player.getHp()));
    ui->textBrowser_2->setText(QString::number(Opponent.getHp()));
    if(Player.getHp() <= 0){
        QMessageBox::information(this, "Oh no...", "You lost!");
        ui->textEdit->clear();
        buttonsetter(false);
        return;
    }
    if(Opponent.getHp() <= 0){
        QMessageBox::information(this, "Congratulations!", "You won!");
        ui->textEdit->clear();
        buttonsetter(false);
        return;
    }
}

void MainWindow::buttonsetter(const bool var) const{
    ui->pushButton_4->setEnabled(var);
    ui->pushButton_5->setEnabled(var);
    ui->pushButton_6->setEnabled(var);
    ui->pushButton_7->setEnabled(var);
}

void MainWindow::setPlayers(Pokemon &player, const QComboBox* combobox, QTextBrowser* textbar, QLabel* label, const std::string gifname, QMovie* &gif) const{
    std::string combotext = (combobox->currentText()).toUtf8().constData();
    player = (*list.find(combotext));
    std::string path = ":/data/data/Pokemon_sprites/" + combotext + gifname;
    gif = new QMovie(QString(QString::fromLatin1(path.data(), path.size())));
    label->setMovie(gif);
    gif->start();
    textbar->setText(QString::number(player.getHp()));
}

int MainWindow::damageCalc(std::string attackname, Pokemon &attacking_player, Pokemon &defending_player, QLabel* label, QMovie* &gif, const std::string playertext, const std::string giftext) const{
    if(attacking_player.getHp() <= 0)
        return 0;
    std::string texts = "- " + playertext + " used " + attackname;
    ui->textEdit->append(QString::fromLatin1(texts.data(), texts.size()));
    auto attack = attacklist.find(attackname);
    std::string attackType = (*attack)->getType();
    std::string opponentType = defending_player.getType();
    if((*attack)->getForm()){
        texts = "   - " + playertext + "'s HP was restored";
        ui->textEdit->append(QString::fromLatin1(texts.data(), texts.size()));
        attacking_player.setHp(attacking_player.getHp() + ((UnusualMove*)(*attack))->getHealing());
        return 0;
    }
    if((rand()%100 +1) > (*attack)->getAccuracy()){
        texts = "   - " + playertext + "'s attack missed!";
        ui->textEdit->append(QString::fromLatin1(texts.data(), texts.size()));
        return 0;
    }
    texts = ":/data/data/Animations/"+ attackType + "_attack_" + giftext + ".gif";
    gif = new QMovie(QString(QString::fromLatin1(texts.data(), texts.size())));
    label->setMovie(gif);
    gif->start();
    double multiplyer = 1;
    if(((DamageMove*)(*attack))->getType() == attacking_player.getType())
        multiplyer *= 1.5;
    if((attackType == "Water" && opponentType == "Fire") || (attackType == "Fire" && opponentType == "Grass") ||
       (attackType == "Grass" && opponentType == "Water") || (attackType == "Electric" && opponentType == "Water")){
        ui->textEdit->append("   - It's supereffective!");
        multiplyer *= 2;
    }
    if((attackType == "Fire" && opponentType == "Water") || (attackType == "Grass" && opponentType == "Fire") ||
        (attackType == "Water" && opponentType == "Grass") || (attackType == "Electric" && opponentType == "Grass") ||
        (attackType == "Water" && opponentType == "Water") || (attackType == "Grass" && opponentType == "Grass") ||
        (attackType == "Fire" && opponentType == "Water") || (attackType == "Electric" && opponentType == "Electric")){
        ui->textEdit->append("   - It's not very effective");
        multiplyer *= 0.5;
    }
    if(((DamageMove*)(*attack))->getCategory() == "Physical")
        return ((((DamageMove*)(*attack))->getAttack()*0.44*attacking_player.getAttack()/defending_player.getDefence()+2)*multiplyer);
    else
        return ((((DamageMove*)(*attack))->getAttack()*0.44*attacking_player.getSpecialAttack()/defending_player.getSpecialDefence()+2)*multiplyer);
}

void MainWindow::one_turn(const std::string buttonText){
    buttonsetter(false);
    if(Player.getSpeed() >= Opponent.getSpeed()){
        ui->textEdit->append("--------This Turn--------");
        Opponent.setHp(Opponent.getHp() - damageCalc(buttonText, Player, Opponent, ui->label_4, frontAttackGIF, "Player", "front"));
        Player.setHp(Player.getHp() - damageCalc(enemy_attacks[rand()%4], Opponent, Player, ui->label_5, backAttackGIF, "Opponent", "back"));
    }
    else{
        ui->textEdit->append("--------This Turn--------");
        Player.setHp(Player.getHp() - damageCalc(enemy_attacks[rand()%4], Opponent, Player, ui->label_5, backAttackGIF, "Opponent", "back"));
        Opponent.setHp(Opponent.getHp() - damageCalc(buttonText, Player, Opponent, ui->label_4, frontAttackGIF, "Player", "front"));
    }
    buttonsetter(true);
    check();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_3_clicked()
{
    ui->textEdit->clear();
    setPlayers(Player, ui->comboBox, ui->textBrowser, ui->label, "_back.gif", backGIF);
    ui->pushButton_4->setText(QString::fromLatin1(Player.getMove1().data(), Player.getMove1().size()));
    ui->pushButton_5->setText(QString::fromLatin1(Player.getMove2().data(), Player.getMove2().size()));
    ui->pushButton_6->setText(QString::fromLatin1(Player.getMove3().data(), Player.getMove3().size()));
    ui->pushButton_7->setText(QString::fromLatin1(Player.getMove4().data(), Player.getMove4().size()));
    setPlayers(Opponent, ui->comboBox_2, ui->textBrowser_2, ui->label_2, "_front.gif", frontGIF);
    enemy_attacks[0] = Opponent.getMove1();
    enemy_attacks[1] = Opponent.getMove2();
    enemy_attacks[2] = Opponent.getMove3();
    enemy_attacks[3] = Opponent.getMove4();
    buttonsetter(true);
}

void MainWindow::on_pushButton_4_clicked()
{
    one_turn((ui->pushButton_4->text()).toUtf8().constData());
}
void MainWindow::on_pushButton_5_clicked()
{
    one_turn((ui->pushButton_5->text()).toUtf8().constData());
}

void MainWindow::on_pushButton_6_clicked()
{
    one_turn((ui->pushButton_6->text()).toUtf8().constData());
}

void MainWindow::on_pushButton_7_clicked()
{
    one_turn((ui->pushButton_7->text()).toUtf8().constData());
}
