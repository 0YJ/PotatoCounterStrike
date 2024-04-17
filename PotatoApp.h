#ifndef POTATOAPP_H
#define POTATOAPP_H

#include <QWidget>
#include <QLineEdit>
#include <QPushButton>

class PotatoApp : public QWidget {
    Q_OBJECT

public:
    explicit PotatoApp(QWidget *parent = nullptr);

private slots:
    void selectInputFolder();
    void selectOutputFolder();
    void runProcessing();

private:
    QLineEdit *inputEdit;
    QLineEdit *outputEdit;
    QPushButton *processButton;
};

#endif // POTATOAPP_H
