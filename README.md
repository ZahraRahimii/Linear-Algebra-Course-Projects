# Linear Algebra Course Projects
Here is the explanation about three projects of Linear Algebra course:
* LU decomposition
* Denoising the signal using least-squares
* Using SVD decomposition for image compression

## LU decomposition
The solution of Ax=b is done with `Row Reduction` in ${O(n^3)}$. But if we have the LU decomposition of the matrix, the solution of the equation can be done in ${O(n^2)}$. We also know that the calculation of the matrices L and U itself takes place in time ${O(n^3)}$. So that, solving a linear equation system by calculating the LU decomposition of its matrix and finding the solution of the device from it is not a effective method.
Now we want to solve a large number of equations in the form of Ax=b in which A is constant and only b is different, we can solve the equation for different b's in ${O(n^2)}$ time, which is much more optimal.

## Denoising the signal using least-squares
The diagram shows the price of Bitcoin every 2 hours from the end of 2020 to the 20th of May. Suppose that the vector 𝒚 is the vector of bitcoin price values, the unknown vector 𝒙 is the noise-free vector of the price we are looking for, and the vector 𝒗 is the uncertain noise vector. That is, we have: ${y=lx+v}$

<p align="center">
<img src="https://user-images.githubusercontent.com/93929227/204270031-a44ab157-77d8-4440-ab70-87d44af3e68a.png" width="50%" height="50%">
<p/>

The results of denoising would be like this:

<pre>   
             λ=10; not denoised                        λ=100; well denoised                       λ=10000; too denoised 

<p align="center">
<img src="https://user-images.githubusercontent.com/93929227/204269434-3ecc545f-9d01-4048-85f6-78bec26e59b2.png">
<!-- <img src="https://user-images.githubusercontent.com/93929227/204267777-e6fca258-d508-4316-8eaa-6407d75134c4.png"> -->
<p/>
</pre>

<!-- `λ=100; well denoised`  -->
<!-- <p align="center"> -->
<!-- <img src="https://user-images.githubusercontent.com/93929227/204267865-b140a6bf-d0e2-44ce-a081-c503d3c4a847.png">
<p/>

`λ=10000; too denoised` 
<p align="center">
<img src="https://user-images.githubusercontent.com/93929227/204267971-2df00093-b2a8-4f0a-9953-9055a2113f7e.png">
<p/>

 -->
 
## Using SVD decomposition for image compression
We can decompose a given image into the three color channels red, green and blue. Each channel can be represented as a (m × n)‑matrix with values ranging from 0 to 255. We will now compress the matrix A representing one of the channels. To do this, we compute an approximation to the matrix A that takes only a fraction of the space to store. Now here's the great thing about SVD: the data in the matrices U, Σ and V is sorted by how much it contributes to the matrix A in the product. That enables us to get quite a good approximation by simply considering only the k-terms of the first important parts of the matrices

<pre>   
                k=50;                                           k=250;                                      k=750;

<p align="center">
<img src="https://user-images.githubusercontent.com/93929227/204275517-6f61054a-babc-4c6e-ae8d-01c84ba60f0e.png">
<!-- <img src="https://user-images.githubusercontent.com/93929227/204267777-e6fca258-d508-4316-8eaa-6407d75134c4.png"> -->
<!-- ![Untitled2](https://user-images.githubusercontent.com/93929227/204275517-6f61054a-babc-4c6e-ae8d-01c84ba60f0e.png) -->

<p/>
</pre>


