#include "PotatoApp.h"
#include <QVBoxLayout>
#include <QFileDialog>
#include <QLabel>
#include "ImageProcessor.h"

PotatoApp::PotatoApp(QWidget *parent) : QWidget(parent) {
    QVBoxLayout *layout = new QVBoxLayout(this);
    QLabel *inputLabel = new QLabel("Input Folder:");
    inputEdit = new QLineEdit();
    QPushButton *inputButton = new QPushButton("Browse...");
    connect(inputButton, &QPushButton::clicked, this, &PotatoApp::selectInputFolder);

    QLabel *outputLabel = new QLabel("Output Folder:");
    outputEdit = new QLineEdit();
    QPushButton *outputButton = new QPushButton("Browse...");
    connect(outputButton, &QPushButton::clicked, this, &PotatoApp::selectOutputFolder);

    processButton = new QPushButton("Run");
    connect(processButton, &QPushButton::clicked, this, &PotatoApp::runProcessing);

    layout->addWidget(inputLabel);
    layout->addWidget(inputEdit);
    layout->addWidget(inputButton);
    layout->addWidget(outputLabel);
    layout->addWidget(outputEdit);
    layout->addWidget(outputButton);
    layout->addWidget(processButton);
}

void PotatoApp::selectInputFolder() {
    QString dir = QFileDialog::getExistingDirectory(this, "Select Input Folder");
    inputEdit->setText(dir);
}

void PotatoApp::selectOutputFolder() {
    QString dir = QFileDialog::getExistingDirectory(this, "Select Output Folder");
    outputEdit->setText(dir);
}

void PotatoApp::runProcessing() {
    ImageProcessor processor;
    processor.processImages(inputEdit->text().toStdString(), outputEdit->text().toStdString());
}
