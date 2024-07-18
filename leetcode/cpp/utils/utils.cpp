// utils/utils.cpp

#include "utils.h"

void printVector(const std::vector<int> &vec)
{
    for (const int &value : vec)
    {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

void printStringVector(const std::vector<std::string> &vec)
{
    for (const std::string &value : vec)
    {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

void print2DVector(const std::vector<std::vector<int>> &vec)
{
    for (const auto &row : vec)
    {
        for (const int &value : row)
        {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
}
