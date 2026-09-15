def get_treatment(disease, affected_percentage):
    
    # Keep percentage between 0 and 100
    affected_percentage = max(
        0.0,
        min(float(affected_percentage), 100.0)
    )

    # =========================
    # HEALTHY
    # =========================

    if disease == "Healthy":
        severity = "LOW"

    # =========================
    # LOW: 0% - BELOW 10%
    # =========================

    elif affected_percentage < 10:
        severity = "LOW"

    # =========================
    # MODERATE: 10% - BELOW 60%
    # =========================

    elif affected_percentage < 60:
        severity = "MODERATE"

    # =========================
    # HIGH: 60% - 100%
    # =========================

    else:
        severity = "HIGH"

    return {
        "severity": severity
    }