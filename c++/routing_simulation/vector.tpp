#include <iostream>


template<class T> void vector<T>::add(T* x) {
  std::cout<<"added 1";
  std::cout<<new T[sizeof(x)]<<"\n";
  v[0] = new T[sizeof(x)];
  std::cout<<v[1]<<" "<<v;
  size += 1;
}

template<class T> void vector<T>::print() {
  //for(int i=0; i<size; i++) {
  //  v[i]->print();
  //}
}
