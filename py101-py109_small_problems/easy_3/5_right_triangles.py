'''Write a function that takes a positive integer, n, as an argument and 
prints a right triangle whose sides each have n stars. The hypotenuse of 
the triangle (the diagonal side in the images below) should have one end 
at the lower-left of the triangle, and the other end at the upper-right.'''

def triangle(num):
    asterisks = 1
    distance_from_right = num
    
    for _ in range(num):
        print(f'{' ' * distance_from_right}{'*' * asterisks}')

        asterisks += 1
        distance_from_right -= 1


triangle(5)

'''Output for Example 1

    *
   **
  ***
 ****
*****'''

triangle(9)

'''Output for Example 2

        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********'''
