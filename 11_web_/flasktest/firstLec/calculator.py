def calcBMI( height, weight):
    stdW = (height-100)*0.85
    obesity = weight/stdW*100
    if obesity <= 90:
        result = "저체중"
        sajin = "/static/image/low.jpg"
    elif 90<obesity<=110:
        result = "정상"
        sajin = "/static/image/normal.jpg"
    elif 110<obesity<=120:
        result = "과체중"
        sajin = "/static/image/high.jpg"
    else:
        result = "비만"
        sajin = "/static/image/fat.jpg"
    return result, sajin