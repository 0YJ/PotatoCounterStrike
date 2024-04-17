#include <QApplication>
#include "PotatoApp.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    PotatoApp window;
    window.show();
    return app.exec();
}
