from transformers import pipeline
from enum import Enum

model = pipeline(model="GroNLP/mdebertav3-subjectivity-english")

test_data = ["The president is the worst.", "Four dead in surprise attack."]


OBJ = "LABEL_0"
SUBJ = "LABEL_1"

HIGH_BOUND = 0.75

class Subjectivity(Enum):
    HIGH_SUBJ = "mostly subjective"
    LOW_SUBJ = "slightly subjective"
    HIGH_OBJ = "mostly objective"
    LOW_OBJ = "slightly objective"


def get_subjectivities(text: list[str]) -> list[str]:
    classifications = model(text)

    subjectivities = []

    for res in classifications:
        label = res["label"]
        score = res["score"]

        if score > HIGH_BOUND:
            if label == OBJ:
                subjectivities.append(Subjectivity.HIGH_OBJ.value)
            else:
                subjectivities.append(Subjectivity.HIGH_SUBJ.value)
        else:
            if label == OBJ:
                subjectivities.append(Subjectivity.LOW_OBJ.value)
            else:
                subjectivities.append(Subjectivity.LOW_SUBJ.value)

    return subjectivities

# print(model(test_data))
# print(get_subjectivity_score(test_data))