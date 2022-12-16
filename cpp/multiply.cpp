// Simple C++ program to multiply two polynomials 
#include <iostream> 
#include<algorithm> 

using namespace std; 

// A[] represents coefficients of first polynomial 
// B[] represents coefficients of second polynomial 
// m and n are sizes of A[] and B[] respectively 
int *multiply(int A[], int B[], int m, int n) { 

    int *prod = new int[m+n-1]; 

    // Initialize the porduct polynomial 
    for (int i = 0; i<m+n-1; i++) prod[i] = 0; 

    // Multiply two polynomials term by term 

    // Take ever term of first polynomial 
    for (int i=0; i<m; i++) { 
	    // Multiply the current term of first polynomial 
	    // with every term of second polynomial. 
	    for (int j=0; j<n; j++) prod[i+j] += A[i]*B[j]; 
    } 
    return prod; 
} 

// A utility function to print a polynomial 
void print_poly(int poly[], int n) { 
	for (int i=0; i<n; i++) { 
	    cout << poly[i]; 
	    if (i != 0) 
		    cout << "x^" << i ; 
	    if (i != n-1) 
	        cout << " + "; 
	} 
    cout << endl;
} 

// int *plus(int *A, int *B, int m, int n){
//     int h = max(m, n);
//     int *prod = new int[h];
//     for (int i=0; i<h; i++) prod[i] = A[i] + B[i];
//     return prod;
// }

// int *dac_multiply(int *A, int *B, int m, int n){
//     int amid = m/2;
//     int bmid = n/2;
//     int *A0 = &A[0];
//     int *A1 = &A[amid];
//     int *B0 = &B[0];
//     int *B1 = &B[bmid];
//     int *X0 = plus(A0, A1, amid, m-amid);
//     int *X1 = plus(B0, B1, bmid, n-bmid);
//     int *X = dac_multiply(, plus(A0, A1, amid, m-amid), );
// }

int main() { 
	// The following array represents polynomial 5 + 10x^2 + 6x^3 
	int A[] = {5, 0, 10, 6}; 

	// The following array represents polynomial 1 + 2x + 4x^2 
	int B[] = {1, 2, 4}; 
    int m = sizeof(A)/sizeof(A[0]);
	int n = sizeof(B)/sizeof(B[0]);

	cout << "First polynomial is: " << endl; 
	print_poly(A, m); 
	cout << "Second polynomial is: " << endl; 
	print_poly(B, n); 

	int *prod = multiply(A, B, m, n); 

	cout << "Product polynomial is: "; 
	print_poly(prod, m); 

	return 0; 
} 
