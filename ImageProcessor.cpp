#include "ImageProcessor.h"
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

void ImageProcessor::processImages(const std::string& inputFolder, const std::string& outputFolder) {
    for (const auto& entry : fs::directory_iterator(inputFolder)) {
        if (!entry.is_regular_file()) continue;
        cv::Mat image = cv::imread(entry.path().string(), cv::IMREAD_COLOR);
        if (image.empty()) {
            std::cerr << "Failed to open image file at " << entry.path() << std::endl;
            continue;
        }

        cv::Mat gray, gauss;
        cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
        cv::GaussianBlur(gray, gauss, cv::Size(9, 9), 0);

        cv::SimpleBlobDetector::Params params;
        params.minThreshold = 10;
        params.maxThreshold = 255;
        params.filterByColor = true;
        params.blobColor = 0;
        params.filterByArea = true;
        params.minArea = 20;
        params.maxArea = 2000;
        params.filterByCircularity = true;
        params.minCircularity = 0.3;
        params.filterByConvexity = true;
        params.minConvexity = 1.0;
        params.filterByInertia = true;
        params.minInertiaRatio = 0.2;

        cv::Ptr<cv::SimpleBlobDetector> detector = cv::SimpleBlobDetector::create(params);
        std::vector<cv::KeyPoint> keypoints;
        detector->detect(gauss, keypoints);

        std::cout << "Detected " << keypoints.size() << " dots in file: " << entry.path().filename() << std::endl;

        cv::Mat im_with_keypoints;
        cv::drawKeypoints(image, keypoints, im_with_keypoints, cv::Scalar(0, 0, 255), cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

        std::string filename = outputFolder + "/" + entry.path().stem().string() + "_result.jpg";
        cv::imwrite(filename, im_with_keypoints);
    }
}
