from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.fraud_detection_analyst.models import AgenticFraudDetectionAnalystSession, AgenticFraudDetectionAnalystItem
from app.domain.fraud_detection_analyst.schemas import AgenticFraudDetectionAnalystSessionCreate, AgenticFraudDetectionAnalystItemCreate

class AgenticFraudDetectionAnalystService:
    @staticmethod
    def create_session(db: Session, data: AgenticFraudDetectionAnalystSessionCreate) -> AgenticFraudDetectionAnalystSession:
        db_obj = AgenticFraudDetectionAnalystSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticFraudDetectionAnalystSession:
        return db.query(AgenticFraudDetectionAnalystSession).filter(AgenticFraudDetectionAnalystSession.id == session_id).first()
