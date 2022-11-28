# Linear_Algebra_Course_Projects
Here is the explanation about three projects of Linear Algebra course:
* LU decomposition
* Denoising the signal using least-square 
* SVD decomposition

## LU decomposition
The solution of Ax=b is done with `Row Reduction` in ${O(n^3)}$. But if we have the LU decomposition of the matrix, the solution of the equation can be done in ${O(n^2)}$. We also know that the calculation of the matrices L and U itself takes place in time ${O(n^3)}$. So that, solving a linear equation system by calculating the LU decomposition of its matrix and finding the solution of the device from it is not a effective method.
Now we want to solve a large number of equations in the form of Ax=b in which A is constant and only b is different, we can solve the equation for different b's in ${O(n^2)}$ time, which is much more optimal.

## Denoising the signal using least-square
The diagram shows the price of Bitcoin every 2 hours from the end of 2020 to the 20th of May. Suppose that the vector 𝒚 is the vector of bitcoin price values, the unknown vector 𝒙 is the noise-free vector of the price we are looking for, and the vector 𝒗 is the uncertain noise vector. That is, we have: ${y=lx+v}$
![Uploading image.png…]()
