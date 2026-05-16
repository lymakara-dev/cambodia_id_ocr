def polygon_to_bbox(points):

    xs=[]

    ys=[]

    for x,y in points:

        xs.append(x)

        ys.append(y)

    return (

        min(xs),
        min(ys),
        max(xs),
        max(ys)
    )