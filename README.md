# Differential-Equations
The three methods used for these simulations are Foward Euler's Method, Heun's Method and Symplectic Euler's Method.

**Foward Euler's Method:**</br>
Euler's method is the first order, explicit method used for numerical integration of differential equations. It uses the initial results to give the final results. For example, it gives the new position of an object using it's old position and adding it with the change in position due to velocity during a certain time step. This will give the new position of that object after that time step has passed. Similarly, it can be used to give the new velocity using inital velocity at a certain time step and adding change in velocity, due to acceleration, to give the final velocity after that time step has passed.</br>
![image](https://user-images.githubusercontent.com/26041014/152056225-01e5d2fe-cfcc-43d2-ad26-7439d5e6323b.png)


**Heun's Method:**</br>
Euler's method is used as the foundation for Heun's method. It is better than the Euler's method as it reduces the Local truncation error and provides a more accurate apprximation. For example, we calculated the new position after a certain time has passed as object moves with a certain velocity. Euler's method assumes that the velocity during that time segment remain constant which might not be the case everytime. Heun's method takes the average of both the initial and final velocity to calculate the change in position. This provides more accurate results for the new position after that certain time step has passed. Similarly, when finding the new velocity of the object, Heun's method uses the average of the change in velocity at the initial and final position to give accurate results for the new velocity after certain time period.</br>

![image](https://user-images.githubusercontent.com/26041014/152056126-db105064-6df2-4620-9ff1-5eaaa58c1741.png)</br>
![image](https://user-images.githubusercontent.com/26041014/152056148-18bfee3e-c5a9-424e-8faa-d2455d5011b1.png)


**Symplectic Euler's Method:**</br>
Symplectic Euler Method is a modification of the Euler method for solving Hamilton's equations. The difference with the standard Euler method is that the semi-implicit Euler method uses v<sub>n+1</sub> in the equation for x<sub>n+1</sub>, while the Euler method uses v<sub>n</sub>. It uses the final position which an object reaches to in the given time step and then uses that position to calculate the velocity. It yields better results than the standard Euler method.</br>

![image](https://user-images.githubusercontent.com/26041014/152057532-1b5ceb61-0469-478f-a311-c966c2444f26.png)</br>
![image](https://user-images.githubusercontent.com/26041014/152057547-fc298e15-eb11-4f42-8e2f-eb08d1488c2e.png)
