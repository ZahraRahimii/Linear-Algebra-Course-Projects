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

![image](https://user-images.githubusercontent.com/93929227/204268099-d0ba9c04-a8bf-4743-8cd3-50f2303fe537.png)

The results of denoising would be like this:

`λ=10; not denoised` 
![λ = 10; not denoised](https://user-images.githubusercontent.com/93929227/204267777-e6fca258-d508-4316-8eaa-6407d75134c4.png)

`λ=100; well denoised` 

![λ = 500; well denoised](https://user-images.githubusercontent.com/93929227/204267865-b140a6bf-d0e2-44ce-a081-c503d3c4a847.png)

`λ=10000; too denoised` 

![λ = 10000; too denoised](https://user-images.githubusercontent.com/93929227/204267971-2df00093-b2a8-4f0a-9953-9055a2113f7e.png)


