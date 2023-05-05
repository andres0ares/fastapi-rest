from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

#define endpoint
@app.get("/")
#define parametro e seu valor padrão
async def read_root(GMT: str = '-3,-5'):
    #retorna valor da função getGMTS
    return getGMTs(GMT)

def getGMTs(gmt: str):
   
    res = list()
    try:
        #cria lista de inteiros com valores do fusos
        gmts = list(map(int, gmt.split(',')))

        #para cada interio da lista adiciona horário correspondente
        for t in gmts:    
            d =  datetime.utcnow() + timedelta(hours=t)
            #formata e adiciona horário
            res.append({f'GMT{"+" if(t >= 0) else ""}{t}': "{:d}:{:02d}:{:02d}".format(d.hour, d.minute, d.second)})
    except ValueError:
        #mensagem de erro casos valor passado por parâmetro seja inválido
        res = 'Inválido. Tente numeros inteiros separados por virgula.'

    #return lista de horários
    return res


