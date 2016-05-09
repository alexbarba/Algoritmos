#include <iostream>
#include <string>

using namespace std;

int cercanos(int A[], int length);
void insertion_sort(int arr[], int length);

int a=0, b=0;
int main() {
	//int length=12;
	//int arr[length]={1, 3, 5, 7, 10, 26, 78, 54, 12, 90, 11, 2};
	int length=3;
	int arr[length]={12, 2, 2};
	insertion_sort(arr, length);
	
	int resultado = cercanos(arr, length);
	//cout<<a<<b<<endl<<A[a]<<endl<<A[b];
	if (resultado!=0){
		cout<<"Posiciones: "<<a<<" y "<<b<<endl<<"Valores: "<<arr[a]<<" y "<<arr[b];
	}else{cout<<"Todos los resultados son iguales o hay un error en la ejecucion";}
}

int cercanos(int arr[], int length){
	int min=0;
	
	//Encuentro la menor diferencia diferente de 0
	for(int i=0; i<length-1;i++){
		int temp=arr[i+1]-arr[i];
		if((temp<min&&temp!=0)||(min==0&&temp!=0)){
			min=arr[i+1]-arr[i];
			a=i;b=i+1;
		}
	}
	if (min!=0){
		return 1;
	}else{return 0;}
	
}

void insertion_sort (int arr[], int length){
	 	int j, temp;
		
	for (int i = 0; i < length; i++){
		j = i;
		
		while (j > 0 && arr[j] < arr[j-1]){
			  temp = arr[j];
			  arr[j] = arr[j-1];
			  arr[j-1] = temp;
			  j--;
			  }
		}
}
