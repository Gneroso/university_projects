#include <iostream>

template<class T> void vector<T>::add(T x) {
  v[size] = x;
  size += 1;
}

template<class T> int vector<T>::compare(T leftElement, T rightElement) {
  if (leftElement == rightElement)
    return 0;

  return leftElement < rightElement ? -1:1;
}

template<class T> void vector<T>::print() {
  for(int i=0; i<size; i++){
    std::cout<<v[i]<<" ";
  }
  std::cout<<"\n";
}

template<class T> void vector<T>::sort(int order=0) {
  T aux;

  for(int i=0; i<size; i++) {
    for(int j=i+1; j<size; j++) {
      if(compare(v[i], v[j]) * order >= 0) {
        aux = v[i];
        v[i] = v[j];
        v[j] = aux;
      }
    }
  }
}
