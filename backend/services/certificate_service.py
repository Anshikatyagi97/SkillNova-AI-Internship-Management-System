"""
Backend service layer for the Certificate Eligibility Analyzer feature.
"""

from ai_modules.certificate_analyzer import service as certificate_ai

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.certificate import Certificate

def get_certificate_eligibility(intern_id: str) -> dict:
    """
    Return certificate eligibility from the database.
    """

    db: Session = SessionLocal()

    try:

        certificate = (
            db.query(Certificate)
            .filter(Certificate.intern_id == intern_id)
            .first()
        )

        if not certificate:
            return {
                "intern_id": intern_id,
                "message": "Certificate record not found."
            }

        status = certificate.status

        if status == "Eligible":
            eligibility_score = 100
            recommendation = "Certificate can be issued."
            next_step = "Congratulations! You have successfully completed all requirements."

        elif status == "Needs Improvement":
            eligibility_score = 70
            recommendation = "Improve your performance before certificate issuance."
            next_step = "Complete the pending requirements and maintain consistency."

        else:
            eligibility_score = 40
            recommendation = "Currently not eligible for certificate."
            next_step = "Focus on attendance, submissions and mentor feedback."

        return {

            "intern_id": intern_id,

            "certificate_status": status,

            "eligibility_score": eligibility_score,

            "issue_date": certificate.issue_date,

            "remarks": certificate.remarks,

            "ai_recommendation": certificate_ai.generate_eligibility_explanation(
              {"status": status}
),

            "next_step": certificate_ai.get_next_step(status),
        }

    finally:
        db.close()