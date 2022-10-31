import os

import joblib
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


class PredictionInput(BaseModel):
    text: str
    
class PredictionOutput(BaseModel):
    category: str
    
class NewsgroupsModel:
    model: Pipeline | None
    targets: list[str] | None

    def load_model(self):
        """Load the model from disk."""
        model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets
        
    async def predict(self, input: PredictionInput) -> PredictionOutput:
        """Runs a prediction"""
        if not self.model or not self.targets:
            raise RuntimeError("Model is not loaded")
        prediction = self.model.predict([input.text])
        category = self.targets[prediction[0]]
        return PredictionOutput(category=category)
    
app = FastAPI()
newsgroup_model = NewsgroupsModel()

@app.post("/prediction")
async def prediction(
    output: PredictionOutput = Depends(newsgroup_model.predict)
):
    return output

@app.on_event("startup")
async def startup_event():
    newsgroup_model.load_model()
        