// C++ program for Merge Sort

#include <iostream.h>

using namespace std;
 

void merge(int ar[], int start, int mid, int last)
{
    int n1 = mid - start + 1;
    int n2 = last - mid;
 
    
    int Lef[n1], Rig[n2];
 
    
    for (int i = 0; i < n1; i++)
        Lef[i] = ar[start + i];
    for (int j = 0; j < n2; j++)
        Rig[j] = ar[mid + 1 + j];
 
    
 
    
    int i = 0;
 
    
    int j = 0;
 
    
    int k = start;
 
    while (i < n1 && j < n2) {
        if (Lef[i] <= Rig[j]) {
            ar[k] = Lef[i];
            i++;
        }
        else {
            ar[k] = Rig[j];
            j++;
        }
        k++;
    }
 
    
    while (i < n1) {
        ar[k] = Lef[i];
        i++;
        k++;
    }
 
    
    while (j < n2) {
        ar[k] = Rig[j];
        j++;
        k++;
    }
}
 

void merSor(int ar[],int start,int last){
    if(start>=last){
        return;
    }
    int m = (start+last-1)/2;
    merSor(ar,start,m);
    merSor(ar,m+1,last);
    merge(ar,start,m,last);
}
 

void prinArr(int A[], int size)
{
    for (int i = 0; i < size; i++)
        cout << A[i] << " ";
}
 

int main()
{
    int ar[] = { 11,30,24,7,31,16,39,41 };
    int ar_size = sizeof(ar) / sizeof(ar[0]);
 
    cout << "Given array is \n";
    prinArr(ar, ar_size);
 
    merSor(ar, 0, ar_size - 1);
 
    cout << "\nSorted array is \n";
    prinArr(ar, ar_size);
    return 0;
}


