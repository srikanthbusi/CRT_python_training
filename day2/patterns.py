# '''1 pattern'''
# # * * * * * 
# # * * * * * 
# # * * * * * 
# # * * * * * 
# # * * * * *
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")         
#     print()       




# '''2 pattern'''
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# '''3 pattern'''
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print("*",end = " ")
#     print()



# '''4 pattern'''
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
# for i in range(1,6):
#     for s in range(1,5-i+1):
#         print(" ",end = " ")
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()


# '''5 pattern'''
# * * * * * * * * * 
# *               *
# *               *
# *               *
# *               *
# *               *
# *               *
# *               *
# * * * * * * * * *
# for i in range(1,10):
#     for j in range(1,10):
#         if i ==1 or i==9 or j == 1 or j==9:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# '''6 pattern'''
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 


# # '''7 pattern'''
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print() 


# # '''7 pattern'''
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# count =1
# for i in range(1,6):
#     for j in range(1,i+1):
#          print(count,end = " ")
#          count +=1
    # print() 


# for i in range(0,6):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()
# for i in range(4,0,-1):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()


##################################################



# num = 8
# for i in range(0,num):
#     for s in range(num,i,-1):
#         print("  ",end=" ")
#     for j in range(0,i):
        
#         if(i%2==0):
#             print("   * ",end=" ")
#         else:
#             print("   0 ",end=" ")

#     print()
# print()

# num = 6
# for i in range(1,num):
#     print("  "*(num-1), "   *" * i )


#################################################




# for i in range(0,6):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()
# for i in range(4,0,-1):
#     for j in range(0,i):
#         print(i , " ",end="")
#     print()


##################################################



# num = 8
# for i in range(0,num):
#     for s in range(num,i,-1):
#         print("  ",end=" ")
#     for j in range(0,i):
        
#         if(i%2==0):
#             print("   * ",end=" ")
#         else:
#             print("   0 ",end=" ")

#     print()
# print()

# num = 6
# for i in range(1,num):
#     print("  "*(num-1), "   *" * i )


#################################################

#                 *
#               *   *
#             *   *   *
#           *   *   *   *
#         *   *   *   *   *
#       *   *   *   *   *   *
#     *   *   *   *   *   *   *


num = 8
for i in range(0,num):
    for s in range(num,i,-1):
        print(" ",end=" ")
    for j in range(0,i):
         
            if(j<3 and j>8):
              print("")
            else:
              print("  *",end=" ")
            


    print()
print()
            
# for i in range(1,5):
#     for j in range(1,i+1):
#           print(i,end=" ")  
#     print()
# for i in range(1,6):
#     for j in range(1,6-i+1):
#           print(6-i,end=" ")  
#     print()  

# for i in range(1,5):
#       for s in range(1,5-i+1):
#          print(" ",end=" ")
#       for j in range(1,2*i):
#          print("*",end =" ")
#       print()