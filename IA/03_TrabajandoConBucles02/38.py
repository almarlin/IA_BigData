nums = [10, 20, 4, 45, 99, 99]

mayor = nums[0]
segundo_mayor = nums[0]

for num in nums:
    if num > mayor:
        segundo_mayor = mayor  
        mayor = num            
    elif num > segundo_mayor and num != mayor:
        segundo_mayor = num    


print("El segundo número más grande es:", segundo_mayor)