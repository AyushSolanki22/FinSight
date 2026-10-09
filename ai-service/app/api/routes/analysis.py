from fastapi import APIRouter
from app.schemas.analysis import AnalysisRequest, AnalysisResponse

router = APIRouter()

@router.post("/analysis", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest):
    # TODO: Connect LangGraph workflow, retrieval, quant engine, and verification.
    return AnalysisResponse(
        status="not_implemented",
        company=request.company,
        question=request.question,
        message="AI analysis workflow is scaffolded but not implemented yet."
    )
