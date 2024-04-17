#ifndef IMAGEPROCESSOR_H
#define IMAGEPROCESSOR_H

#include <string>

class ImageProcessor {
public:
    void processImages(const std::string& inputFolder, const std::string& outputFolder);
};

#endif // IMAGEPROCESSOR_H
