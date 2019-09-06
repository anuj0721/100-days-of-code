'''break out nested loops'''
for x in range(1,11):
    for y in range(1,5):
        if x*y == 36:
            print(x,y)
            # Break the inner loop...
            break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    break

