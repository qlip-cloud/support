from qp_customer_support.services.issue_support_incidents.issue import update_status_close

def auto_close_expired_issues():
    update_status_close(
        issue_status="Esperando cierre",
        expiration_days=3,
        issue_update_to_status="Resolved"
    )
