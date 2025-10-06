from fastapi import FastAPI
app=FastAPI()
@app.post("/search/")
def search(w:int,h:int):
    height = h/100
    bmi_v = w / (height**2)
    if bmi_v < 18:
       a = "lean"
    elif 18 <= bmi_v <25:
       a = "normal"
    elif 25<=bmi_v <30:
       a="overweight"
    else:
       a = "obesity"
    return {"bmi":bmi_v,"a":a}
