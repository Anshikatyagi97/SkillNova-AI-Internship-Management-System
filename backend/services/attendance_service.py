"""
Backend service layer for the Attendance & Performance Analyzer feature.
"""

from sqlalchemy.orm import Session

from ai_modules.attendance_analyzer import service as attendance_ai
from backend.database.database import SessionLocal
from backend.models.attendance import Attendance


def get_intern_attendance(intern_id: str) -> dict:
    """
    Return real attendance analytics for one intern.
    """

    db: Session = SessionLocal()

    try:
        records = (
            db.query(Attendance)
            .filter(Attendance.intern_id == intern_id)
            .all()
        )

        total_days = len(records)

        if total_days == 0:
            return {
                "intern_id": intern_id,
                "message": "No attendance records found."
            }

        present = len(
            [r for r in records if r.status.lower() == "present"]
        )

        absent = len(
            [r for r in records if r.status.lower() == "absent"]
        )

        late = len(
            [r for r in records if r.status.lower() == "late"]
        )

        attendance_percentage = round(
            ((present + late) / total_days) * 100,
            2,
        )

        # Attendance Status
        if attendance_percentage >= 90:
            attendance_status = "Excellent"
        elif attendance_percentage >= 75:
            attendance_status = "Good"
        elif attendance_percentage >= 60:
            attendance_status = "Warning"
        else:
            attendance_status = "Critical"

        # Attendance Grade
        if attendance_percentage >= 90:
            attendance_grade = "A"
        elif attendance_percentage >= 75:
            attendance_grade = "B"
        elif attendance_percentage >= 60:
            attendance_grade = "C"
        else:
            attendance_grade = "D"

        # Risk Level
        if attendance_percentage >= 80:
            risk_level = "Low"
        elif attendance_percentage >= 60:
            risk_level = "Medium"
        else:
            risk_level = "High"

        # Mentor Alert
        mentor_alert = attendance_percentage < 60

        # Consistency Score
        consistency_score = round(
            ((present + late) / total_days) * 100,
            2,
        )

        # AI Summary
        ai_summary = attendance_ai.generate_ai_attendance_summary(
            intern_id=intern_id,
            attendance_percentage=attendance_percentage,
            late_days=late,
            absent_days=absent,
        )

        return {
            "intern_id": intern_id,
            "total_days": total_days,
            "present_days": present,
            "absent_days": absent,
            "late_days": late,
            "attendance_percentage": attendance_percentage,
            "attendance_status": attendance_status,
            "attendance_grade": attendance_grade,
            "risk_level": risk_level,
            "mentor_alert": mentor_alert,
            "consistency_score": consistency_score,
            "attendance_risk": attendance_ai.predict_attendance_risk(
                attendance_percentage
            ),
            "attendance_recommendation": attendance_ai.attendance_recommendation(
                attendance_percentage,
                late,
            ),
            "ai_summary": ai_summary,
        }

    finally:
        db.close()