#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include "pokemonlist.h"
#include "attacklist.h"

#include <QMainWindow>
#include <QComboBox>
#include <QTextBrowser>
#include <QLabel>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_7_clicked();

private:
    void starting();
    void check();
    int damageCalc(const std::string attackname, Pokemon &attackingPlayer, Pokemon &defendingPlayer, QLabel* label, QMovie* &gif, const std::string playerText, const std::string gifText) const;
    void buttonsetter(const bool var) const;
    void setPlayers(Pokemon &player, const QComboBox* combobox, QTextBrowser* textbar, QLabel* label, const std::string gifname, QMovie* &gif) const;
    void one_turn(const std::string buttonText);
    Ui::MainWindow *ui;
    List list;
    AttackList attacklist;
    std::string enemy_attacks[4];
    QMovie *backGIF;
    QMovie *frontGIF;
    QMovie *backAttackGIF;
    QMovie *frontAttackGIF;
    Pokemon Player;
    Pokemon Opponent;
    int m;
};

#endif // MAINWINDOW_H
