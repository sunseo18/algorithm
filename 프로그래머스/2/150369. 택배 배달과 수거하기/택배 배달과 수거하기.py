def solution(cap, n, deliveries, pickups):
    last_del=n-1
    last_pic=n-1
    distance=0


    while deliveries[last_del]==0:
        last_del-=1
        if last_del<0:
            break

    while pickups[last_pic]==0:
        last_pic-=1 
        if last_pic<0:
            break

    while last_del>-1 or last_pic>-1:
        del_stock=0
        pic_stock=0
        distance+=(max(last_del,last_pic)+1)*2

        while del_stock<=cap and last_del>-1:
            del_stock+=deliveries[last_del]
            if del_stock>cap:
                break
            last_del-= 1 


        while pic_stock<=cap and last_pic>-1:
            pic_stock+=pickups[last_pic]
            if pic_stock>cap:
                break
            last_pic-= 1

        if last_pic>-1:
            pickups[last_pic]=pic_stock - cap 
        if last_del>-1:
            deliveries[last_del]=del_stock - cap


    return distance
