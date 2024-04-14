from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ContestInput(BaseModel):
    contest_id: int
    percentage: Optional[float] = None
    completion_time: Optional[float] = None

# Define the response model
class ContestOutput(BaseModel):
    reward: float
    percentage: Optional[float] = None
    completion_time: Optional[float] = None

# Define a function to calculate reward based on completion time and percentage
def calculate_reward(contest_id: int,percentage: Optional[float] = None, completion_time: Optional[float] = None) -> int:
    if contest_id == 1:
        if (percentage is not None and percentage >= 0.8) or (completion_time is not None and completion_time < 30):
            reward_id = 4
        elif (percentage is not None and percentage >= 0.6) or (completion_time is not None and completion_time < 50):
            reward_id = 5
        else:
            reward_id = 6
    elif contest_id == 2:
        if (percentage is not None and percentage >= 0.8) or (completion_time is not None and completion_time < 15):
            reward_id = 3
        elif (percentage is not None and percentage >= 0.6) or (completion_time is not None and completion_time < 30):
            reward_id = 2
        else:
            reward_id = 1
    # elif contest_id == 3:
    #     if percentage >= 0.8 or completion_time < 30:
    #         reward_id = 7
    #     elif percentage >= 0.6 or completion_time < 50:
    #         reward_id = 6
    #     else:
    #         reward_id = 5
    else:
        # Default reward logic if contest ID is not recognized
        reward_id = -1

    return reward_id


# @app.post("/calculate_reward/")
# async def calculate_reward_endpoint(contest_input: ContestInput) -> ContestOutput:
#     contest_id = contest_input.contest_id

#     # Validate that at least one of percentage or completion_time is provided
#     if contest_input.percentage is None and contest_input.completion_time is None:
#         raise HTTPException(status_code=400, detail="Either percentage or completion time must be provided")

#     # Use the values if provided, otherwise set defaults or handle them according to your business logic
#     percentage = contest_input.percentage if contest_input.percentage is not None else 0  # Default or error
#     completion_time = contest_input.completion_time if contest_input.completion_time is not None else 0  # Default or error

#     # Example logic for calculation (you would adjust this to suit your application's logic)
#     reward = calculate_reward(contest_id, percentage, completion_time)

#     # Return the response
#     return ContestOutput(reward=reward, percentage=percentage, completion_time=completion_time)

@app.get("/")
def index():
    return "Input Format : BASE_URL/calculate_reward/?contest_id=X&percentage=X&completion_time=X. Use either percentage or completion_time and contest_id should be either 1 or 2"

@app.get("/calculate_reward/")
async def calculate_reward_get(contest_id: int, percentage: Optional[float] = None, completion_time: Optional[float] = None) -> ContestOutput:
    # Validate that at least one of percentage or completion_time is provided
    if percentage is None and completion_time is None:
        raise HTTPException(status_code=400, detail="Either percentage or completion time must be provided")

    # Calculate the reward
    reward = calculate_reward(contest_id, percentage, completion_time)

    # Return the response
    return ContestOutput(reward=reward, percentage=percentage, completion_time=completion_time)