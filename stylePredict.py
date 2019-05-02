import lightgbm as gbm
import colorsys
import pandas as pd
MODEL_PATH='./model.txt'
EPS=0.7
gbm=gbm.Booster(model_file=MODEL_PATH)

# param: palette,eg:[(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b)]
# return style ['cute','fresh','technology']
# return -1: do not belong to cute, fresh or technology
def style_predict(palette):
    def sortByLight2(elem):
        hls=colorsys.rgb_to_hls(*elem)
        return hls[1]
    # build a color palette
    palette.sort(key=sortByLight2,reverse=True)
    palette1=[*palette[0],*palette[1],*palette[2],*palette[3],*palette[4]]
    for c in palette:
        h,l,s=colorsys.rgb_to_hls(*c)
        palette1=[*palette1,h,l,s]
    x=pd.Series(palette1)
    y_pred = gbm.predict(x, num_iteration=gbm.best_iteration)
    y_pred=y_pred.tolist()
    style=['cute','technology','fresh']
    if(max(*y_pred)<EPS):
        return -1
    pred_Y=y_pred.index(max(y_pred))
    print("Probability：",y_pred)
    return style[pred_Y]