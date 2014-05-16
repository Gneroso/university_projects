template <class T>
class vector {
    T *v;
    int size;
  public:
    int compare(T leftElement, T rightElement);
    void sort(int order);
    void add(T x);
    void print();
};

#include "sort.tpp"
