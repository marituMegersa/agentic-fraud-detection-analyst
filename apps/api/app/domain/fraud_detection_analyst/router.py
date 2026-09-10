from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.fraud_detection_analyst.schemas import AgenticFraudDetectionAnalystSessionCreate, AgenticFraudDetectionAnalystSessionResponse
from app.domain.fraud_detection_analyst.service import AgenticFraudDetectionAnalystService

router = APIRouter(prefix="/api/v1/fraud_detection_analyst", tags=["Agentic Fraud Detection Analyst Domain"])

@router.post("/sessions", response_model=AgenticFraudDetectionAnalystSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticFraudDetectionAnalystSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Fraud Detection Analyst.
    """
    return AgenticFraudDetectionAnalystService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticFraudDetectionAnalystSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticFraudDetectionAnalystService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
