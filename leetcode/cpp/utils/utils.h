// utils/utils.h

#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <iostream>

// Khai báo các hàm bạn muốn sử dụng trong file cpp chính
void printVector(const std::vector<int> &vec);
void printStringVector(const std::vector<std::string> &vec);
void print2DVector(const std::vector<std::vector<int>> &vec);

#endif
