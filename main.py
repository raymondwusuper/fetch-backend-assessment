from fastapi import FastAPI, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime
from collections import defaultdict

app = FastAPI()
transactions = []
balances = defaultdict(int)
class AddPointsRequest(BaseModel):
    payer: str
    points: int
    timestamp: datetime
class SpendPointsRequest(BaseModel):
    points: int
class SpendPointsResponse(BaseModel):
    payer: str
    points: int

@app.post("/add")
def add_points(transaction: AddPointsRequest):
    if transaction.points < 0 and -transaction.points > balances[transaction.payer]: #in the event of negative balances
        raise HTTPException(status_code=400, detail="Negative balance not allowed for any payer.")
    transactions.append(transaction)
    balances[transaction.payer] += transaction.points
    return {"status": "Points added successfully"}

@app.get("/balance")
def get_balance():
    return balances

@app.post("/spend", response_model=List[SpendPointsResponse])
def spend_points(request: SpendPointsRequest):
    #spending more points than user has total (works because at most a single user uses this api)
    if sum(balances.values()) < request.points: 
        raise HTTPException(status_code=400, detail="Not enough points to spend.")
    payer_changes = []
    rem_points = request.points
    payers_by_time = sorted(transactions, key=lambda x: x.timestamp)
    for transaction in payers_by_time:
        if rem_points <= 0: break
        payer = transaction.payer
        #because of the changes illustrated by the comment below, we want to skip over payers with a 0 balance.
        if balances[payer] <= 0: continue
        '''
        In the event that spend is ran multiple times, it will cause it to exceed payer's balance when we want to spend the remaining points \
        available in balance.
        Taking the minimum of the three is a clever way to handle this corner case because if our balance is less than the initial transaction, \
        it will fully exhaust the balance.
        This also works when the net balance is less than one of the transactions for that payer, since the negative that resulted in this \
        deficit will add points to the remaining points if it is before the positive value.
        The converse, where a negative is after the positive value, also is handled since if the positive value transaction fully exhausts \
        the remaining points, the loop will continue and skip over the points that may be added from the negative.
        '''
        spendable_points = min(rem_points, transaction.points, balances[payer]) 
        if rem_points > 0 and balances[payer] >= spendable_points:
            balances[payer] -= spendable_points
            rem_points -= spendable_points
            payer_changes.append((payer, -spendable_points))
    final_changes = defaultdict(int)
    for payer, points_change in payer_changes:
        final_changes[payer] += points_change
    payer_changes = []
    for payer, net_change in final_changes.items():
        payer_changes.append(SpendPointsResponse(payer=payer, points=net_change))
    return payer_changes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
