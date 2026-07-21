import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    c=len(players.columns)
    r=len(players)
    return [r,c]